# -*- coding: utf-8 -*-

import sys
import codecs

from Dependent import Dependent
from Independent import Independent
from Define import *

sys.stdout = codecs.getwriter('utf-8')(sys.stdout)

def append(independent, dependents):
    independent += reduce(lambda x,y: x + y, dependents)
    return independent
def get_dependents_from_surface(self,):
    # kind of morphological analysis. TODO
    return

def create_bunsetsu(indep = u"", deps = []):
    i = Independent( indep )
    d = [ Dependent(dep) for dep in deps ]
    return append(i, d)

def main():
    b1 = create_bunsetsu(indep = u"走r-u",
                         deps = [u"ta-"]
                         )
    sys.stdout.write( "%s\n" %b1 )
    b2 = create_bunsetsu(indep = u"走r-u",
                         deps = [u"ase-ru", u"are-ru",
                                 u"ase-ru", u"are-ru", u"mas-u", u"ta-"]
                         )
    sys.stdout.write( "%s\n" %b2 )
    return

if __name__ == '__main__':
    main()
