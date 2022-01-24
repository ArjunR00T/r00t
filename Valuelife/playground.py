from __future__ import print_function


from datetime import datetime,timedelta
import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/calendar']


def convert24(str1):
      
    # Checking if last two elements of time
    # is AM and first two elements are 12
    if str1[-2:] == "AM" and str1[:2] == "12":
        time= "00" + str1[2:-2]
          
    # remove the AM    
    elif str1[-2:] == "AM":
        time= str1[:-2]
      
    # Checking if last two elements of time
    # is PM and first two elements are 12   
    elif str1[-2:] == "PM" and str1[:2] == "12":
        time= str1[:-2]
          
    else:
        # add 12 to hours and remove PM
        time= str(int(str1[:2]) + 12) + str1[2:6]
    h=time.split(':')[0]
    m=time.split(':')[1]

    return int(h),int(m)

convert24('10:00 PM')


def formatDate(d):
    date=d.split('-')
    y=date[0]
    m=date[1]

    if m[0]=='0':
        m=m[1:]

    dy=d[-2:]

    int(y),int(m),int(dy)


def calendar():

   # y,m,dy=formatDate(d)
   # hour,mint=convert24(t)


    #stime=datetime(y,m,dy,hour,mint,0)
   # etime=datetime(y,m,dy,hour,mint,0)+timedelta(minutes=60)
   # print(stime.strftime("%Y-%m-%dT%H:%M:%S"))
    event = {
  'summary': 'Appointment at ValueLife',
  'location': 'Bengluru,Karanataka',
  'description': 'You have your appointment in 30 Mins',
  'start': {
    'dateTime':'2022-01-18T22:50:00',
    'timeZone':'Asia/Kolkata',
  },
  'end': {
    'dateTime': '2022-01-18T23:00:00',
    'timeZone': 'Asia/Kolkata',
  },
  
  'attendees': [

   
  ],
  'reminders': {
    'useDefault': False,
    'overrides': [
      {'method': 'email', 'minutes': 24*60},
      {'method': 'popup', 'minutes': 10},
    ],
  },
}

    """Shows basic usage of the Google Calendar API.
    Prints the start and name of the next 10 events on the user's calendar.
    """
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'client_sec.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    try:
        service = build('calendar', 'v3', credentials=creds)

        # Call the Calendar API
        '''
        now = datetime.utcnow().isoformat() + 'Z'  # 'Z' indicates UTC time
        print('Getting the upcoming 10 events')
        events_result = service.events().list(calendarId='primary', timeMin=now,
                                              maxResults=10, singleEvents=True,
                                              orderBy='startTime').execute()
        events = events_result.get('items', [])

        if not events:
            print('No upcoming events found.')
            return

        # Prints the start and name of the next 10 events
        for event in events:
            start = event['start'].get('dateTime', event['start'].get('date'))
            print(start, event['summary'])

        '''
            
        event = service.events().insert(calendarId='primary', body=event,sendUpdates='all',sendNotifications= True).execute()
        updated_event = service.events().update(calendarId='primary', eventId=event['id'],sendUpdates='all', body=event,sendNotifications= True).execute()

        print ('Event created: %s' % (event.get('htmlLink')))
        
    except HttpError as error:
        print('An error occurred : %s' % error)

calendar()

