from django.shortcuts import render
from django.http import JsonResponse

def index(request):
    context = {}
    return render(request, 'mesa_ayuda/index.html', context)

def chat_response(request):
    user_message = request.GET.get('message')
    session = request.session

    # Lógica para respuestas
    if 'stage' not in session:
        session['stage'] = 'start'

    if session['stage'] == 'start':
        response_message = ("Hola! Soy un asistente virtual.<br>"
                            "Escribe el número de la opción que deseas:<br>"
                            "1. Agendar cita<br>"
                            "2. Información sobre servicios<br>"
                            "3. Nuestra experiencia<br>"
                            "4. Contacto<br>"
                            "5. Hablar con un asistente virtual<br>"
                            "6. Limpiar chat y mostrar opciones")
        session['stage'] = 'initial_options'

    elif session['stage'] == 'initial_options':
        if user_message == '1':
            response_message = ("Has seleccionado Agendar cita.<br>"
                                "<a href='/agendar-cita/' target='_blank'>Haz clic aquí para agendar tu cita.</a>")
            session['stage'] = 'start'
        elif user_message == '2':
            response_message = ("Has seleccionado Información sobre nuestros servicios.<br>"
                                "Nosotros trabajamos con:<br>"
                                "- Electrónica automotriz<br>"
                                "- Caja de cambios<br>"
                                "- Suspensión<br>"
                                "- Servicio completo<br>"
                                "Importante: solo trabajamos con Diesel y Bencina")
            session['stage'] = 'start'
        elif user_message == '3':
            response_message = ("Has seleccionado Nuestra experiencia.<br>"
                                "Aquí puedes ver algunos de nuestros videos:<br>"
                                "<a href='https://www.youtube.com/watch?v=video_id_1' target='_blank'>Video 1</a><br>"
                                "<a href='https://www.youtube.com/watch?v=video_id_2' target='_blank'>Video 2</a><br>"
                                "<a href='https://www.youtube.com/watch?v=video_id_3' target='_blank'>Video 3</a>")
            session['stage'] = 'start'
        elif user_message == '4':
            response_message = ("Has seleccionado Contacto.<br>"
                                "Puedes contactarnos en: contacto@example.com o llamar al 123-456-7890.")
            session['stage'] = 'start'
        elif user_message == '5':
            response_message = ("Has seleccionado Hablar con un asistente virtual.<br>"
                                "Un momento por favor...")
            session['stage'] = 'start'
        elif user_message == '6':
            response_message = "Has seleccionado Limpiar chat y mostrar opciones."
            session['stage'] = 'start'
            chat_history = session.get('chat_history', [])
            chat_history.clear()  # Limpiar historial del chat
        else:
            response_message = "Opción no válida. Por favor selecciona un número del 1 al 6."

    session.save()
    return JsonResponse({'response': response_message})
