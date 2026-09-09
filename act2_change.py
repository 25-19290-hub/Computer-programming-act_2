# act2_change.py - Calculate change and coin breakdown

amount_due = float(input("Enter amount due: "))
amount_paid = float(input("Enter amount paid: "))

if amount_paid < amount_due:
    print("Insufficient payment!")
else:
    change = amount_paid - amount_due
    print(f"Change: {change:.2f}")

    # Breakdown into bills and coins (PHP currency standard)
    denominations = [1000, 500, 200, 100, 50, 20, 10, 5, 1]
    cents = int(round(change * 100))
    
    print("\nDenomination Breakdown:")
    for d in denominations:
        val = d * 100
        count = cents // val
        if count > 0:
            print(f"₱{d}: {count}")
            cents %= val
