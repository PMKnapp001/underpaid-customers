def check_customer_payments(customer_file):
    payment_report = open(customer_file)
    MELON_COST = 1.00
    for line in payment_report:
        line = line.rstrip()
        words = line.split("|")
        customer_num = words[0]
        customer_name = words[1]
        num_melons = int(words[2])
        amount_paid = float(words[3])
        expected_amount = MELON_COST * num_melons

        if expected_amount != amount_paid:
            print(f"Customer #{customer_num}: {customer_name} paid ${amount_paid:.2f}.")
            print(f"         Expected payment: ${expected_amount:.2f}.")
            print()
        else:
            print(f"Customer #{customer_num}: {customer_name}'s balance is paid.")
            print()

check_customer_payments("customer-orders.txt")