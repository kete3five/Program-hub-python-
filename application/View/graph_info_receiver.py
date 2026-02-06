import requests
import datetime as dt

class GraphInfoReceiver:
    """receives information for the builder class"""
    def get_info(self, crypto):
        """receives the information from the URL"""
        self.dates = []
        self.prices = []
        self.url = f"https://api.coingecko.com/api/v3/coins/{crypto}/market_chart"
        params = {
        "vs_currency": "usd",
        "days": 3,
        "interval": "daily"
        }
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
        }
        try:
            response=requests.get(self.url,params=params,timeout=10, headers=headers)
            response.raise_for_status()
            data=response.json()
            for i in data["prices"]:
                self.dates.append(dt.datetime.fromtimestamp(i[0] / 1000))
                self.prices.append(i[1])
            print("i get triggered")
            return (self.dates, self.prices)
        except requests.exceptions.RequestException as e:
            print(e)

gir = GraphInfoReceiver()
date, price = gir.get_info("bitcoin")
print(date, price)