from abc import ABC, abstractmethod
class DAO (ABC):
    @abstractmethod
    def insert(self, payload):
        pass
    @abstractmethod
    def delete(self, payload):
        pass
    @abstractmethod
    def update(self, payload):
        pass
    def get_list(self):
        pass
    @abstractmethod
    def findByID(self, id):
        pass

class UserDAO(DAO):
    def insert(self, payload):
        print("Insert User")

    def delete(self, payload):
        print("Delete User")

    def update(self, payload):
        print("Update User")

    def get_list(self):
        print("Get list of User")

    def findByID(self, id):
        print("Find User by ID")


class InvitationDAO(DAO):
    def insert(self, payload):
        print("Insert Invitation")

    def delete(self, payload):
        print("Delete Invitation")

    def update(self, payload):
        print("Update Invitation")

    def get_list(self):
        print("Get list of Invitation")

    def findByID(self, id):
        print("Find Invitation by ID")


class EventsDAO(DAO):
    def insert(self, payload):
        print("Insert Events")

    def delete(self, payload):
        print("Delete Events")

    def update(self, payload):
        print("Update Events")

    def get_list(self):
        print("Get list of Events")

    def findByID(self, id):
        print("Find Events by ID")


class EventDAO(DAO):
    def insert(self, payload):
        print("Insert Event")

    def delete(self, payload):
        print("Delete Event")

    def update(self, payload):
        print("Update Event")

    def get_list(self):
        print("Get list of Event")

    def findByID(self, id):
        print("Find Event by ID")
