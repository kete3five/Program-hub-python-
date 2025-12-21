import requests
import tkinter as tk

class coordinatesHolder:
    def get_weather_Info(self, Xcoordinates, Ycoordinates):
        self.url="https://api.open-meteo.com/v1/forecast"
        params={
            "latitude":Xcoordinates,
            "longitude":Ycoordinates,
            "current_weather":"true"
        }
        try:
            response=requests.get(self.url,params=params,timeout=10)
            response.raise_for_status()
            data=response.json()
            return data.get("current_weather", {}).get("temperature")
        except requests.exceptions.RequestException as e:
            print("a error occured")