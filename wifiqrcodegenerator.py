#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import subprocess
import wifi_qrcode_generator as qr

try:
    data = subprocess.check_output(['netsh', 'wlan', 'show', 'interfaces']).decode('utf-8', errors='ignore').split('\n')
    ssid = str([b.split(':')[1][1:-1]
               for b in data if 'Perfil' in b])[2:-3]
    getPass = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles', ssid, 'key=clear']).decode('utf-8', errors='ignore').split('\n')
    password = str([b.split(':')[1][1:-1]
                   for b in getPass if 'Contenido de la clave' in b])[2][2:-2]
except ValueError as ve:
    print(ve)
else:
    qrimg=qr.wifi_qrcode(ssid, False, 'WPA', password)
    qrimg.save('myqr.png')
    print('QR generated successfully')

