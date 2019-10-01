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
                raise Exception('Failed connection to service with status code "{}"'.format(r.status_code))


    
    def getProxyList(self, *args, **kwargs) -> [BProxyItem]:
        """
        type:	        Тип выгружаемых прокси, допустимые значения: http, https, socks4, socks5. Можно указать несколько, через запятую. Если этот параметр не задан, будут выгружены прокси всех типов.
        level:	        Уровень анонимности выгружаемых прокси серверов, допустимые значения: 1, 2, 3, 1 - соответствует высоко анонимным (элитным) прокси, 2 - соответствует анонимным прокси, 3 - соответствует прозрачным прокси. Можно указать несколько, через запятую.
        ports:	        Список портов выгружаемых прокси, можно указать до пяти через запятую. Данный параметр можно использовать, если, например, необходимо выгрузить прокси на стандартных портах (80, 443, 1080, 3128, 8080). Данный параметр нельзя задать через веб-фильтр.
        pex:	        Если равен 1, то вернутся прокси с портами, отсутствующими в списке, заданном параметром ports.
        country:	    Двубуквенные коды  стран выгружаемых прокси в соответствии с ISO 3166-1 alpha-2, можно указать до 20 через запятую.
        cex:	        Если равен 1, то вернутся прокси из стран, отсутствующих в списке, заданном параметром country.
        response:	    Числовое значение максимального времени отклика (в миллисекундах) выгружаемых прокси.
        uptime:	        Числовое значение времени непрерывной работы прокси в часах, допустимые значения находятся в диапазоне 1 - 48.
        speed:	        Скоростной грейд выгружаемых прокси серверов, в зависимости от времени, затраченного на выполнение теста прокси, допустимые значения: 1 (быстрые), 2 (средние по скорости), 3 (медленные). Можно указать несколько, через запятую.
        mail:	        Если равен 1, то вернутся прокси с открытым 25 SMTP портом. Обратите внимание, что отправки почты невозможна через обычные HTTP прокси, а только через HTTPS или SOCKS прокси.
        yandex:	        Если равен 1, то возвращаются прокси, через которые возможны запросы к ПС Яндекс без ввода капчи.
        google:	        Если равен 1, то возвращаются прокси, через которые возможны запросы к ПС Google без ввода капчи.
        mailru:	        Если равен 1, то возвращаются прокси, не забаненные на проектах Mail.Ru, (HTTP, а не SMTP доступ).
        twitter:	    Если равен 1, то возвращаются прокси, не забаненные в сервисе Twitter.
        includeType:	Данный параметр влияет на формат выводимого списка прокси в формате TXT. Если передать этот параметр (можно даже без значения), то прокси возвращаются в формате [type]://[ip]:[port]. Если этот параметр не указан, список возвращается в формате [ip]:[port]. Подробнее о форматах вывода списка прокси читайте ниже.
        limit:	        При помощи этого параметра задаётся максимальное количество выгружаемого списка прокси. Если этот параметр равен 0, выводится список из не более чем 15.000 прокси. Если этот параметр не задан, выводится список, не более чем из 20 прокси.
        nocascade:	    Если равен 1, то возвращаемый список не содержит каскадных прокси. Данный параметр нельзя задать через веб-фильтр.
        """
        params = kwargs
        params['key'] = self.key
        with self.__session.get(self.__hostname + self.__defaultMethod, params=params) as r:
            if r.status_code == 200:
                proxyList = []
                for item in r.json():
                    proxyItem = BProxyItem()
                    for key, value in item.items():
                        if value == '0' or value == '1':
                            value = int(value)
                        if hasattr(proxyItem, key):
                            setattr(proxyItem, key, value)
                    proxyList.append(proxyItem)
                return proxyList
            else:
                raise Exception('Failed connection to service with status code "{}", body: "{}"'.format(r.status_code, r.text))
