import pyttsx3
from PyQt5 import QtCore
import winsound

class VoiceAssistance(QtCore.QObject):
    activation_signal = QtCore.pyqtSignal()
    
    def __init__(self):
        super().__init__()
        self.assistant = pyttsx3.init()
        self.assistant.setProperty('rate', 180)
        self.assistant.setProperty('voice', self.assistant.getProperty('voices')[0].id)
        self.prompt_dict = self.load_prompts()

    def speak(self, prompt: str, prompt_flag=False, signal_flag=True):
        try:
            print('Prompt Flag: ', prompt_flag)
            self.assistant.say(prompt) if prompt_flag else self.assistant.say(self.prompt_dict[prompt])
            self.assistant.runAndWait()
            (winsound.Beep(300, 300), self.assistant.say(self.prompt_dict['assistance']), self.assistant.runAndWait()) if prompt == 'intro' else None
            self.activation_signal.emit() if signal_flag else None
            return
        except RuntimeError:
            pass
        

    def load_prompts(self):
        with open('frames/prompts.txt', 'r') as file:
            prompts = file.readlines()
        prompts = [line.strip() for line in prompts]
        prompt_dict = {}
        for pr in prompts:
            key, value = pr.split(':')
            prompt_dict[key.strip()] = value.strip()
        return prompt_dict



