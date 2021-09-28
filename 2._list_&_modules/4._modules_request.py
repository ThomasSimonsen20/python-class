import requests

r = requests.get('https://python-elective-kea.github.io/fall2021/ses4.html')
#print(r)

f = open('python-elective.html', 'w')
#//laver en fil?
f.write(r.text)