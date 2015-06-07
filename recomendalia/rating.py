#-*- coding: utf-8 -*-
u"""Module for the `Rating` class.

.. moduleauthor:: Martí Congost <marti.congost@whads.com>
"""


class Rating(object):
    """A rating given by a user to a certain concept.

    A rating is made up of three parts:

        - A reference to the `user` who created the rating.
        - A reference to the `concept` being rated.
        - The `score` given by the user to the concept.

    Ratings are automatically added to the `User.ratings` and `Concept.ratings`
    properties as soon as they are instantiated.
    
    All the properties of this class are read only.
    """
    MIN_SCORE = 0
    MAX_SCORE = 5

    def __init__(self, user, concept, score):

        if not (self.MIN_SCORE <= score <= self.MAX_SCORE):
            raise ValueError(
                "%r is not a valid score. Expected a value between %d and %d"
                % (score, self.MIN_SCORE, self.MAX_SCORE)
            )

        self.__user = user
        self.__concept = concept
        self.__score = score

        user._ratings[concept] = self
        concept._ratings[user] = self

    def __repr__(self):
        return "%s(%r, %r, %r)" % (
            self.__class__.__name__,
            self.__user,
            self.__concept,
            self.__score
        )

    @property
    def user(self):
        """The user who created this rating.
        
        This read only property takes the form of an instance of the `User`
        class.
        """
        return self.__user

    @property
    def concept(self):
        """The concept being rated.

        This read only property takes the form of an instance of the `Concept`
        class.
        """
        return self.__concept

    @property
    def score(self):
        """The score given to the rated concept by the user.

        This read only property takes the form of an integer, ranging from
        `MIN_SCORE` to `MAX_SCORE` (both included).
        """
        return self.__score

