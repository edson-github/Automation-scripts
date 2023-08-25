import requests
import sys


def get_prices():

    # Checking there is a coin passed
    if len(sys.argv) > 1:
        coins = sys.argv[1:]
    else:
        # Default coins
        coins = ["BTC", "ETH", "XRP", "LTC", "BCH",
                 "ADA", "DOT", "LINK", "BNB", "XLM"]
    crypto_data = requests.get(
        f'https://min-api.cryptocompare.com/data/pricemultifull?fsyms={",".join(coins)}&tsyms=USD'
    ).json()["RAW"]

    return {
        i: {
            "coin": i,
            "price": crypto_data[i]["USD"]["PRICE"],
            "change_day": crypto_data[i]["USD"]["CHANGEPCT24HOUR"],
            "change_hour": crypto_data[i]["USD"]["CHANGEPCTHOUR"],
        }
        for i in crypto_data
    }


if __name__ == "__main__":
    crypto_data = get_prices()
    message = ""
    for i in crypto_data:
        coin = crypto_data[i]["coin"]
        price = crypto_data[i]["price"]
        change_day = crypto_data[i]["change_day"]
        change_hour = crypto_data[i]["change_hour"]
        message += f"\nCoin: {coin}"
        message += f"\nPrice: ${price:,.2f}"
        message += f"\nHour Change: {change_hour:.3f}%"
        message += f"\nDay Change: {change_day:.3f}%\n"
    print(message)
