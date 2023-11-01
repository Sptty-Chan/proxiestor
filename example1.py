

#Tor with enable ip rotation

from proxiestor import Tor
import requests, time



tor = Tor(ip_rotation=True)

print('Starting tor ....')
#Start
tor.start()
print('Tor has been successfully started')

url = "https://httpbin.org/ip"

print("Use CTRL + C to stop")
while True:
    try:
        r = requests.get(
            url,
            proxies={"https": "socks5://127.0.0.1:9050", "http": "socks5:127.0.0.1:9050"},
        ).json()
        print(f"Your ip: {r['origin']}")
        time.sleep(5)
    except KeyboardInterrupt:
        break

#Close
tor.close()
