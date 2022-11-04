from wrapper import *; import threading; import user_agent

req = 0

def __get__req():
 try:
    global req; pyreq = Client('camo.githubusercontent.com')
    lol = pyreq.get(
        resource='354df9d1428f0ea12987299eb2bb1b9f1830c22ecb276fb4cf42fd43477d5fd4/68747470733a2f2f677076632e6172747572696f2e6465762f616363757361626c65',
        headers={
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'User-Agent': user_agent.generate_user_agent()
        }
    )

    ok = lol.decode() # ; print(ok)
    if 'Profile views' in ok:
        total = ok.split('role="img" aria-label="Profile views: ')[1].split('"')[0]
        req +=1; print(f"views sent | sent: {req} | total views: {total}")
    else:
        print('view failed')
 except Exception:
    pass

while True:
 threading.Thread(target=__get__req).start()
