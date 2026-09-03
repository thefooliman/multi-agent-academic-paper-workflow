# Paper-Agent-Workflow

A Claude Code plugin for writing and humanizing academic papers. It's aimed at 0–30 page course papers and seminar theses: you bring a topic and an outline, it produces a structured draft that doesn't read like a ai wrote it.

## What it does

Three entry points, plus two control commands:

- `/paper-write`: generate a paper from scratch, chapter by chapter.
- `/paper-check`: humanize an existing `.md` / `.tex` / `.docx` manuscript.
- `/paper-radical`: aggressive de-AIGC pass for papers that need to get past Turnitin AI, GPTZero, 知网, or 万方.
- `/paper-stop`: save and pause. `/paper-reset`: wipe state and start over.

A coordinator drives the whole thing from your session and hands work to a set of worker agents: writer, polishing, self-review, blind-fact-check, guard, and io-worker. Each chapter runs write → polish → guard → review → aggregate, then stops and asks whether to iterate again. It never loops on its own; you confirm every round.

## Why it's built this way

The blind fact-checker is the part worth pointing at first. It gets a chapter with zero context, so it can't coast on what it already knows. It catches unsupported claims ("costs have fallen sharply" with no number attached) and structural tells (six paragraphs all the same length) that the other agents pass over.

The other thing that matters is the claim-evidence discipline. Every verb has to match the strength of the evidence behind it. A clean RCT can say "reduced"; an observational result should say "is associated with". That rule does more for academic credibility than any vocabulary swap.

## Install

Command line is the quickest:

```bash
/plugin marketplace add thefooliman/multi-agent-academic-paper-workflow
/plugin install paper-agent-workflow@multi-agent-academic-paper-workflow
/reload-plugins
```

Then run `/paper-write` to confirm it loaded.

Or use the marketplace UI:

1. Open Claude Code and go to Marketplace.
2. Search for Paper-Agent-Workflow and install it.
3. Run `/reload-plugins` if prompted, then `/paper-write` to check it loaded.

Manual clone, if you prefer:

```bash
git clone https://github.com/thefooliman/multi-agent-academic-paper-workflow
# copy the folder into your Claude Code plugins directory, then reload
```

Keep the whole tree intact: `skills/`, `agents/`, `configs/`, `schemas/`, `utils/`.

## Usage

### Write a paper

Run `/paper-write`. It asks for the topic, an outline (paste one or let it draft one), target length, intensity, and optionally a sample of your own previous writing for voice matching. That last one matters: hand it a paragraph you wrote, and the output matches your rhythm and word choices instead of a generic "human" style. Writing your own viewpoints and judgments into the prompt helps the same way — the more of your own thinking you feed in, the more it reads like you and not a clean summary.

### Humanize an existing draft

Put the file in your working directory, run `/paper-check`, give the filename. It splits the manuscript into chapters and runs the same polish-review loop without generating anything new.

### Radical mode

`/paper-radical` runs the full pattern catalog, the six-step loop, and the five-dimension score (pass line 42). Use it when standard polishing isn't enough and the paper has to clear an AI detector.

### Resume

State is saved to `state.json` (plus `workflow-log.json`) in your working directory after every step. `/paper-stop` pauses cleanly. Run `/paper-write` again later and it offers to resume where you left off. Interrupting mid-iteration loses nothing.

## Rules

The humanizer rules live in `configs/`, and they're meant to be edited:

- `humanizer-patterns-en.md`: the pattern catalog, ~45 entries informed by Wikipedia's "Signs of AI writing", the academic-humanizer lineage, and de-aigc-skills. Each entry has a severity (🔴🟡🟢), watch-words, and a before/after. See NOTICE.md for sources and licenses.
- `claim-evidence-discipline.md`: verb↔evidence matching and hedging calibration.
- `scoring-rubric.md`: the five-dimension score used as the convergence measure.
- `section-strategies.md`: per-section rewrite intensity. Abstract and intro get the heaviest rewrite; methods and robustness get the lightest.
- `polishing-rules-en.md`: the operational rules that tie the rest together, plus the standard vs radical intensity tiers.

## Structure

```
skills/       entry skills (the slash commands)
agents/       worker sub-agents
configs/      rule sets and user config
schemas/      JSON contracts for agent output and state
utils/        state_manager + docx/tex parsing placeholders
examples/     sample chapter + humanizer before/after
```

## Limitations

- Built for 0–30 page manuscripts. Longer work will have gaps you'll need to catch yourself.
- `.docx`/`.tex` parsing is basic for now; complex macros won't split cleanly. Better parsing is planned for v1.1.
- It won't invent citations or empirical data, and it shouldn't be asked to.
- You review everything. The tool is an aid, not a substitute for reading your own paper.

## Academic integrity

The humanizer's goal is to return human-written and AI-assisted text to the language distribution of a real researcher, not to help fully AI-generated work evade disclosure. Academic integrity outranks detection scores. When a claim lacks evidence, the fix is to flag it, not to hide it. Comply with your institution's policies.
