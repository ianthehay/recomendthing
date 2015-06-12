#-*- coding: utf-8 -*-
u"""A module providing functions that generate sample data for the exercise.

.. moduleauthor:: Martí Congost <marti.congost@whads.com>
"""
from random import choice, randint
from recomendalia.user import User, FriendSuggestion
from recomendalia.concept import Concept
from recomendalia.rating import Rating
from recomendalia.relation import Relation
import collections

def generate_sample_data(
        user_count = 500,
        ratings_per_user = (8, 9, 10, 10, 11, 11, 12, 12, 13, 14, 15),
        friends_per_user = (5, 6, 7, 8, 8, 9, 9, 9, 10, 12, 15, 25)
    ):
    """Generates a list of fake users and concepts to use in the exercise.

    As well as creating a set of users and concepts, the function establishes
    friendship relations between the created users, and generates ratings for
    the created concepts at random.

    :return: A tuple with two lists: one of `User` objects, another of
        `Concept` objects.
    """
    users = []
    concepts = []

    # Create users
    user_names = set()

    for i in xrange(user_count):
        while True:
            name = random_user_name()
            if name not in user_names:
                user_names.add(name)
                break

        users.append(User(name))

    # Create concepts
    def define(*args, **kwargs):
        concept = Concept(*args, **kwargs)
        concepts.append(concept)
        return concept

    define(u"Restaurants", contains = [
        define(u"Mexican restaurants", contains = [
            define(u"La vieja cantina"),
            define(u"La Tarántula"),
            define(u"Chihuahua")
        ]),
        define(u"Italian restaurants", contains = [
            define(u"Vie Dei Mille"),
            define(u"Pizzeria Il Fuoco"),
            define(u"Pizzeria Roma")
        ]),
        define(u"Japanese restaurants", contains = [
            define(u"Asagaya"),
            define(u"Machiroku"),
            define(u"Shibui")
        ])
    ])

    miles_davis = define(u"Miles Davis")
    duke_ellington = define(u"Duke Ellington")
    john_coltrane = define(u"John Coltrane")
    eagles = define(u"Eagles")
    bruce_springsteen = define(u"Bruce Springsteen")
    rolling_stones = define(u"Rolling Stones")
    jimi_hendrix = define(u"Jimi Hendrix")
    iron_maiden = define(u"Iron Maiden")
    black_sabbath = define(u"Black Sabbath")

    define(u"Music", contains = [
        define(u"Classical", contains = [
            define(u"Beethoven"),
            define(u"Bach"),
            define(u"Strauss"),
            define(u"Mahler")
        ]),
        define(u"Jazz", contains = [
            define(u"Kind of Blue", created_by = miles_davis),
            define(u"Bitches Brew", created_by = miles_davis),
            define(u"Ellington at Newport", created_by = duke_ellington),
            define(u"A Love Supreme", created_by = john_coltrane),
            define(u"Blue Train", created_by = john_coltrane)
        ]),
        define(u"Rock", contains = [
            define(u"Hotel California", created_by = eagles),
            define(u"Born to Run", created_by = bruce_springsteen),
            define(u"Born in the U.S.A", created_by = bruce_springsteen),
            define(u"Some Girls", created_by = rolling_stones),
            define(u"Sticky Fingers", created_by = rolling_stones),
            define(u"Let it Bleed", created_by = rolling_stones),
            define(u"Are You Experienced?", created_by = jimi_hendrix),
            define(u"Electric Ladyland", created_by = jimi_hendrix),
            define(u"Heavy metal", contains = [
                define(u"The Number of the Beast", created_by = iron_maiden),
                define(u"Piece of Mind", created_by = iron_maiden),
                define(u"Fear of the Dark", created_by = iron_maiden),
                define(u"Paranoid", created_by = black_sabbath),
                define(u"The Mob Rules", created_by = black_sabbath)
            ])
        ])
    ])

    paul_thomas_anderson = define(u"Paul Thomas Anderson")
    cohen_brothers = define(u"Cohen Brothers")
    paul_verhoeven = define(u"Paul Verhoeven")
    stallone = define(u"Sylvester Stallone")
    clint_eastwood = define(u"Clint Eastwood")
    sam_mendes = define(u"American Beauty")
    scorsese = define(u"Martin Scorsese")

    define(u"Movies", contains = [
        define(u"Magnolia", created_by = paul_thomas_anderson),
        define(u"Boogie Nights", created_by = paul_thomas_anderson),
        define(u"Fargo", created_by = cohen_brothers),
        define(u"Miller's Crossing", created_by = cohen_brothers),
        define(u"Robocop", created_by = paul_verhoeven),
        define(u"Starship Troopers", created_by = paul_verhoeven),
        define(u"Total Recall", created_by = paul_verhoeven),
        define(u"Rocky", created_by = stallone),
        define(u"Rocky II", created_by = stallone),
        define(u"Rocky III", created_by = stallone),
        define(u"Mystic River", created_by = clint_eastwood),
        define(u"Unforgiven", created_by = clint_eastwood),
        define(u"Million Dollar Baby", created_by = clint_eastwood),
        define(u"Gran Torino", created_by = clint_eastwood),
        define(u"American Beauty", created_by = sam_mendes),
        define(u"Skyfall", created_by = sam_mendes),
        define(u"Taxi Driver", created_by = scorsese),
        define(u"Goodfellas", created_by = scorsese),
        define(u"Cape Fear", created_by = scorsese)
    ])

    for user in users:

        # Establish friendships
        for i in xrange(choice(friends_per_user)):
            while True:
                friend = choice(users)
                if friend is not user and friend not in user.friends:
                    user.befriend(friend)
                    break

        # Rate concepts
        for i in xrange(choice(ratings_per_user)):
            while True:
                concept = choice(concepts)
                if concept not in user.ratings:
                    score = randint(Rating.MIN_SCORE, Rating.MAX_SCORE)
                    Rating(user, concept, score)
                    break

    return users, concepts

# Random name generation
USER_NAMES = [
    "James", "John", "Gerard", "Roger", "Tom", "Charles", "Peter", "Marc",
    "George", "William", "Geoffrey", "Richard", "Nicholas", "David", "Bernard",
    "Martin", "Albert", "Edgar", "Ronald", "Victor", "Sebastian", "Paul",
    "Julia", "Anne", "Martha", "Emily", "Natalia", "Susan", "Hannah", "Lisa",
    "Claire", "Laura", "Elisabeth", "Sylvia", "Abbey", "Rita", "Rochelle",
    "Lucy", "Mandy", "Cristina", "Angela", "Helen", "Rachel", "Lilly",
]

USER_SURNAMES = [
    "Abercrombie", "Ackerson", "Ambrose", "Albridge", "Ballard", "Bancroft",
    "Baldwyn", "Banks", "Cage", "Carroll", "Cusick", "Davies", "Degarmo",
    "Dwight", "Durand", "Eckhardt", "Ensley", "Fortner", "Friedberg",
    "Flemming", "Graham", "Gillmore", "Gregson", "Hicks", "Hoffman", "Hook",
    "Irving", "Jacobson", "Jennings", "Judson", "Kilmer", "Kircher",
    "Keisling", "Lesley", "Lundgren", "Lovejoy", "Monaghan", "Miller",
    "Mitchell", "Newbury", "Nolan", "Nugent", "Oats", "Olney", "Oswald",
    "Percy", "Paton", "Parsons", "Quinn", "Reeves", "Romero", "Rose",
    "Samuels", "Sunderland", "Simmons", "Trautner", "Torrence", "Tucker",
    "Ullman", "Urban", "Upton", "Valentine", "Vasquez", "Voss", "Walsh",
    "Windsor", "Wynslowe", "Young", "Zoeller"
]

def random_user_name():
    return u"%s %s" % (choice(USER_NAMES), choice(USER_SURNAMES))

