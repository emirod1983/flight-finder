import json

def get_json_dict(byte_source):
    data = byte_source.read() # Decode from byte format
    json_response = data.decode('utf-8') # Turns bytes into json
    return json.loads(json_response) # Turns json into a dictionary

def dump_to_file(file_name, file_contents):
    # Run prettier on the file for readable format (Shift + Alt + F on VS Code)
    with open(file_name, 'w', encoding='utf-8') as output_file:
        json.dump(file_contents, output_file)

def open_from_file(file_name):
    with open(file_name) as json_file:
        data = json.load(json_file)
    return data