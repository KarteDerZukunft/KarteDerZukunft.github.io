import json

with open('./Data/kdz.json') as json_file:

	data = json.load(json_file)

	for i, j in data.items():

		if (type(j) is list):

			for k in j:

				if 'qr_target' in k and len(k['qr_target']) != 0:
					print(k['qr_target'])

		elif (type(j) is dict):

			continue

		else:

			continue
