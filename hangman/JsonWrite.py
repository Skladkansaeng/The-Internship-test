import json

data = {}
data['word'] = []

animal = ['razor','shampoo','soap','toothbrush','towel']
hint = ['Use to eliminate excess in the face.','Use to clean hair.','Use to clean the body.','Use to clean the mouth.','Used to make the body dry.']
for i in range(len(animal)):
    data['word'].append({
        'catalog' : 'sport',
        'hint' : hint[i],
        'words' : animal[i]
    })
with open('Catalog_3.json', 'w') as outfile:  
    json.dump(data, outfile)
