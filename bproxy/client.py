from datetime import datetime
import requests
from .models import BProxyItem
from .lib import BProxy


class BProxyClient(BProxy):

    __session = requests.Session()
    __hostname = 'https://api.best-proxies.ru/'
    __defaultMethod = 'proxylist.json'
    __expiredMethod = 'key.txt'

    @property
    def expiredAt(self) -> datetime:
        with self.__session.get(self.__hostname + self.__expiredMethod, params={
            'key': self.key,
            'format': 'seconds'
        }) as r:
            if r.status_code == 200:
                return datetime.fromtimestamp(datetime.today().timestamp() + int(r.text))
            else:
                raise Exception('Failed connection to srvice with status code "{}"'.format(r.status_code))

    def getProxyList(
            self, 
            type=None, 
            level=None, 
            ports:list=[], 
            pex:int=0, 
            country:list=[], 
            cex=0,
            response=None,
            uptime=None,
            speed:list=[],
            mail:bool=None,
            yandex:bool=None,
            google:bool=None,
            mailru:bool=None,
            twitter:bool=None
        ) -> [BProxyItem]:
        proxyList = []
        with self.__session.get(self.__hostname + self.__defaultMethod, params={
            'key': self.key,
            'limit': 100
        }) as r:
            for item in r.json():
                proxyItem = BProxyItem()
                for key, value in item.items():
                    if hasattr(proxyItem, key):
                        setattr(proxyItem, key, value)
                proxyList.append(proxyItem)
        return proxyList
