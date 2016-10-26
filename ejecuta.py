# -*- coding: utf-8 -*-


import telebot
import time
import asis_filro
API_TOKEN = 'TuTokenVaAca' 

bot = telebot.TeleBot(API_TOKEN)
print "Sistema iniciado"
# Señal que recibe el bot al inicio
@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    bot.send_message(message.chat.id,"Bienvenido al Sistema CEUT!\nIngrese 'Menu' para empezar")



#señal que maneja los mensajes entrantes, usa lambda por comodidad y fiabilidad
@bot.message_handler(func=lambda message: True)
def echo_message(message):
        mensaje= message.text
        chat_id= message.chat.id
        
       
        print "Esta hablando una Persona con ID:" + str(chat_id)

        if mensaje == 'Hola':

                msg1 = "Bienvenido y gracias por utilizar el Servicio del CEUT! " 
                print msg1 + '-> enviado a ' + str(chat_id)
                bot.send_message(chat_id,msg1)
                
        elif mensaje == 'Menu' or mensaje.upper() == 'MENU' :
            
                msg12 = "Bienvenido!\nActualmente Disponible:"
                bot.send_message(chat_id,msg12)
                msg12 = "Asistencia de los Docentes."
                bot.send_message(chat_id,msg12)
                msg12 = "Horarios de Biblioteca"
                bot.send_message(chat_id,msg12)
                msg12 = "Servicios del Centro de Estudiantes"
                bot.send_message(chat_id,msg12)
                msg12 = "Calendario académico"
                bot.send_message(chat_id,msg12)
                msg12= 'Horarios de los Ingresantes 2017'
                bot.send_message(chat_id,msg12)
                msg12= "Planes de estudio:A)Civil.\nB)Electrónica.\nC)Electromecánica.\n"
                bot.send_message(chat_id,msg12)
                bot.send_message(chat_id,'AVISO:Los Acentos no son tenidos en cuenta en este sistema,evite el uso!')
                print '-> enviado a ' + str(chat_id)
                time.sleep(5)
                
        elif 'BIBLIOTECA' in mensaje.upper() or 'BIB' in mensaje.upper():
                bot.send_message(chat_id,'Horarios de Biblioteca')
                biblio = open('horarios.jpg','rb')
                bot.send_photo(chat_id,biblio)
                
        elif 'SERVICIOS' in mensaje.upper() or 'COSAS' in mensaje.upper():
                bot.send_message(chat_id,'Estos son nuestros servicios disponibles')
                servicios = open('servicios.jpg','rb')
                bot.send_photo(chat_id,servicios)
                
        elif 'CALENDARIO' in mensaje.upper() or 'CAL' in mensaje.upper():
                bot.send_message(chat_id,'Calendario Académico 2016-2017')
                calendario = open('calendario.jpg','rb')
                bot.send_photo(chat_id,calendario)
                print 'calendario'
                
        elif 'INGRESANTE' in mensaje.upper() or 'ALUMNOS' in mensaje.upper():
                bot.send_message(chat_id,'Ingresante: Estos son tus horarios para el 2017:')
                ing1 = open('ingresantes1.jpg','rb')
                ing2 = open('ingresantes2.jpg','rb')
                bot.send_photo(chat_id,ing1)
                bot.send_photo(chat_id,ing2)
                print 'Consulto ingresante'
                
        elif 'ELECTRONICA' in mensaje.upper():
                send= 'PLAN: Electrónica\nDescargar aquí: '
                bot.send_message(chat_id,send)
                bot.send_message(chat_id,'https://mega.nz/')
                print 'repartio plan electronica'
                
        elif 'CIVIL' in mensaje.upper() or 'CIV' in mensaje.upper():
                send= 'PLAN: Civil\nDescargar aquí: '
                bot.send_message(chat_id,send)
                bot.send_message(chat_id,'https://mega.nz/')
                print 'repartio plan civil'
                
        elif 'ELECTROMECANICA' in mensaje.upper():
                send= 'PLAN: Electromecánica\nDescargar aquí: '
                bot.send_message(chat_id,send)
                bot.send_message(chat_id,'https://mega.nz/')
                print 'repartio plan electromecanica'
                
        elif 'ID?' in mensaje.upper():
                send= 'Tu ID de Telegram es: ' + str(chat_id)
                bot.send_message(chat_id,send)
                
        elif 'ASISTENCIA' in mensaje.upper() or 'PROFESORES' in mensaje.upper():
                bot.send_message(chat_id,'Personal Docente:')
                general = ''
                post = asis_filro.asistencia()
                if len(post) < 1:
                    bot.send_message(chat_id,'El servicio de Asistencia esta fallando por cuestiones ajenas al CEUT o no hay docentes presentes.')
                else:
                    
                    for lista in post:
                        general += lista+'\n'
                    bot.send_message(chat_id, general)
                    bot.send_message(chat_id,'La lista se actualiza constantemente.\nPor favor, no abuse el sistema de consultas.')        
                    print 'Consultaron docentes'
                
                
        else:
                msg104 = " No lo he entendido...\nPara mas opciones, manda un mensaje con la palabra Menu "
                bot.send_message(chat_id,msg104)
                print '-> enviado a ' + str(chat_id)
    
  
bot.polling()
