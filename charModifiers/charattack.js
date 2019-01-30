function assign_damage_to_target(target,damage){
	console.log("assign_damage_to_target",target.id)
	if(damage>0){damage=damage*-1} //damage should always be negative so that it subtracts from the target's health.
		d3.select("#"+target.id).data()[0].health=d3.select("#"+target.id).data()[0].health+damage;
	if (d3.select("#"+target.id).data()[0].health<=0){
		{% include "game/monsters/monster_death.js" %}
	}
}

function charattack(target){
	console.log("charattack",target.id)
	var attacksWith = 'fists' // if no weapon, the character defends with fists
	var charDamage = [1,2]  //default damage is 1-2
	var charColor = "#0000ff"  //color of the message that the character recieves
	var damage = 1 //default damage is 1 (if no weapon is equiped)
	// checktoSee if a character has equipped items that do damage
	if('equiped' in charData){ //first a check to see if they have a character that has the 'equiped' feature
		if(charData["equiped"]["strong hand"] == undefined)
			{ //check that either hand has been defined.
			charData["equiped"]["strong hand"]={}}
		if((charData["equiped"]["off hand"] == undefined))
			{charData["equiped"]["off hand"]={}}
		if ((charData["equiped"]["strong hand"].damage == undefined)&&(charData["equiped"]["off hand"].damage == undefined)){
			objectAlerts('#character',charData['name']+' has no weapon')
			damage=randBetween(charDamage[0],charDamage[1])
			damage = (Math.round(damage*100)/100)*-1
			objectAlerts('#character',
				damage.toString()+": " + charData['name']+' attacks '+ target.name +' with '+ attacksWith,
				color=charColor)
		} else { //strong hand attack
			if(charData["equiped"]["strong hand"].damage != undefined){
				damage=randBetween(charData["equiped"]["strong hand"].damage[0],charData["equiped"]["strong hand"].damage[1])
				damage = (Math.round(damage*100)/100)*-1
				objectAlerts('#character',
						damage.toString()+": " + charData['name']+' attacks with '+charData["equiped"]["strong hand"].name,
						color=charColor)
			}
			
		}
	} else {
		charData["equiped"]= {} //equiped needs to be created if it has not yet been added to charData
		}
	//step two: Apply damage to character
	assign_damage_to_target(target,damage)
}



