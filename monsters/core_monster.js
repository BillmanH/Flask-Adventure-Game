//this is the code thatmonsters do on thier turn. 
//   Turn order is set in the activity_map_boarder.html
//   in the same places as the svgClick function

d3.selectAll(".monster")
	.each(function(d,i) {
		if(get_dist_to_char(d3.select(this).attr("cx"),d3.select(this).attr("cy"))<=15){ //TODO replace arbitrary value with monster's perception
			objectAlerts("#character",d3.select(this).attr("id")+" Has spotted " + charData["name"]);
			nmc = move_towards_char(d3.select(this).attr("cx"),d3.select(this).attr("cy"),d3.select(this).attr("move"))
			d3.select(this).transition()
				.attr("cx",nmc[0])
				.attr("cy",nmc[1])
		}
		else {
			d3.select(this).transition()
				.attr("cx",function(d, i) { return (parseInt(d3.select(this).attr("cx")))+(coordshifter(parseInt(d3.select(this).attr("move"))))})
				.attr("cy",function(d, i) { return (parseInt(d3.select(this).attr("cy")))+(coordshifter(parseInt(d3.select(this).attr("move"))))})
		}
	})
