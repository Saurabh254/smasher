import subprocess


def send_otp(phonenumber, message):
    subprocess.call(["termux-sms-send", "-s", "1", "-n", phonenumber, message])
