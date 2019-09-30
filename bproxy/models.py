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

