import json
import os
from pprint import pprint
path, dirs, files = next(os.walk("/home/navaneeth/work/snapuskin/images/ISIC-images/testset"))
file_count = int(len(files)/2)
for i in range(file_count):
    print(str(i))
    with open('/home/navaneeth/work/snapuskin/images/ISIC-images/testset/ISIC_000000'+str(i)+'.json') as json_file:
        data = json.load(json_file)
    name = str(data['meta']['clinical']['diagnosis'])
    os.rename('/home/navaneeth/work/snapuskin/images/ISIC-images/testset/ISIC_000000'+str(i)'.jpg','/home/navaneeth/work/snapuskin/images/ISIC-images/'+str(name)+str(i)+'.jpg')
