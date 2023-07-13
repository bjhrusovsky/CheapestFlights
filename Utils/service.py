import sys
sys.path.append("/SQL/DAO")
#import Bots.KayakBot as KayakBot


class Service:
    __instance = None
    def __new__(cls, *args, **kwargs):
        if not cls.__instance:
            cls.__instance = super().__new__(cls, *args, **kwargs)
        return cls.__instance
