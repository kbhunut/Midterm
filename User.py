from Events import Events

class User:
    _id = None
    _firstName = None
    _lastName = None
    _email = None
    _events = Events()

    def get_id(self):
        return self._id

    def set_id(self, id):
        self._id = id

    def get_firstName(self):
        return self._firstName
    def set_firstName(self, firstName):
        self._firstName = firstName

    def get_lastName(self):
        return self._firstName

    def set_lastName(self, lastName):
        self._lastName = lastName

    def get_email(self):
        return self._email

    def set_email(self, email):
        self._email = email

    def get_events(self):
        return self._events

    def set_events_collection(self, events):
        self.events = events

    def __str__(self):
        return "%s %s ( %s )" % (self.get_firstName(), self.get_lastName(), self.get_email())



class UserBuilder:

    def create_user_email_only(self, id, email):
        user = User()
        user.set_email(email)
        user.set_id(id)
        return user

    def create_user_full(self, id, firstName, lastName, email):
        user = User()
        user.set_firstName(firstName)
        user.set_lastName(lastName)
        user.set_email(email)
        user.set_id(id)
        return user
