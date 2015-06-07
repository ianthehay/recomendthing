#-*- coding: utf-8 -*-
u"""Module for the `User` class.

.. moduleauthor:: Martí Congost <marti.congost@whads.com>
"""
from recomendalia.rating import Rating
import collections

class User(object):
    """A class representing an end user of the website.
    
    Users have several properties and actions available to them:

        - Their `name` property provides the user's full name.

        - They can can establish friendships with other users (see the
          `befriend` method and the `friends` property).

        - They can rate concepts (see the `ratings` property and the `Rating`
          class).
    """
    name = None

    network =[]

    def __init__(self, name):
        self.name = name
        self._friends = set()
        self._ratings = {}

    def __repr__(self):
        return "%s(%r)" % (self.__class__.__name__, self.name)

    def suggest_friends(self):
        """Suggest potential friends for this user.
        
        :return: An iterable sequence of `FriendSuggestion` objects, ordered by
            decreasing afinity.
        """
        suggestionlist=[]

        # generate the users network
        self.gen_network()
        # remove already friends and self from network 
        nonfriendnetwork=[x for x in self.network if x in self.friends]
        # determine the occurances of each non friend in the network
        counter = collections.Counter(nonfriendnetwork)   
        # get a lsit of the most commonly occuring 4 people
        common = nonfriendnetwork.most_common(4)

        # Iterate over the suggestions in the most common list and create FrienSugesiton Objects
        for suggestion in common:
            userobject = suggestion[0]
            rank=suggestion[1]
            suggestionlist.append(FriendSuggestion(userobject,rank))
        # Return the list of the suggestion objects
        return suggestionlist

    def gen_network(self):
        # Generate a network based on all friends of the users friends
        for friend in self.friends:
            for userfriend in friend.friends:
                self.network.append(userfriend)
        return self.network

    def suggest_concepts(self):
        """Suggest concepts that this user may be interested in.

        :return: An iterable sequence of `ConceptSuggestion` objects, ordered
            by decreasing potential interest.
        """
        raise TypeError("Not implemented yet")

    def befriend(self, user):
        """Establish a friendship with another user.

        Friendship relationships are always reciprocal: if a user A is a friend
        of B, B is necessarily a friend a of A.
        """
        self._friends.add(user)
        user._friends.add(self)

    @property
    def friends(self):
        """The list of friends for this user.

        The property is expressed as a set of `User` objects.
        """
        return self._friends

    @property
    def ratings(self):
        """The ratings given by this user.

        The property is expressed as a mapping of `Rating` objects, indexed by
        the rated `Concept`.
        """
        return self._ratings


class FriendSuggestion(object):
    """A class used to provide information on a friend suggestion for a user.

    This class is used by the `User.suggest_friends` method to describe each
    suggestion it produces. As well as a reference to the potential friend (a
    `User` instance), the class provides properties indicating the matching
    criteria and patterns that the algorithm observed when it decided said user
    could be a potential friend candidate.
    """

    user = None

    def __init__(self, userobject,rank):
        self.user=userobject
        self._rank=rank

    @property
    def rank(self):
        # The rank of the suggested person
        # The property is based on how many of the users friends are friends with the user.
        # For Example a rank of 5 means 5 of the users friends are friends with this person

        return self._rank


class ConceptSuggestion(object):
    """A class used to provide information on a concept that a user may be
    interested in.

    This class is used by the `User.suggest_concepts` method to describe each
    suggestion it produces. As well as a reference to the suggested concept (a
    `Concept` instance), the class provides properties indicating the matching
    criteria and patterns that the algorithm observed when it decided said
    concept could be a potential point of interest.
    """

