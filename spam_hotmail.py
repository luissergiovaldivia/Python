import smtplib
#from smtplib import SMTP

#import smtplib

user = "luis_sergio_valdivia@hotmail.com"
password = "Muplsv835"

send_from = user
to = ['luis_sergio_valdivia@hotmail.com']
subject = 'prueba'
body = 'este es un mail de prueba'

#servidor = smtplib.SMTP("smtp.live.com",587)
#smtp_srv = "smtp.live.com"
smtp_srv = 'smtp-mail.outlook.com'

servidor = smtplib.SMTP(smtp_srv, 587)
#servidor = "smtp.live.com"
#remitente = 'luis_sergio_valdivia@hotmail.com'
texto = 'Estimado =S =A:\n\n'
texto += 'Por la presente le informamos de que nos debe usted la'
texto += 'cantidad de =E euros. Si no abona dicha cantidad antes '
texto += 'de 3 dias, su nombre pasara a nuestra lista de morosos.'

seguir = 's'
while seguir == 's':
	destinatario = input ('Direccion del destinatario: ')
	tratmiento = input ('Tratamiento: ')
	apellido = input('Apellido: ')
	euros = input('Deuda (en euros): ')


	mensaje = 'From: {0}\nTo: {1}\n\n'. format (send_from, destinatario)
	mensaje += texto

	#servidor.login (user, password)
	#stmp.login (user, password)
	#servidor.sendmail (remitente, destinatario, mensaje)


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
		#server.sendmail(send_from, to, email_text)
		server.sendmail(send_from, to, mensaje)
		server.quit()
		server.close()

		print ('Email sent!')

	except:
		print ('Something went wrong ....')

	seguir = input('Si desea enviar otro correo pulse "s": ')

