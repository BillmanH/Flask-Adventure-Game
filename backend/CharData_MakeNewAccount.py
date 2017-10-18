from boto.s3.connection import S3Connection
import boto
import yaml

conn = S3Connection()
mybucket = conn.get_bucket('flaskgame')

def checkIfAccountExists(mybucket,key="william.jeffrey.harding@gmail.comcharData.json"):
	objs = list(mybucket.objects.filter(Prefix=key))
	if len(objs) > 0 and objs[0].key == key:
		return True
	return False

def saveNewCharacterData(formData):
	charData = formData
	charData['account info']['email'] = formData['email']
	charData['account info']['password'] = "password"

	
