import threading
import whisper
import wave
import pyaudio
import queue
import winsound
from PyQt5 import QtCore


CHUNK_SIZE = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
SECONDS = 3.5
FILEPATH = 'data/input_rec.wav'
file_event = threading.Event()

class Speech_Recognition(QtCore.QObject, threading.Thread):
    speech_signal = QtCore.pyqtSignal()

    def __init__(self):
        super().__init__()
        self.model = whisper.load_model('base.en')
        self.result_queue = queue.Queue()

    def run(self):
        frames = self.record_audio()
        """
        self.store_input(frames)
        self.decode_input()
        result = self.decode_input()
        """
        

    def join(self):
        super().join()
        return self.result_queue.get()

    def record_audio(self):
        mic = pyaudio.PyAudio()
        stream = mic.open(format=FORMAT, channels=CHANNELS, rate=RATE, input=True,  output_device_index=0, frames_per_buffer=CHUNK_SIZE)
        frames = []
        print('recorded started')
        winsound.Beep(300, 300)
        for i in range(0, int(RATE / CHUNK_SIZE * SECONDS)):
            data = stream.read(CHUNK_SIZE)
            frames.append(data)
        winsound.Beep(300, 200)
        print('recorded ended')
        stream.stop_stream()
        stream.close()
        mic.terminate()
        threading.Thread(target=self.store_input, args=(frames, mic)).start()
        

    def store_input(self, frames, mic):
        file = wave.open(FILEPATH, 'wb')
        file.setnchannels(CHANNELS)
        file.setsampwidth(mic.get_sample_size(FORMAT))
        file.setframerate(RATE)
        file.writeframes(b''.join(frames))
        file.close()
        print('recording stored')
        file_event.set()
        threading.Thread(target=self.decode_input, args=()).start()
        

    def decode_input(self):
        file_event.wait()
        file_event.clear()
        input = whisper.load_audio(file=FILEPATH)
        input = whisper.pad_or_trim(input)
        mel = whisper.log_mel_spectrogram(input).to(self.model.device)
        options = whisper.DecodingOptions(fp16=False, language='ja')
        result = whisper.decode(model=self.model, mel=mel, options=options)
        self.speech_signal.emit()
        self.result_queue.put(result.text)
        return

        