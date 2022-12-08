from Canard_mode import WeatherData, CurrentDisplay, StatDisplay

currentDisplay = CurrentDisplay()
statDisplay = StatDisplay()
weatherData = WeatherData()
weatherData.add_display(currentDisplay)
weatherData.measurementsChanged()
weatherData.add_display(statDisplay)
weatherData.measurementsChanged()
