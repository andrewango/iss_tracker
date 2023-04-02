import urllib.request
import webbrowser
import turtle
import json
import time
import geocoder
import math

# Load in NASA's astronaut API
url = "http://api.open-notify.org/astros.json"
response = urllib.request.urlopen(url)
result = json.loads(response.read())
file = open("iss_tracker.txt", "w")

# Write the astronauts on the ISS
file.write(str(result["number"]) + " astronauts are currently aboard the International Space Station:\n\n")
for astronaut in result["people"]:
    file.write(str(astronaut["name"]) + " - on board\n")

# Write your location on Earth and its relative distance from the ISS
my_location = geocoder.ip("me")
file.write("\nYou are at the following coordinates: " + str(my_location.latlng) + "\n")
file.close()
webbrowser.open("iss_tracker.txt")

# CREATE MOVING ISS ON WORLD MAP
screen = turtle.Screen()
screen.setup(1280, 720)
screen.setworldcoordinates(-180, -90, 180, 90)

screen.bgpic("world_atlas.gif")
screen.register_shape("iss_spacecraft.gif")
iss_spacecraft = turtle.Turtle()
iss_spacecraft.shape("iss_spacecraft.gif")
iss_spacecraft.setheading(45)
iss_spacecraft.penup()


# Calculates your relative distance to the ISS 
def calc_distance_from_iss(longitude, latitude):
    ground_d = 3963.0 * math.acos((math.sin(my_location.lat) * math.sin(latitude)) + math.cos(my_location.lat) * math.cos(latitude) *  math.cos(longitude - my_location.lng))
    orbit_ht = 253
    d = math.sqrt(pow(ground_d, 2) + pow(orbit_ht, 2))
    return (d * 1.609344) # Convert to km

while True:

    # Load in ISS location information
    url = "http://api.open-notify.org/iss-now.json"
    response = urllib.request.urlopen(url)
    result = json.loads(response.read())

    longitude = float(result["iss_position"]["longitude"])
    latitude = float(result["iss_position"]["latitude"])
    print("ISS Coordinates:\n--------------------\nLong: " + str(round(longitude, 4)) + " | Lat: " + str(round(latitude, 4)))
    print("You are approximately " + str(round(calc_distance_from_iss(longitude, latitude), 4)) + " km away from the ISS.\n")
    
    # Update ISS location on map every 5 seconds
    iss_spacecraft.goto(longitude, latitude)
    
    time.sleep(5)


