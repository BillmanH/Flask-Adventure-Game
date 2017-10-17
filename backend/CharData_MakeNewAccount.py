from boto.s3.connection import S3Connection
import boto
import yaml

conn = S3Connection()

def checkIfAccountExists():
	return True

def saveNewCharacterData(formData):
	charData = formData
	charData['account info']['email'] = formData['email']
	
