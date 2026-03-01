# OpenAI Codex Orchestrator — Architecture Map

```
All OpenClaw Skills
(any task needing AI generation/analysis)
        |
        v
+------------------------------------+
| OPENAI CODEX ORCHESTRATOR          |
|                                    |
|  +-----------+   +---------------+ |
|  | Local     |   | Optimization  | |
|  | First     |   | Pipeline      | |
|  | Check     |   | cache/batch   | |
|  +-----+-----+   | dedup         | |
|        |         +-------+-------+ |
|        +-----------------+---------+
|                          |
|                 +--------v--------+
|                 | Budget + Rate   |
|                 | Limiter         |
|                 +--------+--------+
|                          |
|                 +--------v--------+
|                 | Model Router    |
|                 | Tier 1/2/3      |
|                 +--------+--------+
|                          |
|                 +--------v--------+
|                 | Retry +         |
|                 | Fallback Engine |
|                 +--------+--------+
|                          |
|                 +--------v--------+
|                 | Monitoring +    |
|                 | Alerting        |
|                 +-----------------+
+------------------------------------+
                |
                v
OpenAI API (Codex 5.3 / Mini / Emergency)
```

## Gateway Rule (Mandatory)
- No skill should call OpenAI directly.
- All AI API work must route through the orchestrator preflight and policy gates.
- Direct-call exceptions require explicit human approval.
