cat > docs/architecture.md << 'EOF'
# Architecture

## Goal
Build a simple AI Planner app that collects a task + preferences, then generates a recommended schedule.

## Monorepo layout
- apps/mobile: React Native app (UI)
- services/api: Backend API (FastAPI or similar)
- packages/shared: Shared types/validators (optional but useful)
- docs: Architecture + API contracts
- scripts: Dev scripts

## System overview (v1)
Mobile App  ->  API Service  ->  (Database optional v1)  ->  LLM Provider (later)

### v1 principles
- Keep v1 dumb and reliable.
- Generate schedules with deterministic rules first.
- Add AI later for nicer recommendations.

## Data flow (v1)
1) User enters: Task name, deadline, expected outcome, hours/week, working style
2) Mobile sends request to API
3) API returns a recommended schedule (simple)
4) Mobile renders schedule

## Future add-ons (v2+)
- Auth + user accounts
- Saved plans and history
- Calendar integration
- “Regenerate” and “explain why” with LLM
EOF
