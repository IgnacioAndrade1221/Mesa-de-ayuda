from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.

def index(request):
    context={}
    return render(request,'mesa_ayuda/index.html',context)

#vista para manejar las respuestas
def chat_response(request):
    user_message = request.GET.get('message')
    session = request.session

    if 'stage' not in session:
        session['stage'] = 'start'

    if session['stage'] == 'start':
        response_message = "Selecciona una opción:\n1. Agendar cita\n2. Información sobre servicios\n3. Nuestra experiencia\n4. Contacto\n5. Hablar con un asistente virtual"
        session['stage'] = 'initial_options'
    
    elif session['stage'] == 'initial_options':
        if user_message == '1':
            response_message = "Has seleccionado Agendar cita. <a href='/hora.html/' target='_blank'>Haz clic aquí para agendar tu cita.</a>"
            session['stage'] = 'start'  # Resetear la conversación después de mostrar el enlace
        elif user_message == '2':
            response_message = ("Has seleccionado Información sobre nuestros servicios.\n"
                                "Nosotros trabajamos con:\n"
                                "- Electrónica automotriz\n"
                                "- Caja de cambios\n"
                                "- Suspensión\n"
                                "- Servicio completo\n"
                                "Importante: solo trabajamos con Diesel y Bencina")
            session['stage'] = 'start'
        elif user_message == '3':
            response_message = ("Has seleccionado Nuestra experiencia. Aquí puedes ver algunos de nuestros videos:\n"
                                "<a href='https://www.youtube.com/watch?v=video_id_1' target='_blank'>Video 1</a>\n"
                                "<a href='https://www.youtube.com/watch?v=video_id_2' target='_blank'>Video 2</a>\n"
                                "<a href='https://www.youtube.com/watch?v=video_id_3' target='_blank'>Video 3</a>")
            session['stage'] = 'start'  # Resetear la conversación después de mostrar los enlaces
        elif user_message == '4':
            response_message = "Has seleccionado Contacto. Puedes contactarnos en: contacto@example.com o llamar al 123-456-7890."
            session['stage'] = 'start'
        elif user_message == '5':
            response_message = "Has seleccionado Hablar con un asistente virtual. Un momento por favor..."
            session['stage'] = 'start'
        else:
            response_message = "Opción no válida. Por favor selecciona 1, 2, 3, 4 o 5."

    else:
        response_message = "Algo salió mal. Empezamos de nuevo. Selecciona una opción:\n1. Agendar cita\n2. Información sobre servicios\n3. Nuestra experiencia\n4. Contacto\n5. Hablar con un asistente virtual"
        session['stage'] = 'start'
    
    session.save()
    return JsonResponse({'response': response_message})