


//tool tip should work for all terrain objects
var terrain_tooltip = d3.select("body")
	.append("div")
	.attr("id", "terrain-info")                
	.style("position", "absolute")
	.style("z-index", "10")
	.style("visibility", "hidden")
	.html("<p>Default Text</p>");

//spin through the list of big objects and create
for (item in mapData['area']['Terrain Textures']){
	t = mapData['area']['Terrain Textures'][item]  //loading the current terrain object to t to save text
	//console.log("T= ",t)

	
	//take imput paramerter from t and create an array of data objets for D3. 
	data = []
	for (i=0;i<t['abundance'];i++) {
		cord = get_rnd_coord()
		t.spawnOrigin_x = cord[0]
		t.spawnOrigin_y = cord[1]
		data.push(JSON.parse(JSON.stringify(t)))
	}
	switch(t['spread']){
		case "scatter":
		{% if "scatter" in spreadTypes %}
			{% include "game/terrain/scatter.js" %}	
		{% endif %}
		break;
		case "line":
		{% if "line" in spreadTypes %}
			{% include "game/terrain/line.js" %} 
		{% endif %}
		break;
		default:
//Assumiming that if there is no spread type, just place it randomly, terrain['density'] is ignored
	}
}
</script>
