import json
import os
from pprint import pprint
path, dirs, files = next(os.walk("/home/navaneeth/work/snapuskin/mainset"))
file_count = int(len(files)/2)
for i in range(file_count):
    print(str(i))
    with open('/home/navaneeth/work/snapuskin/mainset/ISIC_0000'+str('%03d' % i)+'.json') as json_file:
        data = json.load(json_file)
    name = str(data['meta']['clinical']['diagnosis'])
    os.rename('/home/navaneeth/work/snapuskin/mainset/ISIC_0000'+str('%03d' % i)+'.jpg','/home/navaneeth/work/snapuskin/renamed/'+str(name)+str(i)+'.jpg')
