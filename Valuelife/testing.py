
import firebase_admin
from firebase_admin import credentials, messaging,storage
from firebase_admin import db
from datetime import datetime,timedelta
import calendar

cred = credentials.Certificate("/home/r00t/Downloads/pkey.json")
firebase_admin.initialize_app(cred, {
      'databaseURL': 'https://valuelife1-4fa75-default-rtdb.firebaseio.com/',
  })
d=db.reference('services/')
d=(d.get())
d=d['Dr Jasna Sushanth(Online)']
for k,v in d.items():
      print(k[2:])
      print(v)
'''

data=(diet_ref).get()
print(data)
for k,v in data.items():
      t.append((v['time']))
'''


'''
def calcDate():
      base = datetime.today()
      print('b: ',base)
      for x in range(0,30):
            date=str(base + timedelta(days=x))
            date=date.split(" ",1)[0]
            dateList.append(date)

#calcDate()

def cl():
      availabe_dates={}
      
      for d in dateList:
            dy= (calendar.day_name[(datetime.strptime(d,'%Y-%m-%d')).weekday()])
            if dy!='Wednesday' and len(availabe_dates)!=15:
                  availabe_dates[d]=dy[0:3]
      return availabe_dates


#print(cl())
'''
'''
diet_ref.update({
      'Dietician':
      {
            'name':'namme',
            'age':'age',
            'date':'date'
            
      }
      })
'''
'''
from datetime import datetime, timedelta

def datetime_range(start, end, delta):
    current = start
    while current <= end:
        yield current
        current += delta

def create():
      a=datetime.strftime(datetime.now(),'%H:%M')
      a1=datetime.strftime(datetime.now(),'%I:%M %p')
      date=datetime.strftime(datetime.today(),'%Y-%m-%d')
      print('Today: ',date)
      h=a[0:2]
     
     
      dts = [dt.strftime('%I:%M %p') for dt in 
             datetime_range(datetime(2022, 1, 1,7), datetime(2022, 1, 1,21), 
             timedelta(minutes=15))]

      print(dts)
      new=[]
      for d in dts:
            if datetime.strptime(d,'%I:%M %p') > datetime.strptime(a1,'%I:%M %p'):
                  new.append(d)

      print('-----------------------')
      print(new)

create()
'''
'''
name='test'
mail='test'
age='test'
typ='test'
time='test'
date='test'

diet_ref=db.reference('Appointments/Yoga')
diet_ref.update({
time:
{
'name':name,
'mail':mail,
'age':age,
'typ':typ,
'time':time,
'date':date,
'conf':'test'
}
})
'''
'''
diet_ref=db.reference('Appointments/Accupunture')
diet_ref.update({
time:
{
'name':name,
'mail':mail,
'age':age,
'typ':typ,
'time':time,
'date':date,
}

})

diet_ref=db.reference('Appointments/DrRaheema')
diet_ref.update({
time:
{
'name':name,
'mail':mail,
'age':age,
'typ':typ,
'time':time,
'date':date,
}

})

diet_ref=db.reference('Appointments/DrHasan')
diet_ref.update({
time:
{
'name':name,
'mail':mail,
'age':age,
'typ':typ,
'time':time,
'date':date,
}

})

diet_ref=db.reference('Appointments/ClinicOnline')
diet_ref.update({
time:
{
'name':name,
'mail':mail,
'age':age,
'typ':typ,
'time':time,
'date':date,
}

})
diet_ref=db.reference('Appointments/DrJasnaOnline')
diet_ref.update({
time:
{
'name':name,
'mail':mail,
'age':age,
'typ':typ,
'time':time,
'date':date,
}

})

diet_ref=db.reference('Appointments/DrJasnaF2F')
diet_ref.update({
time:
{
'name':name,
'mail':mail,
'age':age,
'typ':typ,
'time':time,
'date':date,
}

})

diet_ref=db.reference('Appointments/Dietician')
diet_ref.update({
time:
{
'name':name,
'mail':mail,
'age':age,
'typ':typ,
'time':time,
'date':date,
}

})



name='test'
mail='test'
age='test'
typ='test'
time='test'
date='test'

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
mail_content = 'Name:'+name+',\n'+'Age:'+age+',\n'+'Mail:'+mail+',\n'+'Appoitment for:'+typ+',\n'+'Time:'+time+',\n'+'Date:'+date+','

#The mail addresses and password
sender_address = 'valuelife008@gmail.com'
sender_pass = '123valuelife123'
receiver_address = 'achg904@gmail.com'
#Setup the MIME
message = MIMEMultipart()
message['From'] = sender_address
message['To'] = receiver_address
message['Subject'] = 'New Appoitment'   #The subject line
#The body and the attachments for the mail
message.attach(MIMEText(mail_content, 'plain'))
#Create SMTP session for sending the mail
session = smtplib.SMTP('smtp.gmail.com', 587) #use gmail with port
session.starttls() #enable security
session.login(sender_address, sender_pass) #login with mail_id and password
text = message.as_string()
session.sendmail(sender_address, receiver_address, text)
session.quit()
print('Mail Sent')

'''
'''
if 'Dietician' in request.POST:
                  dayCheck=['Tuesday','Friday','Sunday']
                  ref=db.reference('Appointments/Dietician')
                  serv='Value Life Dietician'
                  t_range=15

            if 'jsf2f' in request.POST:
                  dayCheck=['Sunday']
                  ref=db.reference('Appointments/DrJasnaF2F')
                  serv='Dr.Jasna Sushanth(F2F)' 
                  t_range=15

            if 'jso' in request.POST:
                  dayCheck=['Friday']
                  ref=db.reference('Appointments/DrJasnaOnline')
                  serv='Dr.Jasna Sushanth(Online)' 
                  t_range=15

            if 'clinicO' in request.POST:
                  dayCheck=['Monday','Tuesday','Thursday','Friday','Saturday','Sunday']
                  ref=db.reference('Appointments/ClinicOnline')
                  serv='ValueLife Clinic(Online)'
                  t_range=15

            if 'clinic' in request.POST:
                  dayCheck=['Monday','Tuesday','Thursday','Friday','Saturday','Sunday']
                  ref=db.reference('Appointments/Clinic')
                  serv='ValueLife Clinic(F2F)'
                  t_range=15

            if 'hasan' in request.POST:
                  dayCheck=['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday']
                  ref=db.reference('Appointments/DrHasan')
                  serv='Dr.Hasan Psychiatry & Male Disorders(Online)'
                  t_range=15

            if 'raheema' in request.POST:
                  dayCheck=['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday']
                  ref=db.reference('Appointments/DrRaheema')
                  serv='Dr.Raheema Skin Disorders(Online)' 
                  t_range=15

            if 'accu' in request.POST:
                  dayCheck=['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday']
                  ref=db.reference('Appointments/Accupunture')
                  serv='Accupunture Home Visit'
                  t_range=15

            if 'yoga' in request.POST:
                  dayCheck=['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday']
                  ref=db.reference('Appointments/Yoga')
                  serv='Exercise,Yoga and pilates Trainer(Online)'
                  t_range=15
'''