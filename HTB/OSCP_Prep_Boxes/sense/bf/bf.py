import requests
import re
import urllib3
from requests.packages.urllib3.exceptions import InsecureRequestWarning
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


URL = 'https://10.10.10.60/index.php'

# csrf capture
re_csrf = 'csrfMagicToken = "(.*?)"'

# start a requests session
s = requests.session()

# capture the csrf token
r = s.get(URL, verify=False)
print(r.status_code)
csrf = re.findall(re_csrf, r.text)[0]
print(csrf)

# perform the login
headers = {'__csrf_magic':csrf,'usernamefld':'rohit','passwordfld':'pfsense','login':'login'}
login_r = s.post(URL, data=headers, verify=False)
print(login_r.status_code)
if 'Dashboard' in login_r.text:
    print("Valid Login")
else:
    print("Login Failed")
