# python-weather-app
Weather App by python using API from freeweatherapi.com

### Overview
The Weather App is a simple (GUI) developed using the Tkinter library in Python. It fetches weather data from the WeatherAPI based on user-entered locations and displays various weather parameters.

### Application Components
- **GUI Initialization**: Sets up the main window with the title "Today's Weather" and defines its dimensions.
- **Main Functionality (get_weather)**: Fetches weather data from the WeatherAPI based on the user's location input and updates the UI accordingly.
    - It constructs the API URL using the user-entered location and the API key.
    - Upon successful retrieval of data, it updates labels for temperature, humidity, wind speed, pressure, and precipitation.
    - It handles exceptions for invalid input or network issues and displays error messages.

### User Interface Elements
- **Location Input**: A text box for users to enter the location.
- **Search Button 🔍**: Triggers the `get_weather` function upon clicking.
- **Result Frame**: Displays weather details for the specified location.
    - Labels for temperature, humidity, wind speed, pressure, and precipitation.
- **Status Bar**: Shows the current date and time.

### Functions
- **get_weather()**: Fetches weather data based on user input and updates UI elements accordingly.
- **update_result_frame(city)**: Updates the result frame with the city's weather information.
- **update_description_text(text)**: Updates the weather description label based on weather conditions.
- **update_date_time(date)**: Updates the status bar with the current date and time.

### Usage
1. Run the application.
2. Enter a location in the text box.
3. Click the search button to fetch and display weather data.

### Dependencies
- `requests`: Used to make HTTP requests to the WeatherAPI.
- `tkinter`: Provides the GUI toolkit for creating the application's interface.

### Limitations
- Dependency on the availability and reliability of the WeatherAPI service.
- Limited error handling for specific cases such as invalid user input.
