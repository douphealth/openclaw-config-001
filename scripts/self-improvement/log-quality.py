#!/usr/bin/env python3
"""
Log quality scores for completed tasks to memory/YYYY-MM-DD.md
Usage: python3 log-quality.py "task name" 22 5 4 5 4 4
"""
import sys
from datetime import datetime
from pathlib import Path

WORKSPACE = Path.home() / ".openclaw" / "workspace"
MEMORY_DIR = WORKSPACE / "memory"

def log_quality(task_name, total, functionality, quality, verification, speed, learning):
    today = datetime.now().strftime('%Y-%m-%d')
    memory_file = MEMORY_DIR / f"{today}.md"
    
    entry = f"\n## Quality Log: {task_name}\n"
    entry += f"- Functionality: {functionality}/5\n"
    entry += f"- Quality: {quality}/5\n"
    entry += f"- Verification: {verification}/5\n"
    entry += f"- Speed: {speed}/5\n"
    entry += f"- Learning: {learning}/5\n"
    entry += f"- **Total: {total}/25** {'✅' if total >= 22 else '⚠️'}\n"
    
    with open(memory_file, 'a') as f:
        f.write(entry)
    
    print(f"Logged: {task_name} = {total}/25")

if __name__ == "__main__":
    if len(sys.argv) >= 9:
        log_quality(sys.argv[1], int(sys.argv[2]), int(sys.argv[3]), 
                   int(sys.argv[4]), int(sys.argv[5]), int(sys.argv[6]), int(sys.argv[7]))
    else:
        print("Usage: python3 log-quality.py 'task' total F Q V S L")
