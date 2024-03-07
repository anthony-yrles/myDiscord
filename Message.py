class Message:
    def __init__(self, hour, author, message_text, id_room, reaction_count_1 = 0, reaction_count_2 = 0):
        self.hour = hour
        self.author = author
        self.message_text = message_text
        self.id_room = id_room
        self.reaction_count_1 = reaction_count_1
        self.reaction_count_2 = reaction_count_2

    #getter and setter for hour
    def get_hour(self):
        return self.hour
    def set_hour(self, hour):
        self.hour = hour

    #getter and setter for author
    def get_author(self):
        return self.author
    def set_author(self, author):
        self.author = author

    #getter and setter for message_text
    def get_message_text(self):
        return self.message_text
    def set_message_text(self, message_text):
        self.message_text = message_text

    #getter and setter for id_room
    def get_id_room(self):
        return self.id_room
    def set_id_room(self, id_room):
        self.id_room = id_room

    #getter and setter for reaction_count_1
    def get_reaction_count_1(self):
        return self.reaction_count_1
    def set_reaction_count_1(self, reaction_count_1):
        self.reaction_count_1 = reaction_count_1

    #getter and setter for reaction_count_2
    def get_reaction_count_2(self):
        return self.reaction_count_2
    def set_reaction_count_2(self, reaction_count_2):
        self.reaction_count_2 = reaction_count_2

    def modify_message(self, new_message):
        params = new_message, self.id
        self.client.send_data('MODIFY_MESSAGE', params)

    def modify_reaction_count(self, emoji):
        if emoji == 1:
            self.reaction_count_1 += 1
        elif emoji == 2:
            self.reaction_count_2 += 1
        params = self.reaction_count_1, self.reaction_count_2, self.id
        self.client.send_data('MODIFY_REACTION_COUNT', params)
        