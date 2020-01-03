import configparser
config = configparser.ConfigParser()
config.read('example.ini')
print(f"Config section(s) found: {config.sections()}")
print(config['DEFAULT']['path'])
print(config['mp3count']['path'])

for row in config.sections():
    print(row)
    for key in config[row]:
        print(f"   {key} = {config[row][key]}")
