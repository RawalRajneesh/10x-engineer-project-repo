---
description: Agent Safety
---

Agent Safety: Command Execution

Never enable terminal auto-approval.

All shell commands must be explicitly shown and require manual user approval.

For destructive or high-risk commands (delete, migrate, deploy, publish, infra, prod actions):
- Only suggest the command
- Clearly explain impact
- Provide safer alternatives
- Never insist on execution