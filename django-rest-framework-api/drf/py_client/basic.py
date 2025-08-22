import requests 

#endpoint = "https://www.httpbin.org"
# endpoint = "https://www.httpbin.org/anything"
endpoint = "http://localhost:8000/api/"  #" http://127.0.0.1:8000/"

get_response = requests.get(endpoint, params={"abc":123}) # Application programming interface HTTP request
#phone -> camera

print(get_response.text) #print raw text response


# HTTP Request -> HTML response
# REST API HTTP Request -> JSON(xml) response 

# Javascript Object Notation ~ Python Dict
print(get_response.json())
#print(get_response.status_code)