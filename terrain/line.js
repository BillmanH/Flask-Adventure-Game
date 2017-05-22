for(i=0;i<=t['abundance'];i++){
	var elem = canvas.selectAll(t['name'])  
			.data(data)
			.enter()
			.append("circle")
			.style('z-index',8)
			.attr("cx",function(d){return d.spawnOrigin_x})
			.attr("cy",function(d){return d.spawnOrigin_y})
			.attr("affect",function(d){return d.affect})
			.attr("affectText",function(d){return d.affectText})
			.attr("affectAmt",function(d){return d.affectAmt})
			.attr("id",function(d){return d.name})
			.attr("name",function(d){return d.name})
			.classed("terrain", true)
			.attr("r",function(d){return d.size})
			.style("fill",function(d){return d.hex})
			.on("mouseover", function(d){
				return terrain_tooltip.style("visibility", "visible")
						.html(d.name);
					})
			.on("mousemove", function(d){
				return terrain_tooltip.style("top", (event.pageY-10)+"px").style("left",(event.pageX+10)+"px")
						.html(d.name);
					})
			.on("mouseout", function(){
				return terrain_tooltip.style("visibility", "hidden");
					});
                }

var enterSelection = canvas.selectAll(t['name']).data(data).enter();
xOffset = 0
yOffset = 0

for(i=0;i<=t['abundance'];i++){

	xOffset = xOffset + t['size']
	yOffset = yOffset + t['size']


	enterSelection.append("circle")
                        .style('z-index',8)
                        .attr("cx",function(d){return d.spawnOrigin_x + xOffset})
                        .attr("cy",function(d){return d.spawnOrigin_y + yOffset})
                        .attr("affect",function(d){return d.affect})
                        .attr("affectText",function(d){return d.affectText})
                        .attr("affectAmt",function(d){return d.affectAmt})
                        .attr("id",function(d){return d.name})
                        .attr("name",function(d){return d.name})
                        .classed("terrain", true)
                        .attr("r",function(d){return d.size})
                        .style("fill",function(d){return d.hex})
                        .on("mouseover", function(d){
                                return terrain_tooltip.style("visibility", "visible")
                                                .html(d.name);
                                        })
                        .on("mousemove", function(d){
                                return terrain_tooltip.style("top", (event.pageY-10)+"px").style("left",(event.pageX+10)+"px")
                                                .html(d.name);
                                        })
                        .on("mouseout", function(){
                                return terrain_tooltip.style("visibility", "hidden");
                                        });
}
