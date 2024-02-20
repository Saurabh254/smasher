import os


def send_otp(phonenumber, message):
    os.system(f"termux-sms-send -n {phonenumber} '{message}'")
