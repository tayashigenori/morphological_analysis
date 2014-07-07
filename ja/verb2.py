# -*- coding: utf-8 -*-

import sys

# does not work

class VerbCore:
    SUFFIX = "a"
    GLUE = "a"
    #
    SEPARATOR = "+"
    def __init__(self, surface_form):
        self._sf = surface_form
        return

    def is_consonant(self,):
        core_last = self._core[-1]
        if core_last in ('a', 'i', 'u', 'e', 'o'):
            return False
        else:
            return True

    def __add__(self, suffix):
        separator = GLUE + STEM_SEPARATOR
        return self + separator + suffix

class VerbStem(VerbCore):
    GLUE = "e"
    #
    SEPARATOR = "-"
    def __init__(self,
                 core, #「溶かす」なら tok
                 ):
        self._core = VerbCore(core)
        return

class Verb:
    # １段
    SUFFIX_VOWEL = 'ru'
    # ５段
    SUFFIX_CONSONANT = 'u'
    def __init__(self,
                 core,
                 transitive_type, #「溶かす」"+as-u" type ["s", "u"]
                 intransitive_type, #「溶ける」"+e-ru" type [0, "ru"]
                 ):
        self._stem = VerbStem(core = core)
        return
    """
    終止形
    """
    def get_shuushikei_suffix(self,):
        if self.is_consonant() == True:
            return self.STEM_SUFFIX_CONSONANT
        else:
            return self.STEM_SUFFIX_VOWEL
    def get_shuushikei(self,):
        return self._stem + self.get_shuushikei_suffix()

    """
    自動詞・他動詞
    """
    def get_transitive_form(self,):
        return

class TransitiveVerb(Verb):
    #
    TRANSITIVE_TYPE_0 = False
    TRANSITIVE_SUFFIX_0 = ""
    #
    TRANSITIVE_TYPE_S = True
    TRANSITIVE_SUFFIX_S = "s"

    def __init__(self, core, transitive_type, stem_last):
        self._core = VerbCore(core)
        self._transitive_type = transitive_type
        self._stem_last = stem_last
        self.set_stem()
        return

    def set_stem(self,):
        self.set_transitive_suffix()
        # ??
        if self.is_consonant() == False:
            if self._stem_last == True:
                self._stem += self.STEM_SUFFIX

    def set_transitive_suffix(self,):
        if self.get_transitive_type() == self.TRANSITIVE_TYPE_S:
            if self.get_core_last() == self.CORE_LAST_CONSONANT:
                self._stem += self.CORE_SUFFIX
            self._stem += self.TRANSITIVE_SUFFIX_S
        return
    def get_transitive_type(self,):
        return self._transitive_type

class IntransitiveVerb(Verb):
    #
    INTRANSITIVE_TYPE_0 = False
    INTRANSITIVE_SUFFIX_0 = ""
    #
    INTRANSITIVE_TYPE_R = True
    INTRANSITIVE_SUFFIX_R = "r"

    def __init__(self, core, intransitive_type, stem_last):
        self._core = core
        self._intransitive_type = intransitive_type
        self._stem_last = stem_last
        self.set_stem()
        return

    def set_stem(self,):
        self._stem = self._core
        self._stem += self.CORE_SEPARATOR
        self.set_intransitive_suffix()
        # ??
        if self.get_stem_last() == self.STEM_LAST_VOWEL:
            if self.get_current_stem_last() == self.STEM_LAST_CONSONANT:
                self._stem += self.STEM_SUFFIX

    def set_intransitive_suffix(self,):
        if self.get_intransitive_type() == self.INTRANSITIVE_TYPE_R:
            if self.get_core_last() == self.CORE_LAST_CONSONANT:
                self._stem += self.CORE_SUFFIX
            self._stem += self.INTRANSITIVE_SUFFIX_R
        return
    def get_intransitive_type(self,):
        return self._intransitive_type

def test():
    for tr_type in [False, True]:
        for st_last in [False, True]:
            v = TransitiveVerb(core = "tok",
                               transitive_type = tr_type,
                               stem_last = st_last)
            print v.get_shuushikei()
    for intr_type in [False, True]:
        for st_last in [False, True]:
            v = IntransitiveVerb(core = "tok",
                                 intransitive_type = intr_type,
                                 stem_last = st_last)
            print v.get_shuushikei()

def main():
    test()
    return

if __name__ == '__main__':
    main()
