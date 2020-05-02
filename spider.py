import requests
headers = {'user-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36'}
url = 'https://zhuanlan.zhihu.com'
responts = requests.get(url)
print(responts)
