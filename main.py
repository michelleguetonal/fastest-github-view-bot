from wrapper import *
import threading


pyreq = HTTP(); req = 0

def __get__req():
 try:
    global req
    lol = pyreq.get_req(
        'camo.githubusercontent.com', 
        '354df9d1428f0ea12987299eb2bb1b9f1830c22ecb276fb4cf42fd43477d5fd4/68747470733a2f2f677076632e6172747572696f2e6465762f616363757361626c65'
    )
    if 'HTTP/1.1 200 OK' in lol.decode():
        req +=1; print(f'view sent | sent: {req}')
 except Exception:
    pass


while True:
 threading.Thread(target=__get__req).start()