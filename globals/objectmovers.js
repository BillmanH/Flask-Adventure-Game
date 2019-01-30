function moveTargetToSubject(target,subject){
	
	var move = d3.select("#"+target).attr("move");
	if(move==null){move=1}

	nmc = move_towards_obj(Math.round(d3.select("#"+subject).attr("cx")),
			Math.round(d3.select("#"+subject).attr("cy")),
			char_x,
			char_y,
			move);
console.log(Math.round(d3.select("#"+subject).attr("cx")),
                        Math.round(d3.select("#"+subject).attr("cy")),
                        char_x,
                       char_y,
                        move)

console.log(nmc);	
	d3.select("#"+target).transition()
			.attr("cx",nmc[0])		
			.attr("cy",nmc[1])
}
