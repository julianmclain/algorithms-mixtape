"""
I've been to a restaurant to order some food, but I've forgotten what I ordered in the past. I only remember how much money I spent.

From the following menu, and list of receipt values, determine what I could have ordered.
"""

primary_menu = {
    "veggie sandwich": 6.85,
    "extra veggies": 2.20,
    "chicken sandwich": 7.85,
    "extra chicken": 3.20,
    "cheese": 1.25,
    "chips": 1.40,
    "nachos": 3.45,
    "soda": 2.05,
}

"""
Here is a list of receipts for 9 different orders I've made at the restaurant
"""
receipts = [4.85, 11.05, 13.75, 17.75, 18.25, 19.40, 28.25, 40.30, 75.00]

"""
Constraints:
- this platform will only run your code for 30 seconds
  - it will stop earlier if memory is exceeded or you print too much output
- you must use 100% of the receipt value, we don't want any money left over
- you can order any quantity of any menu item
- none of the receipt values are "tricks", they all have answers


Part One:

Find the first combination of food that adds up to the receipt total, print out only one combination for that receipt, and move on to the next receipt.

The output format is up to you, but here are some examples:

4.85:
3 items, extra veggies, chips, cheese

13.75:
3 items, {'veggie sandwich': 1, 'nachos': 2}


Example:
4.85 receipt has three possible combinations:
- best: nachos, chips (2 total items)
- extra veggies, chips, cheese (3 total times)
- chips, chips, soda (3 total items)
"""


def find_combination(menu, curr_total, start=[]):
    if curr_total == 0:
        return start

    for item, price in menu.items():
        updated_price = round(curr_total - price, 2)
        if updated_price >= 0:
            attempt = find_combination(menu, updated_price, start + [item])
            if attempt:
                return attempt

    return []


print(find_combination(primary_menu, receipts[0]))
