import requests


headers = {

    "Referer": "https://bj.meituan.com/meishi/184175089/",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36",
    "mtgsig": "^{^\\^a1^^:^\\^1.0^^,^\\^a2^^:1663763536636,^\\^a3^^:^\\^1663760274511UGACKQEfd79fef3d01d5e9aadc18ccd4d0c95073805^^,^\\^a4^^:^\\^fd22e281519c0d4381e222fd430d9c517d382a9d3e35b6cc^^,^\\^a5^^:^\\^zpW4UTLcePtP699X7LqLWwDapRIQ+LtGOMa3SSvQzTj91FlfEKI9v8ybApAhaWBrkxNRszXEQFVCBuCtr6IL4ehjTV8jgjhrHiH5uUPUbYpokGkvxQKQPSIqJXWRh2pa08r=^^,^\\^a6^^:^\\^h1.2oK4liElBAxmw1fRPhdHnksDYfh/kyaxCRFzC+LYhzMfY+xhniRazTh2105yoEeacfsmjP/mCd55oyejfB+7V/Ub9djIVqhoOYFvFbUHAOSrWK3OZOVyYh9UPkX/k7fAGTiUwznP0KH4lOkIQKpzwJrKxRUTqiA8rAhiOV3stCoXfNy6KQdZBlb18quYwRr7NrgwpU0Co66cqQ1SCArNiDx5rNmkoV+kAUb/BFZmfTpioz5QrDs3Wyd1CD9QBJfC2JDaaVWLf/9Fx+Ta4FxEyts3lHlAL0lYM6fCdTliGeMekc3QKjbXR8Nx8ytRbyxAi6vBQMTp/HvvfHqAAtQX6KSFhDq1944pvmcXcPBFfK8JcqlBE/0a6W4i8MBzF11/2sI3F4P0JhOU1elV6j7w8F3Hxi2Wbeb7VdFW0OMgUcDkHnCXUskDfTQAq63QrYguJHauSXXdqZrnT8XC+3Xy+r7YrfNHjtk1nkvaA85h61W4K8v4Rd3MylhuRqqrVdiSOF/zHRb16t0igZqy0Ensquw0jivnDzWXZs0f9Z1VFE4tK2bZIXgAXjXCgXLlk+GGMmNH8NX8XS4aHKDgwhve3nHrlmZ5YwyjImznwVfRSFXYijVZPng2sSgNbg0bx9Eiij+zJDuBCPyzV/TTmXB/dFYyBmKBjg+nkfb619+iNRcY=^^,^\\^a7^^:^\\^com.sankuai.web.meishife.pcweb^^,^\\^x0^^:4,^\\^d1^^:^\\^2a296440094307664e2e1f6e0482cdae^^^}",

}
cookies = {
    "uuid": "de164866778245a9aa0c.1663759816.1.0.0",
    "_lxsdk_cuid": "1835fd01c24c8-0515a476fbc44b-26021c51-144000-1835fd01c24c8",
    "ci": "1",
    "rvct": "1",
    "client-id": "3dcb1b7d-1cb2-4dd5-8fd3-983b39791746",
    "mtcdn": "K",
    "lt": "ibWpopV0qQOx1vM0rhCkKdD3WsoAAAAACRQAAF5OWWxceFCegtRp2BxHn5CKOXq6li5pmwCGcTSoWweDIkTK98wfQ_TmxA-dwv3jDA",
    "u": "3737468254",
    "n": "Sej382159795",
    "token2": "ibWpopV0qQOx1vM0rhCkKdD3WsoAAAAACRQAAF5OWWxceFCegtRp2BxHn5CKOXq6li5pmwCGcTSoWweDIkTK98wfQ_TmxA-dwv3jDA",
    "unc": "Sej382159795",
    "_lxsdk": "1835fd01c24c8-0515a476fbc44b-26021c51-144000-1835fd01c24c8",
    "WEBDFPID": "1663760274511UGACKQEfd79fef3d01d5e9aadc18ccd4d0c95073805-1663760274511-1663760274511UGACKQEfd79fef3d01d5e9aadc18ccd4d0c95073805",
    "_hc.v": "34cae61c-cb91-d43d-ae4f-0888b51f42f2.1663760275",
    "_lx_utm": "utm_source^%^3Dbing^%^26utm_medium^%^3Dorganic",
    "__mta": "55491988.1663759820912.1663759820912.1663763511864.2",
    "_lxsdk_s": "1835fd01c25-fae-57c-1ae^%^7C^%^7C34",
    "firstTime": "1663763519832",
    "lat": "40.01477",
    "lng": "116.3527"
}
url = "https://bj.meituan.com/meishi/api/poi/getMerchantComment"
params = {
    "uuid": "de164866778245a9aa0c.1663759816.1.0.0",
    "platform": "1",
    "partner": "126",
    "originUrl": "https^%^3A^%^2F^%^2Fbj.meituan.com^%^2Fmeishi^%^2F184175089^%^2F",
    "riskLevel": "1",
    "optimusCode": "10",
    "id": "184175089",
    "userId": "3737468254",
    "offset": "10",
    "pageSize": "10",
    "sortType": "1",
    "tag": ""
}
response = requests.get(url, headers=headers, cookies=cookies, params=params)

print(response.text)
print(response)