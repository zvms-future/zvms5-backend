# Environment config
IS_XUEHAI = False # Automatically set in thread, don't edit

# Database config
DATABASE_URI = 'sqlite:///:memory:'

# Server config
SERVER_CERT = None
SERVER_PORT = 9009

# Xuehai env check thread
from threading import Thread
def check_zty():
    global IS_XUEHAI
    import urllib.request as urllib2
    try:
        urllib2.urlopen('http://app.yunzuoye.cloud/health')
        IS_XUEHAI = True
    except:
        pass # Timeout: not on Xuehai server
Thread(target=check_zty).start()