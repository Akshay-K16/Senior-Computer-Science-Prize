import tkinter
from PIL import Image
from PIL import ImageTk
import requests
import json


def main():
    data = get_api()
    GUI(data)
    

# Retrieving API data with coronavirus stats
def get_api():
    try:
        response = requests.get("https://disease.sh/v2/countries?yesterday=false")
        print(response.status_code)
        res = response.json()
        return res
    except:
        print("Unexpected error")
        exit(0)

def get_global():
    try:
        response = requests.get("https://disease.sh/v2/all")
        print(response.status_code)
        res = response.json()
        message = "Global Stats:\n\nTotal Confirmed Cases: " + str(res["cases"]) + "\nTotal Deaths: " + str(res["deaths"]) + "\nTotal Countries Affected: " + str(res["affectedCountries"])
        return message
    except:
        print("Unexpected error")
        exit(0)

def GUI(res):
    window = tkinter.Tk()

    # Title and Window Size
    window.title("Covid-19 Tracker")
    window.geometry('750x500')

    # Background Image
    image = Image.open('corona.png')
    image = image.resize((750, 500))
    image = ImageTk.PhotoImage(image)
    img= tkinter.Label(window, image=image)
    img.pack(expand ="YES", fill = "both")
    window.iconphoto(False, image)

    message_text = get_global()
    
    # Creating Widgets
    global_stats = tkinter.Message(img, text=message_text, bg="#000000", fg="#ffffff", justify="center", relief="raised")
    label = tkinter.Label(img, text = "Country:", padx=5, pady=5, bg="#000000", fg="#ffffff", relief="raised")
    entry = tkinter.Entry(img, bd =5, bg="#000000", fg="#ffffff", relief="raised", insertbackground='#ffffff')
    def home():
        window.destroy()
        GUI(res)

    def clicked():
        country = entry.get()
        entry.delete(0, tkinter.END)
        m1 = "Country not found"
        for item in res:
            if item["country"] == country:
                m2 = "Total " + item["country"] + " cases:\n" + str(item["cases"]) + "\n"
                m3 = "Total " + item["country"] + " deaths:\n" + str(item["deaths"]) + "\n"
                m4 = "Total " + item["country"] + " recovered:\n" + str(item["recovered"])
                m1 = m2 + m3 + m4
                break
        m = tkinter.Message(img, text=m1, bg="#000000", fg="#ffffff", justify="center", relief="raised")
        global_stats.destroy()
        label.destroy()
        entry.destroy()
        button.destroy()
        
        return_home = tkinter.Button(img, text="Return Home", command=home, bg="#000000", fg="#ffffff", relief="raised").place(x=640, y=25)
        m.place(x=375, y = 250, anchor='center')
        foot = tkinter.Label(img, text = "Data provided for free by https://corona.lmao.ninja", bg="#000000", fg="#ffffff", relief="raised").place(x=375, y=450, anchor="center")
        
    button = tkinter.Button(img, text="Enter", command=clicked, activebackground='#454545', bg="#000000", fg="#ffffff", relief="raised")

    # Displaying Widgets.
    global_stats.place(x=375, y = 120, anchor='center')
    label.place(x=375, y = 205, anchor='center')
    entry.place(x=375, y = 235, anchor='center')
    button.place(x=375, y = 265, anchor='center')
    end_label = tkinter.Label(img, text = "Data provided for free by https://corona.lmao.ninja", bg="#000000", fg="#ffffff", relief='raised')
    end_label.place(x=375, y=450, anchor='center')

    window.mainloop()


main()


