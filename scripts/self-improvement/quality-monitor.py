#!/usr/bin/env python3
"""
Quality Monitor — Tracks task completion quality across sessions
Run daily to review memory files and report quality trends.
"""
import json, os, re
from datetime import datetime, timedelta
from pathlib import Path

WORKSPACE = Path.home() / ".openclaw" / "workspace"
MEMORY_DIR = WORKSPACE / "memory"

def scan_recent_memories(days=7):
    """Scan memory files from recent days for quality scores."""
    results = []
    for i in range(days):
        date = datetime.now() - timedelta(days=i)
        path = MEMORY_DIR / f"{date.strftime('%Y-%m-%d')}.md"
        if path.exists():
            content = path.read_text()
            # Find scorecard mentions
            scores = re.findall(r'(\d+)/25', content)
            tasks = re.findall(r'## (.+)', content)
            results.append({
                'date': date.strftime('%Y-%m-%d'),
                'scores': [int(s) for s in scores],
                'tasks': len(tasks),
                'lines': len(content.split('\n'))
            })
    return results

def check_skill_health():
    """Check all skills have required sections."""
    skills_dir = WORKSPACE / "skills"
    health = {'total': 0, 'has_performance': 0, 'has_scorecard': 0, 'has_antipatterns': 0}
    for skill_file in skills_dir.glob("*/SKILL.md"):
        health['total'] += 1
        content = skill_file.read_text()
        if 'Performance Optimizations' in content:
            health['has_performance'] += 1
        if '/25' in content:
            health['has_scorecard'] += 1
        if 'Anti-Pattern' in content:
            health['has_antipatterns'] += 1
    return health

def generate_report():
    """Generate quality report."""
    print("=" * 50)
    print("QUALITY MONITOR REPORT")
    print("=" * 50)
    
    # Memory analysis
    memories = scan_recent_memories(7)
    total_scores = []
    for m in memories:
        total_scores.extend(m['scores'])
    
    if total_scores:
        avg = sum(total_scores) / len(total_scores)
        print(f"\n📊 Average Quality Score: {avg:.1f}/25 ({'✅ GOOD' if avg >= 22 else '⚠️ NEEDS WORK'})")
    else:
        print("\n📊 No quality scores found in recent memory")
    
    print(f"\n📝 Memory Activity (7 days):")
    for m in memories:
        if m['lines'] > 10:
            print(f"  {m['date']}: {m['lines']} lines, {m['tasks']} sections")
    
    # Skill health
    health = check_skill_health()
    print(f"\n🏥 Skill Health:")
    print(f"  Total skills: {health['total']}")
    print(f"  With performance: {health['has_performance']}/{health['total']} ({health['has_performance']*100//health['total']}%)")
    print(f"  With scorecard: {health['has_scorecard']}/{health['total']} ({health['has_scorecard']*100//health['total']}%)")
    print(f"  With anti-patterns: {health['has_antipatterns']}/{health['total']} ({health['has_antipatterns']*100//health['total']}%)")
    
    # Recommendations
    print(f"\n💡 Recommendations:")
    if health['has_scorecard'] < health['total']:
        missing = health['total'] - health['has_scorecard']
        print(f"  - Add scorecard to {missing} remaining skills")
    if total_scores and avg < 22:
        print(f"  - Average quality below target (22). Review recent tasks.")
    if not total_scores:
        print(f"  - No quality scores logged. Ensure tasks are scored.")
    print()

if __name__ == "__main__":
    generate_report()
