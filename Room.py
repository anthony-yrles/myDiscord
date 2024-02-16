class Room:
    def __init__(self, name, list_modo, list_admin, list_user):
        self.name = name
        self.list_modo = list_modo
        self.list_admin = list_admin
        self.list_user = list_user

    #getter and setter for name
    def get_name(self):
        return self.name
    def set_name(self, name):
        self.name = name

    #getter and setter for list_modo
    def get_list_modo(self):
        return self.list_modo
    def set_list_modo(self, list_modo):
        self.list_modo = list_modo

    #getter and setter for list_admin
    def get_list_admin(self):
        return self.list_admin
    def set_list_admin(self, list_admin):
        self.list_admin = list_admin

    #getter and setter for list_user
    def get_list_user(self):
        return self.list_user
    def set_list_user(self, list_user):
        self.list_user = list_user

    #create a new room
    def create_room(self, name, list_modo, list_admin, list_user):
        return Room(name, list_modo, list_admin, list_user)

    #modify the room
    def modify_room(self, name, list_modo, list_admin, list_user):
        self.name = name
        self.list_modo = list_modo
        self.list_admin = list_admin
        self.list_user = list_user

    #research a room
    def research_room(self, name):
        if self.name == name:
            return self
        else:
            return f'No room found with the name {name}'

    #delete a room
    def print_details(self):
        print(f"Room: {self.name}")
        print("Moderators:", ", ".join(self.list_modo))
        print("Admins:", ", ".join(self.list_admin))
        print("Users:", ", ".join(self.list_user))

    def delete_room(self, name, list_room):
        for room in list_room:
            if room.name == name:
                list_room.remove(room)
                return f"Room '{name}' deleted successfully."
        return f"No room found with the name '{name}'."

jjk = Room("jjk", ["walid_modo", "anthony_modo"], ["barbadmin"], ["mathis_user", "kevin_user"])
one_piece = Room("one_piece", ["walid_modo", "anthony_modo"], ["barbadmin"], ["mathis_user", "kevin_user"])
rooms = [jjk, one_piece]
print("Avant la suppression :")
for room in rooms:
    room.print_details()

result = rooms[0].delete_room("jjk", rooms)
# result1 = rooms[0].delete_room("one_piece", rooms)
print(result)
# print(result1)
print("\nAprès la suppression :")
for room in rooms:
    room.print_details()
