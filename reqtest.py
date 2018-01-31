# coding:utf-8

import urllib2
import urllib
import requests

# urllib2
proxy_handler = urllib2.ProxyHandler({'http': '180.97.104.14:80'})
opener = urllib2.build_opener(proxy_handler)
r = opener.open('http://httpbin.org/ip')
print(r.read())

# reqeust
r = requests.get('http://httpbin.org/ip', proxies={'http': '124.165.252.72:9999'}).json()
print r

