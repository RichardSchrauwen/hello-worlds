import configparser
config = configparser.ConfigParser()
config['DEFAULT'] = {'path': '/temp',
                     'user': 'admin',
                     'level': '1'}

config['mp3count'] = {}
config['mp3count']['path'] = 'C:/users/$USER/Music'
config['mp3count']['mediatypes'] = 'mp3,mp4,jpg,mpeg'
config['mp3count']['searchString'] = "Gork"

config['filetypecount'] = {}
config['filetypecount']['path'] = 'C:/users/$USER/Documents/GitHub'
config['filetypecount']['searchExtension'] = ".py"
config['filetypecount']['searchString'] = "hello"

with open('example.ini', 'w') as configfile:
    config.write(configfile)
