import requests
from tkinter import *

class WeatherApp:
    def __init__(self, window):
        self.window = window
        self.setup_ui()

    def setup_ui(self):
        
        # Creating the label frame for Entry Frame
        label_frame = Frame(self.window, relief="raised")
        label_frame.grid(row=0, column=0, columnspan=3, sticky="nsew", padx=50, pady=70)

        # Creating Label inside the Label Frame
        label_location = Label(label_frame, text="Location: ", font=("Verdana", 14))
        label_location.grid(row=0, column=0, sticky="ew")

        # Creating the entry box inside the label frame
        self.location_entry = Text(label_frame, width=25, borderwidth=2, height=1)
        self.location_entry.grid(row=0, column=1, columnspan=2, pady=7, sticky="ew")

        # Creating the search button
        search_btn = Button(label_frame, text="🔍", relief="raised", state="normal", command=self.get_weather)
        search_btn.grid(row=0, column=3, sticky="ew", padx=10)

        # Creating the label for result frame
        self.result_frame = LabelFrame(self.window, text=f"Weather in city ", padx=25, pady=20)
        self.result_frame.grid(row=1, column=0, columnspan=3, sticky="nsew", padx=20, pady=10)

        # Other UI elements and labels can be created similarly here
        self.description_label = Label(self.result_frame, text="", pady=20, padx=100, font=("Verdana", 12), foreground="#000000")
        self.description_label.grid(row=1, column=1, columnspan=3, sticky="ew")

        self.temp_label = Label(self.result_frame, text="Temperature: ")
        self.temp_label.grid(row=2, column=1, padx=7)

        self.humidity_label = Label(self.result_frame, text="Humidity: ")
        self.humidity_label.grid(row=3, column=1, pady=7)

        self.wind_speed_label = Label(self.result_frame, text="Wind Speed: ")
        self.wind_speed_label.grid(row=4, column=1, pady=7)

        self.pressure_label = Label(self.result_frame, text="Pressure: ")
        self.pressure_label.grid(row=5, column=1, pady=7)

        self.precip_label = Label(self.result_frame, text="Precipitation: ")
        self.precip_label.grid(row=6, column=1, pady=7)

        # Creating the status bar frame
        status_frame = Frame(self.window, padx=20, pady=10, borderwidth=5)
        status_frame.grid(row=2, column=0, columnspan=3, padx=200, pady=5, sticky="ew")

        self.date_time_status = Label(status_frame, text="")
        self.date_time_status.grid(row=2, column=0, columnspan=3, sticky="ew")


        # Set up the command for the search button
        search_btn = Button(label_frame, text="🔍", relief="raised", state="normal", command=self.get_weather)
        search_btn.grid(row=0, column=3, sticky="ew", padx=10)

    def get_weather(self):
        try:
            city_name = self.location_entry.get(1.0, END).capitalize().strip()
            api_key = "2f3664565caa49b8bb374013233011"
            url = f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={city_name}&aqi=no"

            response = requests.get(url).json()
            if 'error' in response:
                raise ValueError(f"{response['error']}: {response['message']}")
            
             # Extract data from response and update UI elements
            temp_celsius = response['current']['temp_c']
            temp_fahrenheit = response['current']['temp_f']
            humidity_percentage = response['current']['humidity']
            wind_speed_kph = response['current']['wind_kph']
            pressure_hpa = response['current']['pressure_mb']
            precip_percentage = response['current']['precip_mm']
        
            # Extract data from response and update UI elements
            self.update_labels(temp_celsius, temp_fahrenheit, humidity_percentage, wind_speed_kph, pressure_hpa, precip_percentage)

        except requests.exceptions.RequestException as e:
            self.update_description_text(f"Request Exception: {str(e)}")
        except KeyError as e:
            self.update_description_text(f"KeyError: {str(e)}")
        except ValueError as e:
            self.update_description_text(f"API Error: {str(e)}")
        except Exception as e:
            self.update_description_text(f"Unexpected Error: {str(e)}")

    def update_description_text(self, text):
        try:
            if "cloudy" in text.lower():
                self.description_label.config(text=f"{text}   ☁", foreground="#A9A9A9")
            elif "sunny" in text.lower():
                self.description_label.config(text=f"{text}   ☀", foreground="#FFD700")
            elif "rainy" in text.lower():
                self.description_label.config(text=f"{text}   🌧", foreground="#4682B4")
            elif "partly cloudy" in text.lower():
                self.description_label.config(text=f"{text}   ⛅", foreground="#d4d4d4")
            elif "thunder" in text.lower():
                self.description_label.config(text=f"{text}   ⛈", foreground="#4B0082")
            elif "clear" in text.lower():
                self.description_label.config(text= f"{text}   🌃", foreground="#33FFBD")     
            else:
                self.description_label.config(text=f"{text}   ", foreground="#000000")  # Default case

        except Exception as e:
            self.description_label.config(text="Error: Please Enter A Valid City Name!")


# Other helper methods for updating UI elements, configuring frames, labels, etc.
    def update_labels(self, temperature_c, temperature_f, humidity, wind_speed, pressure, precipitation):
        self.temp_label.config(text=f"Temperature: {temperature_c}°C / {temperature_f}°F")
        self.humidity_label.config(text=f"Humidity: {humidity}%")
        self.wind_speed_label.config(text=f"Wind Speed: {wind_speed} km/h")
        self.pressure_label.config(text=f"Pressure: {pressure} hPa")
        self.precip_label.config(text=f"Precipitation: {precipitation}%")


if __name__ == "__main__":
    window = Tk()
    window.title("Today's Weather")
    window.geometry("600x500")


    weather_app = WeatherApp(window)
    window.mainloop()
