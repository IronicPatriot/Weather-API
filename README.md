# Weather-API

Standalone version of the Weather APP that prints results to the terminal instead of being attatched to the output of a HTML page like the one on my portfolio site. 

Both versions use OpenWeathers API to show the weather at any given coordinates. 

Version 2 does not use Python Geocoder to get the local machine's IP, as this would not work as intended when pushed to a server. Instead it uses another API, IPSTACK, to get the coordinates needed by OpenWeather.
