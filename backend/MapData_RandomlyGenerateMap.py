import pandas as pd
import numpy as np
import yaml
from boto.s3.connection import S3Connection

try:
    conn = S3Connection()
except:
    #running visual studio on my desktop, keys are set up differently there. 
    myKeys = yaml.load(open(r'C:\Users\willi\OneDrive\Documents\keyfile.txt', 'r'))
    AWSSecretKey=myKeys['AWSSecretKey']
    AWSAccessKeyId=myKeys['AWSAccessKeyId']
    conn = S3Connection(AWSAccessKeyId, AWSSecretKey)

params = {"worldSize":10}

def get_terrain_detail():

	mybucket = conn.get_bucket('flaskgame')
	myKey = mybucket.get_key('terrain/terrain_details')
	t_detail = yaml.load(myKey.get_contents_as_string())
	return t_detail

t_detail = get_terrain_detail()
terrain_types = [t for t in list(t_detail.keys()) if t_detail[t]['Type']=='normal']

def get_random_chord(df):
	x = np.random.choice(df[df.isnull().any(axis=0)].index.tolist(),1)[0]
	y = np.random.choice(df[df.isnull().any(axis=1)].index.tolist(),1)[0]
	coord = [x,y]
	return coord

def count_remaining_na(df):
	num = sum([df[[n]].isnull().sum().tolist()[0] for n in df.columns])
	return num

def listBlankSpaces(df):
	places = df.T.to_dict()
	blankPlaces = []
	for x in places.keys():
		for y in places[x].keys():
			if pd.isnull(places[x][y]):
			    #print(places[x][y],"is not a string")
			    blankPlaces.append([x,y])
	return blankPlaces

def place_terrain(coord):
	t_type = np.random.choice(terrain_types,1)[0]
	df.loc[coord[0],coord[1]] = t_type
	return df

def getMostCommonTerrain(coord):
	neighbors = []
	#one for each neighboring spot
	try:
		neighbors.append(df.loc[coord[0]+1,coord[1]+1])
	except:
		pass
	try:    
		neighbors.append(df.loc[coord[0],coord[1]+1])
	except:
		pass
	try:
		neighbors.append(df.loc[coord[0]-1,coord[1]+1])
	except:
		pass
	try:
		neighbors.append(df.loc[coord[0]+1,coord[1]])
	except:
		pass
	try:
		neighbors.append(df.loc[coord[0]-1,coord[1]])
	except:
		pass
	try:
		neighbors.append(df.loc[coord[0]+1,coord[1]-1])
	except:
		pass
	try:
		neighbors.append(df.loc[coord[0],coord[1]-1])
	except:
		pass
	try:
		neighbors.append(df.loc[coord[0]-1,coord[1]-1])
	except:
		pass
	#find the terrainthat is most abundant
	try:
		neighbors = [neigh for neigh in neighbors if neigh in terrain_types]  #removing nan and things that aren't terrain types
		mostCommon = neighbors[np.argmax(np.unique(neighbors,return_counts=True))]
		if np.argmax(np.unique(neighbors,return_counts=True))>1:
			t = mostCommon
		else:
			t = np.random.choice(terrain_types,1)[0]
	except:
		t = np.random.choice(terrain_types,1)[0]
	return t

def place_best_terrain(coord,df,dfMeta):
	t = getMostCommonTerrain(coord)
	if t in list(dfMeta.keys()):
		dfMeta[t] = dfMeta[t] + 1
	else:
		dfMeta[t] = 1
	df.loc[coord[0],coord[1]] = t
	return df,dfMeta

def place_specific_terrain(t,coord):
	df.loc[coord[0],coord[1]] = t
	return df

def get_current_terrain(coord):
	ter = df.ix[coord[0],coord[1]]
	return ter


def find_blank_neighbor(coord):
	taken = [[-1,-1]]
	while len(taken)<8:
		if check_if_coord_is_na(coord):
			return coord
		else:
			coord,taken = find_neighboring_spot(coord,taken)
	return [[-1,-1]]
	pass

def MakeMap(saveonly=False):
	grid = [params['worldSize'],params['worldSize']]
	df = pd.DataFrame(columns=range(grid[1]),index=range(grid[0]))
	dfMeta = {}
	while count_remaining_na(df) > 0:
		#print(count_remaining_na(),coord)
		blanks = listBlankSpaces(df)
		coord = blanks[np.random.choice(len(blanks))]
		df,dfMeta = place_best_terrain(coord,df,dfMeta)
	if saveonly:
		mapData = saveWorldMap(df)	
		return mapData,dfMeta
	else:#keeping the DF output for further experimentation
		return df,dfMeta


def saveWorldMap(df):
	worldMap = {}
	#make a json file for exporting
	for x in range(params['worldSize']):
		for y in range(params['worldSize']):
			worldMap[str(x)+":"+str(y)] = {
				"Terrain Code":df.loc[y,x],
                                      "y":y,"x":x
				}
	return worldMap


