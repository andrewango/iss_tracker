Hi!
This program uses NASA's API at http://api.open-notify.org/astros.json and http://api.open-notify.org/iss-now.json to obtain information about astronauts currently aboard the ISS and its latitude and longitude. 

The ISS is shown flying across a map according to the API's given coordinates.
The user's distance from the ISS is calculated using the Haversine formula, the ISS's approximate orbit height (253 miles), and the Pythagorean theorem.