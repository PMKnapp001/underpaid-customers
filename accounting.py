melon_cost = 1.00

customer1_name = "Joe"
customer1_melons = 5
customer1_paid = 5.00

customer2_name = "Frank"
customer2_melons = 6
customer2_paid = 6.00

customer3_name = "Sally"
customer3_melons = 3
customer3_paid = 3.00

customer4_name = "Sean"
customer4_melons = 9
customer4_paid = 9.50

customer5_name = "David"
customer5_melons = 4
customer5_paid = 4.00

customer6_name = "Ashley"
customer6_melons = 3
customer6_paid = 2.00

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