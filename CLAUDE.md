# Inventory Manager - Development Environment

## Team Structure
- **App Architect**: Creates tickets, assigns work
- **Backend Lead + 2 Developers**: Flask app, database, APIs  
- **Frontend Lead + 2 Developers**: Templates, UI, client-side
- **QA Lead + 2 Developers**: Testing, verification

## Task Execution Protocol
1. **You describe requirement**
2. **I create formal ticket**  
3. **You approve ticket**
4. **Agents execute exactly as specified**

## Quality Standards (MVP Lean)
- Code must work correctly
- Basic tests for core functionality
- Code formatted with Black
- Manual verification acceptable

## Development Commands
```bash
python scripts/dev.py      # Development server
python scripts/lint.py     # Code formatting only
python run.py              # Production start
```

## Communication Rules
- Structured reporting only
- No conversational elements
- Immediate accountability for deviations
- Work stops if ticket requirements not met

## Task Control
**BEFORE WORK BEGINS**: Formal ticket approval required
**DURING WORK**: Strict adherence to ticket specifications
**AFTER WORK**: Team lead verification of exact compliance

## Environment Setup
- Uses SQLite database at `instance/dev.db`
- Service account file: `secrets/test-service-key.json` (placeholder - needs real credentials)
- Environment variables in `.env` file

## Known Issues Fixed
- Removed PostgreSQL dependency (psycopg2-binary) - using SQLite
- Updated SQLAlchemy to 2.0.42 for Python 3.13 compatibility
- Database URL uses absolute Windows path to avoid connection issues

## Architecture
- Flask app with SQLAlchemy ORM
- Google Sheets/Drive integration via service account
- Redis for caching/background tasks
- Alembic for database migrations
- Webhook processing for order management

## Development
- Python 3.13
- All dependencies in requirements.txt installed
- Database migrations completed successfully
- App runs on http://127.0.0.1:5000