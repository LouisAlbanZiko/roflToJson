import sys, json	

if __name__ == '__main__':

	if len(sys.argv) != 2:
		print("Usage: python roflToJson.py <path_to_rofl>")
	else:
		file_path = sys.argv[1]
		with open(file_path, 'rb') as file:
	
			magicNumber = file.read(6)

			signature = file.read(256)

			lengths_header = file.read(2)
			lengths_file = file.read(4)
			lengths_metadataOffset = file.read(4)
			lengths_metadata = file.read(4)
			lengths_payloadHeaderOffset = file.read(4)
			lengths_payloadHeader = file.read(4)
			lengths_payloadOffset = file.read(4)

			metadata = file.read(int.from_bytes(lengths_metadata, "little"))

			json_data = json.loads(metadata)
			json_data['statsJson'] = json.loads(json_data['statsJson'])
		
		file_path_out = file_path.split(".")[0]+".json"
		with open(file_path_out, 'w') as file:
			file.write(json.dumps(json_data))
