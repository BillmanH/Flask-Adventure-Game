// This is where the monster attack happens
var damage = randBetween(0,mapData["monsters"]["meta"]["damage"])*-1;
	damage = Math.round(damage*100)/100

//send an alert to the screen about the attack
objectAlerts("#"+d3.select(this).attr("id"),
		damage.toString() + ": " + d3.select(this).attr("name")+" "+mapData["monsters"]["meta"]["attackType"],
		color="#8b0000")

//subtract the damage from the health of the player
charData["health"] = charData["health"]+damage

//action if the characterhas died
if(charData["health"]<0){
	objectAlerts("#character",charData["name"] + " has died")
	charDeath()
} else {charattack(this)} //the character automatically attacks back if able

 
