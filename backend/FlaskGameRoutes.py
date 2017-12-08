import yaml
from flask import Blueprint, render_template,request
import BOTO_functions as bto
import CharData_MakeNewAccount as c 

game = Blueprint('game', __name__, template_folder='templates')
newcharacter = Blueprint('newcharacter', __name__, template_folder='templates')
gamecontinue = Blueprint('gamecontinue', __name__, template_folder='templates')
createcharacter = Blueprint('createcharacter', __name__, template_folder='templates')
welcome = Blueprint('welcome',__name__, template_folder='templates')
gameload = Blueprint('loadedgame',__name__, template_folder='templates')

#listing the routing here so that I don't have to call them individually a second time in the flaskapp.py
GameRoutes = [
	game
	,newcharacter
 	,gamecontinue
	,createcharacter
	,welcome
	,gameload]

@welcome.route('/game/welcome')
def welcomeview():
	return render_template('game/userforms/welcomeview.html')


@game.route('/game',methods=['GET','POST'])
def startgame():
	if request.args.get('path')=="new":	
		formData = yaml.load(request.form['formData'])
		charID = formData['id']
		charToken = formData['token']
		charData = bto.getCharData(user=charID,token=charToken)
	else:
		return "Unable to load character"
	mapData = bto.getAreaInfoFromMap(charData)
	tDetail = bto.getTerrainDetails(mapData['area']['Terrain Code'])
	spreadTypes = [type["spread"] for type in tDetail["Terrain Textures"]]
	#tDetail = {"BOTO fetch Error"}
	return render_template('game/core_view.html',charData=charData,mapData=mapData,terrData=tDetail,spreadTypes=spreadTypes)

@newcharacter.route('/game/newcharacter')
def formnewcharacter():
	raceData = bto.getRaceData()
	classData = bto.getClassData()
	return render_template('game/userforms/newcharacter.html',raceData=raceData,classData=classData)

@createcharacter.route('/game/createcharacter', methods=['GET','POST'])
def returncreatecharacter():
	formData = yaml.load(request.form['formData'])
	mapmeta = c.saveNewCharacterData(formData)
	return render_template('game/userforms/newcharactercreated.html',charData=formData,mapmeta=mapmeta)
	#return str(formData) + "You will get an email soon with your character info and a link" + "\b" + str(mapmeta)

@gameload.route('/game/loadedgame',methods=['GET','POST'])
def startgameload():
	formData = yaml.load(request.form['formData'])
	charEmail = formData['email']
	charToken = "pass"
	#TODO: CharToken needs to happen here
	charData = bto.getCharData(user=charEmail,token=charToken)	
	mapData = bto.getAreaInfoFromMap(charData)
	tDetail = bto.getTerrainDetails(mapData['area']['Terrain Code'])
	spreadTypes = [type["spread"] for type in tDetail["Terrain Textures"]]
	return render_template('game/core_view.html',charData=charData,mapData=mapData,terrData=tDetail,spreadTypes=spreadTypes)

@gamecontinue.route('/gamecontinue', methods=['GET', 'POST'])
def startgamecontinue():
	#Step one: Saving the character data from the last screen
	charDataD = yaml.load(request.form['charData'])
	charData = request.form['charData']
	bto.saveCharData(charData)
	#Step two: loading data for the next area 
	mapData = bto.getAreaInfoFromMap(charDataD) #takes a character object, not a string
	tDetail = bto.getTerrainDetails(mapData['area']['Terrain Code'])
	spreadTypes = [type["spread"] for type in tDetail["Terrain Textures"]]
	return render_template('game/core_view.html',charData=charDataD,mapData=mapData,terrData=tDetail,spreadTypes=spreadTypes)









