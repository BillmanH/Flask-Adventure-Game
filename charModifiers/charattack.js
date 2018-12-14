function charattack(target){
	// default is that the character attacks with fists
	var attacksWith = 'fists'
	var charDamage = [1,2]
	// checktoSee if a character has equipped items that do damage
	if('equiped' in charData){ //first a check to see if they have a character that has the 'equiped' feature
		if ((charData["equiped"]["left hand"].damage == undefined)&&(charData["equiped"]["right hand"].damage == undefined)){
			objectAlerts('#character',charData['name']+'has no weapon')
		} else {
			if(charData["equiped"]["left hand"].damage != undefined){
				damage=randBetween(charData["equiped"]["left hand"].damage[0],charData["equiped"]["left hand"].damage[1])
				damage = (Math.round(damage*100)/100)*-1
				objectAlerts('#character',damage.toString()+": " + charData['name']+' attacks with '+charData["equiped"]["left hand"].name)
			}
			
		}
	}
	//step two: Apply damage to character
	d3.select(target)
	
}

