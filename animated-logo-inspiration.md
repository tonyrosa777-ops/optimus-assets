# Animated Logo Inspiration — GSAP SVG System

## Original: Disney+ Arc Reveal

A glowing cyan arc draws around the Disney+ logo using GSAP timeline. Stars (SVG `<use>` elements) fade in with staggered opacity from their center point. The main timeline is paused and triggered on load or interaction.

```javascript
let select = s => document.querySelector(s),
    selectAll = s => document.querySelectorAll(s),
    mainSVG = select('#mainSVG'),
    allStars = gsap.utils.toArray('#allStars use'),
    popTl = gsap.timeline({ paused: true })

gsap.set('svg', {
  visibility: 'visible'
})

gsap.set(allStars, {
  transformOrigin: '50% 50%',
  opacity: 0
})

allStars.forEach((target, i) => {
  let tl = gsap.timeline();
  tl.set(target, {
    opacity: 1
  })
  // Each star animates independently on its own sub-timeline
  // popTl sequences all star timelines with stagger
})
```

**Stack:** GSAP + SVG inline markup
**Effect:** Arc stroke-dashoffset draw-on, star scatter fade-in, logo scale-up from center
**Trigger:** `popTl.play()` on page load or scroll into view

---

## Variation 1: Nexus AI — Circuit Pulse Logo

**Brand:** Nexus AI — B2B machine learning infrastructure company
**Palette:** Electric blue `#00D4FF` on deep navy `#0A0F1E`
**Effect:** SVG circuit board paths draw themselves in sequence, then the wordmark fades up from 0 opacity. A looping pulse dot travels the circuit lines post-reveal.

```javascript
let select = s => document.querySelector(s),
    selectAll = s => document.querySelectorAll(s),
    circuitPaths = gsap.utils.toArray('#circuit path'),
    wordmark = select('#nexus-wordmark'),
    pulseDot = select('#pulse-dot'),
    masterTl = gsap.timeline({ paused: true })

// Set all circuit paths to invisible (stroke-dashoffset trick)
circuitPaths.forEach(path => {
  const length = path.getTotalLength();
  gsap.set(path, {
    strokeDasharray: length,
    strokeDashoffset: length,
    opacity: 1
  });
});

gsap.set(wordmark, { opacity: 0, y: 10 });
gsap.set(pulseDot, { opacity: 0 });

// Draw circuits in sequence
masterTl
  .to(circuitPaths, {
    strokeDashoffset: 0,
    duration: 1.2,
    stagger: 0.15,
    ease: 'power2.inOut'
  })
  .to(wordmark, {
    opacity: 1,
    y: 0,
    duration: 0.6,
    ease: 'power3.out'
  }, '-=0.2')
  .to(pulseDot, {
    opacity: 1,
    duration: 0.3
  })

// Loop: pulse dot travels path after reveal
function animatePulse() {
  const path = circuitPaths[0];
  const length = path.getTotalLength();
  gsap.fromTo(pulseDot,
    { motionPath: { path: path, align: path, start: 0, end: 0 } },
    { motionPath: { path: path, align: path, start: 0, end: 1 }, duration: 2, ease: 'none', repeat: -1 }
  );
}

masterTl.call(animatePulse);
masterTl.play();
```

**Use case:** SaaS landing pages, AI product launches, dark-mode tech dashboards.

---

## Variation 2: Verdana — Sustainable Energy Brand

**Brand:** Verdana — residential solar and wind energy startup
**Palette:** Leaf green `#3DDC84` → sky blue `#87CEEB` on white `#FAFAFA`
**Effect:** A leaf SVG path grows from stem to tip (stroke draw-on). Petals scale up from 0 with a spring bounce. The tagline "Clean. Simple. Yours." types itself letter by letter after the icon settles.

```javascript
let leafPath = document.querySelector('#leaf-stroke'),
    petals = gsap.utils.toArray('.petal'),
    tagline = document.querySelector('#tagline'),
    logoMark = document.querySelector('#logo-mark'),
    revealTl = gsap.timeline({ paused: true })

const leafLength = leafPath.getTotalLength();

gsap.set(leafPath, {
  strokeDasharray: leafLength,
  strokeDashoffset: leafLength
});

gsap.set(petals, {
  scale: 0,
  transformOrigin: 'center bottom',
  opacity: 0
});

gsap.set(tagline, { opacity: 0 });

revealTl
  .to(leafPath, {
    strokeDashoffset: 0,
    duration: 1.0,
    ease: 'power1.inOut'
  })
  .to(petals, {
    scale: 1,
    opacity: 1,
    duration: 0.5,
    stagger: 0.08,
    ease: 'back.out(1.7)' // spring bounce
  }, '-=0.3')
  .to(logoMark, {
    filter: 'drop-shadow(0 0 12px #3DDC8466)',
    duration: 0.8,
    ease: 'power2.out'
  }, '-=0.2')
  .to(tagline, {
    opacity: 1,
    duration: 1.2,
    ease: 'none'
    // Pair with a text scramble or typewriter plugin for letter-by-letter effect
  })

revealTl.play();
```

**Use case:** Clean energy landing pages, sustainability reports, eco-brand pitch decks.

---

## Variation 3: Kōdo — Japanese Streetwear Label

**Brand:** Kōdo (コード) — minimal streetwear brand, Tokyo-inspired
**Palette:** Off-white `#F5F0EB` on obsidian black `#111111`, with matte red accent `#CC2200`
**Effect:** The kanji character for "code" (コード) draws stroke-by-stroke using carefully ordered path segments. A thin horizontal line sweeps across the full width. The Latin wordmark fades in below with letter-spacing expanding from 0 to 0.4em.

```javascript
let kanjiStrokes = gsap.utils.toArray('#kanji path'),
    sweepLine = document.querySelector('#sweep-line'),
    latinWord = document.querySelector('#latin-wordmark'),
    redDot = document.querySelector('#accent-dot'),
    brandTl = gsap.timeline({ delay: 0.3 })

kanjiStrokes.forEach(stroke => {
  const len = stroke.getTotalLength();
  gsap.set(stroke, {
    strokeDasharray: len,
    strokeDashoffset: len
  });
});

gsap.set(sweepLine, { scaleX: 0, transformOrigin: 'left center' });
gsap.set(latinWord, { opacity: 0, letterSpacing: '-0.1em' });
gsap.set(redDot, { scale: 0, transformOrigin: '50% 50%' });

brandTl
  .to(kanjiStrokes, {
    strokeDashoffset: 0,
    duration: 0.4,
    stagger: 0.18,
    ease: 'power2.out'
  })
  .to(sweepLine, {
    scaleX: 1,
    duration: 0.5,
    ease: 'power3.inOut'
  }, '+=0.1')
  .to(latinWord, {
    opacity: 1,
    letterSpacing: '0.4em',
    duration: 0.7,
    ease: 'power2.out'
  }, '-=0.2')
  .to(redDot, {
    scale: 1,
    duration: 0.3,
    ease: 'back.out(2)'
  }, '-=0.3')
```

**Use case:** Fashion brand intros, lookbook headers, high-end e-commerce splash screens.

---

## Variation 4: Vaulta — Fintech Security Platform

**Brand:** Vaulta — enterprise-grade financial data security
**Palette:** Gold `#C9A84C` on charcoal `#1C1C1E`, with subtle silver `#8E8E93` accents
**Effect:** A shield SVG assembles from 4 quadrant pieces scaling in from center. A lock icon draws itself in the middle. Concentric ring pulses radiate outward (like a sonar ping) twice after assembly, then settle. The wordmark slides up from below.

```javascript
let shieldQuads = gsap.utils.toArray('.shield-quad'),
    lockPath = document.querySelector('#lock-path'),
    rings = gsap.utils.toArray('.sonar-ring'),
    wordmark = document.querySelector('#vaulta-wordmark'),
    assemblyTl = gsap.timeline({ paused: true })

const lockLen = lockPath.getTotalLength();

gsap.set(shieldQuads, {
  scale: 0,
  transformOrigin: '50% 50%',
  opacity: 0
});

gsap.set(lockPath, {
  strokeDasharray: lockLen,
  strokeDashoffset: lockLen,
  opacity: 0
});

gsap.set(rings, { scale: 0.5, opacity: 0, transformOrigin: '50% 50%' });
gsap.set(wordmark, { opacity: 0, y: 16 });

assemblyTl
  .to(shieldQuads, {
    scale: 1,
    opacity: 1,
    duration: 0.45,
    stagger: { amount: 0.3, from: 'center' },
    ease: 'back.out(1.4)'
  })
  .to(lockPath, {
    strokeDashoffset: 0,
    opacity: 1,
    duration: 0.6,
    ease: 'power2.inOut'
  }, '-=0.1')
  .to(rings, {
    scale: 2.5,
    opacity: 0,
    duration: 0.9,
    stagger: 0.2,
    ease: 'power1.out',
    repeat: 1
  }, '+=0.1')
  .to(wordmark, {
    opacity: 1,
    y: 0,
    duration: 0.5,
    ease: 'power3.out'
  }, '-=0.4')

assemblyTl.play();
```

**Use case:** Fintech onboarding screens, security product launches, enterprise SaaS hero sections.

---

## Variation 5: Lumiq — AI Photography Platform

**Brand:** Lumiq — AI-powered photo editing and asset management for creators
**Palette:** Warm white `#FFF8F0` on deep black `#0D0D0D`, lens flare amber `#FFB347`
**Effect:** A camera aperture SVG opens from fully closed (all blades rotated shut) to fully open using a coordinated rotation stagger. As the aperture opens, a flash burst radiates outward and fades. The wordmark materializes inside the aperture using a blur-to-sharp filter transition.

```javascript
let apertureBlades = gsap.utils.toArray('.aperture-blade'),
    flashBurst = document.querySelector('#flash-burst'),
    wordmark = document.querySelector('#lumiq-wordmark'),
    apertureTl = gsap.timeline({ paused: true })

// Blades start closed (rotated inward)
gsap.set(apertureBlades, {
  rotation: -75,
  transformOrigin: '0% 100%',
  opacity: 1
});

gsap.set(flashBurst, { scale: 0, opacity: 0, transformOrigin: '50% 50%' });
gsap.set(wordmark, {
  opacity: 0,
  filter: 'blur(12px)',
  scale: 0.85,
  transformOrigin: '50% 50%'
});

apertureTl
  .to(apertureBlades, {
    rotation: 0,
    duration: 0.7,
    stagger: { amount: 0.2, from: 'start' },
    ease: 'power2.inOut'
  })
  .to(flashBurst, {
    scale: 3,
    opacity: 0,
    duration: 0.5,
    ease: 'power1.out'
  }, '-=0.1')
  .to(wordmark, {
    opacity: 1,
    filter: 'blur(0px)',
    scale: 1,
    duration: 0.6,
    ease: 'power3.out'
  }, '-=0.3')

apertureTl.play();
```

**Use case:** Photography SaaS, creative tool launches, media platform splash screens, portfolio intros.

---

## Variation 6: Driftwood — Boutique Travel Agency

**Brand:** Driftwood — slow travel experiences for remote workers and digital nomads
**Palette:** Sand `#E8D5B7` on ocean deep `#1B3A4B`, coral accent `#FF6B6B`
**Effect:** A compass SVG needle spins freely (like it's searching), then snaps and locks to north with a subtle bounce. The cardinal directions (N, E, S, W) fade in one by one. A watercolor wash texture fades in behind the entire mark, and the tagline "Find your somewhere" slides in from the right.

```javascript
let compassNeedle = document.querySelector('#compass-needle'),
    cardinals = gsap.utils.toArray('.cardinal-letter'),
    watercolor = document.querySelector('#watercolor-bg'),
    tagline = document.querySelector('#driftwood-tagline'),
    compassTl = gsap.timeline({ paused: true })

gsap.set(compassNeedle, { rotation: 0, transformOrigin: '50% 50%' });
gsap.set(cardinals, { opacity: 0, scale: 0.7, transformOrigin: '50% 50%' });
gsap.set(watercolor, { opacity: 0 });
gsap.set(tagline, { opacity: 0, x: 30 });

compassTl
  // Free spin — searching
  .to(compassNeedle, {
    rotation: 720 + 22,  // two full rotations + overshoot to north
    duration: 1.4,
    ease: 'power1.inOut'
  })
  // Snap back to true north with bounce
  .to(compassNeedle, {
    rotation: 0,
    duration: 0.35,
    ease: 'back.out(3)'
  })
  .to(cardinals, {
    opacity: 1,
    scale: 1,
    duration: 0.3,
    stagger: 0.1,
    ease: 'power2.out'
  }, '-=0.1')
  .to(watercolor, {
    opacity: 0.35,
    duration: 1.0,
    ease: 'power1.inOut'
  }, '-=0.3')
  .to(tagline, {
    opacity: 1,
    x: 0,
    duration: 0.6,
    ease: 'power3.out'
  }, '-=0.6')

compassTl.play();
```

**Use case:** Travel brand hero sections, hospitality sites, nomad community platforms, booking page intros.

---

## Variation 7: Stratum — Architecture & Design Firm

**Brand:** Stratum — modernist architecture studio specializing in layered spatial design
**Palette:** Concrete `#C4BDB5` on white `#FFFFFF`, charcoal `#2C2C2C` lines, brass `#B5882A` accents
**Effect:** The logo is built from horizontal layers (SVG rectangles of varying widths) that slide in from alternating left/right directions, stacking up like floors of a building. Once stacked, a thin brass underline draws itself left-to-right. The firm name fades in with precise tracking.

```javascript
let layers = gsap.utils.toArray('.stratum-layer'),
    brassLine = document.querySelector('#brass-underline'),
    firmName = document.querySelector('#stratum-wordmark'),
    buildTl = gsap.timeline({ paused: true })

const brassLen = brassLine.getTotalLength();

// Layers start off-screen, alternating sides
layers.forEach((layer, i) => {
  gsap.set(layer, { x: i % 2 === 0 ? -120 : 120, opacity: 0 });
});

gsap.set(brassLine, {
  strokeDasharray: brassLen,
  strokeDashoffset: brassLen
});
gsap.set(firmName, { opacity: 0, letterSpacing: '0.6em' });

buildTl
  .to(layers, {
    x: 0,
    opacity: 1,
    duration: 0.5,
    stagger: { amount: 0.5, from: 'end' }, // bottom layer first, builds upward
    ease: 'power3.out'
  })
  .to(brassLine, {
    strokeDashoffset: 0,
    duration: 0.6,
    ease: 'power2.inOut'
  }, '-=0.1')
  .to(firmName, {
    opacity: 1,
    letterSpacing: '0.25em',
    duration: 0.7,
    ease: 'power2.out'
  }, '-=0.2')

buildTl.play();
```

**Use case:** Architecture firms, interior design studios, construction company rebrands, luxury real estate.

---

## Variation 8: Hyper — Esports & Gaming Organization

**Brand:** Hyper — competitive esports team and gaming content brand
**Palette:** Neon magenta `#FF00AA` + electric cyan `#00FFEE` on near-black `#0A0A0F`
**Effect:** The logo glitches into existence — rapid random position/skew offsets cycle for 800ms simulating a corrupt signal, then snaps clean. Chromatic aberration (red/blue channel split) fades in and out during the glitch. The team tag `[HYPR]` types on character by character after the glitch resolves.

```javascript
let logoMark = document.querySelector('#hyper-mark'),
    chromaRed = document.querySelector('#chroma-red'),
    chromaBlue = document.querySelector('#chroma-blue'),
    teamTag = document.querySelector('#team-tag'),
    glitchTl = gsap.timeline({ paused: true })

gsap.set([chromaRed, chromaBlue], { opacity: 0 });
gsap.set(teamTag, { opacity: 0 });

// Glitch phase — rapid random transforms
const glitchFrames = 10;
for (let i = 0; i < glitchFrames; i++) {
  glitchTl.to(logoMark, {
    x: (Math.random() - 0.5) * 14,
    y: (Math.random() - 0.5) * 6,
    skewX: (Math.random() - 0.5) * 8,
    duration: 0.06,
    ease: 'none'
  });
  if (i % 3 === 0) {
    glitchTl.to([chromaRed, chromaBlue], {
      opacity: 0.6,
      x: i % 2 === 0 ? 4 : -4,
      duration: 0.06,
      ease: 'none'
    }, '<');
    glitchTl.to([chromaRed, chromaBlue], {
      opacity: 0,
      duration: 0.06,
      ease: 'none'
    });
  }
}

// Snap clean
glitchTl
  .to(logoMark, { x: 0, y: 0, skewX: 0, duration: 0.1, ease: 'power4.out' })
  .to(teamTag, {
    opacity: 1,
    duration: 0.05,
    stagger: { each: 0.07, from: 'start' }
    // Each character of [HYPR] is a separate <tspan> or <span>
  }, '+=0.1')

glitchTl.play();
```

**Use case:** Esports team intros, gaming platform onboarding, streamer overlays, competitive gaming event openers.

---

## Variation 9: Aurelius — Luxury Watchmaker

**Brand:** Aurelius — Swiss-inspired independent watchmaker, ultra-premium positioning
**Palette:** Deep burgundy `#4A0E1A` + aged gold `#C9A84C` on cream `#FAF6EF`
**Effect:** A watch face SVG is revealed by a circular wipe (clip-path radius expanding from center). The hour and minute hands sweep into position from 12 o'clock to the brand's signature time (10:10). Roman numerals around the dial fade in one by one clockwise. The maison name engraves itself via a stroke draw with near-zero opacity fill, then fill fades in.

```javascript
let watchFace = document.querySelector('#watch-face'),
    hourHand = document.querySelector('#hour-hand'),
    minuteHand = document.querySelector('#minute-hand'),
    numerals = gsap.utils.toArray('.roman-numeral'),
    maisonName = document.querySelector('#aurelius-name'),
    watchTl = gsap.timeline({ paused: true })

const nameLen = maisonName.getTotalLength ? maisonName.getTotalLength() : 0;

// Circular reveal via clip-path
gsap.set(watchFace, { clipPath: 'circle(0% at 50% 50%)' });
gsap.set([hourHand, minuteHand], { rotation: 0, transformOrigin: '50% 100%' }); // 12 o'clock
gsap.set(numerals, { opacity: 0 });

if (nameLen) {
  gsap.set(maisonName, {
    strokeDasharray: nameLen,
    strokeDashoffset: nameLen,
    fillOpacity: 0
  });
}

watchTl
  .to(watchFace, {
    clipPath: 'circle(55% at 50% 50%)',
    duration: 1.0,
    ease: 'power2.inOut'
  })
  // Hands sweep to 10:10 (hour = -60deg, minute = 60deg from 12)
  .to(hourHand, {
    rotation: -60,
    duration: 1.2,
    ease: 'power1.inOut'
  }, '-=0.5')
  .to(minuteHand, {
    rotation: 60,
    duration: 1.2,
    ease: 'power1.inOut'
  }, '<')
  .to(numerals, {
    opacity: 1,
    duration: 0.2,
    stagger: { amount: 0.8, from: 'start' }, // clockwise I through XII
    ease: 'none'
  }, '-=0.8')
  .to(maisonName, {
    strokeDashoffset: 0,
    duration: 1.0,
    ease: 'power2.inOut'
  }, '-=0.3')
  .to(maisonName, {
    fillOpacity: 1,
    duration: 0.5,
    ease: 'power1.in'
  })

watchTl.play();
```

**Use case:** Luxury product launches, high-end e-commerce hero sections, watch brand microsites, premium lifestyle brands.

---

## Quick Reference

| Logo | Brand Type | Core Technique | GSAP Feature |
|---|---|---|---|
| Disney+ | Entertainment | Arc draw + star scatter | `timeline`, `stagger`, `paused` |
| Nexus AI | B2B Tech | Circuit path draw + pulse dot | `strokeDashoffset`, `motionPath` |
| Verdana | Clean Energy | Leaf grow + petal bounce | `back.out`, `drop-shadow` filter |
| Kōdo | Streetwear | Kanji stroke-by-stroke + sweep | `letterSpacing`, `scaleX` sweep |
| Vaulta | Fintech | Shield assembly + sonar rings | `stagger from center`, `repeat` |
| Lumiq | Photo/AI | Aperture open + flash burst | `rotation`, `blur` filter transition |
| Driftwood | Travel | Compass spin + snap to north | `back.out(3)`, `watercolor` fade |
| Stratum | Architecture | Layer stack from alternating sides | `stagger from end`, `x` offset |
| Hyper | Esports/Gaming | Glitch corrupt + chromatic aberration | Loop glitch frames, `skewX` |
| Aurelius | Luxury Watches | Circular wipe + hand sweep + engrave | `clipPath`, `fillOpacity`, `strokeDashoffset` |
