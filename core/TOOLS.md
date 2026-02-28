# TOOLS.md - Tool Orchestration & Capability Matrix

# schema
_version: 2.0
_last_updated: 2026-02-28

## Core Capabilities
1. **Search:** Web, Memory, Codebase.
2. **Action:** Computer (Browser), Shell/Bash, File Management.
3. **Integration:** LLM APIs, WordPress XML-RPC/REST, NeuronWriter.

## Preferred Tool Patterns
- Use `search_web` for current trends and SEO entity discovery.
- Use `computer` for deep technical interaction and manual audits.
- Use `read_page` / `get_page_text` for high-density information extraction.

## Safety & Governance
- NO sensitive credential entry (API keys, passwords).
- ALWAYS verify URL parameters for PII leaks.
- Respect bot detection; never attempt bypass.

## Tool Logic
- **Pre-flight:** Check `MEMORY.md` for existing context.
- **Execution:** Atomic, verifiable steps.
- **Post-flight:** Update `STATUS.md` and `HEARTBEAT.md`.
