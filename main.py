# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import socket
import os
import requests

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.
    # addr1 = socket.gethostbyname('uywfveb7x5xhwlfpz69352xvrmxcl1.burpcollaborator.net')
    # print(addr1)
    # # print(f'{addr1}')
    # csrftoken = 'A7MvkJGg-XWQjGC7i8bwprpV_6NDI3nGcJpc'
    #
    # r = requests.post('https://app.snyk.io/org/tsappsec01/manage/settings/ignore',
    #                   data={'_csrf': f'{csrftoken}',
    #                         'orgIgnoreSettings[adminOnly]': 'false',
    #                         'orgIgnoreSettings[reasonRequired]': 'true'},
    #                   cookies={'snyk.id': 's:AA51MO2v8zPib5yXGsL7zECapsSe7kM0.tvBtH477nieEzAyMXOl8/M4w13iiNAWagMkXJtLUiTk'})
    # print(r.text)
    # # for i in r.cookies.items():
    # #     print(i)r.cookies.items()[0])
    # print(r.status_code)
    TCP_IP = '72.14.183.78'
    # TCP_IP = socket.gethostbyname('uywfveb7x5xhwlfpz69352xvrmxcl1.burpcollaborator.net')
    TCP_PORT = 8089
    BUFFER_SIZE = 1024
    MESSAGE = "Hello, World!"
    startport = 21
    endport = 22
    openports = []


    for port in range(startport, endport+1):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(1)
            s.connect((TCP_IP, port))
        except ConnectionRefusedError:
            s.close()
            continue
        except socket.timeout:
            print(f'{port} timeout')
            continue
        openports.append(port)
        s.close()

    for port in openports:
        print(port)
    # s.send(MESSAGE)
    # data = s.recv(BUFFER_SIZE)
    # s.close()
    # print
    # "received data:", data


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

