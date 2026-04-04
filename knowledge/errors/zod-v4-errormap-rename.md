# Error: Zod v4 — `errorMap` renamed to `error` in schema params

**Project:** Enchanted Madison
**Date:** March 2026
**File:** `src/app/contact/page.tsx`

## Symptom

TypeScript build error:

```
Type error: No overload matches this call.
  Overload 1 of 2, '(values: readonly [...], params?: ...)', gave the following error.
    Object literal may only specify known properties, and 'errorMap' does not exist in type
    '{ error?: string | $ZodErrorMap<...> | undefined; message?: string | undefined; }'
```

## Root Cause

Zod v4 renamed the error customization parameter from `errorMap` to `error`. The `$ZodErrorMap` naming convention in the type signature is the indicator that Zod v4 is in use.

**Old (Zod v3):**
```ts
z.enum(["a", "b"], {
  errorMap: () => ({ message: "Please select an option" }),
})
```

**New (Zod v4):**
```ts
z.enum(["a", "b"], {
  error: "Please select an option",
})
```

Or simply pass the message as the second string argument:
```ts
z.string().min(1, "Please select an option")
```

## Fix Applied

Changed the client-side schema to use `z.string().min(1, "...")` instead of `z.enum(..., { errorMap: ... })`. The API route still uses `z.enum` for authoritative server-side validation (no custom error message needed there).

## Watch For

- Any Zod schema using `errorMap` will break at build time under Zod v4
- The `$ZodErrorMap` type name in error messages is the fingerprint of Zod v4
- Applies to all schema types: `.string()`, `.number()`, `.enum()`, etc.
