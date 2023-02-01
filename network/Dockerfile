from ubuntu

RUN apt-get update && apt-get install hostapd iproute2 gettext-base dnsmasq   -y 

COPY hostapd/* /etc/hostapd 

COPY run.sh /run.sh
RUN chmod +x /run.sh


CMD /run.sh
