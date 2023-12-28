import pandas as pd
import datetime
import smtplib
import os
os.chdir(r"E:\python\projects\Automatic Birthday mail sending with Python")
os.mkdir("testing")

#Enter your authenticate details
GMAIL_ID = ''
GMAIL_PSWD = ''

def sendEmail(to, sub, msg):
    print(f"Email to {to} sent with subject: {sub} and {msg}")
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login(GMAIL_ID, GMAIL_PSWD)
    s.sendmail(GMAIL_ID, to , f"subject: {sub}\n\n{msg}")
    s.quit
    


if __name__ =='__main__':
    # just for testing
    sendEmail(GMAIL_ID, "subject", "Happy Birthday bro you are such an awesome friend in my life that i am send you an email on this occassion of your birthday.")

    df = pd.read_excel("data.xlsx")
    # print(df)
    today = datetime.datetime.now().strftime("%d-%m")
    # print(type(today))

    for index, item in df.iterrows():
        # print(index, item['Birthday'])
        bday = item['Birthday'].strftime("%d-%m")
        # print(bday)
        if(today == bday):
            sendEmail(item['Email'], "Happy Birthday", item['Dialogue'])