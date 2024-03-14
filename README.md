# Raspberry-Pi-Alarm
Raspberry Pi email alarm from GPIO pin input

This is a simple python script to send an email alarm based on voltage detected or cleared from a GPIO pin. I created this script to send an email after receiving voltage from an unmonitored alarm system. The voltage output of the alarm was 12v, so a voltage divide was used to bring it down to under 3.3v. WARNING: DO NOT SENT OVER 3.3V to a GPIO PIN. IF YOU DO, YOU WILL FRY THE RAPBERRY PI!!!

It uses a gmail account with an app password to authenticate to gmail over ssl port 465, defines an email message for an alarm and a clear, and uses the GPIO interrupts instead of a loop.

OPTIONAL: I created a systemd service to have it run on startup on the pi without the user logged in. To do this, download the PY file, create a service file in /etc/systemd/system, execute a daemon reload, then start the service. I have attached a sample for my service. 

Special thanks to these pages that helped point me in the right direction:

https://raspi.tv/2013/rpi-gpio-basics-6-using-inputs-and-outputs-together-with-rpi-gpio-pull-ups-and-pull-downs

https://sourceforge.net/p/raspberry-gpio-python/wiki/Inputs/

https://roboticsbackend.com/raspberry-pi-gpio-interrupts-tutorial/

https://docs.python.org/3/library/smtplib.html

https://stackoverflow.com/a/57401680

https://github.com/thagrol/Guides/blob/main/boot.pdf

https://github.com/torfsen/python-systemd-tutorial
