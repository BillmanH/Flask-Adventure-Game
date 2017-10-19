from boto.s3.connection import S3Connection
import boto
import yaml

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
	charData['account info']['email'] = formData['email']
	charData['account info']['password'] = "password"
	charData['id'] = charData[charData['account info']
	if(checkIfAccountExists(charData['id'])):
		characterAlreadyExists()
	else:
		myKey = mybucket.get_key("chars/" + charData['id'])
		myKey.set_contents_from_string(str(charData))

def sendNewCharacterInfo(charData):
	pass

def characterAlreadyExists(charData):
	pass



	
