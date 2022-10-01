# MidJourney-Scraper
A Python Script to Download all MidJourney renders from a user, writtin in python and easy to use.


This will download all of the midjourny renders.  All you need to do is provide a user id and session id. 

If you add this to the top of the sync.py script then it only needs to be added once:
SESSION_TOKEN = "eyJ..."
USER_ID = "4.."

To get the session id go into the developer tools. CLick on hte application tab winthin the developer tool bar,  click on cookes on the left and use
__Secure-next-auth.session-token cookie. 