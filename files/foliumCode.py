#Import the folium package for making maps
import folium

#Create a map, centered (0,0), and zoomed out a bit:
mapWorld = folium.Map(location=[0, 0],zoom_start=3)

folium.Marker(location = [23.777176, 90.399452], popup = "Where I'm from").add_to(mapWorld)
folium.Marker(location = [35.964668, -83.926453], popup = "My first home in the US").add_to(mapWorld)
folium.Marker(location = [40.730610, -73.935242], popup = "Where I currently live").add_to(mapWorld)

aline=folium.PolyLine(locations=[(23.777176, 90.399452),(35.964668, -83.926453)],weight=2,color = 'blue')
bline=folium.PolyLine(locations=[(35.964668, -83.926453), (40.230610, -74.935242)],weight=2,color = 'blue')


#Save the map:
mapWorld.save(outfile='Map.html')