


//tool tip should work for all terrain objects
var monster_tooltip = d3.select("body")
	.append("div")
	.attr("id", "monster-info")                
	.style("position", "absolute")
	.style("z-index", "10")
	.style("visibility", "hidden")
	.html("<p>Default Text</p>");

//spin through the list of big objects and create
monstermeta = mapData['monsters']['meta];
monstermeta['cord'] = get_rnd_coord()


data = []
for (i=0;i<mapData['monsters']['m'];i++) {
		cord = Math.floor(Math.random() * 6) - 6
		//TODO: changes in mapData["monsters"]["meta"]["render type"] should 
		//take affect here.  
		t.spawnOrigin_x = monstermeta['cord'][0] + cord
		t.spawnOrigin_y = monstermeta['cord'][1] + cord
		t.color = i.color
		t.move = i.move
		t.healt = i.health
		t.size = i.size
		data.push(JSON.parse(JSON.stringify(t)))
}

</script>
