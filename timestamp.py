# This is how you can store an audio file you get from the browser
# and later retrieve it from the server, based on a timestamp
# (this assumes that you won't get more than one audio file per second)


from datetime import datetime

# Get the current date and time
now = datetime.now()

# Convert the current date and time into a string
timestamp = now.strftime("%Y%m%d%H%M%S")

print("Timestamp:", timestamp)

AUDIO_FOLDER = "audio"
# save file with timestamp as audio
file_name = f"{AUDIO_FOLDER}/audio_{timestamp}.wav"
# write audio

# store timestamp in your datastructure for the chat 
chat_dict = {"text:": "hello", "audio": timestamp}

# to read the audio file re-create the file name
file_name = f"{AUDIO_FOLDER}/audio_{timestamp}.wav"
# read audio