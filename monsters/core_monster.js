d3.selectAll(".monster")
	.transition()
		.attr("cx",function(d, i) { return (parseInt(d3.select(this).attr("cx")))+(coordshifter(parseInt(d3.select(this).attr("move"))))})	
		.attr("cy",function(d, i) { return (parseInt(d3.select(this).attr("cy")))+(coordshifter(parseInt(d3.select(this).attr("move"))))})
