# -*- coding: utf-8 -*-

import sys
from Define import *

# Independent: 自立語
# Dependent: 付属語

class Independent:
    def __init__(self,
                 definition = "" # 走r-u
                 ):
        self._definition = definition
        self._surface = definition.replace( SEP_STEM, u"" )
        (self._stem, self._suffix) = definition.split( SEP_STEM )
        return
    def __str__(self,):
        return self._surface
    def __add__(self, dependent):
        try:
            definition = self._stem + \
                         dependent._prefix[ self._suffix ] + \
                         dependent._definition
            return IndependentCompound( definition )
        except KeyError:
            raise Exception("Unknown POS")

class IndependentCompound(Independent):
    def __init__(self,
                 definition = "",
                 ):
        Independent.__init__(self, definition)
        return
