######------------ Project 1: Tip Calculator --------------------
bill= int ( input("What the bill?: $"))
tip = int(input("How mush tip you want to give? 10%, 12%,or 20%: "))
tip= bill * tip/100
total_bill = bill + tip
print(f"Your total bill is $ {total_bill}")

