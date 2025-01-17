import os

# input_path = 'data/2018-11-13 10-02-50-CAM.log'
# images = sorted(os.listdir('data/2018-11-14_avdelning_Ribbfors_1-3'))
input_path = 'data/example/2018-11-13 10-02-50-CAM.log'
images = sorted(os.listdir('data/example'))
images = [im for im in images if im.endswith('.JPG')]

with open(input_path, 'r') as f:
    data = f.readlines()

longitudes = []
latitudes = []
alts = []
for d in data[1:]:
    d = d.split(',')
    longitudes.append(float(d[5]))
    latitudes.append(float(d[4]))
    alts.append(float(d[6]))
    
longitudes = tuple(longitudes)
latitudes = tuple(latitudes)
alts = tuple(alts)
new_data = tuple(zip(images, longitudes, latitudes, alts))

with open('geo.txt', 'w', encoding='UTF-8') as f:
    f.write('EPSG:4326')
    f.write('\n')
    for d in new_data:
        for i in d:
            f.write(str(i))
            f.write(' ')
        f.write('\n')