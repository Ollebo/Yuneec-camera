#!/bin/bash
echo "Restart network nic"



echo "Setup network interface"
ip addr add $IPADDR dev $WIFI_DEVICE
ip a

echo "Setuo hostad"
envsubst < /etc/hostapd/hostapd.tpl > /etc/hostapd/hostapd.conf
cat /etc/hostapd/hostapd.conf

hostapd  /etc/hostapd/hostapd.conf
