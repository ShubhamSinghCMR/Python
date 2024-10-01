# Online Voting System with Face Recognition and Two-Factor Authentication

This is an online voting system developed using the Django framework. It integrates face recognition and two-factor authentication to ensure a secure and efficient voting process.

## Features

- **Admin Login**: Managed by the election commission.
- **Voter Login**: Managed by voters.
- **Secure Login**: Voters log in with their voter ID and password after successful registration.
- **Candidate Information**: Voters can view a list of candidates in their area and access background information such as income and work history.
- **Face Recognition**: Voters authenticate using their face via a webcam or front camera.
- **Two-Factor Authentication**: After face recognition, two-factor authentication ensures further security.
- **One-Time Voting**: Once authenticated, voters can cast their vote, and each voter can only vote once per election.

## How It Works

1. **Registration**: Voters register with their voter ID and set up a password.
2. **Login**: Voters log in using their credentials.
3. **Face Verification**: Voters must verify their identity using face recognition.
4. **Two-Factor Authentication**: After face verification, two-factor authentication is required.
5. **Voting**: Voters can view candidates, review their profiles, and cast their vote. Each voter can vote only once per election.

## Prerequisites

* Python version 3.12.0
* PostgreSQL version 16.1
* API Key generated from [2factor](https://2factor.in/).
* App Password generated from Google account; refer to [Sign in with app passwords](https://support.google.com/accounts/answer/185833?hl=en).

## Setup Steps

1. Create a `Digital_Voting` database in PostgreSQL.
2. In `settings.py`, configure `DB USER`, `DB PASSWORD`, `EMAIL_HOST_USER`, `EMAIL_HOST_PASSWORD`, and `TWO_FACTOR_API_KEY`.
3. Install required packages:
   ```bash
   pip install -r requirements.txt

## Run Project

1. Start the development server by executing the command: `python manage.py runserver`.
2. Log in to the Django Administration Page using the superuser credentials and add the details of the superuser in EC_Admins.
3. Navigate to the Login Page, select "Login as Admin," add Voter details, add Candidate details, generate the election, and log out from the Admin dashboard.
4. Click on "Register" and fill out the Voter registration form. Record and upload a video of 5-10 seconds for face registration.
5. Log in as a Voter, click on "Election," select a Candidate, record and upload a video of 5-10 seconds for face verification, and enter the SMS OTP and Email OTP.
6. Log in as Admin, complete the election, and generate the result.