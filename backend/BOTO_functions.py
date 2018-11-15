from boto.s3.connection import S3Connection
import boto
import yaml
import numpy as np
import pandas as pd

#conn = boto.connect_s3()

conn = S3Connection()

def getFullMap(charData):
	UserID = charData['id']
	mybucket = conn.get_bucket('flaskgame')
	myKey = mybucket.get_key("maps/" + UserID + "terrainMap.json")
	worldData = yaml.load(myKey.get_contents_as_string())
	for item in worldData.keys():
		t_type = worldData[item]['Terrain Code']
		worldData[item].update(getTerrainDetails(t_type))
	return worldData


def getAreaInfoFromMap(charData):
	'''
	takes charData as DICT
	returns mapData as DICT
	'''
	charLoc = charData['location']
	UserID = charData['id']
	x = int(charLoc.split(":")[0])
	y = int(charLoc.split(":")[1])
	mybucket = conn.get_bucket('flaskgame')
	myKey = mybucket.get_key("maps/" + UserID + "terrainMap.json")
	data = yaml.load(myKey.get_contents_as_string())
	#getting world dimensions so that we can round if the character ges over
	worldDim = {
		"x":[min([int(x1.split(":")[0]) for x1 in data.keys()]),
		max([int(x1.split(":")[0]) for x1 in data.keys()])],
		"y":[min([int(y1.split(":")[1]) for y1 in data.keys()]),
		max([int(y1.split(":")[1]) for y1 in data.keys()])]
		}
	
	#rounding the values so that if it is less than the min, swap it with the max. And vice versa.
	NArea = [x,y-1]
	if NArea[1] < worldDim['y'][0]:
		NArea = [x,worldDim['y'][1]]
	EArea = [x+1,y]
	#if the x in the east is greater than the max x, change max x to min x.
	if EArea[0] > worldDim['x'][1]:
		NArea = [worldDim['x'][0],y]
	SArea = [x,y+1]
	if SArea[1] > worldDim['y'][1]:
		SArea = [x,worldDim['y'][0]]
	WArea = [x-1,y]
	if WArea[0] < worldDim['x'][0]:
		WArea = [worldDim['x'][1],y]
	area = [x,y]

	mapData = { "area":data[str(x)+":"+str(y)],
		"NArea":data[str(NArea[0])+":"+str(NArea[1])],
		"EArea":data[str(EArea[0])+":"+str(EArea[1])],
		"SArea":data[str(SArea[0])+":"+str(SArea[1])],
		"WArea":data[str(WArea[0])+":"+str(WArea[1])] }
	#adding terrain details foreach terrain code
	for item in mapData.keys():
		t_type = mapData[item]['Terrain Code']
		mapData[item].update(getTerrainDetails(t_type))
	#Adding monsters
	mapData['monsters'] = addMonsters(mapData)
	return mapData



def addMonsters(mapData):
    '''
    takes mapData as DICT
    returns monsters as DICT
    example:
    mapData['monsters'] = addMonsters(mapData) 
    '''
    individualVariables = ["name","move","size","color"]
    monsters = {}
    beastiary = getBeastiary()
    if mapData['area']['Danger Level'] < 1:
        #if the danger level is less than 0, don't load any monsters.
        monsters['message'] = 'The area looks calm and peacefull.'
        return monsters
    creature = beastiary[mapData['area']['creatures']]
    metaVariables = [k for k in list(creature.keys()) if k not in individualVariables]
    d10 = np.random.random(1)[0]
    if d10 > mapData['area']['Creature Probability']:
        #even if there is a danger in the area, that doesn't mean a monster will show.
        monsters['message'] = 'The area looks calm and peacefull.'
        return monsters
    if d10 <= mapData['area']['Creature Probability']:
        monsters['message'] = 'there is a ' + creature['name'] + ' in the area.'
        if creature['group min'] == creature['group max']:
            #if the min and max are the same, the min number will be drawn.
            nMonsters = creature['group min']
        else:
            #otherwise, the number of monsters is a random number between the min and the max.
            nMonsters = np.random.randint(creature['group min'],creature['group max'])
    #metadata about the monsters is useful when they are rendered
    monsters['meta'] = dict([i for i in beastiary[mapData['area']['creatures']].items() if i[0] in metaVariables])
    #a list of monsters is added that is nMonsters long
    m = []
    for i in range(nMonsters):
        mi = dict([i for i in beastiary[mapData['area']['creatures']].items() if i[0] in individualVariables])
        if (('health' in monsters['meta'].keys()) & ('healthMaxVariance' in monsters['meta'].keys())):
            mi['health'] = monsters['meta']['health'] + np.random.randint(0, monsters['meta']['healthMaxVariance'])
        m.append(mi) 
    monsters['m'] = m
    return monsters

def getBeastiary():
	mybucket = conn.get_bucket('flaskgame')
	myKey = mybucket.get_key('terrain/beastiary')
	beastiary = yaml.load(myKey.get_contents_as_string())
	return beastiary

def getRaceData():
	mybucket = conn.get_bucket('flaskgame')
	myKey = mybucket.get_key('chars/raceData.json')
	raceData = yaml.load(myKey.get_contents_as_string())	
	return raceData

def getClassData():
	mybucket = conn.get_bucket('flaskgame')
	myKey = mybucket.get_key('chars/classData.json')
	classData = yaml.load(myKey.get_contents_as_string())	
	return classData


def getTerrainDetails(t_type):
	mybucket = conn.get_bucket('flaskgame')
	myKey = mybucket.get_key('terrain/'+t_type)
	t_details = yaml.load(myKey.get_contents_as_string())	
	return t_details

def getCharData(user,token="notoken"):
	'''
	bto.getCharData(id=charID,token=charToken)
	TODO use the token to authenticate the user
	'''
	mybucket = conn.get_bucket('flaskgame')
	myKey = mybucket.get_key("chars/" + user + "charData.json")
	data = yaml.load(myKey.get_contents_as_string())
	if 'account info' in data.keys():
		data.pop('account info') #removed info pertaining to the account for security
	return data

def saveCharData(cData):
	charData = yaml.load(cData)
	charID = charData["id"]
	mybucket = conn.get_bucket('flaskgame')
	myKey = mybucket.get_key("chars/" + charID + "charData.json")
	oldData = yaml.load(myKey.get_contents_as_string())
	if 'account info' in oldData.keys():
		accountData = oldData.pop('account info') #removed info pertaining to the account for security
		charData['account info'] = accountData
	myKey.set_contents_from_string(str(charData))
	return charData


