import requests
API_KEY = "fca_live_05PiUDJQXCpbopasLUXJWCG5RXR7OmoejTJd4seM"
BASE_URL = f"https://api.freecurrencyapi.com/v1/latest?apikey={API_KEY}"

CURRENCIES = ["USD","CAD","EUR","AUD","INR"]
def convert_currency(base):
    currencies = ",".join(CURRENCIES)
    url = f"{BASE_URL}&base_currency={base}&currencies={currencies}"

    try:
        response = requests.get(url)
        data = response.json()
        return data["data"]

    except:
        print('Invalid Currency')
    
while True:
    user_input = input("Enter the base currency that you need to check: ").upper()
    if user_input == "Q":
        break
        
    data = convert_currency(user_input)
    if not data:
        continue

    amount = float(input("Enter the amount to convert: "))
    del data[user_input]
    for key,value  in data.items():
        print(f"{key}: {value * amount:.2f}")
