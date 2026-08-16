def invoice(name, amount, due_date):
    print(f"Hi, {name}\nYour bill of Rs.{amount: .2f} is due on {due_date}")

    return 0

invoice("Dev", 500.23643, "June 25th")