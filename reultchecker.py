import requests
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import time
import pygame

# Initialize pygame
pygame.init()

def play_sound():
    pygame.mixer.music.load("alarm.mp3")  # Replace "notification_sound.wav" with your sound file
    pygame.mixer.music.play()

def send_email():
    # Email configuration
    sender_email = "virtualmazeopenproject@gmail.com"
    receiver_email = "aswinchithambaram@gmail.com"
    password = "rakm txyt ktfn nbxr"

    # Email content
    subject = "Dental result declared"
    body = "Result declared please check the website."

    # Setup the MIME
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = subject

    # Attach the body to the email
    message.attach(MIMEText(body, "plain"))

    # Create SMTP session for sending the mail
    session = smtplib.SMTP("smtp.gmail.com", 587)  # Use your SMTP server here
    session.starttls()  # enable security
    session.login(sender_email, password)  # login with mail_id and password
    text = message.as_string()
    session.sendmail(sender_email, receiver_email, text)
    print("Mail sent")
    session.quit()

def check_api():
    url = "https://cms2api.tnmgrmu.ac.in/Api/index.php/Login/appLogin"
    registration_no = "540020503522"
    params = {"registration_no": registration_no, "login_type": "result"}



    while True:
        try:
            response = requests.get(url, params=params)
            data = response.json()
            print(data)
            if data.get("resultcode") != "402":
                play_sound()  # Play sound notification
                send_email()

        except Exception as e:
            print("Error occurred: ", e)
        # Sleep for some time before making the next request
        time.sleep(120)  # Sleep for 20 seconds

check_api()
