import requests

API_KEY = 'Your API Key'

API_URL = 'https://v6.exchangerate-api.com/v6/YOUR_API_KEY/latest/USD'

def get_rates():
    response = requests.get(API_URL)
    data = response.json()
    if response.status_code == 200:
        rates = data["conversion_rates"]["RUB"]
        rates = round(float(rates), 2)
        print(f'Актуальный курс доллара к рублю равен - {rates}')
        return rates
    else:
        print(f"Ошибка при выполнении запроса: {response.status_code}")
        return None

def calculate(rates):
    quantity_dollars = float(input('Введите колчество ваших долларов для перевода в рубли:'))
    calculate_rubles = quantity_dollars * rates
    return calculate_rubles

GET_rates = get_rates()
if GET_rates is not None:
    calculate_result = calculate(GET_rates)
    print(f'Количество рублей: {calculate_result}')
else:
    print('Невозможно выполнить расчет. Попробуйте позже.')





