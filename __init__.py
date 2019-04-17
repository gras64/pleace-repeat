from mycroft import MycroftSkill, intent_file_handler


class PleaseRepeat(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)
        data = "ich"
        self.add_event("utterance", self.puffer_data(data))

    def puffer_data(self, data):
        self.puffer = data
        self.speak(data)

    @intent_file_handler('repeat.please.intent')
    def handle_repeat_please(self, message):
        self.speak(self.puffer)


def create_skill():
    return PleaseRepeat()
