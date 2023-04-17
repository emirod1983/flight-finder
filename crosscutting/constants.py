import datetime

# HTTP Verbs
HTTP_GET = "GET"
HTTP_POST = "POST"

# Name of the file to store data dumps (for testing purposes)
timestr = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
filename = 'dumps/api_response_'+timestr+'.json'
