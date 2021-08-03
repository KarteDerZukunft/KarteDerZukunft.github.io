import json
import os

os.system('rm -rf ./spd/*')

with open('./Data/kdz.json') as json_file:

    data = json.load(json_file)

    for i, j in data.items():

        if (type(j) is list):

            for k in j:

                if 'qr_target' in k and len(k['qr_target']) != 0:

                    fileName = './spd/' + \
                        k['qr_target'].replace(
                            'https://www.kartederzukunft.de/spd/', '') + '.html'

                    if (i == "places"):

                        txt = '<script>window.location.replace(\"' \
                            + 'kiezprojektSeite.html?kpid=' + str(k['id']) \
                            + '\");</script>'

                    elif (i == "sections"):

                        txt = '<script>window.location.replace(\"' \
                            + 'abschnittsSeite.html?sid=' + str(k['id']) \
                            + '\");</script>'

                    os.system('echo \'' + txt + '\' > ' + fileName)

        elif (type(j) is dict):

            continue

        else:

            continue
