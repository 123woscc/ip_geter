import requests

def get_addr(ip):
    url = 'https://api.map.baidu.com/location/ip'
    data = {
        'ip': str(ip),
        'ak': 'kPQGVqe2bbc5wm1cB2nopX6s3R241gR9'
    }

    res = requests.post(url, data=data)
    addr = res.json()['address']
    return addr