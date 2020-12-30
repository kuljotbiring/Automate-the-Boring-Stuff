import requests

res = requests.get('http://automatetheboringstuff.com/files/rj.txt')

# check if bad download. if it fails then program will halt, otherwise do nothing
res.raise_for_status()

# make a new file to write in binary
playFile = open('RomeoAndJuiliet.txt', 'wb')


for chunk in res.iter_content(100000):
    playFile.write(chunk)

playFile.close()