from User import UserBuilder
from Events import Event, RecommendationEngineA
from Invitation import Invitation, ResponseType
from datetime import datetime

if __name__ == "__main__":
    userBuilder = UserBuilder()
    user1 = userBuilder.create_user_full("A12345", "Kevin", "Bhunut", "kbhunut@example.com")

    print(user1)
    # Getting list of events that the users ha
    # ve
    events = user1.get_events()

    # Initialize Recommendation Engine
    events.attach(RecommendationEngineA())

    # Create New Event
    event = Event(1234, "Cat Adoption Event")
    event.set_startDate(datetime.strptime("Dec 10 2020 10:30AM", '%b %d %Y %I:%M%p'))
    event.set_endDate(datetime.strptime("Dec 10 2020 6:00PM", '%b %d %Y %I:%M%p'))
    event.set_location("San Francisco, CA")

    # Invitation
    event.append_invitation(Invitation("1234", "A12345"))
    print(event.get_invitation_list()[0])
    events.append(event)
    print(event)

    # Change Invitation Reponse
    print("Accepting Invite")
    response1 = event.get_invitation_list()[0]
    response1.set_response("Yes")

    print(event.get_invitation_list()[0])


    print("Done")

