# Team Coordination Guide

## How to Use Your Development Team

### Starting a New Feature/Project

1. **You (Product Owner) → App Architect**
   ```markdown
   ## Feature Request: [Feature Name]
   
   ### Business Requirements
   - [What the business needs]
   - [Success criteria]
   - [Timeline expectations]
   
   ### User Stories
   - As a [user type], I want [functionality] so that [benefit]
   
   ### Constraints
   - [Technical limitations]
   - [Budget considerations]
   - [Integration requirements]
   ```

2. **App Architect analyzes and breaks down**
   - Reviews current architecture
   - Identifies affected teams
   - Creates technical specifications
   - Assigns work to team leads

3. **Team Leads delegate to developers**
   - Break down specifications into tasks
   - Assign based on expertise and workload
   - Set timelines and dependencies

### Daily Operations

#### Getting Status Updates
Ask me: *"Get status update from [team] team"* or *"What's the current progress on [feature]?"*

I'll simulate:
- App Architect gathering reports from team leads
- Team leads collecting updates from developers  
- Comprehensive status with blockers and timelines

#### Making Changes
Tell me: *"I need to modify the requirements for [feature]"* or *"Change priority to focus on [different area]"*

I'll simulate:
- App Architect assessing impact
- Team leads adjusting plans
- Communication across affected teams

## Team Interaction Examples

### Example 1: New Feature Request
**You**: "I need to add customer notification system for order updates"

**I'll simulate**:
1. **App Architect** analyzes requirements
2. **Backend Lead** designs notification API
3. **Integration Lead** handles email/SMS providers
4. **Frontend Lead** creates notification preferences UI
5. **QA Lead** designs testing strategy
6. **DevOps Lead** sets up monitoring

### Example 2: Bug Report  
**You**: "Users are reporting slow order processing"

**I'll simulate**:
1. **App Architect** coordinates investigation
2. **QA Lead** reproduces and analyzes
3. **Backend Lead** profiles performance
4. **DevOps Lead** checks infrastructure
5. **Team coordination** to implement fix

### Example 3: Architecture Decision
**You**: "Should we switch to microservices?"

**I'll simulate**:
1. **App Architect** evaluates options
2. **All Team Leads** provide domain input
3. **Architect** presents recommendation with pros/cons
4. **Implementation roadmap** if approved

## Communication Commands

### Status Queries
- `"Get weekly report from App Architect"`
- `"What is [team name] team working on?"`
- `"Show me blockers across all teams"`
- `"Give me project timeline update"`

### Task Assignment
- `"Assign [feature] to development teams"`
- `"Prioritize [task] for this sprint"`
- `"I need emergency fix for [issue]"`

### Team Management
- `"Review code quality across teams"`
- `"Plan deployment for [feature]"`
- `"Assess team workload and capacity"`

## Quality Assurance

Every deliverable goes through:
1. **Developer** implements and self-tests
2. **Team Lead** code reviews and approves
3. **QA Team** tests functionality and integration
4. **App Architect** reviews architectural compliance
5. **DevOps** handles deployment and monitoring

## Emergency Protocols

For urgent issues:
1. Tell me: *"Emergency: [issue description]"*
2. I'll simulate immediate escalation
3. All relevant teams get priority tasking
4. Architect coordinates rapid response
5. Regular updates until resolved

Your development team is ready! Give me your first project or ask for a status update to see the system in action.