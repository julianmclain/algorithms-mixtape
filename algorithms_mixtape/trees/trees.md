# Trees

A tree is a frequently-used data structure to simulate a hierarchical tree
structure. Each node of the tree will have a root value and a list of references
to other nodes which are called child nodes. From graph view, a tree can also be
defined as a directed acyclic graph which has N nodes and N-1 edges.

## Binary trees

A Binary Tree is one of the most typical tree structure. As the name suggests, a
binary tree is a tree data structure in which each node has at most two
children, which are referred to as the left child and the right child.

## Traversing a tree

Since trees reduce to graphs, there are 2 primary ways to traverse them:
- Breadth first search
- Depth first search

Within the DFS approach, there are 3 further distinctions:
1. Pre-order traversal - visit the root first. Then traverse the left subtree.
   Finally, traverse the right subtree.
2. In-order traversal - traverse the left subtree first. Then visit the root.
   Finally, traverse the right subtree. Typically, for a binary search tree, we
   can retrieve all the data in sorted order using in-order traversal.
3. Post-order traversal - traverse the left subtree first. Then traverse the
   right subtree. Finally visit the root. Post-order is widely used in
   mathematical expressions. It is easier to write a program to parse a
   post-order expression.

![tree traversal](https://www.dropbox.com/s/w2ukn1pe6qo2c97/tree_traversal.png?raw=1)