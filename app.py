import json
import requests
import pandas as pd

class GetPinterest:
    def __init__(self, token):
        self.token = token

    def getPinFromBoard(self, boardName):
        api = 'https://api.pinterest.com/v1/boards/{boardName}/pins/?access_token={access_token}&fields=id%2Clink%2Cnote%2Curl%2Cattribution%2Cmetadata%2Cboard%2Ccolor%2Ccounts%2Ccreated_at%2Ccreator%2Cimage%2Cmedia%2Coriginal_link'
        url = api.format(boardName=boardName, access_token=self.token)
        r = requests.get(url)
        data = json.loads(r.text)
        print(data)

    def getPinData(self, pinId):
        api = 'https://api.pinterest.com/v1/pins/{pinId}/?access_token={access_token}'
        url = api.format(pinId=pinId, access_token=self.token)
        r = requests.get(url)
        data = json.loads(r.text)
        print(data)

    def getUserData(self, username):
        api = 'https://api.pinterest.com/v1/users/{username}/?access_token={access_token}'
        url = api.format(username=username, access_token=self.token)
        r = requests.get(url)
        data = json.loads(r.text)
        print(data)

    def getBoardInfo(self, boardName):
        api = 'https://api.pinterest.com/v1/boards/{boardName}/?access_token={access_token}&fields=id%2Cname%2Curl%2Ccounts%2Ccreated_at%2Ccreator%2Cdescription%2Cimage%2Cprivacy%2Creason'
        url = api.format(boardName=boardName, access_token=self.token)
        r = requests.get(url)
        data = json.loads(r.text)
        print(data)

    def getMyAccount(self):
        api = 'https://api.pinterest.com/v1/me/?access_token={access_token}&fields=first_name%2Cid%2Clast_name%2Curl'
        url = api.format(access_token=self.token)
        r = requests.get(url)
        data = json.loads(r.text)
        print(data)

    def __del__(self):
        print('取得が完了しました！')

class CreatePinterest:
    def __init__(self, token):
        self.token = token

    def createBoard(self, boardName, description):
        api = 'https://api.pinterest.com/v1/boards/?access_token={access_token}&fields=id%2Cname'
        url = api.format(access_token=self.token)
        param = {
            'name': boardName,
            'description': description
        }
        r = requests.post(url,json=param)
        print(r.status_code)

    def createPin(self, boardName, description, image_url):
        api = 'https://api.pinterest.com/v1/pins/?access_token={access_token}'
        url = api.format(access_token=self.token)
        param = {
            'board': boardName,
            'note': description,
            'image_url': image_url
        }
        r = requests.post(url, json=param)
        print(r.status_code)

    def __del__(self):
        print('作成が完了しました！')