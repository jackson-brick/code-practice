#Write a computer program to evaluate the performance of a business. Your program will ask the user to input:

#The total amount spent/invested on the business: Total costs
#The total amount raised by the business: Total sales
#Your program will then calculate and display the profit made by the business and indicate whether the business made a profit or a loss.
#Your program will then calculate and display the Return On Investment (ROI) of the business as a percentage value.




print("+-+-+-+-+-+-+-+-+--+-+-+-+-+-+-+-+-+")
print("+                                  +")
print("+          ROI Calulator           +")
print("+                                  +")
print("+             Welcome              +")
print("+                                  +")
print("+-+-+-+-+-+-+-+-+--+-+-+-+-+-+-+-+-+")

print("\n")

spent = int(input("How much money have you invested in the business? "))
raised = int(input("How much money has your business earned? "))

profit = raised - spent
if profit > 0:
    print(f"You have made a profit of ${profit}.")
elif profit < 0:

    print(f"You have had a loss of ${profit * -1}.")
elif profit == 0:
    print(f"You have not made any profit or any loss.")

roi = profit / spent
print(f"Your return on investment is {roi}%.")