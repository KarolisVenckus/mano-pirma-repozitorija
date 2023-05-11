import wave
import pyaudio
import threading
import tkinter as tk

# Load audio files
audio_files = {
    'sound1': 'sound1.wav',
    'sound2': 'sound2.wav',
    'sound3': 'sound3.wav'
}

# Define a function to play audio
def play_audio(filename, volume, loop):
    wf = wave.open(filename, 'rb')
    p = pyaudio.PyAudio()
    stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                    channels=wf.getnchannels(),
                    rate=wf.getframerate(),
                    output=True)

    # Set the volume
    stream.set_volume(volume)

    # Loop the audio if requested
    if loop:
        while True:
            data = wf.readframes(1024)
            if not data:
                wf.rewind()
            stream.write(data)
    else:
        data = wf.readframes(1024)
        while data:
            stream.write(data)
            data = wf.readframes(1024)

    stream.stop_stream()
    stream.close()
    p.terminate()

# Initialize PyAudio
p = pyaudio.PyAudio()

# Create a thread for each audio file
threads = []
for name, filename in audio_files.items():
    def callback():
        play_audio(filename, volume, False)
    t = threading.Thread(target=callback)
    threads.append(t)

# Define a function to start looping an audio file
def start_loop(name):
    def callback():
        play_audio(audio_files[name], volume, True)
    t = threading.Thread(target=callback)
    t.start()

# Define a function to stop looping an audio file
def stop_loop(name):
    for t in threads:
        if t._target.__name__ == 'callback' and audio_files[name] in t._args:
            t._is_stopped = True

# Define a function to set the volume
def set_volume(new_volume):
    global volume
    volume = new_volume

# Create the GUI
root = tk.Tk()
root.title('Soundboard')

# Create a volume slider
volume_scale = tk.Scale(root, from_=0, to=1, resolution=0.1, orient='horizontal', label='Volume', command=set_volume)
volume_scale.set(1)
volume_scale.pack()

# Create a button for each audio file
for name in audio_files:
    button_frame = tk.Frame(root)
    button_frame.pack(side='top', padx=10, pady=5)
    label = tk.Label(button_frame, text=name)
    label.pack(side='left')
    play_button = tk.Button(button_frame, text='Play', command=lambda name=name: threading.Thread(target=play_audio, args=(audio_files[name], volume, False)).start())
    play_button.pack(side='left', padx=10)
    loop_button = tk.Button(button_frame, text='Loop', command=lambda name=name: start_loop(name))
    loop_button.pack(side='left', padx=10)
    stop_button = tk.Button(button_frame, text='Stop', command=lambda name=name: stop_loop(name))
    stop_button.pack(side='left', padx=10)

# Start the GUI
root.mainloop()

# Clean up PyAudio
for t in threads:
    t._is_stopped = True
for t in threads:
    t.join()
p.terminate()