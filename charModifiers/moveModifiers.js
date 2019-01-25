var moveRate = charData["speed"]
if ("slowed" in charData["attributes"]){
        moveRate = 1
        charData["attributes"]["slowed"] -= 1
        if (charData["attributes"]["slowed"]<1){
                delete charData["attributes"]["slowed"]
        }       
}
