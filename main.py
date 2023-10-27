# from flask import Flask, request, render_template, redirect, url_for, session
# from flask_socketio import SocketIO, join_room, leave_room, send

# from utils import generate_room_code


# app = Flask(__name__)
# app.config['SECRET_KEY'] = 'SDKFJSDFOWEIOF'
# socketio = SocketIO(app)

# rooms = {}


# @app.route('/', methods=["GET", "POST"])
# def home():
#     session.clear()

#     if request.method == "POST":
#         name = request.form.get('name')
#         create = request.form.get('create', False)
#         code = request.form.get('code')
#         join = request.form.get('join', False)

#         if not name:
#             return render_template('home.html', error="Name is required", code=code)

#         if create != False:
#             room_code = generate_room_code(6, list(rooms.keys()))
#             new_room = {
#                 'members': 0,
#                 'messages': []
#             }
#             rooms[room_code] = new_room

#         if join != False:
#             # no code
#             if not code:
#                 return render_template('home.html', error="Please enter a room code to enter a chat room", name=name)
#             # invalid code
#             if code not in rooms:
#                 return render_template('home.html', error="Room code invalid", name=name)

#             room_code = code

#         session['room'] = room_code
#         session['name'] = name
#         return redirect(url_for('room'))
#     else:
#         return render_template('home.html')


# @app.route('/')
# def room():
#     room = ''
#     name = 'Multimodal Chat'

#     # if name is None or room is None or room not in rooms:
#     #     return redirect(url_for('home'))

#     messages = rooms[room]['messages']
#     return render_template('room.html', room=room, user=name, messages=messages)


# @socketio.on('connect')
# def handle_connect():
#     name = session.get('name')
#     room = session.get('room')

#     if name is None or room is None:
#         return
#     if room not in rooms:
#         leave_room(room)

#     join_room(room)
#     send({
#         "sender": "",
#         "message": f"{name} has entered the chat"
#     }, to=room)
#     rooms[room]["members"] += 1


# @socketio.on('message')
# def handle_message(payload):
#     room = session.get('room')
#     name = session.get('name')

#     if room not in rooms:
#         return

#     message = {
#         "sender": name,
#         "message": payload["message"]
#     }
#     send(message, to=room)
#     rooms[room]["messages"].append(message)


# @socketio.on('disconnect')
# def handle_disconnect():
#     room = session.get("room")
#     name = session.get("name")
#     leave_room(room)

#     if room in rooms:
#         rooms[room]["members"] -= 1
#         if rooms[room]["members"] <= 0:
#             del rooms[room]

#     send({
#         "message": f"{name} has left the chat",
#         "sender": ""
#     }, to=room)


# if __name__ == '__main__':
#     socketio.run(app, debug=True, allow_unsafe_werkzeug=True)


from flask import Flask, jsonify, request, render_template, redirect, send_from_directory, url_for, session
from flask_socketio import SocketIO, send
from gtts import gTTS
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'SDKFJSDFOWEIOF'
socketio = SocketIO(app)

# Define the directory for audio files
audio_directory = os.path.join(app.root_path, 'static', 'audio')
if not os.path.exists(audio_directory):
    os.makedirs(audio_directory)

audio_messages = []

@app.route('/')
def chat():
    name = session.get('name')
    if name is None:
        return redirect(url_for('enter_name'))

    messages = []  # Replace with your logic to retrieve messages
    return render_template('room.html', user=name, messages=audio_messages)


@app.route('/enter_name', methods=['GET', 'POST'])
def enter_name():
    if request.method == 'POST':
        name = request.form.get('name')
        if name:
            session['name'] = name
            return redirect(url_for('chat'))

    # Create an 'enter_name.html' template for entering the name
    return render_template('enter_name.html')


@app.route('/text-to-speech', methods=['POST'])
def text_to_speech():
    try:
        message = request.form.get('message-input')
        print('msg', message)
        if message:
            # Create a unique filename for each audio message
            output_filename = f'output_{len(audio_messages) + 1}.ogg'
            output_audio_path = os.path.join(audio_directory, output_filename)
            # Convert the message to speech using gTTS
            tts = gTTS(message, lang='en')
            tts.save(output_audio_path)
            # Add the new audio message to the audio_messages list
            audio_messages.append(output_filename)
            # Limit the list to store only the last 5 audio messages
            if len(audio_messages) > 5:
                old_audio_filename = audio_messages.pop(0)
                old_audio_path = os.path.join(audio_directory, old_audio_filename)
                os.remove(old_audio_path)  # Remove the oldest message
            return jsonify({'recognized_text': message, 'user_audio': output_filename})
        else:
            return jsonify({'error': 'No text to speak'})
    except Exception as e:
        return jsonify({'error': str(e)})
    
@app.route('/get-audio/<filename>')
def get_audio(filename):
    return send_from_directory(audio_directory, filename)

@app.route('/get-audio-messages', methods=['GET'])
def get_audio_messages():
    return jsonify({'audio_messages': audio_messages})

@socketio.on('connect')
def handle_connect():
    name = session.get('name')
    send({
        "sender": "",
        "message": f"{name} has entered the chat"
    })


@socketio.on('message')
def handle_message(payload):
    name = session.get('name')
    message = {
        "sender": name,
        "message": payload["message"]
    }
    send(message)


@socketio.on('disconnect')
def handle_disconnect():
    name = session.get('name')
    send({
        "message": f"{name} has left the chat",
        "sender": ""
    })


if __name__ == '__main__':
    socketio.run(app, debug=True, allow_unsafe_werkzeug=True)
