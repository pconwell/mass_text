## Overview

This is a very basic and simple script to send out a mass number of text (SMS) messages. The texts will be sent at a rate of approximately 1 SMS per second, so if you send 100 SMS messages it will take approximately 100 seconds.

You will need a [Twilio account](https://www.twilio.com/) and API keys. Additionally, there is a small charge for each text sent (somewhere around 1,000 SMS per $10).

The script in full can be [viewed here](https://github.com/pconwell/mass_text/blob/master/send_text.py). Below, you can see the break down of each step in the script. As you will see, there is not much to it. You will spend more time setting up python (assuming it's not already intalled on your computer) and registering your Twilio account than you will altering and running this script.

## Environment
* Python 3.6
* Microsoft Excel (will be changed to csv in future version)
* Twilio account

## Code
### Import necessary libraries
``` python
from twilio.rest import TwilioRestClient
import openpyxl
```

### Enter your Twilio API credentials here. You can get these from your [Twilio account settings page](https://www.twilio.com/console/account/settings)
``` python
# put your own credentials here

AUTH_SID = '1a2B3c4D' # put your own credentials here
TEST_SID = '1a2B3c4D' # put your own credentials here

AUTH_TOKEN = '1a2B3c4D' # put your own credentials here
TEST_TOKEN = '1a2B3c4D' # put your own credentials here
```

### Turn test mode on or off. Turning test mode on will use the test API keys
``` python
test_mode = True
```

### Variables used for the message
``` python
position = 'Position'
shift = 'dayshift'
poc = 'Point of Contact'
```

### Sets SID and TOKEN to either production or test keys depepding on if test_mode is set to True or False above
``` python
 if test_mode == False:
   token = AUTH_TOKEN
   sid = AUTH_SID
 else:
   token = TEST_TOKEN
   sid = TEST_SID
```

### Set connection to Twilio
``` python
client = TwilioRestClient(sid, token)
```

### Connect to and read a column of phone numbers from excel
``` python
wb = openpyxl.load_workbook("phone.xlsx")
sheet = wb.get_sheet_by_name(str(position))
col = sheet['B']
```

### Iterate over each phone number in column and send text (or if test_mode == True print phone number to console)
``` python
for cell in col:
    if test_mode == True:
        print(cell.value)
    elif test_mode == False:
        client.messages.create(
            to = cell.value,
            from_ = '6155551234', # put your own Twilio phone number here
            body = f'Need {position} to work {shift} today. If you can work, please call {poc}')
```
