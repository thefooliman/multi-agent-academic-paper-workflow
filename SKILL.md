---
name: paper-agent-workflow
description: Multi-agent academic paper workflow. Use /paper-write to generate a new paper, or /paper-check to polish an existing manuscript. /paper-stop to save, /paper-reset to clear.
---

# Paper-Agent-Workflow

A multi-agent academic writing workflow for Claude Code: structured chapter generation, iterative polishing, double review (self-review + blind fact-check), guard rule enforcement, human-in-the-loop confirmation, and breakpoint resume.

## Commands

- /paper-write: generate a new paper chapter by chapter (write mode)
- /paper-check: polish an existing .md / .tex / .docx manuscript (check mode)
- /paper-radical: aggressive de-AIGC humanization (radical mode)
- /paper-stop: save state and stop
- /paper-reset: clear state and start fresh

## Modes

- **Standard** (write/check): fix the must-fix AI-tell patterns plus sentence rhythm, keep the natural academic voice.
- **Radical**: apply the full pattern catalog, the six-step loop, the five-dimension score (pass ≥ 42), and section-by-section rewrite: for passing Turnitin AI, GPTZero, 知网, 万方.

## Resume

State is saved to state.json + workflow-log.json in your working directory after every step. After /paper-stop (or an interrupt), run /paper-write or /paper-check again; it will offer to resume exactly where you left off.

## Agents

The coordinator (this session) dispatches worker sub-agents: writer, polishing, self-review, blind-fact-check, guard, io-worker. All agent-to-agent communication is JSON, following schemas/.
