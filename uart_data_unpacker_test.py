import uart_data_unpacker as up
from logger import Logger

log = Logger(prefix='TEST')


def on_pack(data, ctx):
    print(data)


callback_table = {
    up.EVENT_NEW_PACKAGE: on_pack
}


def callback(e):
    if e.type_key in callback_table:
        callback_table[e.type_key](e.extra_data, e.ctx)


def main():
    cmds = ['U 122344A\r\nB', ' 1231313B\r', 'L 333\n', '\r\n\nW 444\r\n', 'H 555\r', 'END \r\n']
    upk = up.Unpacker(callback)
    for cmd in cmds:
        upk.append_str(cmd)


if __name__ == '__main__':
    main()
