

#Tor without enable ip rotation

from proxiestor import Tor
import requests, time



tor = Tor(ip_rotation=False) #ip_rotation = False

print('Starting tor ....')
#Start
tor.start()
print('Tor has been successfully started')

url = "https://httpbin.org/ip"
r = requests.get(
    url,
    proxies={"https": "socks5://127.0.0.1:9050", "http": "socks5:127.0.0.1:9050"},
).json()
print(f"Your ip: {r['origin']}")

#Close
tor.close()
