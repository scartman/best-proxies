from datetime import datetime, timedelta

class BProxyItem(object):
    """
    Element in proxy list
    """
    ip = None
    port = None
    hostname = None
    http = False
    https = False
    socks4 = False
    socks5 = False
    level = 0
    yandex = False
    google = False
    mailru = False
    twitter = False
    country_code = None
    response = None
    good_count = 0
    bad_count = 0
    __last_check = None
    city = None
    region = None
    real_ip = None
    test_time = None
    me = None

    @property 
    def last_check(self):
        return self.__last_check

    @last_check.setter
    def last_check(self, value):
        self.__last_check = datetime.utcfromtimestamp( datetime.strptime(value, '%Y-%m-%d %H:%M:%S').timestamp() )  


    @property
    def formated(self):
        for item in ['http', 'https', 'socks4', 'socks5']:
            if getattr(self, item):
                return '{}://{}:{}'.format(item, self.ip, self.port)
        if self.ip and self.port:
            return '{}:{}'.format(self.ip, self.port)
        else:
            return type(self)

    def __str__(self):
        return self.formated
            