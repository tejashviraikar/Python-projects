# ----------------------------------------
# Currency Converter
# ----------------------------------------

# Predefined exchange rates (Base Currency: INR)

exchange_rates = {
    "INR": 1.0,
    "USD": 0.012,
    "EUR": 0.010,
    "GBP": 0.0089,
    "JPY": 1.75,
    "AUD": 0.018,
    "CAD": 0.016
}


# ----------------------------
# Display Available Currencies
# ----------------------------
def display_currencies():
    print("\nAvailable Currencies:")

    for currency in exchange_rates:
        print("-", currency)


# ----------------------------
# Currency Conversion Function
# ----------------------------
def convert_currency(amount, from_currency, to_currency):

    amount_in_inr = amount / exchange_rates[from_currency]

    converted_amount = amount_in_inr * exchange_rates[to_currency]

    return converted_amount


# ----------------------------
# Main Program
# ----------------------------
def main():

    print("=" * 45)
    print("      CURRENCY CONVERTER")
    print("=" * 45)

    while True:

        display_currencies()

        try:
            amount = float(input("\nEnter Amount: "))

            if amount <= 0:
                print("Amount must be greater than zero.")
                continue

            from_currency = input("From Currency: ").upper()
            to_currency = input("To Currency: ").upper()

            if from_currency not in exchange_rates:
                print("Invalid source currency.")
                continue

            if to_currency not in exchange_rates:
                print("Invalid destination currency.")
                continue

            result = convert_currency(amount, from_currency, to_currency)

            print(f"\n{amount:.2f} {from_currency} = {result:.2f} {to_currency}")

        except ValueError:
            print("Please enter a valid numeric amount.")
            continue

        choice = input("\nDo you want to convert another currency? (y/n): ").lower()

        if choice != "y":
            print("\nThank you for using Currency Converter!")
            break


if __name__ == "__main__":
    main()