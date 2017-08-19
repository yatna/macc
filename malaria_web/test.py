import urllib.request, json 

from profiles.models import Pcuser
with urllib.request.urlopen("https://gist.githubusercontent.com/yatna/0e6b1ce2435de3e10a779aad40b4375b/raw/c49159dff0727078f721bb7cec473ed56bf16b00/Malaria_users.json") as url:
    data = json.loads(url.read().decode())
    for x in data:
    	print (x['name'],x['email'])
