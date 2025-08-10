# Team Communication System

## Communication Channels

### Daily Standups (Team Level)
Each team lead conducts daily standups with their developers:
- **Time**: 15 minutes max
- **Format**: What did you complete? What are you working on? Any blockers?
- **Output**: Daily developer reports sent to team lead

### Weekly Team Reports (Lead → Architect)
Team leads compile weekly reports for the App Architect:
- **Backend Team**: API endpoints, database changes, performance
- **Frontend Team**: UI components, UX improvements, user feedback
- **Integration Team**: External services, webhooks, API integrations  
- **DevOps Team**: Infrastructure, deployments, monitoring
- **QA Team**: Quality metrics, testing status, bug reports

### Sprint Planning (Architect → Product Owner)
App Architect provides comprehensive updates:
- **Frequency**: Every 2 weeks or as needed
- **Content**: Cross-team progress, architectural decisions, recommendations
- **Format**: Executive summary with technical details

## Decision Escalation

### Developer Level Decisions
- Implementation details within assigned tasks
- Code structure and patterns (following team standards)
- Technical approach for individual features

### Team Lead Level Decisions  
- Task priority within team scope
- Team resource allocation
- Technical standards for their domain
- Code review and approval

### Architect Level Decisions
- Cross-team coordination and dependencies
- Technology stack and framework choices
- System architecture patterns
- Performance and security standards

### Product Owner Level Decisions
- Business requirements and priorities
- Feature scope and timeline
- Budget and resource allocation
- Strategic technical direction

## Communication Templates

### Developer Daily Report
```markdown
## [Developer Name] - [Date]

### Completed
- [Specific tasks completed]

### In Progress  
- [Current work items]

### Blockers
- [Any impediments or dependencies]

### Tomorrow
- [Planned work]
```

### Team Lead Weekly Report
```markdown
## [Team Name] Weekly Report - [Date Range]

### Team Accomplishments
- [Major completions this week]

### Current Sprint Progress
- [Active development items]

### Blockers & Dependencies
- [Cross-team needs or impediments]

### Next Week Focus
- [Priority items for coming week]

### Metrics & Health
- [Relevant team metrics]
```

## Cross-Team Coordination

### API Contract Changes
1. Backend Lead proposes changes
2. Architect reviews for system impact
3. Frontend/Integration leads provide input
4. Architect approves and communicates to all teams

### Database Schema Changes  
1. Database Developer designs changes
2. Backend Lead reviews and approves
3. Architect reviews for system impact
4. All teams notified of migration timeline

### External Service Integration
1. Integration Team Lead designs integration
2. Architect reviews for security/performance
3. Backend Team coordinates data flow
4. QA Team plans testing approach

This system ensures clear communication flows while maintaining autonomy for each team to execute within their domain expertise.