class HashSet:
    """
    A sample implementation of a HashSet. For this first pass I used an array
    for each 'bucket'. In the future I could get fancier and write another
    implementation using a linked list or a BST.
    """

    def __init__(self):
        self.max_buckets = (
            769  # choosing a prime number reduces the likelihood of collisions
        )
        self.buckets = [[] for i in range(self.max_buckets)]

    def hash_key(self, key: int) -> int:
        return key % self.max_buckets

    def add(self, key: int) -> None:
        if key is None:
            return

        bucket_index = self.hash_key(key)
        bucket = self.buckets[bucket_index]
        if key not in bucket:
            bucket.append(key)

    def remove(self, key: int) -> None:
        if key is None:
            return

        bucket_index = self.hash_key(key)
        bucket = self.buckets[bucket_index]
        if key in bucket:
            bucket.remove(key)

    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        if key is None:
            return

        bucket_index = self.hash_key(key)
        return key in self.buckets[bucket_index]
