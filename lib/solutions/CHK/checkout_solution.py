
class CheckoutSolution:

    # skus = unicode string
    def checkout(self, skus):
        items = {"A":0, "B":0, "C":0, "D":0}
        for char in skus:
            if char == "A" or char == "B" or char == "C" or char == "D":
                items[char] += 1
            else:
                return -1
        
        total = items["C"]*20 + items["D"]*15 +(items["A"]//3)*130 + (items["A"]%3)*50 + (items["B"]//2)*45 + (items["B"]%2)*30
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
