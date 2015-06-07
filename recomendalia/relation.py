#-*- coding: utf-8 -*-
u"""Module for the `Relation` class.

.. moduleauthor:: Martí Congost <marti.congost@whads.com>
"""


class Relation(object):
    """A class that expresses a relation from one concept to another.
    
    Relations are directional, having both a `source` and a `target`. They also
    have a `relation_type`, used to describe the nature of the association
    between the related concepts.

    Relations are added to the `Concept.relations` and `Concept.referrers`
    properties automatically, as soon as they are instantiated. All the
    properties of this class are read only.

    Certain types of relations have a complementary relation type, which will
    be used to establish a second relation pointing back to the source concept.
    For example, the following code::

        twin_peaks = Concept("Twin Peaks")
        david_lynch = Concept("David Lynch")
        Relation(twin_peaks, "created_by", david_lynch)

    Produces exactly the same effect as the following snippet::

        twin_peaks = Concept("Twin Peaks")
        david_lynch = Concept("David Lynch")
        Relation(david_lynch, "creator_of", twin_peaks)

    Because the **created_by** and **creator_of** relation types are
    complementary, declaring one end of the relation implicitly declares its
    complementary version.
    """
    __complementary_relations = {}

    for a, b in (
        ("created_by", "creator_of"),
        ("contains", "contained_by")
    ):
        __complementary_relations[a] = b
        __complementary_relations[b] = a

    def __init__(self,
        source,
        relation_type,
        target,
        _is_complementary = False
    ):
        self.__source = source
        self.__relation_type = relation_type
        self.__target = target

        source._relations.append(self)
        target._referrers.append(self)

        # Create the relation's complement, if it has one. Pass an internal
        # parameter to the constructor of the complementary relation, to
        # prevent infinite recursion.
        if not _is_complementary:
            _complementary_relation = \
                self.__complementary_relations.get(relation_type)

            if _complementary_relation:
                self.__class__(
                    target,
                    _complementary_relation,
                    source,
                    _is_complementary = True
                )

    def __repr__(self):
        return "%s(%r, %r, %r)" % (
            self.__class__.__name__,
            self.__source,
            self.__relation_type,
            self.__target
        )

    @property
    def source(self):
        """Indicates the concept that the relation originates from.
        
        This property takes the form of a reference to an instance of the
        `Concept` class.
        """
        return self.__source

    @property
    def target(self):
        """Indicates the concept that acts as the destination of the relation.

        This property takes the form of a reference to an instance of the
        `Concept` class.
        """
        return self.__target

    @property
    def relation_type(self):
        """A classifier that indicates the nature of the relation.

        This property takes the form of an arbitrary string. For the purpose of
        this exercise, consider the following values:

            created_by:
                Specifies who or what is behind the creation of the source
                concept. It can be a person, a musical band, an organization,
                or any other suitable concept.

            creator_of:
                Complements the **created_by** relation type. Indicates an
                artistic creation, product, invention or any other kind of
                development that has been realized by the source concept.

            contained_by: 
                Indicates that the source concept is a part, example or
                specialization of the target concept. This is used to form
                topic hierarchies. For example, "Music" > "Classical Music" >
                "Beethoven's 9th Symphony".

            contains:
                Complements the **contained_by** relation type. Indicates
                that the source concept describes a topic of category which
                the target concept is a part of.
        """
        return self.__relation_type

