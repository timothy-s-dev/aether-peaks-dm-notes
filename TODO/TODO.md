---
tasks-total: 1
tasks-completed: 0
tasks-remaining: 1
---
* [ ] Is it worth thinking about how much time I'll have for the [[1. Kindled]] adventure session(s), then trying to make notes of how long each section should take, so I can try to manage the pace as we play?

# Planning Tasks
```base
filters:
  and:
    - note["tasks-planning-total"] > 0
formulas:
  tasks: '"(" + note["tasks-planning-completed"] + "/" + note["tasks-planning-total"] + ")"'
  priority: |-
    if(
      file.hasTag("#priority/high"),
      "high",
      if(
        file.hasTag("#priority/med"),
        "medium",
        "low"
      )
    )
  prioritySort: |-
    if(
      file.hasTag("#priority/high"),
      1,
      if(
        file.hasTag("#priority/med"),
        2,
        3
      )
    )
views:
  - type: list
    name: List
    order:
      - file.name
      - formula.tasks
      - formula.priority
    sort:
      - property: formula.prioritySort
        direction: ASC
      - property: file.mtime
        direction: ASC

```
## Stub Articles (Top 10)
![[Stub Pages.base#Top 10]]
