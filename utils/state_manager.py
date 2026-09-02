import json
import os
import sys
from pathlib import Path

# state lives next to the paper you are working on, not inside the plugin
BASE_DIR = Path.cwd()
STATE_FILE = BASE_DIR / "state.json"
LOG_FILE = BASE_DIR / "workflow-log.json"


def load_state():
    # read the snapshot, {} if something is broken
    if not STATE_FILE.exists():
        return {}
    try:
        with open(STATE_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except json.JSONDecodeError:
        return {}


def save_state(state_obj):
    # dump snapshot
    with open(STATE_FILE, "w", encoding="utf-8") as f:
        json.dump(state_obj, f, ensure_ascii=False, indent=2)


def reset_state():
    # wipe snapshot and log
    for f in (STATE_FILE, LOG_FILE):
        if f.exists():
            os.remove(f)


def append_log(entry):
    # grow the log
    data = []
    if LOG_FILE.exists():
        try:
            with open(LOG_FILE, "r", encoding="utf-8") as f:
                data = json.load(f)
        except json.JSONDecodeError:
            data = []
    data.append(entry)
    with open(LOG_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


if __name__ == "__main__":
    # tiny cli so you can drive it from bash: python utils/state_manager.py load
    cmd = sys.argv[1] if len(sys.argv) > 1 else "load"
    if cmd == "load":
        print(json.dumps(load_state(), ensure_ascii=False, indent=2))
    elif cmd == "save":
        save_state(json.loads(sys.argv[2]))
    elif cmd == "reset":
        reset_state()
    elif cmd == "log":
        append_log(json.loads(sys.argv[2]))
