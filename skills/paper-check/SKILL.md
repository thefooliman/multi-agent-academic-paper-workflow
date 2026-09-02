---
name: paper-check
description: Optimize an existing local manuscript (md/tex/docx). Split into chapters, then run the polishing-review-iteration loop and global finalization. No draft generation.
---

# Paper Check — Coordinator

Same operating procedure as /paper-write (read ../../skills/paper-write/SKILL.md and follow it), with these differences:

- mode = "check".
- Before the per-chapter loop, dispatch the io-worker sub-agent to read the user's file and split it into chapters. Store the returned chapter list into state.chapters with status "pending".
- Skip the writer dispatch. Start each chapter directly at the polishing step (step 3a).
- Support processing a single selected chapter: if the user names one, set current_chapter_index to it and process only that chapter.
