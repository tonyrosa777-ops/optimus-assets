# Animation Ideas — Three.js Wandering Path System

## Original: Wandering Path (Neural Lightning)

Glowing, jittered branches radiating from a central point using Three.js CatmullRomCurve3. Produces an organic neural/lightning aesthetic with rainbow color cycling.

```javascript
function createWanderingPath(start, dir, length, segments, jitterScale, endPoint) {
  let pts = [start.clone()];
  let curr = start.clone();
  let cDir = dir.clone().normalize();
  for (let i = 0; i < segments; i++) {
    cDir.x += (Math.random() - 0.5) * jitterScale;
    cDir.y += (Math.random() - 0.5) * jitterScale;
    cDir.z += (Math.random() - 0.5) * jitterScale;
    cDir.normalize();
    curr = curr.clone().add(cDir.clone().multiplyScalar(length / segments));
    pts.push(curr);
  }
  if (endPoint) {
    const approach = endPoint.clone().add(new THREE.Vector3(-1.5, 0, 0));
    pts[pts.length - 1] = approach;
    pts.push(endPoint.clone());
  }
  return new THREE.CatmullRomCurve3(pts);
}
```

**Key parameters:**
- `start` — origin Vector3
- `dir` — initial direction Vector3
- `length` — total path length
- `segments` — number of curve control points
- `jitterScale` — how wildly the path wanders (higher = more chaotic)
- `endPoint` — optional snap-to target

---

## Variation 1: Gravity Roots

Same wandering logic but `cDir.y` always biases downward, simulating roots or dripping paint. Paired with earthy colors (brown → orange → gold).

```javascript
function createGravityRoot(start, dir, length, segments, jitterScale) {
  let pts = [start.clone()];
  let curr = start.clone();
  let cDir = dir.clone().normalize();
  for (let i = 0; i < segments; i++) {
    cDir.x += (Math.random() - 0.5) * jitterScale;
    cDir.y -= Math.random() * jitterScale * 1.5; // gravity bias
    cDir.z += (Math.random() - 0.5) * jitterScale * 0.3;
    cDir.normalize();
    curr = curr.clone().add(cDir.clone().multiplyScalar(length / segments));
    pts.push(curr);
  }
  return new THREE.CatmullRomCurve3(pts);
}
```

**Use case:** Hero section background for an organic/natural brand. Think botanical, wellness, earth.

---

## Variation 2: Pulse Web (Spider Threads)

Multiple paths originate from the same center point at evenly distributed angles. Each strand pulses opacity using a sine wave — like a living web or signal broadcast.

```javascript
function createPulseWeb(center, numStrands, length, segments, jitterScale) {
  const strands = [];
  for (let i = 0; i < numStrands; i++) {
    const angle = (i / numStrands) * Math.PI * 2;
    const dir = new THREE.Vector3(Math.cos(angle), Math.sin(angle), 0);
    strands.push(createWanderingPath(center, dir, length, segments, jitterScale));
  }
  return strands;
}

// In animation loop:
// material.opacity = 0.4 + 0.6 * Math.sin(Date.now() * 0.002 + strandIndex)
```

**Use case:** Tech/AI company hero. Visualizes network connectivity, signal, or data flow.

---

## Variation 3: Particle Swarm Along Path

Instead of rendering the curve as a line, spawn particles that travel along each CatmullRomCurve3 path at varying speeds. Particles leave fading trails.

```javascript
function createPathParticle(curve, speed) {
  let t = Math.random(); // random start position on curve
  return {
    update(delta) {
      t = (t + speed * delta) % 1;
      return curve.getPoint(t); // returns Vector3 position
    }
  };
}

// Render: draw a small sphere or point at particle.update(delta)
// Trail: store last N positions, draw fading line between them
```

**Use case:** Data pipeline visualization, loading screens, dashboard backgrounds. Pairs with dark UI.

---

## Variation 4: Branching Recursive Tree

Each path spawns 2 child paths at the endpoint, with reduced length and increased jitter — recursively until a depth limit. Produces an organic tree or lightning bolt structure.

```javascript
function createBranchTree(start, dir, length, segments, jitterScale, depth) {
  if (depth === 0) return [];
  const curve = createWanderingPath(start, dir, length, segments, jitterScale);
  const tip = curve.getPoint(1);
  const branches = [curve];

  const leftDir = dir.clone().applyAxisAngle(new THREE.Vector3(0, 0, 1), 0.4 + Math.random() * 0.3);
  const rightDir = dir.clone().applyAxisAngle(new THREE.Vector3(0, 0, 1), -(0.4 + Math.random() * 0.3));

  branches.push(...createBranchTree(tip, leftDir, length * 0.65, segments, jitterScale * 1.2, depth - 1));
  branches.push(...createBranchTree(tip, rightDir, length * 0.65, segments, jitterScale * 1.2, depth - 1));

  return branches;
}
```

**Use case:** Lightning strike effect, decision tree visualization, fractal logo reveal animation.

---

## Variation 5: Magnetic Field Lines

Two opposing poles (positive/negative). Paths originate from the positive pole and curve toward the negative using a lerp-based attraction force instead of pure jitter. Produces smooth arc field lines.

```javascript
function createFieldLine(positive, negative, segments, jitterScale) {
  const pts = [positive.clone()];
  let curr = positive.clone();
  for (let i = 0; i < segments; i++) {
    const t = i / segments;
    // Direction = blend between random wander and pull toward negative pole
    const toNeg = negative.clone().sub(curr).normalize();
    const jitter = new THREE.Vector3(
      (Math.random() - 0.5) * jitterScale,
      (Math.random() - 0.5) * jitterScale,
      (Math.random() - 0.5) * jitterScale
    );
    const step = toNeg.lerp(jitter, 1 - t).normalize(); // attraction strengthens as t increases
    curr = curr.clone().add(step.multiplyScalar(positive.distanceTo(negative) / segments));
    pts.push(curr);
  }
  pts.push(negative.clone());
  return new THREE.CatmullRomCurve3(pts);
}
```

**Use case:** Science/physics visualization, magnetic or energy brand hero, abstract tech background.

---

## Variation 6: DNA Helix Strand

Two wandering paths generated in parallel with a phase offset, connected by perpendicular rungs at regular intervals. Rotates slowly on the Y axis — produces a living double helix.

```javascript
function createHelixPair(center, length, segments, jitterScale) {
  const pts1 = [];
  const pts2 = [];
  for (let i = 0; i < segments; i++) {
    const t = i / segments;
    const angle = t * Math.PI * 6; // 3 full rotations
    const radius = 1.2;
    const jx = (Math.random() - 0.5) * jitterScale;
    const jz = (Math.random() - 0.5) * jitterScale;
    pts1.push(new THREE.Vector3(
      center.x + Math.cos(angle) * radius + jx,
      center.y + (t - 0.5) * length,
      center.z + Math.sin(angle) * radius + jz
    ));
    pts2.push(new THREE.Vector3(
      center.x + Math.cos(angle + Math.PI) * radius + jx,
      center.y + (t - 0.5) * length,
      center.z + Math.sin(angle + Math.PI) * radius + jz
    ));
  }
  // Connect rungs every N points
  const rungs = [];
  for (let i = 0; i < segments; i += 4) {
    rungs.push([pts1[i].clone(), pts2[i].clone()]);
  }
  return {
    strand1: new THREE.CatmullRomCurve3(pts1),
    strand2: new THREE.CatmullRomCurve3(pts2),
    rungs
  };
}
```

**Use case:** Biotech, health tech, genomics, or any science-forward brand hero.

---

## Variation 7: Orbit Trails

Multiple paths orbit a central attractor in 3D space. Each path slowly decays its orbit radius over time, spiraling inward. On reset, they burst outward and re-converge — like a black hole or galaxy core.

```javascript
function createOrbitTrail(center, radius, tilt, segments, jitterScale) {
  const pts = [];
  for (let i = 0; i <= segments; i++) {
    const t = i / segments;
    const angle = t * Math.PI * 2;
    const decay = 1 - t * 0.4; // spiral inward
    const jitter = new THREE.Vector3(
      (Math.random() - 0.5) * jitterScale,
      (Math.random() - 0.5) * jitterScale,
      (Math.random() - 0.5) * jitterScale
    );
    const pt = new THREE.Vector3(
      center.x + Math.cos(angle) * radius * decay,
      center.y + Math.sin(tilt) * Math.sin(angle) * radius * decay,
      center.z + Math.sin(angle) * radius * decay
    ).add(jitter);
    pts.push(pt);
  }
  return new THREE.CatmullRomCurve3(pts);
}

// Spawn 8–20 trails with varied radius and tilt values
// In loop: shift t offset per frame to animate travel along path
```

**Use case:** Space, astronomy, fintech (orbiting assets), abstract brand identity animations.

---

## Variation 8: Seismic Wave

A single long horizontal path with vertical jitter only — simulating an EKG heartbeat or seismic signal. A glowing pulse dot travels the length of the line in real time.

```javascript
function createSeismicWave(originX, y, z, width, segments, amplitude) {
  const pts = [];
  for (let i = 0; i < segments; i++) {
    const t = i / segments;
    // Spike region: high amplitude in center 20% of the path
    const isSpikeZone = t > 0.4 && t < 0.6;
    const verticalJitter = isSpikeZone
      ? (Math.random() - 0.5) * amplitude * 3
      : (Math.random() - 0.5) * amplitude * 0.3;
    pts.push(new THREE.Vector3(originX + t * width, y + verticalJitter, z));
  }
  return new THREE.CatmullRomCurve3(pts);
}

// Pulse dot: small emissive sphere traveling curve.getPoint(t)
// t increments each frame, resets to 0 on completion
// Trail: last 10 positions rendered with fading opacity
```

**Use case:** Medical tech, fitness/health dashboards, audio visualizers, real-time data monitors.

---

## Variation 9: Constellation Connect

Spawn N random points in 3D space. For each point, find its K nearest neighbors and draw a wandering path between them. Points glow as nodes. Produces a star map / knowledge graph aesthetic.

```javascript
function buildConstellation(points, k, segments, jitterScale) {
  const edges = [];
  for (let i = 0; i < points.length; i++) {
    // Sort other points by distance
    const sorted = points
      .map((p, j) => ({ point: p, dist: points[i].distanceTo(p), index: j }))
      .filter(p => p.index !== i)
      .sort((a, b) => a.dist - b.dist)
      .slice(0, k);

    for (const neighbor of sorted) {
      const dir = neighbor.point.clone().sub(points[i]).normalize();
      edges.push(createWanderingPath(points[i], dir, points[i].distanceTo(neighbor.point), segments, jitterScale, neighbor.point));
    }
  }
  return edges;
}

// Node rendering: small glowing sphere at each point
// Edge animation: particles traveling edges, opacity based on distance
```

**Use case:** Knowledge graphs, AI/ML concept maps, network topology visualization, interactive portfolios.

---

## Variation 10: Ink Diffusion

Paths grow outward from a center point but slow to a near-stop as they extend — simulating ink dropped in water. New paths continuously spawn from slightly offset origins, layering over each other.

```javascript
function createInkStroke(origin, dir, maxLength, segments, jitterScale) {
  const pts = [origin.clone()];
  let curr = origin.clone();
  let cDir = dir.clone().normalize();
  for (let i = 0; i < segments; i++) {
    const t = i / segments;
    const speed = Math.pow(1 - t, 2); // eases to near-zero at tip
    cDir.x += (Math.random() - 0.5) * jitterScale * (1 + t * 2); // jitter increases over distance
    cDir.y += (Math.random() - 0.5) * jitterScale * (1 + t * 2);
    cDir.z += (Math.random() - 0.5) * jitterScale * 0.2;
    cDir.normalize();
    curr = curr.clone().add(cDir.clone().multiplyScalar((maxLength / segments) * speed));
    pts.push(curr);
  }
  return new THREE.CatmullRomCurve3(pts);
}

// Spawn a new stroke every 200ms from origin ± small random offset
// Each stroke fades in over 500ms, fades out over 3s
// Color: deep indigo → violet → transparent at tips
```

**Use case:** Luxury branding, art/creative agency heroes, fashion tech, high-end editorial sites.

---

## Quick Reference

| Variation | Visual Style | Best Use Case |
|---|---|---|
| Original | Neural lightning, rainbow | Generic tech hero |
| Gravity Roots | Dripping roots, earthy | Organic / wellness brands |
| Pulse Web | Spider threads, pulsing | AI / network / connectivity |
| Particle Swarm | Glowing particles on paths | Dashboards, data visualization |
| Branching Tree | Recursive fractal tree | Lightning, decision flows |
| Magnetic Field | Smooth arcing field lines | Science, energy brands |
| DNA Helix | Double helix with rungs | Biotech, health, genomics |
| Orbit Trails | Spiraling inward orbits | Space, fintech, galaxy core |
| Seismic Wave | EKG heartbeat pulse | Medical tech, audio, fitness |
| Constellation | Node-edge star map | AI/ML, knowledge graphs, portfolios |
| Ink Diffusion | Slowing ink strokes | Luxury, fashion, editorial |
