import smtplib
from smtplib import SMTP

#import smtplib

user = "luis_sergio_valdivia@hotmail.com"
password = "Muplsv835"

#servidor = smtplib.SMTP("smtp.live.com",587)
#smtp_srv = "smtp.live.com"
smtp_srv = 'smtp-mail.outlook.com'
servidor = smtplib.SMTP(smtp_srv, 587)
#servidor = "smtp.live.com"
remitente = 'luis_sergio_valdivia@hotmail.com'
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


	mensaje = 'From: {0}\nTo: {1}\n\n'. format (remitente, destinatario)
	mensaje += texto

	servidor.login (user, password)
	#stmp.login (user, password)
	servidor.sendmail (remitente, destinatario, mensaje)

	seguir = input('Si desea enviar otro correo pulse "s": ')

