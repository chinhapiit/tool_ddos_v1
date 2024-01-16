import os, sys, requests
import concurrent.futures
os.system('cls' if os.name == 'nt' else 'clear')
from threading import Thread
def run():
 luu = input(' Nhập Files Lưu Proxy Live: ')
 list = []
 f = requests.get("https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt").text.split("\n")
 for p in f:
  prx = p.strip('\n').strip("\r")
  list.append("http|"+prx)
 f = requests.get("https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks4.txt").text.split("\n")
 for p in f:
  prx = p.strip('\n').strip("\r")
  list.append("sock4|"+prx)
 f = requests.get("https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks5.txt").text.split("\n")
 for p in f:
  prx = p.strip('\n').strip("\r")
  list.append("sock5|"+prx)
 def runc(proxys):
  try:
   if "http|" in proxys:
    proxy = proxys.split("|")[1]
    testing = requests.get('http://httpbin.org/ip', proxies={'http': 'https://'+proxy, 'https': 'https://'+proxy}, timeout=3).json()
    print ('\033[1;32m Working | '+proxys)
    open(luu,'a').write(proxy+'\n')
   elif "sock4|" in proxys:
    proxy = proxys.split("|")[1]
    testing = requests.get('http://httpbin.org/ip', proxies={'socks4': 'socks4://'+proxy}, timeout=3).json()
    print ('\033[1;32m Working | '+proxys)
    open(luu,'a').write(proxy+'\n')
   elif "sock5" in proxys:
    proxy = proxys.split("|")[1]
    testing = requests.get('http://httpbin.org/ip', proxies={'socks5': 'socks5://'+proxy}, timeout=3).json()
    print ('\033[1;32m Working | '+proxys)
    open(luu,'a').write(proxy+'\n')
  except:
    print ('\033[1;31m Time Out | '+proxys)
 with concurrent.futures.ThreadPoolExecutor(max_workers=100) as executor:
  executor.map(runc, list)
run()


