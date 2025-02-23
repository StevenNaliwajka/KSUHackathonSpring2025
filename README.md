# KSUHackathonSpring2025
## SETUP:
Ensure you have python installed, tested on 3.9+

run 'run_setup.py' in the root directory to populate json files and secret .env files
for email and text automation

' python3 run_setup.py '

### If using Mac:
Must also have HomeBrew Installed and install:

'brew install freetds'
### IF using Linux:
Must also install freetds, package manager is unique per distro.

-----------------------------------------------

## CONFIG:
After setup. See "Secret/" in project root to fill out 
- db_secret.env : Stores login info for an MS SQL DB.
- mail_secret.env : Stores login info for automation of sending emails.
- text_secret.env : stores login info for automation of sending texts.

------------------------------------------------------------------------------

# UseCase:

## "ComeToTheGame"
For bulk messaging (email/text) people:  
In project root:  
' python3 run_message_people.py '

## "AtTheGame"
launches website on localhost:  
In project root:  
' python3 run_main_website.py '