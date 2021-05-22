
# Copyright (c) Microsoft. All rights reserved.
# Licensed under the MIT license. See LICENSE.md file in the project root for full license information.

# <code>
import time
import pygame
import constants
import azure.cognitiveservices.speech as speechsdk
import threading

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
        # speech_key, service_region = "3c236e183b574f138845948fd63ea658", "brazilsouth"
        speech_key, service_region = "cf101b2e6c994dd1860167b3b2c283ee", "westus"

        speech_config = speechsdk.SpeechConfig(subscription=speech_key, region=service_region)
        speech_config.speech_recognition_language="es-ES"
        self.speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config)

        phrase_list_grammar = speechsdk.PhraseListGrammar.from_recognizer(self.speech_recognizer)
        phrase_list_grammar.addPhrase(constants.C_JUMP)
        phrase_list_grammar.addPhrase(constants.C_RIGHT)
        phrase_list_grammar.addPhrase(constants.C_LEFT)
        phrase_list_grammar.addPhrase(constants.C_STOP)
        phrase_list_grammar.addPhrase(constants.C_PAUSE)
        phrase_list_grammar.addPhrase(constants.C_START)
        phrase_list_grammar.addPhrase(constants.C_RESTART)
        phrase_list_grammar.addPhrase(constants.C_CONTINUE)
        phrase_list_grammar.addPhrase(constants.C_OUT)
        phrase_list_grammar.addPhrase(constants.C_CLOSE)

        self.done = False
        self.textRecognized = ['']

        self.speech_recognizer.recognizing.connect(lambda evt: self.use_result(evt))
        self.speech_recognizer.recognized.connect(lambda evt: self.use_result_end(evt))
        self.speech_recognizer.session_started.connect(lambda evt: print('SESSION STARTED: {}'.format(evt)))
        self.speech_recognizer.session_stopped.connect(lambda evt: print('SESSION STOPPED {}'.format(evt)))
        self.speech_recognizer.canceled.connect(lambda evt: print('CANCELAR {}'.format(evt)))

        self.speech_recognizer.session_stopped.connect(lambda evt: self.stop_cb(evt))
        self.speech_recognizer.canceled.connect(lambda evt: self.stop_cb(evt))

        self.speech_recognizer.start_continuous_recognition_async()

        while not self.done:
            time.sleep(.5)


    def stop_cb(self, evt):
        print('CLOSING on {}'.format(evt))
        self.speech_recognizer.stop_continuous_recognition()
        # nonlocal done
        self.done = True

    def use_result(self, evt):
        self.new_text_recognized(evt.result.text)
        self.textRecognized[0] = evt.result.text
        # print('RECONIZING {}'.format(evt.result.text))

    def use_result_end(self, evt):
        # self.new_text_recognized(evt.result.text)
        self.textRecognized[0] = ""
        # print('RECONIZED {}'.format(evt.result.text))

    def new_text_recognized(self, text):
        self.textRecognizing = text.replace(",", "", 1).replace(self.textRecognized[0], "", 1).lower()
        self.postEvent()
        # tt = threading.Thread(target=self.postEvent)
        # # # starting thread 1
        # # t1.daemon = True
        # tt.daemon = True
        # tt.start()
        

    def postEvent(self):
        if(constants.C_JUMP in self.textRecognizing):
            pygame.event.post(constants.E_JUMP)
            print('Command: {}'.format(self.textRecognizing))
        elif(constants.C_RIGHT in self.textRecognizing.lower()):
            pygame.event.post(constants.E_GO_RIGTH)
            print('Command: {}'.format(self.textRecognizing))
        elif(constants.C_LEFT in self.textRecognizing.lower()):
            pygame.event.post(constants.E_GO_LEFT)
            print('Command: {}'.format(self.textRecognizing))
        elif(constants.C_STOP in self.textRecognizing.lower()):
            pygame.event.post(constants.E_STOP)
            print('Command: {}'.format(self.textRecognizing))
        elif(constants.C_PAUSE in self.textRecognizing.lower()):
            pygame.event.post(constants.E_PAUSE)
            print('Command: {}'.format(self.textRecognizing))
        elif(constants.C_RESTART in self.textRecognizing.lower()):
            pygame.event.post(constants.E_RESTART)
            print('Command: {}'.format(self.textRecognizing))
        elif(constants.C_START in self.textRecognizing.lower()):
            pygame.event.post(constants.E_START)
            print('Command: {}'.format(self.textRecognizing))
        elif(constants.C_CONTINUE in self.textRecognizing.lower()):
            pygame.event.post(constants.E_CONTINUE)
            print('Command: {}'.format(self.textRecognizing))
        elif(constants.C_OUT in self.textRecognizing.lower()):
            pygame.event.post(constants.E_OUT)
            print('Command: {}'.format(self.textRecognizing))
        elif(constants.C_CLOSE in self.textRecognizing.lower()):
            pygame.event.post(constants.E_CLOSE)
            print('Command: {}'.format(self.textRecognizing))


