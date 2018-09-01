//this is the code thatmonsters do on thier turn. 
//   Turn order is set in the activity_map_boarder.html
//   in the same places as the svgClick function

d3.selectAll(".monster")
	.each(function(d,i) {
		if(get_dist_to_char(d3.select(this).attr("cx"),d3.select(this).attr("cy"))<=15){ //TODO replace arbitrary value with monster's perception
			if (d3.select(this).classed("detectsPlayer")==false){
				objectAlerts("#character",d3.select(this).attr("id")+" Has spotted " + charData["name"]);
				d3.select(this).classed("detectsPlayer",true);
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
		else {
			d3.select(this).transition()
				.attr("cx",function(d, i) { return (parseInt(d3.select(this).attr("cx")))+(coordshifter(parseInt(d3.select(this).attr("move"))))})
				.attr("cy",function(d, i) { return (parseInt(d3.select(this).attr("cy")))+(coordshifter(parseInt(d3.select(this).attr("move"))))})
			d3.select(this).classed("detectsPlayer",false)
		}
	})
