# Flask-Game
One of my private dev goals for 2017 is to build an entire RPG game. To make it an especailly interesting challenge, ALL of the code was either built out of a Jupyter Notebook or VIM. From scratch, line by line.

The main theme is to be extensible. All of the code is so compartmentalized that a single person can manage the whole system. Simply by adding attributes to objects, the world becomes more rich. By adding front end code, objects react to the properties of other objects in a way that is simple to maintain. 

* Built using:
 * EC2 for server and data processing
 * S3 for storing data
 * Apache for serving
 * Flask for backend processing
 * D3.js for frontend
 * Jupyter Notebooks for design and development (and documentation) as well as managing the data.
 
The creative part of the game is in designing attributes and objects within the game. I've designed this process to be managed in a spreadsheet:
 * Parameters for terrain, terrain textures, monsters, character attributes and all other objects is stored in S3
 * See the `notebooks` folder for more documentation on that process. 

The game is currently located [here](http://williamjeffreyharding.com/game).

The __Front End__ is managed in Flask templates. This allows me to limit the amount of JavaScript that needs to be deployed. If an object requires some JS code in order to render or function, that script file is included in the template. You can see this in the `core view.html` of the template. 

## Terrain Parameters:
Details of the terrain are stored separately to save space. This includes both the terrain texture objects AND the monsters. This way only the data for the current area given to the user. This keeps the application light. 
`getTerrainDetails(mapData['area']['Terrain Code'])`

each tile on the world map has it's own data:
### Example charData:
{'accountInfo': {'email': 'william.jeffrey.harding@gmail.com'},
 'attributes': {},
 'background': {},
 'class': 'ranger',
 'health': 8,
 'id': 'william.jeffrey.harding@gmail.com',
 'inventory': {'bow': {'name': 'bow'}},
 'location': '5:5',
 'name': 'William',
 'race': 'Human',
 'size': 10,
 'speed': 10,
 'starting weapon': 'bow'}
 
### Example terrData:
[{'ds': {'Code': 'ds,.',
  'Creature Probability': 0.1,
  'Danger Level': 1,
  'Description': 'a barren desert',
  'Detailed Description': None,
  'Terrain Textures': "[         {'name':'Sand',         'abundance':300,         'density':5} ]",
  'Treasure Level': 1,
  'Type': 'normal',
  'Type Name': 'desert',
  'common': True,
  'creatures': 'scorpion'},
 'fo': {'Code': 'fo',
  'Creature Probability': 0.5,
  'Danger Level': 4,
  'Description': 'a quiet deciduous forest',
  'Detailed Description': None,
  'Terrain Textures': "[         {'name':'Tree',         'density':6,         'abundance':10},         {'name':'Bush',         'abundance':5,         'density':5},        {'name':'Lake',         'abundance':3,         'density':2} ]",
  'Treasure Level': 3,
  'Type': 'normal',
  'Type Name': 'forest',
  'common': True,
  'creatures': 'goblin'}]
  
### Example mapData:
{'0:0': {'Terrain Code': 'ds', 'x': 0, 'y': 0},
 '0:1': {'Terrain Code': 'sa', 'x': 0, 'y': 1},
 '0:2': {'Terrain Code': 'sa', 'x': 0, 'y': 2},
 '0:3': {'Terrain Code': 'ic', 'x': 0, 'y': 3}
 }


## global variables used in game
* **charData** - character related information - minus account information
* **mapData** - Map information
* contains all terrain details from the local area, plus the terrain info for the four surrounding areas. 
* **terrData** - Local Terrain informaiton, including terrain textures and interactions
* **monsterData** - stats for monsters, how they are rendered and how they behave

