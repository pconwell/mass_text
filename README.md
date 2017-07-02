## mass_text

Import necessary libraries
``` python
from twilio.rest import TwilioRestClient
import openpyxl
```

Enter your Twilio API credentials here. You can get these from ...
``` python
# put your own credentials here

AUTH_SID = '1a2B3c4D' # put your own credentials here
TEST_SID = '1a2B3c4D' # put your own credentials here

AUTH_TOKEN = '1a2B3c4D' # put your own credentials here
TEST_TOKEN = '1a2B3c4D' # put your own credentials here
```

Turn test mode on or off. Turning test mode on will use the test API keys (i.e. not send any real texts)
``` python
test_mode = True
```

variables used for the message
``` python
position = 'Position'
shift = 'dayshift'
poc = 'Point of Contact'
```

Sets SID and TOKEN to either production or test keys depepding on if test_mode is set to True or False above
``` python
 if test_mode == False:
   token = AUTH_TOKEN
   sid = AUTH_SID
 else:
   token = TEST_TOKEN
   sid = TEST_SID
```

Set connection to Twilio
``` python
client = TwilioRestClient(sid, token)
```

Connect to and read from excel list of phone numbers. Sheet should be formatted as ...
``` python
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
```



## Welcome to GitHub Pages

You can use the [editor on GitHub](https://github.com/pconwell/ESP01/edit/master/README.md) to maintain and preview the content for your website in Markdown files.

Whenever you commit to this repository, GitHub Pages will run [Jekyll](https://jekyllrb.com/) to rebuild the pages in your site, from the content in your Markdown files.

### Markdown

Markdown is a lightweight and easy-to-use syntax for styling your writing. It includes conventions for

```markdown
Syntax highlighted code block

# Header 1
## Header 2
### Header 3

- Bulleted
- List

1. Numbered
2. List

**Bold** and _Italic_ and `Code` text

[Link](url) and ![Image](src)
```

For more details see [GitHub Flavored Markdown](https://guides.github.com/features/mastering-markdown/).

### Jekyll Themes

Your Pages site will use the layout and styles from the Jekyll theme you have selected in your [repository settings](https://github.com/pconwell/ESP01/settings). The name of this theme is saved in the Jekyll `_config.yml` configuration file.

### Support or Contact

Having trouble with Pages? Check out our [documentation](https://help.github.com/categories/github-pages-basics/) or [contact support](https://github.com/contact) and we’ll help you sort it out.
