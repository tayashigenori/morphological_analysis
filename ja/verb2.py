# -*- coding: utf-8 -*-

import sys

class VerbCore(str):
    SUFFIX_GLUE = "a"
    #
    SEPARATOR = "+"
    def __init__(self,
                 surface_form, #「溶かす」なら tok
                 ):
        self._sf = surface_form
        return

    def is_consonant(self,):
        if self._sf[-1] in ('a', 'i', 'u', 'e', 'o'):
            return False
        else:
            return True

    def __add__(self, suffix):
        if isinstance(suffix, (VerbSuffixTransitiveSV, VerbSuffixTransitiveEV,
                               VerbSuffixIntransitiveRV, VerbSuffixIntransitiveEV)):
            self._sf = self._sf + suffix.PREFIX_GLUE

        if self.is_consonant() == True:
            self._sf = self._sf + self.SUFFIX_GLUE

        self._sf = self._sf + self.SEPARATOR + suffix._sf
        return self._sf

    #def __str__(self,):
    #    return self._sf

class VerbStem(str):
    SUFFIX_GLUE = "e"
    #
    SEPARATOR = "-"
    def __init__(self,
                 surface_form, #「溶かす」なら tokas
                 ):
        self._sf = surface_form
        return

    def is_consonant(self,):
        if self._sf[-1] in ('a', 'i', 'u', 'e', 'o'):
            return False
        else:
            return True

    def __add__(self, suffix):
        if self.is_consonant() == True:
            self._sf = self._sf + self.SEPARATOR + suffix._sf
        else:
            self._sf = self._sf + self.SEPARATOR + suffix.PREFIX_GLUE + suffix._sf
        return self._sf

    #def __str__(self,):
    #    return self._sf

class Verb:
    def __init__(self,
                 surface_form, #「溶かす」なら tokas
                 ):
        self._sf = surface_form
        return

    def __add__(self, suffix):
        if self.is_consonant() == True:
            self._sf = self._sf + suffix._sf
        else:
            self._sf = self._sf + suffix._pg + suffix._sf
        return

    def is_consonant(self,):
        if self._sf[-1] in ('a', 'i', 'u', 'e', 'o'):
            return False
        else:
            return True

    #def __str__(self,):
    #    return self._sf

class VerbSuffix:
    PREFIX_GLUE = ''
    SURFACE_FORM = ''
    def __init__(self,
                 ):
        self._sf = self.SURFACE_FORM
        return

    def is_consonant(self,):
        if self._sf[-1] in ('a', 'i', 'u', 'e', 'o'):
            return False
        else:
            return True

    #def __str__(self,):
    #    return self._sf

class VerbSuffixShuushikei(VerbSuffix):
    PREFIX_GLUE = 'r'
    SURFACE_FORM = 'u'

class VerbSuffixTransitive(VerbSuffix):
    # override me
    PREFIX_GLUE = ''
    SURFACE_FORM = ''

class VerbSuffixTransitiveSV(VerbSuffixTransitive):
    PREFIX_GLUE = 'e'
    SURFACE_FORM = 's'

class VerbSuffixTransitiveEV(VerbSuffixTransitive):
    PREFIX_GLUE = 'e'
    SURFACE_FORM = ''

class VerbSuffixTransitiveSC(VerbSuffixTransitive):
    PREFIX_GLUE = ''
    SURFACE_FORM = 's'

class VerbSuffixTransitiveEC(VerbSuffixTransitive):
    PREFIX_GLUE = ''
    SURFACE_FORM = ''

class VerbSuffixIntransitive(VerbSuffix):
    # override me
    PREFIX_GLUE = ''
    SURFACE_FORM = ''

class VerbSuffixIntransitiveRV(VerbSuffixIntransitive):
    PREFIX_GLUE = 'e'
    SURFACE_FORM = 'r'

class VerbSuffixIntransitiveEV(VerbSuffixIntransitive):
    PREFIX_GLUE = 'e'
    SURFACE_FORM = ''

class VerbSuffixIntransitiveRC(VerbSuffixIntransitive):
    PREFIX_GLUE = ''
    SURFACE_FORM = 'r'

class VerbSuffixIntransitiveEC(VerbSuffixIntransitive):
    PREFIX_GLUE = ''
    SURFACE_FORM = ''

def test():
    # initialize with VerbStem
    print VerbStem("toke") + VerbSuffixShuushikei()
    print VerbStem("tokas") + VerbSuffixShuushikei()
    # initialize with VerbCore + VerbSuffixTransitive / VerbSuffixIntransitive
    print VerbCore("tok") + VerbSuffixTransitiveSC()
    print VerbCore("tok") + VerbSuffixIntransitiveEV()
    #print VerbCore("tok") + VerbSuffixTransitiveSC() + VerbSuffixShuushikei()
    #print VerbCore("tok") + VerbSuffixIntransitiveRV() + VerbSuffixShuushikei()



def main():
    test()
    return

if __name__ == '__main__':
    main()
