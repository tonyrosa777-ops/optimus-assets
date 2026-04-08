# Pattern: "More" Overflow Dropdown for Crowded Desktop Nav
**Category:** Navigation / UX
**First used:** Where2 Junk — April 2026

## What
When a desktop nav has 8+ links and starts overflowing visually, secondary/lower-conversion links (Gallery, FAQ, Pricing, Shop) are grouped behind a `≡ ∨` button (Menu icon + ChevronDown) that reveals them in a click-toggled dropdown. Primary conversion links stay always visible.

## When to Use
- Desktop nav has >6 links and looks cramped at 1280px
- Some links are lower-priority (Gallery, FAQ, Pricing) and can be one click deeper
- Services/About/Contact/Blog should always be primary nav — never hidden
- Client or internal review flags nav as "too crowded"

## How

**1. Define which labels go into More:**
```tsx
const MORE_LABELS = new Set(['Gallery', 'FAQ', 'Pricing', 'Shop']);
```

**2. Filter them out of the main nav loop:**
```tsx
{siteData.nav.links.filter(l => !MORE_LABELS.has(l.label)).map((link) => {
  // ... normal nav rendering
})}
```

**3. Add the "More" button after the main loop:**
```tsx
<div ref={moreDropdownRef} className="relative">
  <button
    onClick={() => setMoreOpen(!moreOpen)}
    className="flex items-center gap-1 px-3 py-2 font-display font-black uppercase text-sm tracking-widest"
    style={{ color: moreOpen ? 'var(--text-primary)' : 'var(--text-secondary)' }}
    onMouseEnter={(e) => (e.currentTarget.style.color = 'var(--text-primary)')}
    onMouseLeave={(e) => { if (!moreOpen) e.currentTarget.style.color = 'var(--text-secondary)'; }}
    aria-label="More navigation links"
  >
    <Menu size={16} />
    <ChevronDown size={13} className={`transition-transform ${moreOpen ? 'rotate-180' : ''}`} />
  </button>

  <AnimatePresence>
    {moreOpen && (
      <motion.div className="absolute top-full right-0 mt-2 w-48 z-50 border" ...>
        <p className="px-4 pt-4 pb-2 font-mono text-xs uppercase tracking-widest">More</p>
        <div className="pb-2">
          {siteData.nav.links.filter(l => MORE_LABELS.has(l.label)).map(link => (
            <Link key={link.href} href={link.href} onClick={() => setMoreOpen(false)} ...>
              <span className="w-1.5 h-1.5" style={{ background: 'var(--primary)' }} />
              <span className="font-body text-sm">{link.label}</span>
            </Link>
          ))}
        </div>
      </motion.div>
    )}
  </AnimatePresence>
</div>
```

**4. Add state + ref + click-outside:**
```tsx
const [moreOpen, setMoreOpen] = useState(false);
const moreDropdownRef = useRef<HTMLDivElement>(null);
// In click-outside handler: check moreDropdownRef same as other dropdowns
```

## Key Rules
1. "More" is click-toggle, NOT hover-open — it's an overflow menu, not a category
2. Dropdown aligns `right-0` (not `left-1/2`) to avoid overflow past screen edge
3. Keep in `siteData.nav.links` — just filter on the `MORE_LABELS` set. Don't create a separate data structure
4. Always include `aria-label="More navigation links"` on the button for accessibility
5. Primary conversion links (Services, About, Contact, Book Now) must NEVER go into More

## What goes in More vs. stays primary
| Always Primary | Can Go In More |
|----------------|----------------|
| Services | Gallery |
| Service Areas | FAQ |
| About | Pricing |
| Blog | Shop |
| Testimonials | |
| Contact | |

## Reuse Condition
Any service business site that has grown beyond 6 nav links. Common when Gallery, FAQ, Pricing, and Shop are all built (as all Optimus Pro+ builds include).

## Related
- [[patterns/hover-open-click-navigate-nav-dropdown]] — the pattern for Services/Service Areas dropdowns
- Error #2 — nav overflow with >4 links (original problem this solves)
