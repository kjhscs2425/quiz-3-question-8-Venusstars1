import json

# read `expenses.json`
with open ("expenses.json", "r") as f:
    data = json.load(f)

# get and print total "price" for all expenses at the "pet store"
prices_total = 0
new_dict = data["pet store"]
for key in new_dict:
    prices_total += key["price"]
print(prices_total)