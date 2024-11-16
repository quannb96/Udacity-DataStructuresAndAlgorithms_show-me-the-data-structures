## Reasoning Behind Decisions:
Recursive Approach: The function uses recursion to explore subdirectories of unknown depth, making it efficient for traversing complex directory structures.
File and Suffix Checks: It checks if each entry is a file and whether the filename ends with the specified suffix, ensuring only relevant files are included in the result.

## Time Efficiency:
Time Complexity: O(n), where n is the total number of files and directories. Each entry is checked once, and suffix matching is a constant-time operation.

## Space Efficiency:
Space Complexity: O(n), where n is the number of matching files. The space is primarily used to store the result list. The recursion stack does not add significant overhead unless the directory depth is extremely large.
