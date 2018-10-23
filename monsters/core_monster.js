//this is the code thatmonsters do on thier turn. 
//   Turn order is set in the activity_map_boarder.html
//   in the same places as the svgClick function

d3.selectAll(".monster")
	.each(function(d,i) {
		// the perception is in the metadata for monsters. if the character moves within the range of perception, the character is noticed. 
		if(get_dist_to_char(d3.select(this).attr("cx"),d3.select(this).attr("cy"))<=mapData["monsters"]["meta"]["perception"]){
			// detectsPlayer defaults to False
			if (d3.select(this).classed("detectsPlayer")==false){
				objectAlerts("#character",d3.select(this).attr("id")+" Has spotted " + charData["name"]);
				d3.select(this).classed("detectsPlayer",true);
			}
			// if the character is close enough to attack, it attacks.
			if(get_dist_to_char(d3.select(this).attr("cx"),d3.select(this).attr("cy"))<=charData["size"]){
				// TODO : break the attack out to it's own function.
				objectAlerts("#character",d3.select(this).attr("id")+" struck at the player ");
			}	
			nmc = move_towards_obj(Math.round(d3.select(this).attr("cx")),
						Math.round(d3.select(this).attr("cy")),
						char_x,
						char_y,
						d3.select(this).attr("move"));
			d3.select(this).transition()
				.attr("cx",nmc[0])
				.attr("cy",nmc[1])
		}
		// else if the character is not detected the moster does whateverthey were going to do
		else {
			d3.select(this).transition()
				.attr("cx",function(d, i) { return (parseInt(d3.select(this).attr("cx")))+(coordshifter(parseInt(d3.select(this).attr("move"))))})
				.attr("cy",function(d, i) { return (parseInt(d3.select(this).attr("cy")))+(coordshifter(parseInt(d3.select(this).attr("move"))))})
			d3.select(this).classed("detectsPlayer",false)
		}
	})
