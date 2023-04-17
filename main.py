from config import api_host, headers
from crosscutting.constants import filename, HTTP_POST
from flask import Flask, render_template
from skyscanner_service.payload_builder import get_payload
import http.client, json

# run app with: flask --app main run --debug

app = Flask(__name__)

@app.route("/get/")
def api_call():
    # Get response
    conn = http.client.HTTPSConnection(api_host)
    conn.request(HTTP_POST, "/v3e/flights/live/search/synced", get_payload(), headers)
    response = conn.getresponse()

    # Process response
    data = response.read() # Decode from byte format
    json_response = data.decode('utf-8') # Turns bytes into json
    json_dictionary = json.loads(json_response) # Turns json into a dictionary

    # Dump response into a file
    with open(filename, 'w', encoding='utf-8') as output_file:
        json.dump(json_dictionary, output_file) # Once the file is created, run prettier on it -> Shift + Alt + F

    return render_template('main.html', input="Fetch successful!")
