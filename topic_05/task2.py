import requests

def convert_currency(amount, currency):
    url = f"https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?valcode={currency}&json"
    response = requests.get(url)
    exchange_rate = response.json()[0]['rate']
    converted_amount = amount * exchange_rate
    return converted_amount

amount = float(input("Enter the amount: "))
currency = input("Enter the currency (EUR, USD, PLN): ")

converted_amount = convert_currency(amount, currency)
print(f"{amount} {currency} is equal to {converted_amount:.2f} UAH")