# A simple python program
# that displays the exact location
# of a particular location
# showcases the use of the folium library

import folium 

my_latitude = -15.455392
my_longitude = 28.275311

map_center = [-15.455392, 28.275311]
mymap = folium.Map(location=map_center, zoom_start=16)

folium.Marker (
    [-15.455392, 28.275311],
    popup = "Ndonaika Residence",
    icon = folium.Icon(color="blue",icon="info-sign")
).add_to(mymap)

mymap.save("Ndonaika Residence.html")

import webbrowser
webbrowser.open("Ndonaika Residence.html")