import os
import sys
import shutil
import subprocess
import time
import uuid

def call_api(prompt, options, context):
    soul_path = options.get('config', {}).get('soul_path')

    # Change this to your nanobot workspace directory
    workspace_dir = os.path.abspath("/home/albertajiang/.nanobot/workspace")

    shutil.copy(soul_path, os.path.join(workspace_dir, "SOUL.md"))
    time.sleep(1)
    unique_prompt = f"{prompt} (Ref: {uuid.uuid4().hex[:8]})"
    try:
        result = subprocess.run(
            ["nanobot", "agent", "-m", unique_prompt],
            capture_output=True,
            text=True,
            timeout=60,
            cwd=workspace_dir
        )
        return {"output": result.stdout.strip()}
    except Exception as e:
        return {"error": str(e)}
