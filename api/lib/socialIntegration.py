import requests
import json

class UserInfo(object):
    def __init__(self, name, email, picture, login):
        self.name = name
        self.email = email
        self.picture = picture
        self.login = login

def FacebookTokenValidate(token):
    #https://developers.facebook.com/docs/facebook-login/manually-build-a-login-flow#checktoken
    data = None
    endpoint = "https://graph.facebook.com/me?fields=name,email,id,picture.width(100).height(100)&access_token=" + token
    r = requests.get(endopoint)
    if r.status_code == 200:
        obj = json.loads(r.content)
        data = UserInfo(obj["name"], obj["email"], obj["picture"]["data"]["url"], obj["id"])
    if data is None:
        raise Exception("Unable to authenticate")
    return Data
    
def GoogleTokenValidate(token):
    #https://oauth2.googleapis.com/tokeninfo?id_token=XYZ123
    data = None
    endpoint = "https://oauth2.googleapis.com/tokeninfo?id_token=" + token
    r = requests.get(endopoint)
    if r.status_code == 200:
        obj = json.loads(r.content)
        data = UserInfo(obj["name"], obj["email"], obj["picture"], obj["email"])
    if data is None:
        raise Exception("Unable to authenticate")
    return Data
