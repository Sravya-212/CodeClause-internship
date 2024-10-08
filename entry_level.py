def currency_converter(amount, from_currency, to_currency, exchange_rates):
    if from_currency not in exchange_rates or to_currency not in exchange_rates:
        return "Invalid currency code."

    # Convert the amount to the base currency (USD in this example)
    amount_in_usd = amount / exchange_rates[from_currency]

    # Convert from the base currency to the target currency
    converted_amount = amount_in_usd * exchange_rates[to_currency]

    return converted_amount

# Exchange rates with USD as the base currency
exchange_rates = {
    'USD': 1,
    'EUR': 0.85,
    'GBP': 0.75,
    'INR': 74.3,
    'JPY': 110.0,
    'CAD': 1.25,
    'AUD': 1.35
}

# Take user input
amount = float(input("Enter the amount: "))
from_currency = input("Enter the currency you have (e.g., USD, EUR): ").upper()
to_currency = input("Enter the currency you want to convert to (e.g., USD, EUR): ").upper()

# Perform the conversion
converted_amount = currency_converter(amount, from_currency, to_currency, exchange_rates)

print(f"{amount} {from_currency} is equal to {converted_amount:.2f} {to_currency}.")