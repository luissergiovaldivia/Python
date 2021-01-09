import smtplib

user = 'luissergiovaldivia52@gmail.com'
password = '156780240'

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
	server = smtplib.SMTP_SSL('smtp.gmail.com' , 465)
	server.ehlo()
	#server.starttls()
	server.login(user, password)
	#....send emails
	server.sendmail(send_from, to, email_text)
	server.close()

	print ('Email sent!')

except:
	print ('Something went wrong ....')