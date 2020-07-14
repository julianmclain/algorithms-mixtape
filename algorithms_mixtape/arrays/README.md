# Arrays

An array is a collection of similar items. The items are stored in neighboring
(contiguous) memory locations. 

![array](https://www.dropbox.com/s/53xjnd0p7hrhtrn/array.png?raw=1)

Since arrays use a contiguous block of memory,
their size has to be specified at the time of creation. When an array is
created, programming languages typically initialize a default value at each
index. For example, Java always initializes empty Array slots to null if the
Array contains objects, or to default values if it contains primitive types. An
array int [] would contain the default value of 0 for each element, float[]
would contain default values of 0.0, and bool[] would contain default values of
false.

## Operations

Arrays are ideal for ccessing elements at random indices and insertion / deletion operations on the last element of the array.

### Access

Array elements are accessed by index.

> Accessing any element takes *O*(1) time

### Insertion

Inserting an element into an array generally requires shifting elements to make
room for the new one. For example, if you want to add an element to the front of
the array, you need to shift all *n* elements one index to the right before
inserting the new element. Adding to the front of the array is the worst-case
runtime scenario.

![array-insertion](https://www.dropbox.com/s/l68bqgko9fmdl4f/array-insertion.png?raw=1)

> Inserting a random element takes *O*(*n*) time.

Note: inserting an element to the **end of the array** can be done in constant time.

### Deletion

With array insertion, you typically need to shift elements to the right in order to make space for a new element. On the other hand, with array deletion, you typically need to shift elements to the left in order to fill in the vacant space created by deleting an element. The time complexity for deletions is the same as insertions. 

![array-deletion](https://www.dropbox.com/s/m4tixajyttzblvb/array-deletion.png?raw=1)

> Deleting a random element takes *O*(*n*) time.

Note: deleting an element to the **end of the array** can be done in constant time.
