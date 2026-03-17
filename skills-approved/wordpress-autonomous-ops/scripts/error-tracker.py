#!/usr/bin/env python3
"""
WordPress Error Pattern Tracker — Log, query, and learn from WordPress operation errors.
Usage: python3 error-tracker.py --log "error description" --pattern wpautop
       python3 error-tracker.py --match "symptom text"
       python3 error-tracker.py --stats
"""

import json
import os
import argparse
from datetime import datetime
from pathlib import Path

# Error pattern database location
PATTERN_DB = Path.home() / '.openclaw' / 'workspace' / 'memory' / 'wp-error-patterns.json'


class ErrorPatternTracker:
    def __init__(self):
        self.db_path = PATTERN_DB
        self.db_path.parent.mkdir(parents=True, exist_ok=True)
        self.patterns = self._load()

    def _load(self) -> dict:
        if self.db_path.exists():
            with open(self.db_path) as f:
                return json.load(f)
        return {'patterns': {}, 'history': []}

    def _save(self):
        with open(self.db_path, 'w') as f:
            json.dump(self.patterns, f, indent=2)

    def log_error(self, pattern_id: str, description: str,
                  site: str = '', operation: str = '',
                  symptoms: list = None, fix_applied: str = '',
                  fix_worked: bool = None):
        """Log an error occurrence."""
        entry = {
            'timestamp': datetime.utcnow().isoformat() + 'Z',
            'pattern_id': pattern_id,
            'description': description,
            'site': site,
            'operation': operation,
            'symptoms': symptoms or [],
            'fix_applied': fix_applied,
            'fix_worked': fix_worked
        }

        self.patterns['history'].append(entry)

        # Update pattern stats
        if pattern_id not in self.patterns['patterns']:
            self.patterns['patterns'][pattern_id] = {
                'first_seen': entry['timestamp'],
                'occurrences': 0,
                'fix_success_rate': 0,
                'fix_attempts': 0,
                'fix_successes': 0,
                'symptoms': symptoms or [],
                'known_fixes': []
            }

        p = self.patterns['patterns'][pattern_id]
        p['occurrences'] += 1
        p['last_seen'] = entry['timestamp']

        if fix_worked is not None:
            p['fix_attempts'] += 1
            if fix_worked:
                p['fix_successes'] += 1
                if fix_applied and fix_applied not in p['known_fixes']:
                    p['known_fixes'].append(fix_applied)
            p['fix_success_rate'] = p['fix_successes'] / p['fix_attempts']

        # Update symptoms
        if symptoms:
            for s in symptoms:
                if s not in p['symptoms']:
                    p['symptoms'].append(s)

        self._save()
        return entry

    def match_symptoms(self, symptoms: list) -> list:
        """Match current symptoms against known patterns."""
        matches = []
        for pid, pattern in self.patterns['patterns'].items():
            score = 0
            matched_symptoms = []
            for symptom in symptoms:
                for known in pattern['symptoms']:
                    if symptom.lower() in known.lower() or known.lower() in symptom.lower():
                        score += 1
                        matched_symptoms.append(known)

            if score > 0:
                matches.append({
                    'pattern_id': pid,
                    'confidence': min(score / max(len(pattern['symptoms']), 1), 1.0),
                    'occurrences': pattern['occurrences'],
                    'fix_success_rate': pattern['fix_success_rate'],
                    'matched_symptoms': matched_symptoms,
                    'known_fixes': pattern['known_fixes']
                })

        return sorted(matches, key=lambda x: x['confidence'], reverse=True)

    def get_stats(self) -> dict:
        """Get overall statistics."""
        patterns = self.patterns['patterns']
        history = self.patterns['history']

        total_errors = sum(p['occurrences'] for p in patterns.values())
        avg_success_rate = 0
        if patterns:
            rates = [p['fix_success_rate'] for p in patterns.values() if p['fix_attempts'] > 0]
            avg_success_rate = sum(rates) / len(rates) if rates else 0

        # Most common patterns
        sorted_patterns = sorted(patterns.items(),
                                 key=lambda x: x[1]['occurrences'], reverse=True)

        return {
            'total_patterns': len(patterns),
            'total_error_occurrences': total_errors,
            'total_operations_logged': len(history),
            'average_fix_success_rate': round(avg_success_rate, 2),
            'top_patterns': [
                {'id': pid, 'occurrences': p['occurrences'],
                 'success_rate': p['fix_success_rate']}
                for pid, p in sorted_patterns[:10]
            ]
        }

    def get_prevention_rules(self) -> list:
        """Generate prevention rules from known patterns."""
        rules = []
        for pid, pattern in self.patterns['patterns'].items():
            if pattern['fix_success_rate'] > 0.7 and pattern['occurrences'] > 2:
                rules.append({
                    'pattern': pid,
                    'prevention': f"Before operation, check for: {', '.join(pattern['symptoms'][:3])}",
                    'confidence': pattern['fix_success_rate'],
                    'based_on': f"{pattern['occurrences']} occurrences"
                })
        return rules

    def recommend_strategy(self, operation_type: str) -> dict:
        """Recommend execution strategy based on historical performance."""
        ops_history = [h for h in self.patterns['history']
                      if h.get('operation') == operation_type]

        if not ops_history:
            return {'strategy': 'learning', 'confidence': 0.5,
                    'recommendation': 'No history for this operation type. Use learning strategy.'}

        success_count = sum(1 for h in ops_history if h.get('fix_worked'))
        error_count = len(ops_history) - success_count
        success_rate = success_count / len(ops_history) if ops_history else 0

        if success_rate > 0.9:
            strategy = 'aggressive'
            rec = 'High success rate. Use aggressive strategy with reduced verification.'
        elif success_rate > 0.7:
            strategy = 'safe_first'
            rec = 'Moderate success rate. Use safe-first strategy with standard verification.'
        else:
            strategy = 'learning'
            rec = 'Low success rate. Use learning strategy with full verification and logging.'

        return {
            'strategy': strategy,
            'confidence': round(success_rate, 2),
            'total_attempts': len(ops_history),
            'successes': success_count,
            'errors': error_count,
            'recommendation': rec
        }


def main():
    parser = argparse.ArgumentParser(description='WordPress error pattern tracker')
    parser.add_argument('--log', help='Log an error (description)')
    parser.add_argument('--pattern', help='Pattern ID for this error')
    parser.add_argument('--site', default='', help='Site URL')
    parser.add_argument('--operation', default='', help='Operation type')
    parser.add_argument('--symptoms', nargs='+', help='Symptom keywords')
    parser.add_argument('--fix', default='', help='Fix applied')
    parser.add_argument('--fix-worked', action='store_true', help='Fix worked')
    parser.add_argument('--fix-failed', action='store_true', help='Fix failed')
    parser.add_argument('--match', nargs='+', help='Match symptoms against known patterns')
    parser.add_argument('--stats', action='store_true', help='Show statistics')
    parser.add_argument('--prevention', action='store_true', help='Show prevention rules')
    parser.add_argument('--strategy', help='Get strategy recommendation for operation type')

    args = parser.parse_args()
    tracker = ErrorPatternTracker()

    if args.log:
        fix_worked = None
        if args.fix_worked:
            fix_worked = True
        elif args.fix_failed:
            fix_worked = False

        entry = tracker.log_error(
            pattern_id=args.pattern or 'unknown',
            description=args.log,
            site=args.site,
            operation=args.operation,
            symptoms=args.symptoms,
            fix_applied=args.fix,
            fix_worked=fix_worked
        )
        print(f"Logged: {entry['pattern_id']} at {entry['timestamp']}")

    elif args.match:
        matches = tracker.match_symptoms(args.match)
        if matches:
            print(f"Found {len(matches)} matching patterns:\n")
            for m in matches:
                print(f"Pattern: {m['pattern_id']}")
                print(f"  Confidence: {m['confidence']:.0%}")
                print(f"  Occurrences: {m['occurrences']}")
                print(f"  Fix success rate: {m['fix_success_rate']:.0%}")
                print(f"  Known fixes: {', '.join(m['known_fixes'])}")
                print()
        else:
            print("No matching patterns found. This may be a new error type.")

    elif args.stats:
        stats = tracker.get_stats()
        print("=== WordPress Error Pattern Statistics ===")
        print(f"Total patterns: {stats['total_patterns']}")
        print(f"Total error occurrences: {stats['total_error_occurrences']}")
        print(f"Total operations logged: {stats['total_operations_logged']}")
        print(f"Average fix success rate: {stats['average_fix_success_rate']:.0%}")
        if stats['top_patterns']:
            print(f"\nTop patterns:")
            for p in stats['top_patterns']:
                print(f"  {p['id']}: {p['occurrences']} occurrences, {p['success_rate']:.0%} fix rate")

    elif args.prevention:
        rules = tracker.get_prevention_rules()
        print("=== Prevention Rules ===")
        for r in rules:
            print(f"\n{r['pattern']} (confidence: {r['confidence']:.0%})")
            print(f"  {r['prevention']}")
            print(f"  Based on: {r['based_on']}")

    elif args.strategy:
        rec = tracker.recommend_strategy(args.strategy)
        print(f"=== Strategy for: {args.strategy} ===")
        print(f"Recommended: {rec['strategy']}")
        print(f"Confidence: {rec['confidence']:.0%}")
        print(f"History: {rec.get('successes', 0)}/{rec.get('total_attempts', 0)} successes")
        print(f"{rec['recommendation']}")


if __name__ == '__main__':
    main()
