Automating access to Home Access Center, or HAC, which is used by a number of school systems for access to attendance, grades, and more.

## monitor_hac_attendance

Monitor for new absences and tardies, as well as retroactive changes made to attendance in the current week, and SMS all updates via twilio.

Create secrets/login.json with your "username" and "password" for HAC

Create secrets/twilio.json with AccountSID, AuthToken, TwilioPhoneNumber, and DestPhoneNumbers.  DestPhoneNumbers should be a list of phone numbers to text.

Sample crontab entry to poll for changes:

    */5 * * * * cd DIRECTORYNAME/hac_automation && .venv/bin/python3 utils/run-notebook.py monitor_hac_attendance.ipynb
