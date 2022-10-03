# MidJourney-Scraper
A Python Script to Download all MidJourney renders from any user, writtin in python and easy to use.

- Easy to identify english named files
- Downloads all files on all pages for any midjourny user.
- keeps json metadata and command used to render in a seperate .json file
- Only downloads new files, can be run more than once to keep sync.

This will download all of the midjourny renders.  All you need to do is provide a user id and your session id from your browser.

If you add this to the top of the sync.py script then it only needs to be added once:
SESSION_TOKEN = "eyJ..."
USER_ID = "4.."

To get the session id go into the developer tools. CLick on the application tab winthin the developer tool bar,  click on cookes on the left and use
__Secure-next-auth.session-token cookie. 

If you don't provide a userid it will download your own files.
