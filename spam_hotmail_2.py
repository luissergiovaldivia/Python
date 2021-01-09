import smtplib

#user = 'luissergiovaldivia52@gmail.com'
#password = '156780240'

user = 'luis_sergio_valdivia@hotmail.com'
password = 'Muplsv835'


send_from = user
to = ['luis_sergio_valdivia@hotmail.com']
subject = 'prueba'
body = 'este es un mail de prueba'  


email_text = """\
From: %s
To: %s
Subject: %s

%s
""" %(send_from, ",". join(to), subject, body)

try:
	smtp_srv = 'smtp-mail.outlook.com'
	#smtp_srv = 'smtp.live.com'
	#smtp_srv = 'smtp.gmail.com'

	#server = smtplib.SMTP_SSL('smtp.gmail.com' , 465)
	#server = smtplib.SMTP('smtp.live.com',587)
	server = smtplib.SMTP(smtp_srv,587)
	
	server.ehlo()
	#server.starttls()
	server.starttls()
	server.ehlo()
	server.login(user, password)
	#....send emails
	server.sendmail(send_from, to, email_text)
	server.quit()
	server.close()

	print ('Email sent!')

except:
	print ('Something went wrong ....')