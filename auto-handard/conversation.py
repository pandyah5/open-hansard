class Speaker:
    def __init__(self, name, party):
        self.name = name
        self.party = party

    def set_name(self, name):
        self.name = name

    def set_party(self, party):
        self.party = party

    def get_name(self):
        return self.name

class Dialogue:
    def __init__(self, speaker, conversation, conversation_summary):
        self.speaker = speaker
        self.conversation = conversation
        self.conversation_summary = conversation_summary

    def get_conversation(self):
        return self.conversation

    def set_conversation(self, conversation):
        self.conversation = conversation

    def set_summary(self, summary):
        self.conversation_summary = summary

class Collection:
    def __init__(self, title):
        self.title = title
        self.dialogues = []

    def add_dialogue(self, dialogue):
        self.dialogues.append(dialogue)