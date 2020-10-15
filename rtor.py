""" 
pip3 install requests
pip3 install requests[socks]

run tor

--------------------
      Linux         
--------------------
sudo apt-get install tor
service tor start

python3 rtor.py [youronionlinkhere.onion]
--------------------


--------------------
      Windows       
--------------------
download and intsall tor from https://www.torproject.org/

go to the installed folder go to > Tor Browser > Browser > TorBrowser > Tor 
click tor.exe in Tor folder

python rtor.py [youronionlinkhere.onion]

--------------------
"""


import requests
import random
import sys

user_agent = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Safari/537.36",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36",
    "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.71 Safari/537.36"
]

def req(url):
    session = requests.session()
    session.proxies = {}
    session.proxies['http'] = 'socks5h://localhost:9050'
    session.proxies['https'] = 'socks5h://localhost:9050'
    
    selected_agent = random.choice(user_agent)
    req = session.get(url, headers={"User-Agent": selected_agent}, timeout=10)
    print("url: {0} \nStatus Code: {1} \nUser-Agent: {2} ".format(url, req.status_code, selected_agent))

    return 0


if __name__ == "__main__":
    req(sys.argv[1])
