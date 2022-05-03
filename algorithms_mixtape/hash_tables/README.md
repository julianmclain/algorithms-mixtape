# Hash Tables

A Hash Table is a data structure which organizes data using hash functions in
order to support quick lookups.

Hash Tables are used to implement several data structures such as Hash Maps,
Hash Sets, and Bloom Filters.

The key idea behind hash tables is to use a hash function to map keys to
buckets. To be more specific:

- When we insert a new key, the hash function will decide which bucket the key
  should be assigned and the key will be stored in the corresponding bucket
- When we want to search for a key, the hash table will use the same hash
  function to find the corresponding bucket and search only in the specific
  bucket.

![hash-table](https://www.dropbox.com/s/km0x4g5mp0lbvs6/hash-table.png?raw=1)

In the example, we use y = x % 5 as our hash function. Let's go through the
insertion and search strategies using this example.

Insertion:
- We pass the keys through the hash function to map them into the corresponding
  bucket.
- For example, 1987 is assigned to bucket 2 while 24 is assigned to bucket 4.

Search:
- We pass the keys through the same hash function and search only in the
  specific bucket.
- For example, if we search for 1987, we will use the same hash function to map
  1987 to 2. So we search in bucket 2 and we successfully find out 1987 in that
  bucket.
- For example, if we search for 23, will map 23 to 3 and search in bucket 3. And
  We find out that 23 is not in bucket 3 which means 23 is not in the hash
  table.

## Applications

Practical programming applications of sets
- Detecting duplicates
- Detecting cycles
- Tracking items "seen" so far
- Identifying unions, intersections, or whether collections are disjoint
- When you need to store 2 pieces of related together (key, value)
- When you want fast information lookup by key [common restaurant example](https://leetcode.com/explore/learn/card/hash-table/184/comparison-with-other-data-structures/1177/)
- When you want to aggregate information by key
  - e.g. Counter in Python [first unique character example](https://leetcode.com/explore/learn/card/hash-table/184/comparison-with-other-data-structures/1119/)
  - e.g. Designing a key function that will group data [Design the key](https://leetcode.com/explore/learn/card/hash-table/185/hash_table_design_the_key/1125/)


## The hash function

The hash function is the most important component of a hash table. The idea is
to try to assign keys to buckets as uniform as you can. Ideally, a perfect hash
function will be a one-one mapping between the key and the bucket. However, in
most cases a hash function is not perfect and there is a tradeoff between the
amount of buckets and the capacity of a bucket.

## Collisions

Ideally, if our hash function is a perfect one-one mapping, we will not need to
handle collisions. Unfortunately, in most cases, collisions are almost
inevitable. For instance, in our previous hash function (y = x % 5), both 1987
and 2 are assigned to bucket 2. That is a collision.

A collision resolution algorithm should solve the following questions:

- How to organize the values in the same bucket?
- What if too many values are assigned to the same bucket?
- How to search a target value in a specific bucket?

These questions are related to the capacity of the bucket and the number of keys
which might be mapped into the same bucket according to our hash function.

For example, assume that a bucket, which holds the maximum number of keys, has N
keys. Typically, if N is constant and small, we can simply use an array to store
keys in the same bucket. If N is variable or large, we might need to use
height-balanced binary search tree instead.

There are several strategies for resolving collisions:

- Separate Chaining: for values with the same hash key, we keep them in a
  bucket, and each bucket is independent from each other.
- Open Addressing: whenever there is a collision, we keep on probing on the main
  space with certain strategy until a free slot is found.
- 2-Choice Hashing: we use two hash functions rather than one, and we pick the
  generated address with fewer collision.

More info at [Wikipedia Hash Table](https://en.wikipedia.org/wiki/Hash_table).

## Designing your own hash table

When designing a hashtable there are two main issues that to tackle.

1. The hash function design
2. Collision handling

Hash function design

- the purpose of the hash function is to map a key to an address in the
  storage space, similarly to the system that we assign a postcode to each mail
  address. As one can image, for a good hash function, it should map different
  keys evenly across the storage space, so that we don't end up with the case
  that the majority of the keys are concentrated in a few spaces.]

### Approach 1: chaining

This is the simplest and most intuitive solution to hash collisions.

The modulo operator is a common choice for the hashing function, i.e:

```
hash = value % base
```

Here, the *base* of modulo operation would be the number of buckets that in the
Hash Table. Theoretically, the more buckets we have (hence the larger the space
would be), the less likely that we would have collisions. The choice of base is
a tradeoff between the space usage and the collision probability.

In addition, it is generally advisable to use a prime number as the base of the
modulo, e.g. 769, in order to reduce the potential collisions.

Each element in the array (i.e. bucket) is a LinkedList, which has a constant time complexity for the insertion as well
as deletion, once we locate the position to update.

Time complexity: O(n/k)
Space complexity: O(n + k)

where *n* is the maximum number of possible entries and *k* is the number of buckets

### Approach 2: binary search tree as the bucket
