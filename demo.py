from bproxy import BProxyClient


KEY = ''

client = BProxyClient(KEY)
proxyList = client.getProxyList()
expired = client.expiredAt