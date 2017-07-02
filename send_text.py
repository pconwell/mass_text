from twilio.rest import TwilioRestClient
import openpyxl
# put your own credentials here

AUTH_SID = '1a2B3c4D' # put your own credentials here
TEST_SID = '1a2B3c4D' # put your own credentials here

AUTH_TOKEN = '1a2B3c4D' # put your own credentials here
TEST_TOKEN = '1a2B3c4D' # put your own credentials here

test_mode = True

position = 'Position'
shift = 'dayshift'
poc = 'Point of Contact'

 if test_mode == False:
   token = AUTH_TOKEN
   sid = AUTH_SID
 else:
   token = TEST_TOKEN
   sid = TEST_SID


client = TwilioRestClient(sid, token)

wb = openpyxl.load_workbook("phone.xlsx")
sheet = wb.get_sheet_by_name(str(rank))
col = sheet['B']

for cell in col:
    if test_mode == True:
        print(cell.value)
    elif test_mode == False:
        client.messages.create(
            to = cell.value,
            from_ = '6155551234', # put your own Twilio phone number here
            body = f'Need {position} to work {shift} today. If you can work, please call {poc}')
