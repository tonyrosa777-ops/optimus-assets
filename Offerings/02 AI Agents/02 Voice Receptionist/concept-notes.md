# Voice Receptionist — Concept Notes

Voice-specific patterns. Cross-product agent patterns live in [[../shared-knowledge/concept-notes]].

Voice is not chat with audio bolted on. Latency is unforgiving. Interrupts are the norm. Background noise is real. The user can't see retries or loading states — silence reads as "the agent broke."

## Patterns to capture

### Latency budgets
- **Perceived response time target: <500ms** from end of caller utterance to start of agent audio. Anything over 1s reads as "did it hear me?"
- Streaming TTS while the LLM is still generating to mask end-to-end latency
- Pre-warmed LLM connection (no cold-start handshake on first turn)
- Use Haiku for intent detection on the front end; route to Sonnet/Opus only when needed

### Interrupt / barge-in handling
- Caller talks over the agent → cut TTS immediately, route the new speech to ASR
- Detect false-positive interrupts (caller says "uh-huh" while listening) — don't cut for backchannels
- Resume gracefully when the agent was mid-sentence and got cut off

### Ambient sound / noise robustness
- Construction sites, kitchens, cars — service business callers are rarely in a quiet room
- Test ASR against typical caller environments before shipping
- Confirm critical info (phone number, address, appointment time) by reading it back

### Accent / dialect handling
- Don't assume General American
- ASR provider choice affects this — test against the client's actual market demographics

### Call transfer
- Warm transfer: agent gives the human a one-paragraph summary before connecting
- What context survives the transfer — full transcript? structured summary? both?
- What happens if no human answers — voicemail with the same summary

### Post-call summaries to CRM
- Structured fields: caller name, contact, intent, outcome (booked / transferred / info-only / escalated), action items
- Free-text transcript optional
- SMS recap to caller for any booking confirmation

### When to escalate vs when to handle
- Hard escalators: complaint, billing dispute, legal topic, explicit human request
- Soft escalators: low confidence on 2 consecutive turns, caller frustration detected, off-domain question
- Default to escalating when in doubt — a missed handoff is worse than an unnecessary one for v1

### Failure modes that don't have a chat equivalent
- Caller hangs up mid-conversation — partial CRM record, no SMS recap
- Bad ASR transcription leads agent to make a wrong booking — read-back confirmations are mandatory for any tool call that writes data
- Network glitch drops audio — agent must recover or hand off

---

#offering/ai-voice #status/draft
