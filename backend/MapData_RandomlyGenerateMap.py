import pandas as pd
import numpy as np

params = {"worldSize":100}

def get_random_chord(df):
	x = np.random.choice(df[df.isnull().any(axis=0)].index.tolist(),1)[0]
	y = np.random.choice(df[df.isnull().any(axis=1)].index.tolist(),1)[0]
	coord = [x,y]
	return coord

def count_remaining_na():
	num = sum([df[[n]].isnull().sum().tolist()[0] for n in df.columns])
	return num

def listBlankSpaces():
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

def place_best_terrain(coord):
	t = getMostCommonTerrain(coord)
	if t in list(dfMeta.keys()):
		dfMeta[t] = dfMeta[t] + 1
	else:
		dfMeta[t] = 1
	df.loc[coord[0],coord[1]] = t
	return df

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

def MakeMap():
	grid = [10,10]
	df = pd.DataFrame(columns=range(grid[1]),index=range(grid[0]))
	dfMeta = {}
	while count_remaining_na() > 0:
		#print(count_remaining_na(),coord)
		blanks = listBlankSpaces()
		coord = blanks[np.random.choice(len(blanks))]
		place_best_terrain(coord)
	return df,dfMeta

	
