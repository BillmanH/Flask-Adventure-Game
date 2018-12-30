function calculateDamage(damageRange=[0,1]){
	
}

function charattack(target){
	// default is that the character attacks with fists
	var attacksWith = 'fists'
	var charDamage = [1,2]
	var charColor = "#0000ff"
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
				damage.toString()+": " + charData['name']+' attacks with '+ attacksWith,
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
	}
	//step two: Apply damage to character
	
}


