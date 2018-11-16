from app import GetPinterest, CreatePinterest

token = 'AqID5E77gHhK_n5AhoLIZ3O-qoNpFVzVvmGoI_ZFToUf6uBS_gjPADAAAbm2RU6NWvOAW2wAAAAA'

g = GetPinterest(token)
c = CreatePinterest(token)

# username/boardName
boardName = 'put in board name'
g.getPinFromBoard(boardName)
g.getBoardInfo(boardName)

# pin id is tail of URL
pinId = 'put in pin id'
g.getPinData(pinId)

# account name
username = 'put in username'
g.getUserData(username)

# only token
g.getMyAccount()

# with description
boardName = 'put in board name'
description = 'こんな所に行ってみたい！'
c.createBoard(boardName, description)