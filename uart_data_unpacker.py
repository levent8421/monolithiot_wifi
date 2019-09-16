import logger

log = logger.Logger(prefix='UART_UNPACKER')
EVENT_NEW_LINE = 0x01
EVENT_NEW_PACKAGE = 0x02


class Event:
    def __init__(self, type_key, ctx, extra_data):
        self.type_key = type_key
        self.ctx = ctx
        self.extra_data = extra_data


class Unpacker:
    def __init__(self, callback, line_delimiter='\r\n', new_package_cmd='END'):
        self.__callback = callback
        self.__buffer = ''
        self.__package_data = ''
        self.__line_delimiter = line_delimiter
        self.__new_package_cmd = new_package_cmd

    def append_str(self, cmd_str):
        for c in cmd_str:
            if c in self.__line_delimiter:
                self.__report_new_line()
            else:
                self.__buffer += c

    def __report_new_line(self):
        line = self.__buffer.strip()
        if len(line) > 0:
            if line.startswith(self.__new_package_cmd):
                event = Event(EVENT_NEW_PACKAGE, self, self.__package_data)
                self.__callback(event)
                self.__reset_package_data()
            else:
                self.__store_line(line)
                event = Event(EVENT_NEW_LINE, self, line)
                self.__callback(event)

            self.__reset_buffer()

    def __store_line(self, line):
        if len(self.__package_data) > 0:
            self.__package_data += ';'
            self.__package_data += line
        else:
            self.__package_data = line

    def __reset_buffer(self):
        self.__buffer = ''

    def __reset_package_data(self):
        self.__package_data = {}
