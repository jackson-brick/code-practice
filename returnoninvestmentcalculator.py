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

spent = input("How much money have you invested in your business? ")
while not spent.isdigit():
    print("That is an invalid response. Please try again.")
    spent = input("How much money have you invested in your business? ")

raised = input("How much money has your business earned? ")
while not raised.isdigit():
    print("That is an invalid response. Please try again.")
    raised = input("How much money has your business earned? ")

profit = int(raised) - int(spent)
if profit > 0:
    print(f"You have made a profit of ${profit}.")
elif profit < 0:

    print(f"You have had a loss of ${profit * -1}.")
elif profit == 0:
    print(f"You have not made any profit or any loss.")

roi = profit / int(spent)
print(f"Your return on investment is {int(roi)}%.")