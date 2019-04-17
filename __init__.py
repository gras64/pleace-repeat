from mycroft import MycroftSkill, intent_file_handler


class PleaseRepeat(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('repeat.please.intent')
    def handle_repeat_please(self, message):
        self.speak_dialog('repeat.please')


def create_skill():
    return PleaseRepeat()
