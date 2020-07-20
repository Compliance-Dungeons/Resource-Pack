import os
import json
import math

texturesPath = '../Block Textures/'

count = 0
count1 = 0

with open('block_textures.json') as json_file:
  textures = json.load(json_file)
  for filename,copies in textures.items():
    if os.path.isfile(texturesPath + filename):
      count1 += 1
      print(filename + ' | is present')
    if not os.path.isfile(texturesPath + filename):
      count += 1

  total = len(textures)
  print('----------------------------------------')
  print('  Total present textures: ' + str(count1))
  print('  Percentage complete:    ' + str(math.floor((total - count) * 100 / total)) + '%')
  print('----------------------------------------')