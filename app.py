from flask import Flask,jsonify,request

import os

import requests

app=Flask(__name__)
app.secret_key=os.urandom(24)

def get_addr(ip):
    url = 'https://api.map.baidu.com/location/ip'
    data = {
        'ip': str(ip),
        'ak': 'kPQGVqe2bbc5wm1cB2nopX6s3R241gR9'
    }
    res = requests.post(url, data=data)
    addr = res.json()['address']
    return addr

@app.route('/get_ip')
def get_ip():
    try:
        ip = request.remote_addr
        address = get_addr(ip)
        return jsonify(msg='ok',ip=ip, address=address)
    except:
        return jsonify(msg='error')


if __name__ == '__main__':
    app.run()