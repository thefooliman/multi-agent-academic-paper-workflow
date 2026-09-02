---
name: paper-stop
description: Safely save the current workflow state and stop. Resume later with /paper-write or /paper-check.
---

If state.json exists in the current working directory, append {"event": "user_stop"} to workflow-log.json and confirm: "Workflow saved. Resume later with /paper-write or /paper-check."

If no state.json exists, say: "No active workflow to stop."
