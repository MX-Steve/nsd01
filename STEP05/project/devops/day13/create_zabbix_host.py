import requests
import json
url = "http://176.4.16.101/api_jsonrpc.php"
headers = {'Content-Type':'application/json-rpc'}
data={
    "jsonrpc": "2.0",
    "method": "host.create",
    "params": {
        "host": "python Linux server",
        "interfaces": [
            {
                "type": 1,
                "main": 1,
                "useip": 1,
                "ip": "192.168.1.2",
                "dns": "192.168.1.5",
                "port": "10050"
            }
        ],
	"groups": [
            {
                "groupid": "2"
            }
        ],
    },
    "auth": "970fce4e6014856681dd91ccecf6e906",
    "id": 1
}
r = requests.post(url,headers=headers,data=json.dumps(data))
print(r.json())
