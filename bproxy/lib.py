class BProxy:

    __KEY_LENGHT = 32

    def __init__(self, key):
        self.key = key

    @property
    def key(self):
        return self.__key

    @key.setter
    def key(self, key):
        if not key or type(key) is not str:
            raise TypeError('argument "key" is required!')
        if len(key) < self.__KEY_LENGHT:
            raise ValueError('argument "key" must be {} character length'.format(self.__KEY_LENGHT))
        self.__key = key

    def __str__(self):
        return 'Instance of BProxyClient with key: "{}"'.format(self.key)

