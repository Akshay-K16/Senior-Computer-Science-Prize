# Import libraries needed to run the GUI and retrieve the data.
import tkinter
from PIL import Image
from PIL import ImageTk
import requests
import json


# Main Function
def main():
    # Functions to get API data
    data = get_api()
    global_data = get_global()

    # Runs the Graphical User Interface
    GUI(data, global_data)
    

# Retrieving API data with countries' coronavirus stats
def get_api():
    try:
        response = requests.get("https://disease.sh/v2/countries?yesterday=false")
        print(response.status_code) # Should be 200
        res = response.json()
        return res
    except:
        print("Unexpected error")
        exit(1) # End Progarm


# Retrieving API global coronavirus data.
def get_global():
    try:
        response = requests.get("https://disease.sh/v2/all")
        print(response.status_code) # Should be 200
        res = response.json()
        message = "Global Stats:\n\nTotal Confirmed Cases: " + str(res["cases"]) + "\nTotal Deaths: " + str(res["deaths"]) + "\nTotal Countries Affected: " + str(res["affectedCountries"])
        return message
    except:
        print("Unexpected error")
        exit(1) # End Program
        

# Runs the User Interface
def GUI(res, message_text):
    window = tkinter.Tk()
    # Start of code for tkinter window.

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
    
    # Creating Widgets
    global_stats = tkinter.Message(img, text=message_text, bg="#000000", fg="#ffffff", justify="center", relief="raised")
    label = tkinter.Label(img, text = "Country:", padx=5, pady=5, bg="#000000", fg="#ffffff", relief="raised")
    entry = tkinter.Entry(img, bd =5, bg="#000000", fg="#ffffff", relief="raised", insertbackground='#ffffff')
    end_label = tkinter.Label(img, text = "Data provided for free by https://corona.lmao.ninja", bg="#000000", fg="#ffffff", relief='raised')

    # Functions that are run on button clicks.
    def home():
        # Returns Home
        window.destroy()
        GUI(res, message_text)
    def close():
        # Close Windows
        window.destroy()
    def clicked():
        # Displays Country Information when button is clicked.

        m1 = "Country not found"
        try:
            # Turn user input into correct format
            Country = entry.get()
            country = Country.lower()
            c = chr(ord(country[0])-32) + country[1:]
            entry.delete(0, tkinter.END)

            # Search data for country
            for item in res:
                if item["country"] in [Country, c, country.upper()]:
                    m2 = "Total " + item["country"] + " cases:\n" + str(item["cases"]) + "\n"
                    m3 = "Total " + item["country"] + " deaths:\n" + str(item["deaths"]) + "\n"
                    m4 = "Total " + item["country"] + " recovered:\n" + str(item["recovered"])
                    m1 = m2 + m3 + m4
                    break
        except:
            # No country entered.
            m1 = "Please Enter a Country"
            
        m = tkinter.Message(img, text=m1, bg="#000000", fg="#ffffff", justify="center", relief="raised")

        #Remove Homepage Widgets
        global_stats.destroy()
        label.destroy()
        entry.destroy()
        button.destroy()

        # Creating and Displaying widgets.
        return_home = tkinter.Button(img, text="Return Home", command=home, bg="#000000", fg="#ffffff", relief="raised").place(x=683, y=30, anchor="center")
        close_button = tkinter.Button(img, text="Close", command=close, bg="#000000", fg="#ffffff", relief="raised").place(x=40, y=30, anchor="center")
        m.place(x=375, y = 250, anchor='center')
        foot = tkinter.Label(img, text = "Data provided for free by https://corona.lmao.ninja", bg="#000000", fg="#ffffff", relief="raised").place(x=375, y=465, anchor="center")

        
    button = tkinter.Button(img, text="Enter", command=clicked, activebackground='#454545', bg="#000000", fg="#ffffff", relief="raised")

    # Displaying Widgets.
    global_stats.place(x=375, y = 145, anchor='center') # Global Stats Message  (Homepage)
    label.place(x=375, y = 220, anchor='center')        # "Country" label       (Homepage)
    entry.place(x=375, y = 250, anchor='center')        # Entry Box             (Homepage)
    button.place(x=375, y = 280, anchor='center')       # Enter Button          (Homepage)
    end_label.place(x=375, y=465, anchor='center')      # Footer Label          (Homepage)

    # End of code for tkinter window.
    window.mainloop()


main()


