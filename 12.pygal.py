
import pygal 
worldmap =  pygal.maps.world.World() 
worldmap.title = 'Child Labour Percentage in Different Countries'
worldmap.add("India",{"in":40})
worldmap.add("Japan",{"jp":30})
worldmap.add("turkey",{"tr",40})
worldmap.add("USA",{"us",45})
worldmap.add("South Africa",{"za",40})
worldmap.add("Pakisthan",{"pk",40})
worldmap.render_to_file('abc.svg') 
print("Success") 
