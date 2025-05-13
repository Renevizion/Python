'''
Challenge: Allow the user to choose from multiple currency pairs and implement appropriate error handling for invalid currency inputs.
==============================================
Input: Ask the user to enter an amount in one currency (e.g., USD).
Processing: Convert the amount to another currency (e.g., EUR) using a fixed exchange rate.
Output: Display the converted amount in the target currency.
'''


rates = {
    "USD to EUR": 0.85,
    "EUR to USD": 1.18,
    "USD to GBP": 0.75,
    "GBP to USD": 1.33,
    "EUR to GBP": 0.88,
    "GBP to EUR": 1.14
}

print("Choose a currency pair:")
for pair in rates:
    print("-", pair)

pair = input("Enter pair (USD to EUR): ").strip()

if pair in rates:
    try:
        amount = float(input("Enter amount: "))
        if amount < 0:
            print("The amount must be negative.")
        else:
            result = amount * rates[pair]
            from_currency, _, to_currency = pair.split()
            print(f"{amount:.2f} {from_currency} = {result:.2f} {to_currency}")
    except ValueError:
        print("Invalid amount.")
else:
    print("Invalid currency pair.")
