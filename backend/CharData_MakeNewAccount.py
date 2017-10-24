from boto.s3.connection import S3Connection
from boto.s3.key import Key
import boto
import yaml

import MapData_RandomlyGenerateMap as m

conn = S3Connection()
mybucket = conn.get_bucket('flaskgame')


def checkIfAccountExists(id="william.jeffrey.harding@gmail.comcharData.json"):
	myKey = mybucket.get_key("chars/" + id)
	if myKey==None:
		return False
	else:
		return True


def saveNewCharacterData(formData):
	charData = formData
	charData['account info'] = {}
	charData['account info']['email'] = formData['email']
	charData['account info']['password'] = "password"
	charData['id'] = charData['account info']['email']
	charData['account info']['token'] = formData['token']
	if checkIfAccountExists(charData['id']):
		characterAlreadyExists()
	else:
		myKey = Key(mybucket)
		myKey.key = "chars/" + charData['id'] + 'charData.json'
		myKey.set_contents_from_string(str(charData))
		mapData,meta = m.MakeMap(saveonly=True)
		myKey.key = "maps/" + charData['id'] + "terrainMap.json"
		myKey.set_contents_from_string(str(mapData))
		return meta

def sendNewCharacterInfo(charData):
	pass

def characterAlreadyExists(charData):
	pass



	
