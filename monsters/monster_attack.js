// This is where the monster attack happens
var damage = randBetween(0,mapData["monsters"]["meta"]["damage"])*-1;
	damage = Math.round(damage*100)/100
objectAlerts("#"+d3.select(this).attr("id"),d3.select(this).attr("name")+" "+mapData["monsters"]["meta"]["attackType"])
objectAlerts("#character", damage.toString())
charData["health"] = charData["health"]+damage
if(charData["health"]<0){objectAlerts("#character",charData["name"] + " has died")} 
