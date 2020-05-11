import tkinter
import requests
import json



window = tkinter.Tk()
window.title("Covid-19 Tracker")
label = tkinter.Label(window, text = "Test Label").pack()
button_widget = tkinter.Button(window,text="Test Button").pack()
label = tkinter.Label(window, text = "Data provided for free by covid19api.com and sourced from John Hopkins CSSE").pack()
window.mainloop()

try:
    test = requests.get("https://api.covid19api.com/summary")
    print(test.status_code)
    test1 = test.json()
    print("Total Global Deaths: " + str(test1["Global"]["TotalDeaths"]))
    print("Total Global Cases: " + str(test1["Global"]["TotalConfirmed"]))
except:
    print("Unexpected error")
    exit(0)

country = input("Country: ")

for item in test1["Countries"]:
    if item["Country"] == country or item["CountryCode"] == country:
        print(country + " total cases: " + str(item["TotalConfirmed"]))
        print(country + " total deaths: " + str(item["TotalDeaths"]))
        print(country + " total recovered: " + str(item["TotalRecovered"]))


