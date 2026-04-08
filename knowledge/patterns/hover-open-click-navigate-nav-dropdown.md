# Pattern: Hover-to-Open + Click-to-Navigate Nav Dropdowns
**Category:** Navigation / UX
**First used:** Where2 Junk — April 2026

## What
Nav items that have sub-pages (Services, Service Areas) behave as both links AND dropdown triggers: clicking navigates to the parent page (`/services`, `/areas`), while hovering reveals a dropdown of sub-pages. Standard mega-nav behavior that most users expect.

## When to Use
- Nav button has a parent page AND sub-pages (category + individual items)
- Currently implemented as click-toggle `<button>` that only opens a dropdown (never navigates)
- User feedback: "when you click Services it should go to /services"

## How

**Key: put hover handlers on the outer container div, not the link.**

```tsx
<div
  ref={dropdownRef}
  className="relative"
  onMouseEnter={() => setServicesOpen(true)}
  onMouseLeave={() => setServicesOpen(false)}
>
  <Link
    href="/services"
    onClick={() => setServicesOpen(false)}
    className="flex items-center gap-1 px-3 py-2 ..."
    style={{ color: servicesOpen ? 'var(--text-primary)' : 'var(--text-secondary)' }}
    onMouseEnter={(e) => (e.currentTarget.style.color = 'var(--text-primary)')}
    onMouseLeave={(e) => { if (!servicesOpen) e.currentTarget.style.color = 'var(--text-secondary)'; }}
  >
    {link.label}
    <ChevronDown size={13} className={`transition-transform ${servicesOpen ? 'rotate-180' : ''}`} />
  </Link>

  <AnimatePresence>
    {servicesOpen && (
      <motion.div className="absolute top-full ...">
        {/* dropdown items */}
      </motion.div>
    )}
  </AnimatePresence>
</div>
```

**Why the outer div works:** Moving from `<Link>` into the dropdown panel stays inside the container div, so `onMouseLeave` never fires mid-hover. The dropdown stays open. Mouse exiting the entire container closes it.

**Keep click-outside handler:** The existing `mousedown` listener for closing on outside click still works — keep it for keyboard/accessibility edge cases.

## Key Rules
1. Hover handlers go on the outer `div`, NOT on the `<Link>` or `<button>`
2. The trigger is `<Link href="/parent">` not `<button>` — clicking navigates
3. `onClick` on the Link calls `setOpen(false)` to close the dropdown before navigation
4. Keep the click-outside `mousedown` handler — hover-open doesn't eliminate need for it
5. Do NOT use this pattern for the "More" overflow dropdown — that one should be click-only (see [[patterns/more-overflow-dropdown-desktop-nav]])

## Reuse Condition
Any nav item where: (a) a parent page exists at the top-level route, and (b) sub-pages exist beneath it. Standard pattern for Services and Service Areas in service business sites.

## Related
- [[patterns/more-overflow-dropdown-desktop-nav]] — click-only overflow for secondary links
