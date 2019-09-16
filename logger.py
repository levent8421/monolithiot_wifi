class Logger:
    def __init__(self, prefix):
        self.prefix = prefix

    @staticmethod
    def __as_str(tpl, param):
        if len(param) > 0:
            return tpl % param
        else:
            return tpl

    def debug(self, tpl, param=()):
        print('DEBUG:', self.__as_str(tpl, param))

    def warn(self, tpl, param=()):
        print('WARN:', self.__as_str(tpl, param))
