---
name: paper-radical
description: Aggressive de-AIGC humanization of an academic manuscript. Apply the full AI-tell catalog with the six-step loop and five-dimension score to an existing paper, or to a newly drafted one. Use when standard polishing is not enough and the paper must pass AI detection (Turnitin AI, GPTZero, 知网, 万方).
---

# Paper Radical — Coordinator

Same operating procedure as /paper-write and /paper-check (read ../../skills/paper-write/SKILL.md and follow it), with these differences:

- intensity = "radical" (write it into the config copy stored in state).
- Apply the FULL pattern catalog (🔴🟡🟢) in configs/humanizer-patterns-en.md, not just the 🔴 set.
- Run the six-step loop: intake → audit → claim-evidence check → differentiated rewrite → five-dimension self-score → cold-reader recheck.
- Apply the section-by-section rewrite strategies in configs/section-strategies.md.
- Converge when the weighted five-dimension score (configs/scoring-rubric.md) reaches the pass line (≥ 42) AND the user confirms; below 35, rewrite rather than patch.
- Enforce rhythm hard: per ~200 words, one ≤8-word and one ≥40-word sentence; zero em dashes in final output.
- Source: if the user has an existing .md/.tex/.docx manuscript, split it with the io-worker sub-agent (check path). If starting fresh, write then aggressively humanize (write path, radical intensity).
