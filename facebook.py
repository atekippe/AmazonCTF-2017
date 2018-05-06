import requests
import re

url = 'http://52.10.160.233:4080/user/'

i = 1998
patterns = re.compile('restricted')

while i < 2500:
    user_id = str(i)
    r = requests.get(url + user_id)
    regex = re.search(patterns, r.text)
    print(regex)
    i += 1

    if regex is None:
        user = str(i)
        r = requests.get(url + user)
        print(r.text)
    else:
        print(user_id)
        continue

