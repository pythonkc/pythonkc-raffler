# -*- coding: utf-8 -*-
import random
import webbrowser

from pythonkc_meetups import PythonKCMeetups
from optparse import OptionParser


def raffle_time(api_key=None, event_id=None):
    client = PythonKCMeetups(api_key=api_key)
    attendees = client.get_event_attendees(event_id)
    random.seed()
    random.shuffle(attendees)
    winner = random.choice(attendees)
    if winner.photo:
        webbrowser.open_new(winner.photo.url)
    print("\n\nAnd the winner is, %s \n\n" % winner.name)


if __name__ == '__main__':
    parser = OptionParser()
    parser.add_option("-k", "--key", help="api key for meetup.com", dest="api_key", type="string")
    parser.add_option("-e", "--event_id", help="event id from meetup.com", dest="event_id",
                      type="int")
    options, args = parser.parse_args()
    raffle_time(api_key=options.api_key, event_id=options.event_id)
