# Website Build Template — Luxury Personal Brand

> Derived from the Gray Method Training build. Apply this template to any service-based personal brand, coach, consultant, or creator website. Replace all brand-specific copy, colors, and assets — the architecture, animation patterns, and conversion infrastructure stay the same.

---

## Stack

| Layer | Technology | Notes |
|-------|-----------|-------|
| Framework | Next.js (App Router) | ISR for blog/dynamic content |
| Styling | Tailwind CSS 4 + PostCSS | Custom design tokens in `globals.css` |
| Animations | Framer Motion + `react-intersection-observer` | All scroll-triggered |
| CMS | Sanity | Blog, testimonials, dynamic content |
| E-commerce | Stripe + Printful + Resend | Custom React cart, hosted checkout, POD fulfillment, owner alerts |
| Forms | React Hook Form + Zod | Quiz, contact, newsletter |
| Payments | Stripe | Checkout sessions |
| Analytics | Vercel Analytics | Core Web Vitals |
| Images | Next.js Image + Sharp | Responsive srcsets |

---

## Design Tokens

Define these CSS custom properties in `globals.css` before writing any components. Everything inherits from them.

```css
:root {
  /* Brand Colors — swap these per client */
  --primary: rgb(200, 169, 110);        /* Gold/accent */
  --primary-muted: rgba(200, 169, 110, 0.6);
  --accent: rgb(232, 98, 26);           /* Secondary accent */

  /* Background Scale (dark theme) */
  --bg-base: #0a0a0a;
  --bg-elevated: #141414;
  --bg-card: #1a1a1a;

  /* Text Scale */
  --text-primary: #f5f5f5;
  --text-secondary: rgba(245, 245, 245, 0.7);
  --text-muted: rgba(245, 245, 245, 0.4);
}
```

**Typography:**
- `font-display` — Headlines (large, bold, high impact)
- `font-body` — Paragraph text (readable, neutral)
- `font-mono` — Labels, eyebrows, UI micro-copy

---

## Directory Structure

```
/src
  /app
    page.tsx                     ← Homepage (compose sections here)
    layout.tsx                   ← Root layout (fonts, analytics, Snipcart)
    /about/page.tsx
    /services/page.tsx           ← Or /programs
    /services/[slug]/page.tsx    ← Individual service pages
    /pricing/page.tsx            ← ROI calculator + tier comparison
    /quiz/page.tsx               ← Multi-step quiz (QuizClient.tsx)
    /blog/page.tsx
    /blog/[slug]/page.tsx
    /shop/page.tsx
    /reviews/page.tsx
    /contact/page.tsx
    /studio/[[...tool]]/page.tsx ← Sanity CMS editor
    /api
      /contact/route.ts
      /newsletter/route.ts
      /printful/products/route.ts
      /printful/variants/[id]/route.ts  ← variant sizes + colors for picker
      /stripe/checkout/route.ts
      /stripe/webhook/route.ts          ← CRITICAL: fulfillment trigger
      /revalidate/route.ts

  /components
    /animations                  ← Reusable animation wrappers
    /layout                      ← Navbar, MobileNav, Footer
    /sections                    ← Full-width page sections
    /blog                        ← PostCard, PostBody, TOC, Newsletter
    /shop                        ← CartDrawer, ProductCard, VariantPicker
    /ui                          ← Button, Card, Badge, Input, Divider

  /data
    site.ts                      ← ALL copy/content lives here
    shop.ts                      ← Product catalog

  /lib
    cart.tsx                     ← React Context cart (NOT Snipcart)
    printful.ts                  ← Printful API client + TypeScript interfaces
    printful-seeded-products.json ← Fallback data when Printful API is down
    photos.ts                    ← Photo asset mappings
    utils.ts                     ← prefersReducedMotion, cn(), etc.

  /sanity
    /lib
      client.ts
      queries.ts                 ← GROQ queries
      image.ts
    /schemaTypes
      post.ts
      category.ts
      author.ts
      blockContent.ts
```

> **Rule:** All copy lives in `/data/site.ts`. No hard-coded strings in components. This makes client handoff and future edits trivial.

---

## Animation Library

Build these eight wrappers once. Use them everywhere. All respect `prefers-reduced-motion`.

```tsx
// /components/animations/FadeIn.tsx
// Opacity 0 → 1, scroll-triggered via useInView
// Props: delay?, duration?, threshold?

// /components/animations/FadeUp.tsx
// Opacity + Y translate (-20px → 0), scroll-triggered
// Most common wrapper for section content

// /components/animations/SlideIn.tsx
// X translate + fade, direction prop: "left" | "right"

// /components/animations/ScaleIn.tsx
// Scale (0.9 → 1) + opacity, good for cards

// /components/animations/StaggerContainer.tsx
// Wraps children, applies staggered delay to each child
// Props: staggerDelay? (default 0.1s)

// /components/animations/CountUp.tsx
// Animates a number from 0 to target when in view
// Props: end, duration?, decimals?, suffix?

// /components/animations/ParallaxWrapper.tsx
// Scroll-speed offset for depth effects

// /components/animations/RevealText.tsx
// Word-by-word or character reveal
// Props: text, type: "words" | "chars", stagger?
```

**Pattern for every scroll animation:**

```tsx
const { ref, inView } = useInView({ threshold: 0.2, triggerOnce: true });

<motion.div
  ref={ref}
  initial={{ opacity: 0, y: 20 }}
  animate={inView ? { opacity: 1, y: 0 } : {}}
  transition={{ duration: 0.6, delay }}
/>
```

---

## Section 1 — Luxury Hero

**Goal:** Stop the scroll, establish authority, drive two actions.

### Layout

```
[Left 55%]                          [Right 45%]
  Eyebrow label (mono, primary)       Client photo or brand image
  H1 Headline (display, shimmer)      Rounded border + inset glow
  Tagline (word-by-word reveal)
  [CTA Primary] [CTA Secondary]
  Trust micro-copy (★ · years · stat)
```

Mobile: single column, image hidden or below copy.

### Animation 1 — Canvas Particle System (`HeroParticles.tsx`)

Replace the static background. Three particle types rendered on `<canvas>`:

| Type | Count | Behavior | Color |
|------|-------|----------|-------|
| Stars | ~145 | Twinkle, slow drift | White/primary |
| Embers | ~58 | Rise upward, fade out | Primary/accent |
| Glimmers | Occasional | 4-point star burst, flash | White |

```tsx
// Initialization pattern
const STAR_COUNT = 145;
const EMBER_COUNT = 58;

// Each particle has: x, y, vx, vy, opacity, targetOpacity, size, color
// requestAnimationFrame loop at 60fps
// Canvas resizes with window via ResizeObserver
```

### Animation 2 — Three Breathing Orbs

Radial gradient blobs behind the content. Pure CSS `@keyframes`:

```tsx
// Orb 1 — Bottom left, primary color, 12s breathing cycle
// Orb 2 — Top right, muted primary, offset phase (+4s delay)
// Orb 3 — Top center, accent, scale + opacity pulse

<div className="orb orb-1" /> // position: absolute, pointer-events: none
<div className="orb orb-2" />
<div className="orb orb-3" />
```

```css
@keyframes breathe {
  0%, 100% { transform: scale(1); opacity: 0.15; }
  50% { transform: scale(1.15); opacity: 0.25; }
}
.orb { animation: breathe 12s ease-in-out infinite; }
.orb-2 { animation-delay: -4s; }
.orb-3 { animation: breathe 8s ease-in-out infinite; }
```

### Animation Sequence (Hero Load Order)

| Element | Delay | Animation |
|---------|-------|-----------|
| Eyebrow | 0.1s | FadeIn |
| Headline | 0.3s | FadeIn + Y up |
| Tagline | 0.9s | Word-by-word reveal (0.06s stagger per word) |
| CTAs | 2.4s | FadeIn |
| Trust copy | 2.8s | FadeIn |

### CTA Pair Pattern

```tsx
<div className="flex gap-4 flex-wrap">
  <Button variant="gold" size="lg" href="/booking">
    {hero.ctaPrimary}         {/* "Schedule a Free Call" */}
  </Button>
  <Button variant="ghost" size="lg" href="/quiz">
    {hero.ctaSecondary}       {/* "Take the Quiz" */}
  </Button>
</div>

{/* Trust micro-copy below buttons */}
<p className="text-muted font-mono text-sm mt-4">
  {hero.trustCopy}             {/* "4.9★ rating · 11+ years · 100% recommend" */}
</p>
```

---

## Section 2 — Pain Points

**Goal:** Mirror the prospect's internal struggle so they feel seen.

```tsx
// 4 cards in a 2x2 grid (desktop) / 1-col (mobile)
// Each card: emoji + headline + 1-2 line description
// ScaleIn animation, staggered 0.1s per card
// Border: 1px var(--primary-muted) on hover
// No CTAs — this section is only empathy
```

Data shape:
```ts
painPoints: [
  { emoji: "⚡", headline: "Can't stay consistent", body: "..." },
  { emoji: "🪫", headline: "Always drained", body: "..." },
  { emoji: "📉", headline: "Stuck on results", body: "..." },
  { emoji: "🧠", headline: "Stress derails everything", body: "..." },
]
```

---

## Section 3 — About / Founder Story

**Goal:** Build trust through credibility + vulnerability. One human, not a brand.

### Layout Options

**Option A (Text-heavy, intimate):**
```
Eyebrow: "Meet [Name]"
H2: Origin story headline
2-3 paragraphs: journey, turning point, mission
Credentials list (inline badges or simple list)
Photo: full-bleed right side or below
```

**Option B (Stats + story):**
```
Stats row: [X years] [X clients] [X rating]  ← CountUp animations
Narrative below
Photo left
```

### Animation Pattern
- SlideIn from left for photo, from right for copy
- Stats row: CountUp triggers on scroll
- Stagger paragraphs with FadeUp (0.15s between each)

---

## Section 4 — Services / Programs

**Goal:** Show the range of engagement levels. One should feel like the obvious right fit.

### 3-Card Layout (Standard)

```tsx
// Card structure:
// Badge (optional: "Most Popular", "Limited Spots")
// Icon or photo
// Service name (H3)
// One-line positioning statement
// 3-4 bullet points
// Price anchor (optional at this stage)
// CTA button → individual service page
```

**Highlight the middle tier** with a border, background lift, or badge. This anchors perception and drives that choice.

```tsx
// Featured card gets: border border-primary, bg-elevated vs bg-card
// Non-featured: opacity-90, hover lifts to match featured styling
```

### Individual Service Pages (`/services/[slug]`)

Each service page follows this skeleton:
```
1. Hero (service name, who it's for, primary CTA)
2. What you get (bullet list with icons)
3. Who it's for (3 persona cards)
4. How it works (numbered steps)
5. Testimonials specific to this service
6. FAQ (Radix Accordion)
7. Final CTA
```

---

## Section 5 — Testimonials / Reviews

**Goal:** Social proof from people who look like the prospect.

### Homepage Section (3-4 featured)

```tsx
// Grid: 3-col desktop, 1-col mobile
// Each card:
//   Avatar (circular, 60px)
//   Name + identifier (e.g., "Sarah M. · 6-month client")
//   Star rating (5 gold stars)
//   Quote (2-4 sentences, first-person)
//   Optional: transformation stat ("Lost 18lbs in 90 days")
```

### Full Reviews Page (`/reviews`)

- All testimonials from `site.ts`
- Filter by program type (optional, use URL params)
- Featured quote at top (full-width, large type)
- Grid below
- Video testimonials section (if available) — YouTube embeds

### Data Shape

```ts
testimonials: [
  {
    name: "Ava R.",
    identifier: "3-month 1:1 client",
    rating: 5,
    quote: "...",
    program: "one-on-one",
    stat: "Down 22lbs",            // optional
    photo: "testimonialAva",       // key into photos.ts
  }
]
```

---

## Section 6 — Blog Architecture

**CMS:** Sanity (headless, schema-driven)

### Sanity Schema — Post

```ts
// Fields:
title: string (required)
slug: slug (auto from title, required)
publishedAt: datetime (required)
mainImage: image (with alt text)
excerpt: text (max 300 chars)
categories: array<reference to category>
body: blockContent (Portable Text)
seo: {
  metaTitle: string (max 60 chars)
  metaDescription: string (max 160 chars)
}
```

### Blog Index Page

```
1. Featured post — large card, full-width (first/pinned post)
2. Post grid — 3-col desktop, 1-col mobile
3. Category filter (optional)
4. Newsletter signup CTA at bottom
```

### Blog Post Page (`/blog/[slug]`)

```
Layout: 70/30 split (article / sidebar) on desktop

Article:
  - Hero image (full-width)
  - Title, date, category badge, reading time
  - PostBody (Portable Text → semantic HTML)
  - NewsletterSignup (end of post)

Sidebar:
  - TableOfContents (auto from h2/h3 headers)
  - Author card
  - Related posts (by category)
```

### TableOfContents Implementation

```tsx
// Parse heading nodes from Portable Text body
// Build anchor IDs (slugified heading text)
// Render sticky sidebar nav
// Highlight active section on scroll via IntersectionObserver
```

### ISR + Revalidation

```ts
// app/blog/[slug]/page.tsx
export const revalidate = 3600; // hourly

// Sanity webhook → /api/revalidate → revalidatePath('/blog')
// This means live edits in Sanity appear within seconds
```

---

## Section 7 — Shop Architecture

**Stack:** Custom React Context cart + Stripe hosted checkout + Printful API (POD fulfillment) + Resend (owner order alerts)

> This architecture was battle-tested in production on `coachandreaabellamarie.com`. Every gotcha below was discovered in a real live-money transaction. Follow it exactly.

### Fulfillment Model

Two product types with different fulfillment paths — both flow through the same cart and Stripe checkout:

| Type | Fulfillment | Who ships | Examples |
|------|-------------|-----------|---------|
| POD (Print-on-Demand) | Printful API — automatic | Printful ships to customer | Tees, hoodies, mugs, tumblers |
| Manual / Handmade | Flagged in owner email — manual | Owner ships | Jewelry, signed prints, handmade items |

The webhook splits cart items by product ID at checkout time. POD items go straight to Printful. Manual items get flagged in the owner alert email.

---

### Data Shape (`/data/shop.ts` or `/src/lib/products.ts`)

```ts
export interface Product {
  id: string | number       // For POD: use Printful sync product ID (number)
                            // For manual: use a stable slug string (e.g. "resilience-necklace")
  name: string
  price: number
  description: string
  category: string
  badge?: string            // "LIMITED STOCK", "NEW", etc.
  image?: string            // absolute URL or /public path
  printful_variant_id?: number  // pre-set if you want to skip variant resolution at checkout
  variants?: Variant[]      // loaded dynamically from /api/printful/variants/[id]
}
```

**Manual fulfillment items** use a string slug as their ID. Register those slugs in the webhook's `RESILIENCE_IDS` set (see webhook section below). As long as the ID is in that set, it routes to manual — never to Printful.

---

### Shop Page Layout

```
1. Page hero (eyebrow + headline + 1-line description)
2. Category filter tabs: All / [category names]
3. Product grid: 3-col desktop, 2-col tablet, 1-col mobile
4. Each ProductCard:
     - Product image (next/image, absolute URLs for Printful CDN images)
     - Badge ("LIMITED STOCK" for manual items)
     - Name, price
     - Short description
     - Variant picker: color swatches + size chips (see below)
     - "Add to Cart" button
5. Skeleton loaders while variants fetch (never show broken UI)
6. ?success=true query param → success toast/banner after Stripe return
```

---

### Cart Context (`/src/lib/cart.tsx`)

Do NOT use Snipcart. Build a custom React Context cart. This gives full control over what metadata goes to Stripe, which is critical for the webhook.

```tsx
"use client";
import { createContext, useContext, useState, useEffect, useCallback } from "react";

export interface CartItem {
  id: string | number
  name: string
  price: number
  quantity: number
  image?: string
  selectedSize?: string
  selectedColor?: string
  printful_variant_id?: number  // CRITICAL — must be passed to Stripe → webhook → Printful
}

interface CartContextType {
  items: CartItem[]
  isOpen: boolean
  addItem: (item: CartItem) => void
  removeItem: (id: string | number) => void
  updateQuantity: (id: string | number, qty: number) => void
  clearCart: () => void
  openCart: () => void
  closeCart: () => void
  total: number
  count: number
}

// Persist to localStorage — cart survives page refresh
// Key: "cart" — serialize/deserialize on mount
// CartDrawer: slides in from right, shows items + checkout button
// Navbar: shows item count badge via useCart()
```

**On "Add to Cart":** The item must include `printful_variant_id` (the Printful sync variant ID). This ID flows through Stripe metadata and is used by the webhook to create the Printful order. If it's missing, the webhook falls back to resolving the first available variant — which may be wrong for size-specific items.

---

### Variant Picker (`VariantPicker` or inline in `ProductCard`)

Variants are fetched live from `/api/printful/variants/[syncProductId]` when a user clicks a product.

```tsx
// Show skeleton while loading
// Render:
//   - Color swatches: circular buttons with hex color fill, border on selected
//   - Size chips: text buttons, border on selected
// Color-only products (tumblers, mugs) have no size selector
// Size-only products have no color selector
// On select: update state, look up matching variant, set printful_variant_id on cart item
```

**Color Swatch Map** — Add these to `ShopContent.tsx` or a shared `colorMap.ts`. Lookup MUST be case-insensitive (Printful returns inconsistent casing):

```ts
const COLOR_MAP: Record<string, string> = {
  "Black": "#1a1a1a",
  "White": "#ffffff",
  "Navy": "#1a2744",
  "Navy Blue": "#1a2744",
  "Forest Green": "#2d4a2d",
  "Military Green": "#4a5c3a",
  "Bottle Green": "#1e3d2f",
  "Sport Grey": "#9a9a9a",
  "Dark Heather": "#5a5a5a",
  "Heather": "#b0b0b0",
  "Maroon": "#6b1a1a",
  "Red": "#cc2200",
  "Royal Blue": "#1a4799",
  "Royal": "#1a4799",
  "Purple": "#5a2d82",
  "Gold": "#c8a96e",
  "Ash": "#d4d4d4",
  "Sand": "#d4c4a0",
  "Charcoal": "#3a3a3a",
  "Storm": "#6a7a8a",
  "Light Blue": "#87b8d4",
  "Vintage White": "#f5f0e8",
  // ... add more as needed
};

// Case-insensitive lookup helper:
const normalizeKey = (k: string) =>
  k.toLowerCase().replace(/\b\w/g, (c) => c.toUpperCase());

const getColorHex = (color: string): string =>
  COLOR_MAP[color] ?? COLOR_MAP[normalizeKey(color)] ?? "#999999";
```

---

### Variant Name Parser (`/api/printful/variants/[id]/route.ts`)

Printful variant names come in two formats. The parser must handle both correctly or color/size assignment breaks.

```ts
// KNOWN_COLORS — used to detect if a name segment is a color vs a size
const KNOWN_COLORS = new Set([
  "Black", "White", "Navy", "Navy Blue", "Red", "Forest Green", "Military Green", "Bottle Green",
  "Storm", "Sport Grey", "Dark Heather", "Heather", "Maroon", "Ash", "Sand",
  "Royal", "Royal Blue", "Purple", "Orange", "Gold", "Yellow", "Pink", "Light Pink",
  "Charcoal", "Light Blue", "Vintage White", "Carolina Blue", "Heather Blue", "Olive",
  "Brown", "Chocolate", "Burgundy", "Mustard", "Cream", "Cranberry", "Dark Navy",
  "Slate", "Mint", "Coral", "Teal", "Indigo", "Green", "Blue", "Grey", "Gray",
  "Silver", "Rose Gold", "Rose", "Lavender", "Sky Blue", "Cobalt", "Aqua",
]);

function parseVariantName(name: string): { size: string; color: string } {
  const parts = name.split(" / ").map((p) => p.trim());

  if (parts.length === 1) {
    // e.g. "One Size" — no color
    return { size: parts[0], color: "" };
  }

  if (parts.length === 2) {
    // e.g. "Insulated tumbler / Black" → color=Black, size=""
    // e.g. "S / Black" → size=S, color=Black
    // e.g. "L / Forest Green" → size=L, color=Forest Green
    const [a, b] = parts;
    if (KNOWN_COLORS.has(b)) {
      return { size: a === name.split(" / ")[0] && !KNOWN_COLORS.has(a) ? a : "", color: b };
    }
    return { size: b, color: a };
  }

  if (parts.length >= 3) {
    // e.g. "Unisex Hoodie / S / Black" → size=S, color=Black
    // Last segment is usually color, middle is size
    const candidate1 = parts[parts.length - 2]; // size candidate
    const candidate2 = parts[parts.length - 1]; // color candidate
    if (KNOWN_COLORS.has(candidate2)) {
      return { size: candidate1, color: candidate2 };
    }
    // Guard: sometimes order is reversed — "Product / Black / S"
    if (KNOWN_COLORS.has(candidate1) && !KNOWN_COLORS.has(candidate2)) {
      return { size: candidate2, color: candidate1 };
    }
    return { size: candidate1, color: candidate2 };
  }

  return { size: "", color: "" };
}
```

---

### Seeded Fallback Data (`/src/lib/printful-seeded-products.json`)

The Printful API can be slow or unavailable. Keep a seeded JSON snapshot so the shop always renders.

```json
{
  "storeId": 12345678,
  "products": [
    {
      "printful_id": 987654321,
      "slug": "black-glossy-mug-15oz",
      "name": "Black Glossy Mug 15oz",
      "description": "...",
      "price": 21.00,
      "category": "drinkware",
      "images": ["https://cdn.printful.com/..."]
    }
  ]
}
```

The `/api/printful/products` route tries the live API first, falls back to the seeded file on error. `storeId` in this file is used by the webhook — keep it accurate.

---

### API Route: Stripe Checkout (`/api/stripe/checkout/route.ts`)

```ts
export async function POST(req: NextRequest) {
  const { items }: { items: CartItemPayload[] } = await req.json();

  const stripe = new Stripe(process.env.STRIPE_SECRET_KEY!, {
    apiVersion: "2026-02-25.clover",
  });

  const session = await stripe.checkout.sessions.create({
    payment_method_types: ["card"],
    mode: "payment",
    customer_creation: "always",  // ← REQUIRED: ensures Stripe sends receipt email to customer
    line_items: items.map((item) => ({
      price_data: {
        currency: "usd",
        product_data: {
          name: item.name,
          // Only pass images if they are absolute HTTPS URLs
          // Local /public paths will cause Stripe to silently drop the image
          ...(item.image?.startsWith("http") ? { images: [item.image] } : {}),
        },
        unit_amount: Math.round(item.price * 100),
      },
      quantity: item.quantity,
    })),
    shipping_address_collection: {
      allowed_countries: ["US", "CA", "GB", "AU", "NZ"],
    },
    success_url: `${siteUrl}/shop?success=true`,
    cancel_url: `${siteUrl}/shop`,
    metadata: {
      // Store full cart as JSON — webhook reads this to create Printful order
      cart: JSON.stringify(
        items.map((i) => ({
          id: i.id,
          name: i.name,
          quantity: i.quantity,
          price: i.price,
          printful_variant_id: i.printful_variant_id, // ← CRITICAL
        }))
      ),
    },
  });

  return NextResponse.json({ url: session.url });
}
```

---

### API Route: Stripe Webhook (`/api/stripe/webhook/route.ts`)

This is the fulfillment engine. It fires after every successful payment.

```ts
// Manual-fulfillment item IDs — anything in this set routes to owner email, NOT Printful
const MANUAL_ITEM_IDS = new Set([
  "resilience-necklace",
  "inner-peace-lotus-earrings",
  // add more handmade/manual items here
]);

export async function POST(req: NextRequest) {
  const body = await req.text();
  const sig = req.headers.get("stripe-signature")!;

  // Always verify the signature — never skip this
  const event = stripe.webhooks.constructEvent(body, sig, process.env.STRIPE_WEBHOOK_SECRET!);

  if (event.type === "checkout.session.completed") {
    const session = event.data.object as Stripe.Checkout.Session;

    // 1. Parse cart from metadata
    const cart: CartItem[] = JSON.parse(session.metadata?.cart ?? "[]");

    // 2. Collect shipping address
    const shipping = (session as any).collected_information?.shipping_details
      ?? (session as any).shipping_details;

    // 3. Split POD vs manual
    const manualItems = cart.filter((i) => MANUAL_ITEM_IDS.has(String(i.id)));
    const podItems = cart.filter((i) => !MANUAL_ITEM_IDS.has(String(i.id)));

    // 4. Create Printful order for POD items
    if (podItems.length > 0 && shipping?.address) {
      const orderPayload = {
        recipient: {
          name: shipping.name ?? session.customer_details?.name ?? "Customer",
          address1: shipping.address.line1 ?? "",
          city: shipping.address.city ?? "",
          state_code: shipping.address.state ?? "",
          country_code: shipping.address.country ?? "US",
          zip: shipping.address.postal_code ?? "",
          email: session.customer_details?.email ?? undefined,
        },
        items: podItems.map((i) => ({
          sync_variant_id: i.printful_variant_id,  // must be the sync variant ID, not catalog ID
          quantity: i.quantity,
        })),
        confirm: true,  // passed as query param in printful.ts — NOT in this body
      };

      await createOrder(seededProducts.storeId, orderPayload);
    }

    // 5. Send owner alert via Resend (non-fatal — wrap in try/catch)
    await sendOrderAlertToOwner(session, cart, manualItems.length > 0);
  }

  return NextResponse.json({ received: true });
}
```

---

### Printful API Client (`/src/lib/printful.ts`)

Critical implementation details:

```ts
// ── createOrder: confirm MUST be a query param, NOT a body field ──
export async function createOrder(storeId: number, orderData: OrderData): Promise<Order> {
  const { confirm, ...body } = orderData;
  const path = confirm ? "/orders?confirm=true" : "/orders";
  //           ↑ query param — Printful ignores confirm in the request body
  return pfetch<Order>(path, {
    method: "POST",
    storeId,
    body: JSON.stringify(body),  // body does NOT include confirm
  });
}

// ── Store ID header: required for all store-scoped endpoints ──
function getHeaders(storeId?: number) {
  const headers: Record<string, string> = {
    Authorization: `Bearer ${process.env.PRINTFUL_API_KEY}`,
    "Content-Type": "application/json",
  };
  if (storeId) headers["X-PF-Store-Id"] = String(storeId);
  return headers;
}
```

---

### Owner Order Alert (`sendOrderAlertToOwner`)

```ts
import { Resend } from "resend";

async function sendOrderAlertToOwner(
  session: Stripe.Checkout.Session,
  cart: CartItem[],
  hasManualItems: boolean
) {
  if (!process.env.RESEND_API_KEY) return; // skip silently if not configured

  const resend = new Resend(process.env.RESEND_API_KEY);
  const total = ((session.amount_total ?? 0) / 100).toFixed(2);
  const customer = session.customer_details;

  const manualFlag = hasManualItems
    ? "\n⚠️  MANUAL FULFILLMENT REQUIRED — ship these items yourself.\n"
    : "";

  const itemLines = cart
    .map((i) => `  • ${i.name} x${i.quantity} — $${i.price.toFixed(2)}`)
    .join("\n");

  try {
    await resend.emails.send({
      from: "orders@yourdomain.com",       // must be on a Resend-verified domain
      to: "owner@email.com",
      subject: `New Order — $${total}`,
      text: `New order!\n${manualFlag}\nCustomer: ${customer?.name} <${customer?.email}>\nTotal: $${total}\n\nItems:\n${itemLines}\n\nStripe: ${session.id}`,
    });
  } catch (err) {
    console.error("[webhook] Failed to send order alert:", err); // non-fatal
  }
}
```

**Resend setup:**
1. Create account at resend.com (free — 3,000 emails/month)
2. Add and verify your sending domain (GoDaddy: use "Auto-configure" — it sets DKIM + SPF automatically)
3. Create an API key → add to Vercel as `RESEND_API_KEY`
4. Use `from: "orders@yourdomain.com"` — must match the verified domain

---

### Infrastructure Gotchas — Learn From Production

These bugs cost real money to discover. Don't repeat them:

**1. Stripe webhook URL must match canonical domain exactly — no redirects**
- If your domain redirects `example.com` → `www.example.com`, register the webhook as `https://www.example.com/api/stripe/webhook`
- Stripe does NOT follow HTTP redirects. A 307 redirect = webhook silently fails
- Fix: check Stripe Dashboard → Webhooks → your endpoint URL. Must be the final URL, not the redirecting one
- Also set `NEXT_PUBLIC_SITE_URL=https://www.example.com` (with www) in Vercel

**2. Printful `confirm=true` is a query param, NOT a body field**
- Orders created without `?confirm=true` land as **Draft** — Printful will not fulfill them
- The `confirm` field in the request body is silently ignored by Printful
- Pattern: `POST /orders?confirm=true` with confirm removed from the JSON body

**3. Stripe guest checkout does not send customer receipts by default**
- Add `customer_creation: "always"` to the Stripe checkout session
- Without this, guest customers get no receipt email

**4. Printful billing card must be on file with sufficient funds**
- When Printful creates and confirms an order, they immediately charge the store owner's card
- If the card fails, the order stays in "Waiting for transaction approval" and will not ship
- Ensure the owner has an active payment method in Printful → Billing → Payments

**5. Only pass absolute HTTPS image URLs to Stripe**
- `/public/images/product.jpg` will cause Stripe to silently drop the image
- Printful CDN URLs (`https://cdn.printful.com/...`) work fine

**6. Printful variant IDs: sync variant ID ≠ catalog variant ID**
- `sync_variant_id` (used in order creation) is the ID from the store's sync product
- `variant_id` is the catalog variant — cannot be used to create orders
- Fetch sync variant IDs via `GET /store/products/{syncProductId}` → `sync_variants[].id`

**7. Resend API key security**
- Never paste your Resend API key in a screenshot or share it in any channel
- If exposed: immediately go to Resend → API Keys → revoke + create new → update Vercel env var + redeploy

---

### Checklist: Printful Store Setup

Before any live purchase:
- [ ] Printful store created, connected to your account
- [ ] Products synced to store (create sync products via dashboard or API)
- [ ] Store ID noted — goes in `printful-seeded-products.json`
- [ ] Printful billing: active payment method on file
- [ ] In Printful → Store → Settings: confirm "Send shipping notifications to end customers" is ON
- [ ] Test order created in Printful manually to verify card works

### Checklist: Stripe Setup

- [ ] Stripe account in live mode
- [ ] Webhook registered at `https://www.yourdomain.com/api/stripe/webhook` (with www if that's your canonical)
- [ ] Webhook event: `checkout.session.completed` only
- [ ] Webhook secret copied → Vercel `STRIPE_WEBHOOK_SECRET`
- [ ] `shipping_address_collection` allowed countries match your Printful shipping zones

---

## Section 8 — Quiz (Engagement + Lead Acquisition)

**Goal:** Segment the prospect, generate qualified lead data, deliver personalized CTA.

### 3-Step Flow

```
Step 0 — Intro screen
  Headline: "Find Your Perfect Plan"
  3 bullet points explaining what the quiz does
  CTA: "Start the Quiz →"

Step 1 — Problems (multi-select, 6 options)
  Headline: "What's holding you back right now?"
  Options with emojis (visual, scannable)
  Continue button (disabled until ≥1 selected)

Step 2 — Goals (single-select, 4 options)
  Headline: "What matters most to you?"
  Options with emojis
  Continue button (disabled until 1 selected)

Step 3 — Lead capture form
  Fields: Name (required), Email (required), Message (optional)
  CTA: "Get My Personalized Plan →"
  Trust copy below button: "No spam. Just your results."

Post-submit — Results screen
  Show selected problems + goal
  Personalized message based on selections
  Primary CTA: "Schedule Your Free Call"
  Secondary CTA: "Explore Programs"
```

### Implementation (`QuizClient.tsx`)

```tsx
// State
const [step, setStep] = useState(0);              // 0=intro, 1=problems, 2=goals, 3=form, 4=results
const [selectedProblems, setSelectedProblems] = useState<string[]>([]);
const [selectedGoal, setSelectedGoal] = useState<string>("");

// Progress bar
const progress = step === 0 ? 0 : ((step - 1) / 3) * 100;

// Step transitions via AnimatePresence + variants
<AnimatePresence mode="wait">
  <motion.div key={step} initial="hidden" animate="visible" exit="exit">
    {renderStep(step)}
  </motion.div>
</AnimatePresence>

// Form submission → /api/contact with quiz data appended
// Include: name, email, message, selectedProblems, selectedGoal
```

### Quiz CTA Section (Homepage)

```tsx
// Teaser section before footer
// Headline: "Not sure where to start?"
// Sub: "Take the 2-minute quiz..."
// Large CTA button → /quiz
// Background: subtle gradient or pattern
```

---

## Section 9 — Pricing Page

**Goal:** Eliminate price objection, show ROI, drive tier selection.

> **IMPORTANT:** The Tier Comparison Chart and ROI Calculator are **development/sales tools**. Remove or comment them out before the public page goes live. They exist to help the client understand value during the sales process — not to confuse public visitors.

---

### 9a — Three-Tier Pricing Cards

**Architecture principle:** Three tiers create anchoring. The middle tier should look "right." The top tier makes the middle look reasonable.

```tsx
// Tier data shape
tiers: [
  {
    name: "Starter",
    price: 1500,           // or monthly, or range
    badge: null,
    headline: "Get started",
    description: "...",
    features: string[],    // 5-7 bullet points
    cta: "Get Started",
    ctaHref: "/contact?tier=starter",
    featured: false,
  },
  {
    name: "Pro",
    price: 3000,
    badge: "Most Popular",
    headline: "The complete solution",
    description: "...",
    features: string[],    // 8-10 bullet points (more than Starter)
    cta: "Get Started",
    ctaHref: "/contact?tier=pro",
    featured: true,        // ← highlighted, larger card
  },
  {
    name: "Premium",
    price: 5500,
    badge: "Full Service",
    headline: "Done for you",
    description: "...",
    features: string[],
    cta: "Get Started",
    ctaHref: "/contact?tier=premium",
    featured: false,
  }
]
```

**Card layout:**
```
┌─────────────────────┐
│ [Badge if featured] │
│ Tier name           │
│ $X,XXX              │
│ Positioning line    │
│ ─────────────────── │
│ ✓ Feature 1         │
│ ✓ Feature 2         │
│ ✓ Feature 3         │
│ ...                 │
│ [CTA Button]        │
└─────────────────────┘
```

Featured card: `border border-primary`, larger `scale(1.02)` on desktop, full gold CTA button. Others: ghost/outline CTA.

---

### 9b — ROI Calculator (Dev/Sales Only — Remove Before Launch)

Interactive tool that helps the client see the financial return on their investment before committing.

**Three input sliders:**

| Slider | Range | Default | Label |
|--------|-------|---------|-------|
| Monthly leads from site | 1–20 | 10 | "Monthly website leads" |
| Close rate | 5%–50% | 25% | "Lead-to-client conversion rate" |
| Average client value | $500–$10,000 | $3,000 | "Average client lifetime value" |

**Calculated outputs (real-time, with CountUp animations):**

```ts
const closedPerMonth = leads * (closeRate / 100);
const revenuePerMonth = closedPerMonth * avgClientValue;
const revenuePerYear = revenuePerMonth * 12;
const breakEvenMonths = selectedTierPrice / revenuePerMonth;
const breakEvenClients = selectedTierPrice / avgClientValue;
```

**Display cards:**
```
┌──────────────────┐  ┌──────────────────┐  ┌──────────────────┐
│ Monthly Revenue  │  │ Annual Revenue   │  │ Break-even Time  │
│   $X,XXX         │  │   $XX,XXX        │  │   X.X months     │
└──────────────────┘  └──────────────────┘  └──────────────────┘
```

**Package selector tabs** above the calculator — switching tier updates all calculations instantly.

**Implementation:**

```tsx
// PricingClient.tsx (client component for interactivity)
const [selectedTier, setSelectedTier] = useState(1); // default: middle tier
const [leads, setLeads] = useState(10);
const [closeRate, setCloseRate] = useState(25);
const [avgValue, setAvgValue] = useState(3000);

// Use useMemo for calculated values
const metrics = useMemo(() => ({
  closedPerMonth: leads * (closeRate / 100),
  revenuePerMonth: leads * (closeRate / 100) * avgValue,
  revenuePerYear: leads * (closeRate / 100) * avgValue * 12,
  breakEvenMonths: tiers[selectedTier].price / (leads * (closeRate / 100) * avgValue),
  breakEvenClients: tiers[selectedTier].price / avgValue,
}), [leads, closeRate, avgValue, selectedTier]);
```

---

### 9c — Tier Comparison Chart (Dev/Sales Only — Remove Before Launch)

Feature matrix showing exactly what each tier includes. Helps client understand what they're buying.

```tsx
// Feature rows with ✓ / — indicators
const features = [
  { label: "Custom homepage & hero", starter: true, pro: true, premium: true },
  { label: "About / Contact / Services pages", starter: true, pro: true, premium: true },
  { label: "Mobile responsive", starter: true, pro: true, premium: true },
  { label: "Basic SEO setup", starter: true, pro: true, premium: true },
  { label: "Blog / CMS integration", starter: false, pro: true, premium: true },
  { label: "Instagram feed integration", starter: false, pro: true, premium: true },
  { label: "Testimonials section", starter: false, pro: true, premium: true },
  { label: "Quiz / lead capture", starter: false, pro: true, premium: true },
  { label: "Shop / e-commerce", starter: false, pro: false, premium: true },
  { label: "Revenue architecture", starter: false, pro: false, premium: true },
  { label: "Priority revisions", starter: false, pro: false, premium: true },
  { label: "1-on-1 training handoff", starter: false, pro: false, premium: true },
];

// Table header: Tier names with prices
// Featured column (Pro): highlighted background
// ✓ = checkmark icon in primary color
// — = dash in muted color
```

> **Remove before launch:** Wrap both the ROI Calculator and Comparison Chart in a `DEV_MODE` environment variable check, or simply delete the components once the client has signed.

```tsx
// Safest pattern:
{process.env.NEXT_PUBLIC_SHOW_PRICING_TOOLS === 'true' && (
  <>
    <ROICalculator />
    <TierComparisonChart />
  </>
)}
// Set NEXT_PUBLIC_SHOW_PRICING_TOOLS=false in production .env
```

---

## Navigation

### Navbar

```tsx
// Fixed header, full width
// Transparent on page load → blurred/dark bg on scroll
// Transition: useEffect listening to window.scrollY

// Left: Logo
// Center: Nav links (desktop only)
// Right: [Cart icon + count] [CTA button]

// Scroll detection:
const [scrolled, setScrolled] = useState(false);
useEffect(() => {
  const handler = () => setScrolled(window.scrollY > 20);
  window.addEventListener('scroll', handler);
  return () => window.removeEventListener('scroll', handler);
}, []);

// className: scrolled ? 'bg-bg-base/90 backdrop-blur-md' : 'bg-transparent'
```

### Mobile Nav

```tsx
// Hamburger icon opens drawer from right
// Spring animation (Framer Motion)
// Full-height overlay with nav links
// Closes on: link click, outside click, Escape key
// Include cart icon + CTA at bottom of drawer
```

### Nav Link Count Rule

If total nav links > 4:
- Primary nav: max 3 items (conversion-critical only — booking, services, contact)
- Remaining links: grouped under a "More" dropdown
- Never let the nav overflow or wrap to a second line at 390px

---

## Asset Placement Rules

All project media must live inside `/public`. Never commit assets to the repo root.

| Asset type | Directory | Naming convention |
|------------|-----------|-------------------|
| Hero video | `/public/videos/` | `hero-[descriptor].mp4` |
| Section images | `/public/images/` | `[section]-[descriptor].jpg` |
| AI-generated photos | `/public/images/` | `[section]-ai-[descriptor].jpg` |
| Client-provided photos | `/public/photos/` | original filename — do not rename |
| Logos / icons | `/public/brand/` | `logo.[ext]`, `favicon.[ext]` |
| OG / meta images | `/public/og/` | `og-[page].jpg` |

**Rule:** Claude must flag any media file not in `/public` before committing.
**Rule:** Video elements must always include `autoPlay muted loop playsInline` and a `poster` fallback image.

---

## AI Asset Generation

**Hero sections always use animated SVG — never a photo, never fal.ai.**
fal.ai is strictly for blog post card thumbnail images. Do not use it for heroes,
about pages, service cards, or OG images.

Service cards, about page, and OG images use real client photos when provided.
If not provided, build sections that work without photo content until photos arrive.

### Blog Card Images — fal.ai

Used for blog post card thumbnails only. Requires `FAL_KEY` in `.env.local`.

Prompt source: `design-system.md` → Section 6 (Photography & Media Direction)
Output: `/public/images/blog/` — commit immediately after generation

```ts
// scripts/generate-blog-images.ts
import * as fal from "@fal-ai/serverless-client";

fal.config({ credentials: process.env.FAL_KEY });

// Pull mood, setting, and prohibited content from design-system.md Section 6
// Generate one card image per blog article
// Save to /public/images/blog/ with slug-matching filenames
// Commit all outputs in the same commit as the script run
```

See: `knowledge/patterns/fal-ai-image-generation.md` for full implementation.

### Videos — Kling (manual step)

Kling (kling.ai) is a web app — not automatable via API.

1. Write scene prompt from `design-system.md` brand identity + photography direction
2. Generate in Kling → download as MP4
3. Place in `/public/videos/hero-[descriptor].mp4`
4. Implement:

```tsx
<video autoPlay muted loop playsInline poster="/images/hero-fallback.jpg">
  <source src="/videos/hero-[descriptor].mp4" type="video/mp4" />
</video>
```

See: `knowledge/patterns/kling-video-hero.md` for full implementation.

---

## Homepage Teaser Rule

**Every page on the site must have a teaser section on the homepage.**

The homepage is a curated preview of the entire site. Each internal page (services, blog,
about, quiz, booking, shop) gets a teaser block on the homepage that:
- Introduces the page in 1–3 sentences
- Shows enough to create desire (3 featured posts, 3 featured services, etc.)
- Has a clear CTA link to the full page

This keeps visitors on the homepage longer, signals depth to search engines, and ensures
every page gets organic discovery through the homepage.

| Page | Homepage Teaser Component |
|------|--------------------------|
| Services | `<ServicesPreview />` — 3 service cards with 1-line description + CTA |
| Blog | `<BlogPreview />` — 3 latest posts with title + excerpt + "Read more" |
| About | `<FounderStory />` — Origin paragraph + photo + link to full about page |
| Quiz | `<QuizCTA />` — "Not sure where to start?" hook + quiz launch button |
| Booking | `<BookingPreview />` — Calendly widget embedded inline (see Calendly section) |
| Shop | `<ShopPreview />` — 3 featured products + "Shop all" link |

Never create a page that has no presence on the homepage. If the page exists, it gets a teaser.

---

## Calendly Booking Widget

**Use Calendly. Not cal.com. Not a redirect link.**

Calendly is the standard booking tool across all Optimus projects. It must be embedded
directly inside the site — never as a redirect to calendly.com. The goal is that the
visitor never feels like they left the site.

### Environment Variable

```env
NEXT_PUBLIC_CALENDLY_URL=https://calendly.com/[clientname]/[eventtype]
```

Add to Vercel environment variables at project setup. This is a standard variable on
every project that has a booking flow.

### Inline Widget Component

```tsx
// components/sections/BookingWidget.tsx
"use client";
import { useEffect } from "react";

interface BookingWidgetProps {
  url?: string;
  className?: string;
}

export function BookingWidget({ url, className }: BookingWidgetProps) {
  const calendlyUrl = url ?? process.env.NEXT_PUBLIC_CALENDLY_URL ?? "";

  useEffect(() => {
    const script = document.createElement("script");
    script.src = "https://assets.calendly.com/assets/external/widget.js";
    script.async = true;
    document.body.appendChild(script);
    return () => { document.body.removeChild(script); };
  }, []);

  return (
    <div
      className={`calendly-inline-widget ${className ?? ""}`}
      data-url={`${calendlyUrl}?background_color=0a0a0a&text_color=f5f5f5&primary_color=${encodeURIComponent(
        "var(--primary-hex, c8a96e)"
      )}`}
      style={{ minWidth: "320px", height: "700px" }}
    />
  );
}
```

**Brand color params** — pass background_color, text_color, and primary_color as URL params.
Pull primary_color from the client's design system. The widget will match the site's theme.

**Placement** — embed in `/app/booking/page.tsx` and as a teaser section on the homepage.
The homepage version can be height-constrained with `overflow: hidden` to show the first
week of availability without the full calendar chrome.

See Pattern #13 in build-log.md for full implementation details.

---

## Google Maps Embed

**Always use the real Google Maps iframe. No API key required.**

Center the map on the client's service area — not just their address. For service-area
businesses (fence contractors, mobile services, regional consultants), set the zoom level
to show the full territory they cover, not a street-level pin.

```tsx
// components/sections/ServiceAreaMap.tsx
export function ServiceAreaMap({
  location,
  zoom = 11,
}: {
  location: string;   // e.g. "Nashua, NH" or "New England, USA"
  zoom?: number;
}) {
  const src = `https://maps.google.com/maps?q=${encodeURIComponent(location)}&z=${zoom}&output=embed`;

  return (
    <div className="relative w-full h-[400px] rounded-xl overflow-hidden border border-white/10">
      <iframe
        src={src}
        width="100%"
        height="100%"
        style={{ border: 0 }}
        allowFullScreen
        loading="lazy"
        referrerPolicy="no-referrer-when-downgrade"
        title={`${location} service area map`}
      />
    </div>
  );
}
```

**Zoom guide:**
| Business type | Recommended zoom |
|---------------|-----------------|
| Single address (office, studio) | 15–16 |
| City-wide service area | 12–13 |
| Multi-city / regional | 9–11 |
| State or multi-state | 7–8 |

See Pattern #11 in build-log.md for notes on iframe compatibility.

---

## Homepage Composition

Assemble sections in this order. Each is a separate component, full viewport width.

```tsx
// app/page.tsx
export default function HomePage() {
  return (
    <>
      <Hero />              {/* 1. Hook */}
      <PainPoints />        {/* 2. Empathy */}
      <FounderStory />      {/* 3. Trust — teaser for /about */}
      <Philosophy />        {/* 4. Methodology / Why */}
      <Services />          {/* 5. What you offer — teaser for /services */}
      <ShopPreview />       {/* 6. Products — teaser for /shop (if applicable) */}
      <Stats />             {/* 7. Social proof — numbers */}
      <Testimonials />      {/* 8. Social proof — humans */}
      <InstagramFeed />     {/* 9. Live / current (optional) */}
      <QuizCTA />           {/* 10. Engagement hook — teaser for /quiz */}
      <BlogPreview />       {/* 11. Authority content — teaser for /blog */}
      <BookingPreview />    {/* 12. Calendly widget inline — teaser for /booking */}
      <FinalCTA />          {/* 13. Last chance CTA */}
    </>
  );
}
```

---

## API Routes

| Route | Method | Purpose |
|-------|--------|---------|
| `/api/contact` | POST | Contact form + quiz submission → email |
| `/api/newsletter` | POST | Newsletter signup → email list |
| `/api/printful/products` | GET | Fetch Printful sync catalog; falls back to seeded JSON |
| `/api/printful/variants/[id]` | GET | Fetch variant sizes + colors for picker; parses KNOWN_COLORS |
| `/api/stripe/checkout` | POST | Create Stripe checkout session; stores cart in metadata |
| `/api/stripe/webhook` | POST | **Fulfillment trigger** — splits POD/manual, creates Printful order, alerts owner |
| `/api/instagram` | GET | Proxy Instagram Graph API |
| `/api/revalidate` | POST | ISR webhook from Sanity |

---

## Content Data Structure (`/data/site.ts`)

Every piece of copy should live here. Zero hard-coded strings in components.

```ts
export const siteData = {
  brand: {
    name: string,
    tagline: string,
    logo: string,
  },
  nav: {
    links: Array<{ label: string, href: string }>,
    cta: { label: string, href: string },
  },
  hero: {
    eyebrow: string,
    headline: string,
    tagline: string,
    ctaPrimary: { label: string, href: string },
    ctaSecondary: { label: string, href: string },
    trustCopy: string,
  },
  painPoints: Array<{ emoji, headline, body }>,
  about: { headline, paragraphs[], credentials[], stats[] },
  philosophy: { headline, pillars: Array<{ icon, title, body }> },
  services: Array<{ slug, name, tagline, description, features[], badge? }>,
  stats: Array<{ value: number, suffix: string, label: string }>,
  testimonials: Array<{ name, identifier, rating, quote, program?, stat?, photo? }>,
  quizCTA: { headline, subtext, cta },
  finalCTA: { headline, subtext, cta },
  footer: { links[], social[], legal },
  pricing: {
    tiers: Array<{ name, price, badge?, headline, features[], cta, featured }>,
  },
}
```

---

## Checklist: Before Launch

### Remove Dev-Only Components
- [ ] ROI Calculator (or set `NEXT_PUBLIC_SHOW_PRICING_TOOLS=false`)
- [ ] Tier Comparison Chart (same env flag)
- [ ] Any `console.log` statements
- [ ] Hardcoded test emails in API routes

### Environment Variables

**Local development (`.env.local`):**
```env
STRIPE_SECRET_KEY=sk_test_...
STRIPE_WEBHOOK_SECRET=whsec_...
RESEND_API_KEY=re_...
PRINTFUL_API_KEY=...
NEXT_PUBLIC_CALENDLY_URL=https://calendly.com/clientname/meeting
NEXT_PUBLIC_SITE_URL=https://www.yourdomain.com
NEXT_PUBLIC_SHOW_PRICING_TOOLS=true
```

**Vercel production (add all of the above, plus):**
- [ ] `SANITY_PROJECT_ID`, `SANITY_DATASET`
- [ ] `PRINTFUL_API_KEY` — from Printful → Settings → API
- [ ] `STRIPE_SECRET_KEY` — use live key (not test key) in production
- [ ] `STRIPE_WEBHOOK_SECRET` — from Stripe → Webhooks → your endpoint → Signing secret
- [ ] `RESEND_API_KEY` — from Resend → API Keys (see onboarding checklist — domain must be verified first)
- [ ] `NEXT_PUBLIC_CALENDLY_URL` — client's Calendly event link
- [ ] `NEXT_PUBLIC_SITE_URL` — canonical domain with protocol and www (e.g. `https://www.yourdomain.com`)
- [ ] `INSTAGRAM_ACCESS_TOKEN`
- [ ] `NEXT_PUBLIC_SHOW_PRICING_TOOLS=false`

### Content
- [ ] All copy reviewed by client
- [ ] Real photos replacing placeholders
- [ ] Real testimonials (with permission)
- [ ] Sanity schema deployed (`npx sanity deploy`)
- [ ] At least 3 blog posts in Sanity

### Technical
- [ ] `next.config.ts` image domains updated for client's CDN
- [ ] Analytics connected (Vercel Analytics or GA)
- [ ] OG images created for all major pages
- [ ] Sitemap generated (`next-sitemap`)
- [ ] robots.txt configured
- [ ] DNS + Vercel project connected
- [ ] Vercel Root Directory: blank (Next.js at repo root)

---

## Applying This Template to a New Client

1. **Clone the repo** → rename → new git remote
2. **Update `globals.css`** → swap design tokens (primary color, accent, fonts)
3. **Update `/data/site.ts`** → swap all copy with client's brand voice
4. **Update `/data/shop.ts`** → client's products (or remove shop entirely)
5. **Update `/lib/photos.ts`** → map client's photo assets
6. **Swap Sanity project ID** → new project in Sanity dashboard
7. **Update pricing tiers** → client's actual offer names and prices
8. **Update quiz options** → client's specific pain points and goals
9. **Connect environment variables** → `PRINTFUL_API_KEY`, `STRIPE_SECRET_KEY`, `STRIPE_WEBHOOK_SECRET`, `RESEND_API_KEY`, `NEXT_PUBLIC_SITE_URL` (with www if canonical), Sanity keys
10. **Deploy to Vercel** → connect domain

Sections to remove if not applicable:
- Shop → delete `/shop`, `/api/printful`, `/api/stripe/checkout`, `/api/stripe/webhook`, `CartDrawer`, cart context, seeded JSON fallback; remove `STRIPE_*`, `PRINTFUL_API_KEY`, `RESEND_API_KEY` env vars
- Blog → delete `/blog`, `/studio`, Sanity config
- Instagram → delete `InstagramFeed` section, `/api/instagram`
- Quiz → delete `/quiz`, `QuizCTA` section

The hero animations (particles + orbs), the layout system, the animation library, and the pricing architecture are **always kept** — they are the core conversion infrastructure.
