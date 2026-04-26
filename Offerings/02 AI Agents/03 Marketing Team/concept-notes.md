# Marketing Team — Concept Notes

Product-specific concepts. Cross-product agent patterns live in [[../shared-knowledge/concept-notes]].

## Patterns to capture

### Pillar frameworks
- **Current default:** Health / Wealth / Wisdom / Integration. These are Optimus's own pillars and they bias toward personal-development / business-coaching audiences.
- **Productization need:** per-client pillar configuration. A trade business doesn't have "Wisdom" as a content pillar — it has "Education / Trust / Behind-the-scenes / Promotions" or similar.
- Open question: do we ship a library of pillar templates (by industry vertical) or do we co-design per client?
- Once a client has pillars, the engine respects the split — no week skews entirely to one pillar based on last week's performance.

### Identity signal tracking
Saves, shares, repeat-viewers, follower-conversion, comment quality — these are downstream of the algorithm. They indicate whether the audience is becoming a community.

- **Save rate** — strongest signal that content was useful enough to revisit. Higher signal than likes.
- **Repeat-viewer rate** — same person watching multiple posts is the precursor to follow + buy.
- **Follower-conversion per post** — net follows attributable to a post. Direct indicator that the post is doing identity work (the viewer wants more of THIS).
- **Comment quality** — surface area for both NLP scoring and human review. Generic "great post!" vs specific reaction is the differentiator.

The engine tracks these as primary metrics. Reach + likes are secondary because they're inflated and inconsistent across platforms.

### Saturation detection
A pillar / topic / format starts producing diminishing returns when reach holds but identity signals fall.

- Engine compares last 7-day rolling window to the prior 21-day baseline per pillar/topic/format
- Flags when save rate or follower-conversion drop >25% with reach steady (audience is seeing it but no longer responding)
- Recommends rest or rotation before the client burns the audience

### Cross-platform output
Same pillar strategy, different format per platform. The engine outputs a per-platform plan, not a generic plan to be reformatted by the client.

- **Instagram** — carousels for Wisdom/Integration, Reels for Health/Wealth proof points
- **TikTok** — short-form proof points, hot takes, behind-the-scenes
- **Twitter/X** — short-form Wisdom + thread-form Wealth
- **LinkedIn** — Wealth + Wisdom dominant, longer-form, professional tone shift
- **YouTube (long-form)** — TBD whether v1 includes this or it's a v2 add

### Identity-conversion vs reach-conversion
- A post with 100k reach and zero saves does not convert the audience.
- A post with 5k reach and 200 saves converts harder than the 100k post.
- The engine optimizes for the second pattern. Clients who measure success in views need to be re-educated as part of onboarding.

---

#offering/content-engine #status/draft
