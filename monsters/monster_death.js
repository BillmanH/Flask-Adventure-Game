function monster_death(target){
	console.log(target,"died!");
	d3.select("#"+target.id)
	//d3.select(target)
		.transition()
		.attr('r',4)
		.fill("white")
			
}
