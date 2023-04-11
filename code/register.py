class Register:
    cart = []
    credit = 0
    sum = 0
    taxsum = 0
    finsum = 0
    def performCheckout(cart, credit):
        if not cart:
            "Error! There are no items in your cart.\n"
        else:
            for x in cart:
                print(x)
                print(x.quantity)
                print(x.price, "\n")
            #res1 = input("Are these items correct? Please press y or n.")
            #if res1 == 'y' or res1 == 'Y':

            for x in cart:
                sum = x.price + sum
            taxsum = sum * .0475
            finsum = sum + taxsum

            print("Cost: ", sum, "\n")
            print("Tax: ", taxsum, "\n")
            print("Total Cost: ", finsum, "\n")

            res2 = input("Do you have any instore credit? Please enter y or n.")
            print("\n")
            if res2 == 'y' or res2 == 'Y':
                res3 = input("Please enter your phone number.")
                print("\n")
            else:
                res4 = input("How would you like to pay? We accept Credit, Debit, and Paypal.")
                print("\n")
                if res4 == 'debit' or res4 == 'Debit':
                    res5 = input("Please enter your 4 digit pin")
                    print("\n")
                    print("Your purchase was successful\n")
                    print("Thank you for shopping with us at ITSCmart")

                


            
