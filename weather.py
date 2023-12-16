#API Key:2f3664565caa49b8bb374013233011
#http://api.weatherapi.com/v1/current.json?key=2f3664565caa49b8bb374013233011&q=London&aqi=no

# The Frame of tkinter 
#creating the window
from tkinter import *
import requests

window= Tk()
window.title("Today's Weather")
window.iconbitmap("cloud-sun-rain.ico")
window.geometry("500x560+200+50")
window.maxsize(width= 650, height = 650)


##-------------------------Main Functionality----------------------------
def get_weather():
    global city_name, date_time, condition_txt
    city_name= location_entry.get(1.0, END).capitalize()
    api_key= "2f3664565caa49b8bb374013233011"
    url= f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={city_name}&aqi=no"
    try:
        response= requests.get(url).json()
        if not "error" in response :
            print(response)
            city_name = response['location']['name']    #update City in Lable Frame
            date_time = response['location']['localtime'] #update date in status bar

            temp_celsius = response['current']['temp_c']
            temp_fahrenheit = response['current']['temp_f']
            wind_speed_kph = response['current']['wind_kph']
            humidity_percentage = response['current']['humidity']
            precip_percentage = response['current']['precip_mm']  
            pressure_hpa = response['current']['pressure_mb']
            condition_txt = response['current']['condition']['text']

            #UPDATE THE LABELS

            temp_label.config(text= f"Temperature: {temp_celsius}°C / {temp_fahrenheit}°F")
            humidity_label.config(text= f"Humidity: {humidity_percentage}%")
            wind_speed_label.config(text= f"Wind Speed: {wind_speed_kph} km/h")
            pressure_label.config(text= f"Pressure: {pressure_hpa} hPa")
            precip_label.config(text= f"Precipitation: {float(precip_percentage)*100}%" )

            

            #Update Result Frame 
            update_result_frame(city_name)
            #update Status Bar
            update_date_time(date_time)
            #upate Condition Lable
            upadate_description_text(condition_txt)

        else :
            raise ValueError(f"{response['error']}: {response['message']}")
    except Exception  as e:
       upadate_description_text(e)
    

def update_result_frame(city):
    city= city_name.capitalize()
    result_frame.config(text= f"Weather in {city}")

def upadate_description_text(text): # label 
    try :
        text =condition_txt
        if "cloudy" in text.lower():
            description_label.config(text= f"{text}   ☁", foreground="#A9A9A9")
        elif "sunny" in text.lower():
            description_label.config(text= f"{text}   ☀", foreground="#FFD700")    
        elif "rainy" in text.lower():
            description_label.config(text= f"{text}   🌧", foreground="#4682B4")    
        elif "partly cloudy" in text.lower():
            description_label.config(text= f"{text}   ⛅", foreground="#d4d4d4")    
        elif "thunder" in text.lower():
            description_label.config(text= f"{text}   ⛈", foreground="#4B0082")
        elif "clear" in text.lower():
             description_label.config(text= f"{text}   🌃", foreground="#33FFBD")       

    except Exception  as e:
        text = e
        print(text)
        description_label.config(text= f"Error: Please Enter A Valid City Name!")

def update_date_time(date): # Status Bar
    date_time_status.config(text= f" Today: {date}", background="#c1c1c1")



#Creating the lable frame for Entry Frame 

label_frame = Frame(window, relief="raised")
label_frame.grid(row=0 , column= 0 ,columnspan= 3, sticky= "nsew",padx= 50, pady= 70)

# creating Lable inside the Lable Frame :
label_location = Label(label_frame, text="Location: ", font= ("Verdana", 14))
label_location.grid(row= 0 , column = 0, sticky= "ew")

#creating the entry box inside the lable frame :
location_entry= Text(label_frame, width= 25,borderwidth=2, height=1)
location_entry.grid(row=0, column= 1, columnspan= 2, pady=7, sticky="ew")

#creation the search button 
search_btn= Button(label_frame, text="🔍",relief="raised",state="normal", command=get_weather)
search_btn.grid(row=0, column= 3, sticky="ew", padx=10)

#--------------------------------------------------------------------------------
#creating the label for result frame 
result_frame = LabelFrame(window, text=f"Weather in city ", padx= 25, pady= 20)
result_frame.grid(row=1 , column=0, columnspan=3, sticky="nsew", padx= 20, pady=10)

description_label= Label(result_frame, text= "", pady= 20 ,padx=100 ,font=("Verdana", 12), foreground="#000000") # udate description
description_label.grid(row=1, column=1, columnspan= 3, sticky="ew" )

temp_label= Label(result_frame, text="Temperature: ")
temp_label.grid(row=2, column= 1, padx= 7)

humidity_label= Label(result_frame, text="Humidity: ")
humidity_label.grid(row=3, column= 1, pady=7)

wind_speed_label= Label(result_frame, text="Wind Speed: ")
wind_speed_label.grid(row=4, column= 1, pady=7)

pressure_label= Label(result_frame, text="Pressure: ")
pressure_label.grid(row=5, column= 1, pady= 7)

precip_label= Label(result_frame, text="Precipitation: ")
precip_label.grid(row=6, column= 1, pady= 7)

#_---------------------------------------------------------------------------------
# Creating Status Bar 
status_frame = Frame(window, padx= 20 , pady= 10, borderwidth=5)
status_frame.grid(row= 2, column=0 , columnspan= 3, padx= 200, pady= 5, sticky="ew")

date_time_status= Label(status_frame, text="", )
date_time_status.grid(row = 2, column=0 , columnspan= 3, sticky="ew")



window.mainloop()