# Arrays

An array is a collection of similar items. The items are stored in neighboring
(contiguous) memory locations.

## Operations

### Access

Array elements are accessed by index. Elements at any index can be accessed in
constant time.

### Insertion

Adding an element to the end of the array can be done in constant time. However,
an element anywhere else will take *O*(*n*) time. For example, if you want to
add an element to the front of the array, you need to shift all *n* elements one
index to the right before inserting the new element. Adding to the front of the
array is the worst-case runtime scenario.

### Deletion

The time complexity for deletions is the same as insertions.