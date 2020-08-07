import os
import sys

sav_pro=os.popen('netsh wlan show profiles').read()
print(sav_pro)

avail_pro=os.popen('netsh wlan show networks').read()
print(avail_pro)

preferred_ssid=input('Enter the preferred wifi for your connection:')

response=os.popen("netsh wlan disconnect").read()
print(response)

if preferred_ssid not in sav_pro:
    print("Profile for "+preferred_ssid+" is not saved in system")
    print("Sorry but can't establish the connection")
    sys.exit()

else:
    print("Profile for "+preferred_ssid+" is saved in system")

while True:
    avail=os.popen('netsh wlan show networks').read()
    if preferred_ssid in avail:
        print("Found")
        break

print('----------------Connecting----------------')
res=os.popen('netsh wlan connect name='+'"'+preferred_ssid+'"').read()
print(res)