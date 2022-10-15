import webbrowser
import os

flag = 0
data = {}
while flag == 0:
    scene = input('Номер сцены')
    url = input('URL')
    data.update({scene: url})
    x = input('Ещё?')
    if x == 'y':
        continue
    else:
        print(data)
        flag = 1
while True:
    os.system("taskkill /IM chrome.exe /f")
    request = input('Номер сцены?')
    if request == 'stop':
        break
    try:
        webbrowser.open(data.get(request))
    except:
        continue

