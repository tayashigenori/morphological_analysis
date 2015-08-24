# -*- coding: utf-8 -*-

import sys
from Define import *

# Independent: 自立語
# Dependent: 付属語


# prefix
DEPENDENTS_PREFIXES = {
    u"ase-ru": {SUFFIX_VV: u"s", SUFFIX_VC: u"",},
    u"are-ru": {SUFFIX_VV: u"r", SUFFIX_VC: u"",},
    u"mas-u":  {SUFFIX_VV: u"",  SUFFIX_VC: u"i",},
    }

class Dependent:
    def __init__(self,
                 definition = "" # u"ase-ru"
                 ):
        self._definition = definition
        try:
            self._prefix = DEPENDENTS_PREFIXES[ definition ]
        except KeyError:
            self._prefix = ""
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
            return DependentCompound( self._prefix, definition )
        except KeyError:
            raise Exception("Unknown POS")

class DependentCompound(Dependent):
    def __init__(self,
                 prefix = "",
                 definition = ""
                 ):
        self._definition = definition
        self._prefix = prefix
        self._surface = definition.replace( SEP_STEM, u"" )
        (self._stem, self._suffix) = definition.split( SEP_STEM )
        return
        
