# Pattern: Bilingual Toggle via React Context + Cookie + Static JSON Dictionaries

**Category:** Internationalization / Conversion
**First used:** Sylvia Rich Hungarian Consul (EN/HU) — Mar 2026
**Ported to:** LMP Financial (EN/ES) — May 2026
**Status:** VALIDATED — 2026-05-02

## What

A lightweight bilingual (or trilingual+) toggle for Next.js App Router sites using only React Context, a `NEXT_LOCALE` cookie, and statically-imported JSON dictionaries per namespace. Zero new npm dependencies. No middleware, no `/locale` URL prefix, no `next-intl` / `next-i18next` overhead. The toggle persists locale via cookie, sets `<html lang>` server-side at every request, and re-renders the entire tree client-side on locale switch in <100ms.

Source of truth for translatable strings stays in `src/locales/<locale>/<namespace>.json`. Components consume via a `useTranslation(namespace)` hook returning `t(key)` for strings and `ta<T>(key)` for typed arrays/objects.

## When to Use

- Client market includes a non-English-speaking audience (LMP: large Spanish-speaking borrower population across MA + 8 licensed states; Sylvia: Hungarian diaspora in the US Northeast)
- Site is small-to-medium (≤30 namespaces / ≤500KB total JSON)
- URL structure can stay single-locale (no `/es/...` paths required)
- SEO indexability of the second locale is not a hard requirement (cookie-only locale is invisible to crawlers as a separate URL)
- Two locales typical, but the pattern scales to 3-4 with no architectural change

## When NOT to Use

- Large enterprise i18n: 5+ locales, RTL/LTR mix, CMS-driven translation workflows → use a real i18n library (`next-intl`, `react-intl` with ICU MessageFormat)
- SEO-critical second locale: if the second-locale audience needs to find the site via Google in their language → use middleware-based locale routing with `/<locale>/...` URL prefixes and `hreflang` tags
- Per-user content that varies independently of locale (auth-gated dashboards with per-user translations) → richer i18n library with key-level fallback rules
- Bundle size matters: this pattern bundles all locales statically. If you have 10 locales × 100 namespaces, the cost is real

## Files (5 plumbing files + N×2 JSON namespaces)

```
src/
├── lib/i18n.ts                    # ~50 lines — locale type + cookie helpers
├── contexts/I18nContext.tsx       # ~40 lines — provider, useI18n() consumer
├── hooks/useTranslation.ts        # ~30 lines — hook with t() + ta<T>()
├── locales/
│   ├── index.ts                   # static aggregator — imports every JSON namespace
│   ├── en/
│   │   ├── common.json            # nav, footer, buttons, shared chrome
│   │   ├── home.json
│   │   └── ... (one file per page or content domain)
│   └── es/                        # mirror of en/ with Spanish values + _meta block
└── components/ui/LanguageToggle.tsx  # ~60 lines — segmented EN/ES pill
```

Plus integration in `src/app/layout.tsx` (server) — read cookie, set `<html lang>`, wrap with `<I18nProvider initialLocale={locale}>`.

## Pattern — Plumbing

**`src/lib/i18n.ts`** — locale primitives + cookie helpers. Pure, no React.
```ts
export type Locale = 'en' | 'es';

export const SUPPORTED_LOCALES: Locale[] = ['en', 'es'];
export const DEFAULT_LOCALE: Locale = 'en';
export const LOCALE_COOKIE = 'NEXT_LOCALE';

export function resolvePath(obj: Record<string, unknown>, key: string): unknown {
  return key.split('.').reduce<unknown>((acc, part) => {
    if (acc && typeof acc === 'object') {
      return (acc as Record<string, unknown>)[part];
    }
    return undefined;
  }, obj);
}

export function parseLocaleCookie(cookieHeader: string | null | undefined): Locale {
  if (!cookieHeader) return DEFAULT_LOCALE;
  const match = cookieHeader.match(new RegExp(`(?:^|;\\s*)${LOCALE_COOKIE}=([^;]*)`));
  const value = match?.[1];
  return SUPPORTED_LOCALES.includes(value as Locale) ? (value as Locale) : DEFAULT_LOCALE;
}

export function setLocaleCookie(locale: Locale): void {
  document.cookie = `${LOCALE_COOKIE}=${locale};path=/;max-age=31536000;SameSite=Lax`;
}

export function ogLocale(locale: Locale): string {
  return locale === 'es' ? 'es_US' : 'en_US';
}
```

**`src/locales/index.ts`** — static aggregator. Imports every namespace JSON and exposes `translations = { en, es }`. Statically bundled, zero runtime fetch on switch.
```ts
import enCommon from './en/common.json';
import enHome from './en/home.json';
// ... one import per namespace per locale

const en = { common: enCommon, home: enHome /* ... */ };
const es = { common: esCommon, home: esHome /* ... */ };

export const translations = { en, es } as const;
export type Translations = typeof en;
```

**`src/contexts/I18nContext.tsx`** — provider. Client component. Reads `initialLocale` from layout, exposes `setLocale` that writes the cookie and triggers re-render.
```tsx
'use client';
import { createContext, useContext, useState, useCallback } from 'react';
import { type Locale, DEFAULT_LOCALE, setLocaleCookie } from '@/lib/i18n';
import { translations, type Translations } from '@/locales';

interface I18nContextValue {
  locale: Locale;
  setLocale: (locale: Locale) => void;
  t: Translations;
}

const I18nContext = createContext<I18nContextValue>({
  locale: DEFAULT_LOCALE,
  setLocale: () => {},
  t: translations[DEFAULT_LOCALE],
});

export function I18nProvider({
  initialLocale,
  children,
}: { initialLocale: Locale; children: React.ReactNode }) {
  const [locale, setLocaleState] = useState<Locale>(initialLocale);
  const setLocale = useCallback((next: Locale) => {
    setLocaleCookie(next);
    setLocaleState(next);
  }, []);
  return (
    <I18nContext.Provider value={{ locale, setLocale, t: translations[locale] }}>
      {children}
    </I18nContext.Provider>
  );
}

export function useI18n(): I18nContextValue {
  return useContext(I18nContext);
}
```

**`src/hooks/useTranslation.ts`** — namespace-scoped hook with `t()` and `ta<T>()`.
```ts
'use client';
import { useI18n } from '@/contexts/I18nContext';
import { resolvePath } from '@/lib/i18n';
import type { Translations } from '@/locales';

export function useTranslation(namespace: keyof Translations) {
  const { locale, setLocale, t: allTranslations } = useI18n();
  const ns = allTranslations[namespace] as Record<string, unknown>;

  function t(key: string): string {
    const value = resolvePath(ns, key);
    if (typeof value === 'string') return value;
    return key; // visible miss — surfaces in QA
  }

  function ta<T>(key: string): T | undefined {
    const value = resolvePath(ns, key);
    return value === undefined ? undefined : (value as T);
  }

  return { t, ta, locale, setLocale };
}
```

**`src/components/ui/LanguageToggle.tsx`** — segmented pill. Two `<button>` elements, `aria-pressed` per active state, role-grouped, dual-language `aria-label`. Two size variants for desktop nav vs mobile drawer. Brand tokens via CSS custom properties — no hardcoded color literals.

## Pattern — Layout Integration

`src/app/layout.tsx` stays a server component. Read the cookie via `next/headers`, derive `Locale`, set `<html lang>`, pass `initialLocale` to the provider.

```tsx
import { cookies } from 'next/headers';
import { I18nProvider } from '@/contexts/I18nContext';
import { type Locale, DEFAULT_LOCALE, LOCALE_COOKIE, SUPPORTED_LOCALES, ogLocale } from '@/lib/i18n';

async function readLocale(): Promise<Locale> {
  const store = await cookies();
  const value = store.get(LOCALE_COOKIE)?.value;
  return SUPPORTED_LOCALES.includes(value as Locale) ? (value as Locale) : DEFAULT_LOCALE;
}

export async function generateMetadata(): Promise<Metadata> {
  const locale = await readLocale();
  return { openGraph: { locale: ogLocale(locale), /* ... */ }, /* ... */ };
}

export default async function RootLayout({ children }) {
  const locale = await readLocale();
  return (
    <html lang={locale}>
      <body>
        <I18nProvider initialLocale={locale}>
          {children}
        </I18nProvider>
      </body>
    </html>
  );
}
```

## Pattern — Component Consumption

Every component that renders translatable copy is `'use client'` and consumes via the hook. Use `?? siteConfig.foo` as a structural fallback when the dictionary may not yet contain the key — this lets dictionary scaffolding ship before every key is filled, and keeps the build green during EN→ES translation passes.

```tsx
'use client';
import { useTranslation } from '@/hooks/useTranslation';
import { siteConfig } from '@/data/site';

export default function HeroSection() {
  const { t, ta } = useTranslation('home');
  const trustStrip = ta<string[]>('hero.trustStrip') ?? siteConfig.hero.trustStrip;
  return (
    <>
      <h1>{t('hero.tagline')}</h1>
      <p>{t('hero.subheadline')}</p>
      <ul>{trustStrip.map((item, i) => <li key={i}>{item}</li>)}</ul>
    </>
  );
}
```

## Reference Implementations

- **Sylvia Rich Hungarian Consul (EN/HU)** — `tonyrosa777-ops/Sylvia-Rich-Hungary-Consul-NE`. Original. Hungarian-American honorary consul; cookie-driven toggle, no URL changes.
- **LMP Financial (EN/ES)** — this build. 17 namespaces × 2 locales = 34 JSON files. Compliance-aware: 7 verbatim items stay English under both locales (mortgage broker regulatory requirement); small ES legal note rendered adjacent to the verbatim block.

## Pitfalls

- **Server/client split**: layout / page / metadata can stay server, but every component consuming `useTranslation` MUST be `'use client'`. Forgetting `'use client'` produces a runtime "Hooks can only be called inside the body of a function component" error or a silent cache/render mismatch.
- **Toggle in a server component**: `<LanguageToggle />` writes `document.cookie` on click — server components cannot. Always render the toggle inside a client tree.
- **`html lang` doesn't update on toggle without refresh**: by design — the cookie is read server-side at request time, so `<html lang>` updates on the next navigation/reload, not on the in-page toggle click. This is fine for screen readers (they re-evaluate per page), and acceptable for SEO since this pattern intentionally trades second-locale crawlability for simplicity. If you need lang to flip live, also `useEffect` to set `document.documentElement.lang = locale` on the client.
- **Compliance copy translated by accident**: the LMP build maintains 7 verbatim regulatory strings that MUST render in English under both locales. The ES dictionary should reference these strings via a `compliance.legalNotice` key (the small ES adjacent note), NOT translate the underlying broker disclosure / NMLS link / SMS opt-in disclaimer. See LMP CLAUDE.md Compliance Rule + Bilingual Copy Rule.
- **Spanish averages 15-25% longer than English**: hero H1, button labels, and nav items often overflow at 375px mobile in Spanish. Test both locales at 375 in the multi-breakpoint browser audit.
- **Missing keys silently render the dot-notation key**: `t('hero.tagline')` returns the literal string `"hero.tagline"` if the key is missing. This is intentional — surfaces misses in QA — but means a build can ship with visible key paths if the auditor doesn't catch them. Pre-launch-auditor enforces deep-diff parity to prevent this.
- **Bundle size scales linearly with locales × namespaces**: the static-import aggregator pulls everything into the client bundle. For LMP-scale (~17 namespaces × 2 locales) this is ~50KB gzip and the right tradeoff — zero runtime fetch latency on switch. At 10+ locales you'll want to switch to dynamic imports per locale.

## CLAUDE.md Add-On (paste into future bilingual project rules)

```markdown
## Bilingual Copy Rule (project-specific — non-negotiable)
This project ships in <LOCALE_A> and <LOCALE_B> via a custom React Context i18n
system (see `C:\Projects\Optimus Assets\knowledge\patterns\bilingual-toggle-react-context-pattern.md`).
Locale persists via `NEXT_LOCALE` cookie; `<html lang>` is set server-side from
the cookie at every request.

Every new user-facing string ships in BOTH locales in the same commit. Adding a
key to `src/locales/<a>/<namespace>.json` without a matching key path in
`src/locales/<b>/<namespace>.json` (and vice versa) is a build failure. The
pre-launch-auditor enforces this with a deep key-path diff.

Components consume copy via `useTranslation()`, never hardcoded strings, and
never directly from `siteConfig` for translatable fields. Components that
consume `useTranslation` MUST be `'use client'` — server components cannot read
context.

[Project-specific exceptions for verbatim regulatory / branded copy go here.]

[Translation discipline rules go here — register, em-dash policy, translation
review status workflow.]

[Untranslatable content list goes here — testimonial quotes, proper nouns,
acronyms, dollar amounts.]
```

## Related

- `homepage-dark-light-section-rhythm.md` — applies in BOTH locales; gradient/motion budget unchanged
- `end-of-build-multi-breakpoint-browser-audit.md` — must run in BOTH locales for bilingual sites
- `optimus-luxury-modern-positioning.md` — visual floor unchanged across locales

---

Status: VALIDATED — 2026-05-02
