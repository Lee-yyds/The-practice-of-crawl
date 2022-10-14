import requests

data = {
    'group': 'rpc-test',
    'action': 'gc'
}
res = requests.get("http://127.0.0.1:5620/business-demo/invoke",params=data)
print(res.text)

