
# Copyright (c) Microsoft. All rights reserved.
# Licensed under the MIT license. See LICENSE.md file in the project root for full license information.

# <code>
import time
import azure.cognitiveservices.speech as speechsdk

class VoiceCommand:
    # Creates an instance of a speech config with specified subscription key and service region.
    # Replace with your own subscription key and service region (e.g., "westus").
    # speech_key, service_region = "3c236e183b574f138845948fd63ea658", "brazilsouth"

    # speech_config = speechsdk.SpeechConfig(subscription=speech_key, region=service_region)
    # speech_config.speech_recognition_language="es-ES"
    speech_recognizer = None
    done = False
    textRecognized = ['']

    # Creates a recognizer with the given settings
    def __init__(self):
        speech_key, service_region = "3c236e183b574f138845948fd63ea658", "brazilsouth"

        speech_config = speechsdk.SpeechConfig(subscription=speech_key, region=service_region)
        speech_config.speech_recognition_language="es-ES"
        self.speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config)

        phrase_list_grammar = speechsdk.PhraseListGrammar.from_recognizer(self.speech_recognizer)
        phrase_list_grammar.addPhrase("Saltar")
        phrase_list_grammar.addPhrase("Salta")
        phrase_list_grammar.addPhrase("Inicio")

        self.done = False
        self.textRecognized = ['']

        self.speech_recognizer.recognizing.connect(lambda evt: print('RECONIZING {}'.format(evt.result.text)))
        self.speech_recognizer.recognized.connect(self.use_result_end)
        self.speech_recognizer.session_started.connect(lambda evt: print('SESSION STARTED: {}'.format(evt)))
        self.speech_recognizer.session_stopped.connect(lambda evt: print('SESSION STOPPED {}'.format(evt)))
        self.speech_recognizer.canceled.connect(lambda evt: print('CANCELAR {}'.format(evt)))

        self.speech_recognizer.session_stopped.connect(self.stop_cb)
        self.speech_recognizer.canceled.connect(self.stop_cb)

        self.speech_recognizer.start_continuous_recognition_async()

        while not self.done:
            time.sleep(.5)

    # def update(self):
    #     while not self.done:
    #         time.sleep(.5)

    # def start(self):
    #     self.speech_recognizer.start_continuous_recognition_async()


    def stop_cb(evt):
        print('CLOSING on {}'.format(evt))
        self.speech_recognizer.stop_continuous_recognition()
        # nonlocal done
        self.done = True

    def use_result(evt):
        # new_text_recognized(evt.result.text)
        # self.textRecognized[0] = evt.result.text
        print('RECONIZING {}'.format(evt.result.text))

    def use_result_end(evt):
        # new_text_recognized(evt.result.text)
        self.textRecognized[0] = ""
        # print('RECONIZED {}'.format(evt.result.text))

    def new_text_recognized(text):
        self.textRecognizing = text.replace(",", "", 1).replace(self.textRecognized[0], "", 1)
        ev = pygame.event.Event(pygame.USEREVENT, {'action': self.textRecognizing})
        pygame.event.post(ev)
        print('Command {}'.format(self.textRecognizing))




