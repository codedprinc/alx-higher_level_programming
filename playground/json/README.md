# Project: Fetching **Current Weather Data**
---
Overall, the program does the following:
- Reads the requested location from the command line.
- Downloads JSON weather data from OpenWeatherMap.org.
- Converts the string of JSON data to a Python data structure.
- Prints the weather for today and the next two days.

---


So the code will need to do the following:
- Join strings in sys.argv to get the location.
- Call requests.get() to download the weather data.
- Call json.loads() to convert the JSON data to a Python data structure.
- Print the weather forecast.