import os
from InsData import Ing as Instagram

if __name__ == '__main__':
        try:os.mkdir('/sdcard/Ress')
        except:pass
        try:os.mkdir('Data')
        except:pass
        try:
                Instagram.security()
        except requests.exceptions.ConnectionError:
                print('Connection Close')
