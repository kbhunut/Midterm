import enum

class ResponseType(enum.Enum):
    No = 0
    Yes = 1
    Maybe = 2
    Pending = 3

class Invitation:
    _id = None
    _eventID = None
    _userID = None
    _response = None

    def __init__(self, eventID, userID):
        self._eventID = eventID
        self._userID = userID
        self._response = ResponseType.Pending

    def set_response(self, response):
        self._response = ResponseType[response]

    def get_respose(self):
        return self._response.name

    def __str__(self):
        return "EventID: %s | UserID: %s | Response: %s " % (self._eventID, self._userID, self.get_respose())


