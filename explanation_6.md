## Union Function

### Reasoning:
The union function combines two linked lists by collecting unique elements in a set. It ensures no duplicates by leveraging the set's property of holding only unique values, and then constructs a new linked list with these elements.

### Time Efficiency:
- **Time Complexity**: O(n + m) where n and m are the sizes of the two lists, due to traversing both lists and adding elements to the set.
- **Overall**: O(n + m).

### Space Efficiency:
- **Space Complexity**: O(n + m) for storing the unique elements in a set and creating the result linked list.

## Intersection Function

### Reasoning:
The intersection function finds common elements between two linked lists by storing their values in sets and computing the intersection of these sets, followed by constructing a new linked list for the result.

### Time Efficiency:
- **Time Complexity**: O(n + m) where n and m are the sizes of the two lists, for traversing the lists and computing the intersection.
- **Overall**: O(n + m).

### Space Efficiency:
- **Space Complexity**: O(n + m) due to storing the elements in sets and the resulting intersection list.
