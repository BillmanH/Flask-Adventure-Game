from boto.s3.connection import S3Connection
import boto
import yaml

conn = S3Connection()
mybucket = conn.get_bucket('flaskgame')

def checkIfAccountExists(key="william.jeffrey.harding@gmail.comcharData.json"):
	folder = 'chars'
	objs = list(mybucket.objects.filter(Prefix=folder + key))
	if len(objs) > 0 and objs[0].key == key:
		return True
	return False

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

	
