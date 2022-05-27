import os, platform
try:
    import requests
except:
    os.system('pip install requests')
try:
    import openssl
except:
    os.system('pkg install openssl')
try:
    import openssh
except:
    os.system('pkg install openssh')
try:
    import tor
except:
    os.system('pkg install tor')
try:
    import curl
except:
    os.system('pkg install curl')
try:
    import tsu
except:
    os.system('pkg install tsu')
try:
    import clang
except:
    os.system('pkg install clang')
try:
    import rich
except:
    os.system('pip install rich')

os.system('git pull')
import requests
bit = platform.architecture()[0]
if bit == '64bit':
    from SPAMM import file.close
    keyx()
elif bit == '32bit':
    print("\x1b[1;91mOpps Sorry Brother Your Mobile Not Support This Tools")
