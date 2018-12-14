function charattack(target){
	//step one: deterimine damage
	if('equiped' in charData){ //first a check to see if they have a character that has the 'equiped' feature
		if (charData["equiped"]["left hand"].damage == undefined)&(charData["equiped"]["right hand"].damage == undefined){
			objectAlerts('#character',charData['name']+'has no weapon')
		}
	}
	//step two: Apply damage to character
	d3.select(target)
	
}

