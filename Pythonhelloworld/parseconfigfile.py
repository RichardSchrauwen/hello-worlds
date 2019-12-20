import configparser
config = configparser.ConfigParser()
config.read('example.ini')
print(f"Config section found: {config.sections()}")
print(config['DEFAULT']['path'])
print(config['mp3count']['path'])
