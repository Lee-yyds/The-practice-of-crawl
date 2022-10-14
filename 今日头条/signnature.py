import requests

data = {
    'group': 'rpc-test',
    'action': 'gc',
    'a':'https://lf3-config.bytetcc.com/obj/tcc-config-web/tcc-v2-data-toutiao.fe.toutiao_web_pc-common'
}
res = requests.get("http://127.0.0.1:5620/business-demo/invoke",params=data)
print(res.text)