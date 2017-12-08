from boto.s3.connection import S3Connection
import boto
import yaml

#conn = boto.connect_s3()

conn = S3Connection()

def getAreaInfoFromMap(charData):
    charLoc = charData['location']
    UserID = charData['id']
    x = int(charLoc.split(":")[0])
    y = int(charLoc.split(":")[1])
    mybucket = conn.get_bucket('flaskgame')
    myKey = mybucket.get_key("maps/" + UserID + "terrainMap.json")
    data = yaml.load(myKey.get_contents_as_string())
    mapData = { "area":data[str(x)+":"+str(y)],
                "NArea":data[str(x)+":"+str(y-1)],
                "EArea":data[str(x+1)+":"+str(y)],
                "SArea":data[str(x)+":"+str(y+1)],
                "WArea":data[str(x-1)+":"+str(y)] }
    for item in mapData.keys():
      t_type = mapData[item]['Terrain Code']
      mapData[item].update(getTerrainDetails(t_type))
    return mapData

def createCharacter(formData):
	return "pass"

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
	#bto.getCharData(id=charID,token=charToken)
	#TODO use the token to authenticate the user
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

# This function returns a default blog article, it is set to return my first article in the event of an error.
def getBlogArticle(article):
        mybucket = conn.get_bucket('flaskgame')
        if article==None:
            defaultKey = mybucket.get_key("blog/" + "d3_backend.json")
            myKey = mybucket.get_key(defaultKey)
            content = yaml.load(myKey.get_contents_as_string())
            return content
        potentialKey = "blog/" + article + ".json"
        if potentialKey in [item.name for item in mybucket.list() if "blog/" in item.name]:
                defaultKey = mybucket.get_key("blog/" + article + ".json")
                content = yaml.load(defaultKey.get_contents_as_string())
        else:
                defaultKey = mybucket.get_key("blog/" + "d3_backend.json")
                myKey = mybucket.get_key(defaultKey)
                content = yaml.load(myKey.get_contents_as_string())
        return content

def getContentList():
	mybucket = conn.get_bucket('flaskgame')
	myKey = mybucket.get_key('blog/contentlist')
	content = yaml.load(myKey.get_contents_as_string())
	return content


