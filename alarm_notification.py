import signal
import sys
import RPi.GPIO as GPIO
from time import sleep
import smtplib
from email.message import EmailMessage

#Define the email accounts and password
from_address = "from@gmail.com"
to_address = "to@gmail.com" #comma seperated for multiple
password = "from_account_app_password"

#Define the alarm activated email body
email_alarm = f"""
Alarm activated notification email body text
"""

#Define the alarm cleared email body
email_cleared = f"""
Alarm cleared notification email body text
"""

#Setup the email
msg = EmailMessage()
msg['Subject'] = "Subject of Email Alarm"
msg['From'] = from_address
msg['To'] = to_address

#if run as a script, define the exit function for ctrl+c
def signal_handler(sig, frame):
        GPIO.cleanup()
        sys.exit(0)

#define the GPIO change function and email
def alarm_sent(channel):
        if GPIO.input(11):
                while GPIO.input(11) == 1: #email loop until cleared
                        try:
                                msg.set_content(email_alarm)
                                server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
                                server.login(from_address, password)
                                server.send_message(msg)
                                server.quit()
                        except Exception as e:
                                print(e)
                        sleep(60) #set to time desired between emails in seconds
                return 0 #must return out of the function, otherwise it will send a cleared email twice
        if not GPIO.input(11):
                try:
                        msg.set_content(email_cleared)
                        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
                        server.login(from_address, password)
                        server.send_message(msg)
                        server.quit()
                except Exception as e:
                        print(e)
                return 0 

#define the main function
if __name__ == '__main__':
        #set to GPIO.BCM to call the pin by named GPIO number, leave as GPIO.BOARD to call by actual pin number on Pi
        GPIO.setmode(GPIO.BOARD) 
        #pin number, set to receive input, pull_up_down to GPIO.PUD_DOWN to let it know it's 0 by default for this application
        GPIO.setup(11, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) 
        #set pin number since .BOARD, tell it to monitor both directions, i.e. 0-1 and 1-0, tell it the callback function to execute, and a bouncetime interval in milliseconds to ignore the change
        GPIO.add_event_detect(11, GPIO.BOTH, callback=alarm_sent, bouncetime=50) 

        signal.signal(signal.SIGINT, signal_handler)
        signal.pause()
