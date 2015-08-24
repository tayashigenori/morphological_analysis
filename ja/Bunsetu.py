# -*- coding: utf-8 -*-

import sys
import codecs

from Dependent import Dependent
from Independent import Independent
from Define import *

sys.stdout = codecs.getwriter('utf-8')(sys.stdout)

class Bunsetu:
    def __init__(self, independent=""):
        self._independent = independent
        return
    def __str__(self,):
        return self._independent._surface
    def append_dependents(self, dependents):
        self._independent += reduce(lambda x,y: x + y, dependents)
        return self._independent
    def get_dependents_from_surface(self,):
        # kind of morphological analysis. TODO
        return

def main():
    b = Bunsetu( Independent(u"走r-u") )
    dependents = [
        Dependent( u"ase-ru" ),
        Dependent( u"are-ru"),
        Dependent( u"ase-ru" ),
        Dependent( u"are-ru"),
        Dependent( u"mas-u"),
        ]
    b.append_dependents(dependents)
    sys.stdout.write(b)
    return

if __name__ == '__main__':
    main()
