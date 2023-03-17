

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

def contact(request):
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
        return render(request, 'base.html')



'''
from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail, BadHeaderError
from django.contrib import messages
from django.conf import settings

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        subject = request.POST.get('subject', '')
        message = request.POST.get('message', '')
        from_email = settings.EMAIL_HOST_USER
        if subject and message and from_email and name and email:
            try:
                message_body = f"Nombre: {name}\nCorreo: {email}\nMensaje: {message}"
                send_mail(subject, message_body, from_email, [settings.EMAIL_RE])
            except BadHeaderError:
                messages.error(request, 'El asunto del correo electrónico es inválido.')
            except Exception as e:
                messages.error(request, 'Ocurrió un error al enviar el correo electrónico: ' + str(e))
            else:
                messages.success(request, 'El correo electrónico fue enviado correctamente.')
                return render(request, 'base.html', {'success_message': 'El correo electrónico fue enviado correctamente.'})
        else:
            return render(request, 'base.html')
    else:
        return render(request, 'base.html')'''

'''
def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        subject = request.POST.get('subject', '')
        message = request.POST.get('message', '')
        from_email = EMAIL_HOST_USER
        if subject and message and from_email and name and email:
            try:
                message_body = f"Nombre: {name}\nCorreo: {email}\nMensaje: {message}"
                send_mail(subject, message_body, from_email, [EMAIL_RE])
            except BadHeaderError:
                    messages.error(request, 'El asunto del correo electrónico es inválido.')
            except Exception as e:
                    messages.error(request, 'Ocurrió un error al enviar el correo electrónico: ' + str(e))
            else:
                messages.success(request, 'El correo electrónico fue enviado correctamente.')
                return HttpResponse('El correo electrónico fue enviado correctamente.')
        else:
            return render(request, '#contact')
'''



'''
def enviar_correo(request):
    if request.method == 'POST':
        asunto = request.POST.get('asunto', '')
        mensaje = request.POST.get('mensaje', '')
        correo_remitente = request.POST.get('correo_remitente', '')
        

        try:
            send_mail(asunto, mensaje, correo_remitente, [EMAIL_RE], fail_silently=False)
        except BadHeaderError:
            messages.error(request, 'El asunto del correo electrónico es inválido.')
        except Exception as e:
            messages.error(request, 'Ocurrió un error al enviar el correo electrónico: ' + str(e))
        else:
            messages.success(request, 'El correo electrónico fue enviado correctamente.')
            return HttpResponse('El correo electrónico fue enviado correctamente.')
    else:
        return render(request, 'formulario_correo.html')
'''
