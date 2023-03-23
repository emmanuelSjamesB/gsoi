

from django.shortcuts import render
from django.contrib import messages
from django.core.mail import EmailMultiAlternatives
from django.conf import settings
from django.template.loader import render_to_string
from crud.settings import EMAIL_HOST_USER,EMAIL_RE



def home(request):
    return render(request, 'base.html',{})

def about(request):
    return render(request, 'about.html',{})

def cliente(request):
    return render(request, 'client.html',{})

def hero(request):
    return render(request, 'hero.html',{})

import time

def contact(request):
    # Obtener la hora actual
    current_time = int(time.time())
    # Obtener la hora en que se envió el último mensaje desde la sesión
    last_message_time = request.session.get('last_message_time', 0)
    # Obtener el número de mensajes enviados desde la sesión
    num_messages_sent = request.session.get('num_messages_sent', 0)
    
    if request.method == 'POST':
        if num_messages_sent >= 3 and current_time - last_message_time < 4 * 60 * 60:
            # Si se han enviado más de 3 mensajes en las últimas 4 horas, mostrar un mensaje de error
            messages.error(request, 'Ha superado el límite de mensajes que puede enviar.')
            return render(request, 'base.html')
        elif num_messages_sent >= 3:
            # Si se han enviado más de 3 mensajes pero han pasado más de 4 horas, reiniciar el contador
            num_messages_sent = 0
        
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        subject = request.POST.get('subject', '')
        message = request.POST.get('message', '')
        from_email = settings.EMAIL_HOST_USER
        if subject and message and from_email and name and email:
            try:
                # Renderizamos el cuerpo del mensaje con una plantilla HTML
                html_content = render_to_string('email_template.html', {'name': name, 'email':email, 'message': message})
                # Creamos el mensaje
                msg = EmailMultiAlternatives(subject, '', from_email, [settings.EMAIL_RE])
                # Agregamos el cuerpo del mensaje HTML y texto plano
                msg.attach_alternative(html_content, "text/html")
                msg.send()
            except Exception as e:
                # Si ocurre un error, mostramos un mensaje de error
                messages.error(request, 'Ocurrió un error al enviar el correo electrónico: ' + str(e))
            else:
                # Si todo está bien, mostramos un mensaje de éxito y actualizamos los contadores
                num_messages_sent += 1
                request.session['num_messages_sent'] = num_messages_sent
                request.session['last_message_time'] = current_time
                messages.success(request, 'El correo electrónico fue enviado correctamente.')
                return render(request, 'base.html', {'success_message': 'El correo electrónico fue enviado correctamente.'})
        else:
            return render(request, 'base.html')
    else:
        return render(request, 'base.html')


''' ultimo codigo funcionando >> def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        subject = request.POST.get('subject', '')
        message = request.POST.get('message', '')
        from_email = settings.EMAIL_HOST_USER
        if subject and message and from_email and name and email:
            try:
                # Renderizamos el cuerpo del mensaje con una plantilla HTML
                html_content = render_to_string('email_template.html', {'name': name, 'email':email, 'message': message})
                # Creamos el mensaje
                msg = EmailMultiAlternatives(subject, '', from_email, [settings.EMAIL_RE])
                # Agregamos el cuerpo del mensaje HTML y texto plano
                msg.attach_alternative(html_content, "text/html")
                msg.send()
            except Exception as e:
                # Si ocurre un error, mostramos un mensaje de error
                messages.error(request, 'Ocurrió un error al enviar el correo electrónico: ' + str(e))
            else:
                # Si todo está bien, mostramos un mensaje de éxito
                messages.success(request, 'El correo electrónico fue enviado correctamente.')
                return render(request, 'base.html', {'success_message': 'El correo electrónico fue enviado correctamente.'})
        else:
            return render(request, 'base.html')
    else:
        return render(request, 'base.html')'''


