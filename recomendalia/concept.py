#-*- coding: utf-8 -*-
u"""Module for the `Concept` class.

.. moduleauthor:: Martí Congost <marti.congost@whads.com>
"""
from recomendalia.relation import Relation


class Concept(object):
    """A class representing any concept that can be promoted and rated on the
    website.

    Concepts have the following traits:

        - Their `name` property gives a human readable label.
        - They can be rated by users. See the `ratings` property and the
          `Rating` class.
        - They can be related to other concepts, forming a graph. See the
          the `relations` and `referrers` properties, and the `Relation` class.
    """
    name = None

    def __init__(self, name, **relations):
        self.name = name
        self._ratings = {}
        self._relations = []
        self._referrers = []

        for relation_type, target in relations.iteritems():
            if isinstance(target, Concept):
                Relation(self, relation_type, target)
            else:
                for item in target:
                    Relation(self, relation_type, item)

    def __repr__(self):
        return r"%s(%r)" % (self.__class__.__name__, self.name)

    @property
    def ratings(self):
        """The ratings given to this concept by the users of the website.

        The property is expressed as a mapping of `Rating` objects, indexed by
        `User`.
        """
        return self._ratings

    @property
    def relations(self):
        """The list of concepts that this concept is related to.
        
        The property is expressed as a list of `Relation` objects. Each of
        those objects will have this concept as its `Relation.source`.
        """
        return self._relations

    @property
    def referrers(self):
        """The list of concepts that refer to this concept.

        The property is expressed as a list of `Relation` objects. Each of
        those objects will have this concept as its `Relation.target`.
        """
        return self._referrers

