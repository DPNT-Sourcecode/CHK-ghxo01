
class CheckoutSolution:

    # skus = unicode string
    def checkout(self, skus):
        items = {"A":0, "B":0, "C":0, "D":0, "E":0}
        for char in skus:
            if char == "A" or char == "B" or char == "C" or char == "D" or char == "E":
                items[char] += 1
            else:
                return -1
        
        items["B"] = max(0, items["B"] - (items["E"]//2))

        A_remaining = items["A"]
        A_multi5 = A_remaining//5
        A_remaining %= 5
        A_multi3 = A_remaining//3
        A_remaining %= 3
        A_cost = (A_multi5 * 200) + (A_multi3 * 130) + (A_remaining * 50)
        
        total = items["C"]*20 + items["D"]*15 + (items["B"]//2)*45 + (items["B"]%2)*30 + A_cost + items["E"]*40
        return total

# 1

#+------+-------+----------------+
#| Item | Price | Special offers |
#+------+-------+----------------+
#| A    | 50    | 3A for 130     |
#| B    | 30    | 2B for 45      |
#| C    | 20    |                |
#| D    | 15    |                |
#+------+-------+----------------+

# Brute force works

# 2

#+------+-------+------------------------+
#| Item | Price | Special offers         |
#+------+-------+------------------------+
#| A    | 50    | 3A for 130, 5A for 200 |
#| B    | 30    | 2B for 45              |
#| C    | 20    |                        |
#| D    | 15    |                        |
#| E    | 40    | 2E get one B free      |
#+------+-------+------------------------+

# Need to calculate for get one B free, so -1