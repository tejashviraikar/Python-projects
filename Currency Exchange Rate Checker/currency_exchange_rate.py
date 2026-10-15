# Develop a program that fetches and displays the latest currency exchange rates


import requests 

def get_exchange_rate(base_currency, symbols):
    """
    Fetches exchange rates for the specified base currency against selected currencies.
    Args:
        base_currency (str): The currency code to use as the base.
        symbols (list): List of currency codes to compare against the base currency.
    Returns:
        dict: A dictionary with currency codes as keys and exchange rates as values.
    """
    url = f"https://api.exchangerate-api.com/v4/latest/{base_currency}"  # API URL with the base currency

    # Send GET request to the API and get JSON response
    response = requests.get(url)
    data = response.json()  # Parse the JSON data

    # Filter and return only the relevant currency symbols
    rates = {currency: data["rates"][currency] for currency in symbols if currency in data["rates"]}
    return rates

# User input for the base currency and currencies to compare
base_currency = "USD"
compare_currencies = ["EUR", "GBP", "JPY"]

# Fetch and display exchange rates
exchange_rates = get_exchange_rate(base_currency, compare_currencies)
print(f"Latest exchange rates for {base_currency}:")
for currency, rate in exchange_rates.items():
    print(f"- {currency}: {rate}")
