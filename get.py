import json
import requests
import pandas as pd

class Pinterest:
    def __init__(self, token):
        self.token = token

    def getPinFromBoard(self, boardName):
        api = 'https://api.pinterest.com/v1/boards/{boardName}/pins/?access_token={access_token}&fields=id%2Clink%2Cnote%2Curl%2Cattribution%2Cmetadata%2Cboard%2Ccolor%2Ccounts%2Ccreated_at%2Ccreator%2Cimage%2Cmedia%2Coriginal_link'
        url = api.format(boardName=boardName, access_token=self.token)
        r = requests.get(url)
        data = json.loads(r.text)
        print(data)

    def __del__(self):
        print('取得が完了しました！')


token = 'AqID5E77gHhK_n5AhoLIZ3O-qoNpFVzVvmGoI_ZFToUf6uBS_gjPADAAAbm2RU6NWvOAW2wAAAAA'
boardName = 'hisjapan/his_blue'
pinterest = Pinterest(token)
pinterest.getPinFromBoard(boardName)