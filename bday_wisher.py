import datetime
def date_of_today():
    return str(datetime.date.today().day)+'-'+str(datetime.date.today().month)

def find_bdayboy():
    names=[]
    bday_list = {'name1': '28-5', 'name2': '18-5'}
    email_list = {'name1': 'name1@gmail.com', 'name2': 'name2@gmail.com'}
    for name,dte in bday_list.items():
        if date_of_today() == dte:
            names.append(name)


    print names
    if not names:
        print "code to exit"

    for name in names:
        email_id=email_list[name]
        print email_id
        import email


        from email.MIMEMultipart import MIMEMultipart
        from email.MIMEText import MIMEText
        from email.MIMEImage import MIMEImage


        # Define these once; use them twice!
        strFrom = 'from@gmail.com'
        strTo = email_id

        # Create the root message and fill in the from, to, and subject headers
        msgRoot = MIMEMultipart('related')
        msgRoot['Subject'] = 'Happy Birthday Dear' + name
        msgRoot['From'] = strFrom
        msgRoot['To'] = strTo
        msgRoot.preamble = 'This is a multi-part message in MIME format.'

        # Encapsulate the plain and HTML versions of the message body in an
        # 'alternative' part, so message agents can decide which they want to display.
        msgAlternative = MIMEMultipart('alternative')
        msgRoot.attach(msgAlternative)

        msgText = MIMEText('This is the alternative plain text message.')
        msgAlternative.attach(msgText)

        # We reference the image in the IMG SRC attribute by the ID we give it below
        msgText = MIMEText('<b> <h2>From me ;-) !!! </h2></b> <br><img src="cid:image1">', 'html')
        msgAlternative.attach(msgText)

        # This example assumes the image is in the current directory
        fp = open('Happy-Birthday-Wishes-Images-Hd-15.jpg', 'rb')
        msgImage = MIMEImage(fp.read())
        fp.close()

        # Define the image's ID as referenced above
        msgImage.add_header('Content-ID', '<image1>')
        msgRoot.attach(msgImage)

        # Send the email (this example assumes SMTP authentication is required)
        import smtplib
        smtp = smtplib.SMTP("smtp.gmail.com",587)
        smtp.starttls()
        #smtp.connect('smtp.gmail.com',587)
        smtp.login('username', 'password')
        smtp.sendmail(strFrom, strTo, msgRoot.as_string())
        smtp.quit()


find_bdayboy()
