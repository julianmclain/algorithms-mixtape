from typing import List
import unittest

"""Mutually-referential data

Whereas self-referential data types can represent information of
an arbitrary size in 1 dimension (e.g. lists), mutually-referential
data types can represent information of an arbitrary size in 2 dimensions.

Tree data structures are an example of mutually-referential data types.
At each level below the root, it could be arbitrarily wide. It could
also be arbitrarily deep.

For example:
- A Person is Person(name: str, age: int, children: List[Person])
- A List[Person] is either [] or [Person] + List[Person] 

Template for functions operating on mutually-referential data:
```
def fn_for_person(p: Person):
    if not person:                                      # base case
        return ???
    else:                                               # recursive case
        return person.name, person.age ??? fn_for_person(person.children)

def fn_for_lop(lop: List[Person]):
    if not lop:                                         # base case
        return ???
    else:                                               # recursive case
        return fn_for_person(lop[0]) ??? fn_for_lop(lop[1:])
```
"""


class Person:
    def __init__(self, name: str, age: int, children: list):
        self.name = name
        self.age = age
        self.children = children


def count_members(family_tree):
    """This one done strictly according to the recursion template"""
    def fn_for_person(person):
        if not person:
            return 0
        return 1 + fn_for_lop(person.children)

    def fn_for_lop(lop):
        if not lop:
            return 0
        return fn_for_person(lop[0]) + fn_for_lop(lop[1:])

    return fn_for_person(family_tree)


def count_members_blend(family_tree):
    """This one using a blend of recursion and iteration"""
    if not family_tree:
        return 0

    curr_count = 1
    for child in family_tree.children:
        curr_count += count_members_blend(child)

    return curr_count


def count_members_iter(family_tree):
    """This one using only iteration"""
    stack = [family_tree]
    count = 0
    while stack:
        person = stack.pop()
        count += 1
        stack.extend(person.children)

    return count


def create_roster_blend(person):
    if not person:
        return {}

    roster = {person.name: person.age}
    for child in person.children:
        roster = {**roster, **create_roster_blend(child)}

    return roster


def create_roster_acc(person, acc={}):
    if not person:
        return acc

    acc[person.name] = person.age
    for child in person.children:
        create_roster_acc(child, acc=acc)

    return acc


def max_age1(family_tree):
    """This one done strictly according to the template"""
    def fn_for_person(person):
        if not person:
            return 0

        if person.age > fn_for_lop(person.children):
            return person.age
        else:
            fn_for_lop(person.children)

    def fn_for_lop(lop):
        if not lop:
            return 0

        if lop[0].age > fn_for_lop(lop[1:]):
            return lop[0].age
        else:
            return fn_for_lop(lop[1:])

    return fn_for_person(family_tree)


def max_age2(family_tree):
    """This one done with better practices but still 2 functions"""
    def fn_for_person(person):
        if not person:
            return 0

        max_child_age = fn_for_lop(person.children)
        return person.age if person.age > max_child_age else max_child_age

    def fn_for_lop(lop):
        if not lop:
            return 0

        if lop[0].age > fn_for_lop(lop[1:]):
            return lop[0].age
        else:
            return fn_for_lop(lop[1:])

    return fn_for_person(family_tree)


class TestMutualReference(unittest.TestCase):
    def setUp(self):
        self.family_tree = Person(
            "James Potter",
            67,
            [
                Person(
                    "Harry Potter",
                    46,
                    [Person("James Sirius Potter", 10, []), Person("Lily Luna Potter", 8, [])],
                )
            ],
        )

    def test_count_members(self):
        self.assertEqual(4, count_members(self.family_tree))
        self.assertEqual(4, count_members_blend(self.family_tree))
        self.assertEqual(4, count_members_iter(self.family_tree))

    def test_max_age(self):
        self.assertEqual(67, max_age1(self.family_tree))
        self.assertEqual(67, max_age2(self.family_tree))

    def test_create_roster(self):
        expected = {'James Potter': 67, 'Harry Potter': 46, 'James Sirius Potter': 10, 'Lily Luna Potter': 8}
        self.assertEqual(expected, create_roster_blend(self.family_tree))
        self.assertEqual(expected, create_roster_acc(self.family_tree))
