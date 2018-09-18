import requests
import json
url = "http://176.4.16.101/api_jsonrpc.php"
headers = {'Content-Type':'application/json-rpc'}
data={
    "jsonrpc": "2.0",
    "method": "hostgroup.get",
    "params": {
        "output": "groupids",
        "filter": {
            "name": [
                "Linux servers"
            ]
        }
    },
    "auth": "970fce4e6014856681dd91ccecf6e906",
    "id": 1
}





r = requests.post(url,headers=headers,data=json.dumps(data))
print(r.json())
