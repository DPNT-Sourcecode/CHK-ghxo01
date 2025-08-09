
class CheckoutSolution:

    # skus = unicode string
    def checkout(self, skus):
        items = {"A":0, "B":0, "C":0, "D":0, "E":0, "F":0}
        for char in skus:
            if char in "ABCDEF":
                items[char] += 1
            else:
                return -1

        A_remaining = items["A"]
        A_multi5 = A_remaining//5
        A_remaining %= 5
        A_multi3 = A_remaining//3
        A_remaining %= 3
        A_cost = (A_multi5 * 200) + (A_multi3 * 130) + (A_remaining * 50)
        
        items["B"] = max(0, items["B"] - (items["E"]//2))
        B_cost = (items["B"]//2)*45 + (items["B"]%2)*30

        C_cost = items["C"]*20

        D_cost = items["D"]*15

        E_cost = items["E"]*40

        F_cost = (items["F"]//3 * 2 * 10) + (items["F"]%3 * 10)
        
        total = A_cost + B_cost + C_cost + D_cost + E_cost + F_cost
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

# 3

#+------+-------+------------------------+
#| Item | Price | Special offers         |
#+------+-------+------------------------+
#| A    | 50    | 3A for 130, 5A for 200 |
#| B    | 30    | 2B for 45              |
#| C    | 20    |                        |
#| D    | 15    |                        |
#| E    | 40    | 2E get one B free      |
#| F    | 10    | 2F get one F free      |
#+------+-------+------------------------+

# Now with F, get one F for free. So that means F//3 * 2 for cost, also time to refactor code