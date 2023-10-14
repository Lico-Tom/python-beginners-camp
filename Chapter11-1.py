from http.client import HTTPConnection
from urllib import request, parse

import requests

url = 'https://baidu.com/s'
parms = {
    'ie': 'utf-8',
    'wd': 'cctv1'
}
headers = {
    'User-agent': 'none/ofyourbusiness',
    'Spam': 'Eggs'
}
querystring = parse.urlencode(parms)


def simple_request_0():
    print(url + '?' + querystring)
    u = request.urlopen(url + '?' + querystring)
    return u.read()


def simple_request_1():
    req = request.Request(url, querystring.encode('ascii'), headers=headers)
    u = request.urlopen(req)
    return u.read()


def simple_request_post_0():
    resp = requests.post(url, data=parms, headers=headers)
    return resp.json


def simple_request_get_0():
    resp = requests.get(url, auth=('username', 'password'))


def simple_request_get_1():
    files = {'file': {'data.csv', open('data.csv', 'rb')}}
    resp = requests.get(url, files=files)


def simple_httpconnection_0():
    c = HTTPConnection(url, 80)
    c.request('HEAD', '/index.html')
    resp = c.getresponse()
    print('status', resp.status)
    for name, value in resp.getheaders():
        print(name, value)

        
if __name__ == '__main__':
    print(simple_request_0())
    print("=" * 100)
    print(simple_request_1())
    print("=" * 100)
    print(simple_request_post_0())
