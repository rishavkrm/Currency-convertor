import requests
import tkinter
import customtkinter

list1 = requests.get("https://v6.exchangerate-api.com/v6/87dce9a4abbc1ef551252f75/latest/USD").json()[
    "conversion_rates"]
countries = list(list1.keys())



app = App()
app.mainloop()
