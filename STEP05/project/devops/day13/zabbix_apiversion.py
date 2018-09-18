import requests
import json
url = "http://176.4.16.101/api_jsonrpc.php"
headers = {'Content-Type':'application/json-rpc'}
# data 是从官方文档处获得
# 
data={
	"jsonrpc":"2.0",
	"method":"apiinfo.version",
	"id":1,
	"params":{}
}
r = requests.post(url,headers=headers,data=json.dumps(data))
print(r.json())
