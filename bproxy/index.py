from bproxy import BProxyClient
import logging

logging.basicConfig(level=logging.DEBUG)

client = BProxyClient('d7f380bccef40d690aa0442dff9fa977')
print(client.expiredAt)
for item in client.getProxyList():
    print(item.last_check)