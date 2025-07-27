total = 0
while True:
    desc = input("Enter expense description or 'q' to quit: ")
    if desc.lower() == 'q': break
    amt = float(input("Amount: "))
    total += amt
    with open("expenses.txt", "a") as f:
        f.write(f"{desc}: Rs.{amt}\n")
print(f"Total Spent: Rs.{total}")