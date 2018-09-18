import requests
import json
url = "http://176.4.16.101/api_jsonrpc.php"
headers = {'Content-Type':'application/json-rpc'}
# data 是从官方文档处获得
# 手册==》用户==》user.login 
data={ 
    "jsonrpc":"2.0",
    "method": "user.login",
    "params": { 
    	"user" : "Admin" ,
        "password" : "zabbix"
    } ,
    "id" : 1 
}
r = requests.post(url,headers=headers,data=json.dumps(data))
print(r.json())
