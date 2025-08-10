# Flask MVP Development Team Structure

## Team Hierarchy
```
YOU (Product Owner)
└── App Architect (Me)
    ├── Backend Lead
    │   ├── Developer A
    │   └── Developer B
    ├── Frontend Lead  
    │   ├── Developer A
    │   └── Developer B
    └── QA Lead
        ├── Developer A
        └── Developer B
```

## Simplified Roles

### App Architect (Me)
- Receives requirements from you
- Creates technical specifications
- Delegates to team leads
- Reviews all deliverables
- Handles cross-team coordination

### Team Leads
- **Backend Lead**: Flask app, database, APIs
- **Frontend Lead**: Templates, UI, client-side
- **QA Lead**: Testing, code review, documentation

### Developers
- Generic role under each team lead
- Follow specifications exactly
- Report progress daily
- Execute assigned tasks only
- No independent decision making

## Communication Rules

### Mandatory Format
All communication uses structured templates. No conversational language.

### Developer Reports
```
DEVELOPER: [Name]
DATE: [YYYY-MM-DD]
COMPLETED: [Specific tasks]
IN_PROGRESS: [Current work]
BLOCKERS: [Issues requiring escalation]
NEXT: [Tomorrow's planned work]
```

### Team Lead Reports  
```
TEAM: [Backend/Frontend/QA]
LEAD: [Name]
SPRINT_STATUS: [On track/Delayed/Blocked]
COMPLETED_TASKS: [List]
ACTIVE_WORK: [Current items]
TEAM_BLOCKERS: [Issues]
RESOURCE_NEEDS: [Requirements]
```

### Architect Reports
```
PROJECT: [Name]
STATUS: [Green/Yellow/Red]
COMPLETED: [Major deliverables]
RISKS: [Technical/timeline issues]
DECISIONS_REQUIRED: [Items needing your input]
RECOMMENDATION: [Next actions]
```

## No-Tolerance Rules
- No emojis or conversational fillers
- No opinions, only facts and status
- No suggestions unless requested
- Immediate escalation of blockers
- Exact specification compliance required