class Register:
    cart = []
    creditID = []
    sum = 0
    taxsum = 0
    finsum = 0
    def performCheckout(cart, creditID):
        if not cart:
            "Error! There are no items in your cart.\n"
        else:
            for x in cart:
                print(x)
                print(x.quantity)
                print(x.price, "\n")
            z = 0
            while z == 0:
                res1 = input("Are these items correct? Please press y or n. ")
                if res1 == 'n' or res1 == 'N':
                    res6 = input("\nWhich Item is incorrect? *Caps Sensitive*")
                    if res6 in cart:
                        cart.index(res6)
                        z = 1
                    else:
                        print("The Item entered is incorrect.")

            for x in cart:
                sum = x.price + sum
            taxsum = sum * .0475
            finsum = sum + taxsum

            print("Cost: ", sum, "\n")
            print("Tax: ", taxsum, "\n")
            print("Total Cost: ", finsum, "\n")

            res2 = input("Would you like to use instore credit? Please enter y or n.")
            print("\n")
            if res2 == 'y' or res2 == 'Y':
                res3 = input("Please enter your phone number.")
                print("\n")
                y = 0
                while y == 0:
                    if res3 in creditID:
                        res7 = input("You have ", res3.amount, " available. How much would you like to use?")
                        print("\n")
                        if res3.amount < res7:
                            print("That amount exceeds your current balance. Please enter a valid amount.")
                        else: 
                            finsum = finsum - res7
                            print("Total Cost: ", finsum, "\n")
                            y = 1
            res4 = input("How would you like to pay? We accept Credit, Debit, and Paypal.")
            print("\n")
            if res4 == 'debit' or res4 == 'Debit':
                res5 = input("Please enter your 4 digit pin")
                print("\n")
                print("Your purchase was successful\n")
                print("Thank you for shopping with us at ITSCmart")
            else:
                print("Your purchase was successful\n")
                print("Thank you for shopping with us at ITSCmart")


                


            
