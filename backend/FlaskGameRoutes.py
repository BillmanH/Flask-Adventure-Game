
from flask import Blueprint, render_template, abort

import BOTO_functions as bto

game_bp = Blueprint('game', __name__, template_folder='templates')
newcharacter_bp = Blueprint('newcharacter', __name__, template_folder='templates')
gamecontinue_bp = Blueprint('gamecontinue', __name__, template_folder='templates')
createcharacter_bp = Blueprint('createcharacter', __name__, template_folder='templates')

 
@game.route('/game')
def game():
	charData = bto.getCharData()
	mapData = bto.getAreaInfoFromMap(charData)
	tDetail = bto.getTerrainDetails(mapData['area']['Terrain Code'])
	spreadTypes = [type["spread"] for type in tDetail["Terrain Textures"]]
	#tDetail = {"BOTO fetch Error"}
	return render_template('game/core_view.html',charData=charData,mapData=mapData,terrData=tDetail,spreadTypes=spreadTypes)

@newcharacter.route('/game/newcharacter')
def newcharacter():
	raceData = bto.getRaceData()
	classData = bto.getClassData()
	return render_template('game/userforms/newcharacter.html',raceData=raceData,classData=classData)

@createcharacter.route('/game/createcharacter', methods=['GET','POST'])
def createcharacter():
	formData = yaml.load(request.form['formData'])
	return str(formData) + "You will get an email soon with your character info and a link"

@gamecontinue.route('/gamecontinue', methods=['GET', 'POST'])
def gamecontinue():
	#Step one: Saving the character data from the last screen
	charDataD = yaml.load(request.form['charData'])
	charData = request.form['charData']
	bto.saveCharData(charData)
	#Step two: loading data for the next area 
	mapData = bto.getAreaInfoFromMap(charDataD) #takes a character object, not a string
	tDetail = bto.getTerrainDetails(mapData['area']['Terrain Code'])
	spreadTypes = [type["spread"] for type in tDetail["Terrain Textures"]]
	return render_template('game/core_view.html',charData=charDataD,mapData=mapData,terrData=tDetail,spreadTypes=spreadTypes)









