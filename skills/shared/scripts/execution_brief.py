#!/usr/bin/env python3
"""
Generate a structured execution brief for serious OpenClaw tasks.
"""
import json
import sys
from datetime import datetime

TEMPLATE = {
    "objective": "",
    "scope": {"included": [], "excluded": []},
    "constraints": {
        "environment": "production",
        "downtime_tolerance": "none unless explicitly approved",
        "seo_data_preservation": True,
        "time_budget": "",
        "model_constraint": "",
        "user_specific": []
    },
    "current_state": {
        "what_exists_now": [],
        "evidence_gathered": [],
        "known_blockers": [],
        "unknowns": []
    },
    "risk_class": [],
    "best_strategy": "",
    "skills": [],
    "execution_plan": [],
    "parallelization": {
        "safe": [],
        "serialized": [],
        "workers": []
    },
    "verification": {
        "api_state_proof": [],
        "live_render_proof": [],
        "sampling_requirement": "",
        "completion_threshold": ""
    },
    "rollback": {
        "backup_location": "",
        "restore_path": "",
        "stop_conditions": [],
        "escalation_path": ""
    },
    "completion_rule": []
}

def make_brief(objective, strategy="plan-first execution", skills=None):
    brief = TEMPLATE.copy()
    brief["generated_at"] = datetime.utcnow().isoformat() + "Z"
    brief["objective"] = objective
    brief["best_strategy"] = strategy
    brief["skills"] = skills or []
    return brief

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: execution_brief.py 'objective' [strategy] [skill1,skill2,...]")
        sys.exit(1)
    objective = sys.argv[1]
    strategy = sys.argv[2] if len(sys.argv) > 2 else "plan-first execution"
    skills = sys.argv[3].split(',') if len(sys.argv) > 3 and sys.argv[3] else []
    print(json.dumps(make_brief(objective, strategy, skills), indent=2))
