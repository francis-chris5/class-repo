

price = float(input("yeah, how much is it? "))

percent = float(input("how much do you want to tip: "))

tip = price * percent

total = price + tip

print("you should probably tip $" + format(tip, ".2f") + " today for a total of $" + format(total, ".2f"))

