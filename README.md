# KSUHackathonSpring2025
### Everything in this repo was created within 30~ hours for a Hackathon.

-----------------------------------------------
## Overview:
Our group's work for the KSU Sports Innovation Hackathon in Feb 2025.  
We placed first for the 'Fan Engagement' section.

Justin Owen: front end web dev  
Katherine smith: front end web dev, interface with the back end  
Jean-Jacques Mutumbo: cloud DB management  
Steven Naliwajka: back end  

[PPT Presentation](https://github.com/StevenNaliwajka/KSUHackathonSpring2025/blob/main/KSU%20Hackathon%20February%202025%20Presentation.pdf)  
[Demo Video](https://youtu.be/4KzcPm3jDe8)
-----------------------------------------------
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