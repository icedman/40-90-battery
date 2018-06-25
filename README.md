# 40-90-battery
Saves laptop battery by disconnecting charger power at 90, reconnecting at 40.

[Xiaomi Smart Power Socket](https://www.aliexpress.com/item/Original-Xiaomi-MiJia-Mi-Smart-Power-Socket-Plug-Basic-Wireless-WiFi-APP-Remote-Control-Timer-Switch/32801060790.html)

require npm miio
``npm install -g miio``

crontab -e
``45 * * * * /usr/local/bin/40-90-battery.py``