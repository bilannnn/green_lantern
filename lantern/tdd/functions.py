import requests

def fun():
    #return 1
    return 1



def return_boolean_value(n):
    if n %2 == 0:
        return True
    return False

def call_to_different_service():
    resp = requests.get("https://www.instagram.com/?hl=ru")
    return resp

def parse_response():
    data = call_to_different_service()
    if data:
        return data