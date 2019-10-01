# best-proxies.ru python3 client
http://best-proxies.ru
### Как использовать?

    from bproxy import BProxyClient
    
    KEY = ''
    client = BProxyClient(KEY)
    proxyList = client.getProxylist()
    expired = client.expiredAt
    

**proxyList params**

|  argument  | description   |
| ------------ | ------------ |
|  type |  Тип выгружаемых прокси, допустимые значения: http, https, socks4, socks5. Можно указать несколько, через запятую. Если этот параметр не задан, будут выгружены прокси всех типов.  |

