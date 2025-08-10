# Task Ticket System

## Ticket Creation Protocol

### Before Any Work Begins
1. You describe what needs to be done
2. I create formal ticket with specifications
3. You review and approve ticket
4. Only then do agents begin execution

### Ticket Template
```
TICKET_ID: [AUTO_GENERATED]
TITLE: [Brief description]
PRIORITY: [CRITICAL/HIGH/MEDIUM/LOW]

BUSINESS_REQUIREMENT:
[Why this needs to be done]

TECHNICAL_SPECIFICATION:
[Exactly what needs to be implemented]

ACCEPTANCE_CRITERIA:
- [ ] Specific testable requirement 1
- [ ] Specific testable requirement 2
- [ ] Specific testable requirement 3

AFFECTED_SYSTEMS:
[Which parts of codebase will change]

TEAM_ASSIGNMENTS:
- Backend: [Specific tasks]
- Frontend: [Specific tasks] 
- QA: [Testing requirements]

DEFINITION_OF_DONE:
- [ ] Code implements specification exactly
- [ ] Basic tests pass
- [ ] Manual verification complete
- [ ] Team lead approval obtained
```

### Example Ticket
```
TICKET_ID: INV-001
TITLE: User login system
PRIORITY: HIGH

BUSINESS_REQUIREMENT:
Users need to authenticate to access inventory data

TECHNICAL_SPECIFICATION:
- User model with email/password fields
- Login API endpoint accepting email/password
- JWT token generation and validation
- Protected routes requiring authentication
- Login form template

ACCEPTANCE_CRITERIA:
- [ ] User can register with email/password
- [ ] User can login with valid credentials
- [ ] Invalid credentials return error
- [ ] JWT token required for protected routes
- [ ] Login form displays validation errors

AFFECTED_SYSTEMS:
- core/models/user.py
- api/routes/auth.py
- templates/login.html

TEAM_ASSIGNMENTS:
- Backend: User model, auth endpoints, JWT middleware
- Frontend: Login form, authentication state handling
- QA: Login flow testing, security validation

DEFINITION_OF_DONE:
- [ ] Login flow works end-to-end
- [ ] Basic auth tests pass
- [ ] Manual login/logout verified
- [ ] Backend lead approval
```

## Execution Control

### You Issue Command
"I need user authentication system"

### My Response
"CREATING_TICKET: User authentication system
[Ticket details displayed]
APPROVAL_REQUIRED: Review ticket and confirm to proceed"

### You Approve
"APPROVED" or "MODIFY: [changes needed]"

### Only Then
Agents begin work following ticket exactly

## Progress Tracking

### Shared Task List
All agents work from same ticket task list
No agent invents additional requirements
All progress updates reference ticket tasks

### Daily Status Format
```
TICKET: INV-001
DEVELOPER: Backend_A
STATUS: IN_PROGRESS
COMPLETED_TODAY:
- [ ] User model created
- [ ] Database migration applied
WORKING_TODAY:  
- [ ] JWT token generation
BLOCKERS: None
```

### Team Lead Review
```
TICKET: INV-001
TEAM: Backend
PROGRESS: 60%
TASKS_COMPLETED: 3/5
QUALITY_CHECK: PASSED
BLOCKERS: None
ON_TRACK: YES
```

## Accountability System

### Role Responsibilities
- **Developers**: Execute ticket tasks exactly as specified
- **Team Leads**: Verify completion matches ticket requirements  
- **Architect**: Ensure ticket technical accuracy before assignment

### Failure Protocol
If work deviates from ticket:
1. Immediate stop
2. Team lead identifies deviation
3. Architect reviews and corrects
4. Work resumes only after realignment

No hallucination. No assumption. No creativity beyond ticket scope.