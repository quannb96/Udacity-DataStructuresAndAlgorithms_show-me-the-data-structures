## Reasoning Behind Decisions:
Group Hierarchy: The class models a group with sub-groups and users, reflecting real-world organizational structures.
Iterative Search: The is_user_in_group function uses an iterative DFS to check if a user is in the group or any sub-group.


## Time Efficiency:
Time Complexity: O(n) where n is the total number of groups (including sub-groups), as each group is checked once.

## Space Efficiency:
Space Complexity: O(n) due to the DFS stack and the storage for groups and users.
