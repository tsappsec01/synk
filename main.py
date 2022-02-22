# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import socket
import os
import requests

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.
    # addr1 = socket.gethostbyname('wyycjvaegwxg6336qvo3o2i6jxpndc.burpcollaborator.net')
    # print(f'{addr1}')
    csrftoken = 'A7MvkJGg-XWQjGC7i8bwprpV_6NDI3nGcJpc'

    r = requests.post('https://127.0.0.1/org/tsappsec01/manage/settings/ignore',
                      data={'_csrf': f'{csrftoken}',
                            'orgIgnoreSettings[adminOnly]': 'false',
                            'orgIgnoreSettings[reasonRequired]': 'true'},
                      cookies={'snyk.id': 's:AA51MO2v8zPib5yXGsL7zECapsSe7kM0.tvBtH477nieEzAyMXOl8/M4w13iiNAWagMkXJtLUiTk'})
    print(r.text)
    # for i in r.cookies.items():
    #     print(i)r.cookies.items()[0])
    print(r.status_code)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

