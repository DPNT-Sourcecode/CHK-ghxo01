
class CheckoutSolution:

    # skus = unicode string
    def checkout(self, skus):
        SKU_characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        items = {}
        for letter in SKU_characters:
            items[letter] = 0

        for char in skus:
            if char in SKU_characters:
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
        
        G_cost = items["G"]*20

        H_remaining = items["H"]
        H_multi10 = H_remaining//10
        H_remaining %= 10
        H_multi5 = H_remaining//5
        H_remaining %= 5
        H_cost = (H_multi10 * 80) + (H_multi5 * 45) + (H_remaining * 10)

        I_cost = items["I"]*35
        
        J_cost = items["J"]*60

        K_cost = (items["K"]//2)*150 + (items["K"]%2)*80
        
        L_cost = items["L"]*90

        items["M"] = max(0, items["M"] - (items["N"]//3))
        M_cost = items["M"]*15
        
        N_cost = items["N"]*40

        O_cost = items["O"]*10
        
        P_cost = (items["P"]//5)*200 + (items["P"]%5)*50

        items["Q"] = max(0, items["Q"] - (items["R"]//3))
        Q_cost = (items["Q"]//3)*80 + (items["Q"]%3)*30
        
        R_cost = items["R"]*50

        S_cost = items["S"]*30
        
        T_cost = items["T"]*20

        U_cost = (items["U"]//4 * 3 * 40) + (items["U"]%4 * 40)
        
        V_remaining = items["V"]
        V_multi3 = V_remaining//3
        V_remaining %= 3
        V_multi2 = V_remaining//2
        V_remaining %= 2
        V_cost = (V_multi3 * 130) + (V_multi2 * 90) + (V_remaining * 50)

        W_cost = items["W"] * 20
        
        X_cost = items["X"] * 90

        Y_cost = items["Y"] * 10

        Z_cost = items["Z"] * 50
        
        total = A_cost + B_cost + C_cost + D_cost + E_cost + F_cost + G_cost+ H_cost + I_cost+ J_cost + K_cost+ L_cost + M_cost+ N_cost + O_cost + P_cost + Q_cost + R_cost + S_cost + T_cost + U_cost + V_cost + W_cost + X_cost + Y_cost +Z_cost
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

# 4

#+------+-------+------------------------+
#| Item | Price | Special offers         |
#+------+-------+------------------------+
#| A    | 50    | 3A for 130, 5A for 200 |
#| B    | 30    | 2B for 45              |
#| C    | 20    |                        |
#| D    | 15    |                        |
#| E    | 40    | 2E get one B free      |
#| F    | 10    | 2F get one F free      |
#| G    | 20    |                        |
#| H    | 10    | 5H for 45, 10H for 80  |
#| I    | 35    |                        |
#| J    | 60    |                        |
#| K    | 80    | 2K for 150             |
#| L    | 90    |                        |
#| M    | 15    |                        |
#| N    | 40    | 3N get one M free      |
#| O    | 10    |                        |
#| P    | 50    | 5P for 200             |
#| Q    | 30    | 3Q for 80              |
#| R    | 50    | 3R get one Q free      |
#| S    | 30    |                        |
#| T    | 20    |                        |
#| U    | 40    | 3U get one U free      |
#| V    | 50    | 2V for 90, 3V for 130  |
#| W    | 20    |                        |
#| X    | 90    |                        |
#| Y    | 10    |                        |
#| Z    | 50    |                        |
#+------+-------+------------------------+