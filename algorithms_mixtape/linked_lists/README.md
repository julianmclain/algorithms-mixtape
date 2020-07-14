# Linked Lists

A linked list is a collection of elements that are linked together by
`reference`.

## Singly-Linked Lists

In a singly-linked list, each element in the list is an object that stores a
value and reference to the next element. In most cases, the `head` node (the
first node) is used to represent the whole list.

![singly-linked-list](https://www.dropbox.com/s/lau2023zvxjdsly/singly-linked-list.png?raw=1)

### Operations

The real magic of linked lists happens when you're able to limit your operations
to using only the `head` of the list or the `tail` of the list.

#### Access

Unlike arrays, you can't access an element from the middle of a linked
list in constant time. To access the *i*<sup>th</sup> element, you have to
traverse *i* elements.

> Accessing a random element takes *O*(*n*) time.

For instance, in the example above, the head is the node 23. The only way to
visit the 3rd node is to use the "next" field of the head node to get to the 2nd
node (node 6); Then with the "next" field of node 6, we are able to visit the
3rd node.

Note: accessing the **head element** always takes constant time.

#### Insertion

With insertion, linked lists have an advantage over arrays.

![linked-list-insertion](https://www.dropbox.com/s/huyw8yisska03o3/linked-list-add-element.png?raw=1)

Adding an element can be done by simply pointing the `prev` node to the `cur`
node and pointing the `cur` node to the `next` node.

> Inserting any element takes *O*(1) time.

Note: the insertion time-complexity assumes that references to `prev` and `next`
are already available. If that's not the case, then it will take *O*(*n*) time
to scan the list until `prev` is found. An element can always be inserted **at the
head** of the list in constant time.

#### Deletion

The story for linked list deletion is the same as insertion.

![linked-list-deletion](https://www.dropbox.com/s/q763jbr8kk25wx6/linked-list-deletion.png?raw=1)

Deleting an element can be done by pointing the `prev` node to the `next` node.
`cur` isn't actually deleted, but the fact that there's no reference to `cur`
means that it can't be accessed.

> Deleting any element takes *O*(1) time.

Note: the same note about insertion time-complexity above applies here as well.