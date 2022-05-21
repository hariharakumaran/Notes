# Web Page for Creating  Notes

## Setup & Installtion

Make sure you have the latest version of Python installed.

```bash
git clone <repo-url>
```

```bash
pip install -r requirements.txt
```

## Running The App

```bash
python main.py
```

## Viewing The App

Go to `http://127.0.0.1:5000`

## App Features

Create new users

Login for exisitng users

OTP generation via SMS and Mail for password forget and OTP log in


## Change your Fast2sms Key and Gmail to send comms.

In send_comss.py file , change headers['authorization'] = 'YOUR KEY' in function - send_sms

In send_comss.py file , change smtp.login('abc@gmail.com', 'abc123') to your smtp.login('Your mail id','Your Password') in function - send_mail
