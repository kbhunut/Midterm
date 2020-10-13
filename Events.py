from abc import ABC, abstractmethod

class Events:
    _id = None
    _events = list()
    _recommendation_engine = None

    def attach(self, recommendation):
        self._recommendation_engine = recommendation

    def detach(self):
        self._recommendation_engine = None

    def notify(self):
        print("Notifying recommendation engine")
        self._recommendation_engine.update(self)

    def append(self, event):
        print("Adding Event")
        self._events.append(event)
        self.notify()
    def remove(self, event):
        self._events.remove(event)


class Event:
    _id = None
    _name =None
    _startDate = None
    _endDate = None
    _note = None
    _location = None
    _invitation = list()

    def __init__(self, id, name):
        self._id = id
        self._name = name

    def get_name(self):
        return self._name
    def set_name(self, name):
        self._name = name

    def get_startDate(self):
        return self._startDate

    def set_startDate(self, startDate):
        self._startDate = startDate

    def get_endDate(self):
        return self._endDate

    def set_endDate(self, endDate):
        self._endDate = endDate

    def get_location(self):
        return self._location

    def set_location(self, location):
        self._location = location


    def get_note(self):
        return self._note

    def set_note(self, note):
        self._note = note

    def append_invitation(self, invite):
        self._invitation.append(invite)

    def remove_invitation(self, invite):
        self._invitation.remove(invite)

    def get_invitation_list(self):
        return self._invitation

    def __str__(self):
        return "Event: %s from %s to %s @ Location: %s" % (self.get_name(), self.get_startDate(), self.get_endDate(), self.get_location())

class Recommendation(ABC):

    @abstractmethod
    def update(self, events: Events) -> None:
        pass


class RecommendationEngineA(Recommendation):
    def update(self, events: Events) -> None:
        print("You might also like to go to this event ???????")
