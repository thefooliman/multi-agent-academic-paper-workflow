# warp.md: Developer Guide

Architecture notes for contributors. End users should read the portal skill instead.

## Layout

- .claude-plugin/plugin.json: plugin manifest
- skills/: user-facing entry skills (slash commands): paper-write, paper-check, paper-radical, paper-stop, paper-reset
- agents/: worker sub-agents dispatched by the coordinator
- configs/: user-config + rule sets (humanizer pattern catalog, claim-evidence discipline, scoring rubric, section strategies)
- schemas/: JSON Schema contracts for agent outputs and state
- utils/: python helpers (state_manager + parsing placeholders)

## Modes and intensity

- mode: write (generate) / check (existing manuscript)
- intensity: standard (fix 🔴 + rhythm) / radical (full catalog + six-step loop + five-dimension score ≥ 42)
- radical mode maps to /paper-radical; standard maps to /paper-write and /paper-check

## How it runs

The coordinator is the main Claude session (skills/paper-write/SKILL.md holds the operating procedure). It reads config + state, then dispatches worker sub-agents with the Agent tool. Workers return pure JSON; the coordinator aggregates and persists.

## State

state.json + workflow-log.json live in the user's working directory. The coordinator saves after every step so an interrupt can be resumed. See schemas/state.schema.json.

## Agent contract

Every worker returns JSON matching a schema in schemas/. The coordinator passes rule text inline because workers cannot read the plugin files.

## Extending

- Add a worker: create agents/<name>.md (frontmatter name/description) and update the dispatch step in the coordinator.
- Add a rule set: put it in configs/ and reference it in the relevant agent + coordinator.
