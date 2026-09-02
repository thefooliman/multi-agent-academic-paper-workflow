# Humanizer before/after

A short demo of what the polishing agent does in a standard pass. Rule numbers
refer to `configs/humanizer-patterns-en.md`.

## Before (AI-flavored)

In recent years, carbon pricing has attracted increasing attention from scholars
and policymakers alike. The policy plays a pivotal role in the evolving landscape
of climate governance, underscoring the critical importance of market-based
instruments. Our groundbreaking results demonstrate that carbon pricing
significantly improves firm efficiency, highlighting the need for further
research in this important area.

## After (standard pass)

After carbon pricing, compliance costs in our sample rose 2.1% on average, and
the effect was largest for energy-intensive firms. That gap persists when we add
controls for size and industry. Whether the policy caused the change is harder to
say. The treated provinces were chosen, not randomized, so we read the result as
suggestive rather than causal.

## What changed

| Pattern | Rule | Fix |
|---|---|---|
| "In recent years, ... increasing attention" | 2.1 formulaic opener | replaced with a concrete fact |
| "plays a pivotal role ... evolving landscape ... underscoring" | 1.1 inflated importance | cut; the claim now hangs on a number |
| "Our groundbreaking results" | 1.4 promotional adjectives | removed |
| "demonstrate that ... significantly improves" | 1.3 / 1.7 | downgraded to a hedged, evidence-anchored statement |
| ", highlighting the need for further research" | 2.4 -ing tail | removed |

The after-version is shorter, anchors each claim to a number, and keeps the
causal claim at the strength the design supports. That last part is the
claim-evidence discipline in `configs/claim-evidence-discipline.md`; it is the
difference between academic humanizing and plain synonym swapping.
