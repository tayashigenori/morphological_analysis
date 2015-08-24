# -*- coding: utf-8 -*-

import sys

class Verb:
    CORE_LAST_VOWEL = True
    CORE_LAST_CONSONANT = False
    CORE_SUFFIX = "a"

    # １段
    STEM_LAST_VOWEL = False
    STEM_SUFFIX_VOWEL = 'ru'
    # ５段
    STEM_LAST_CONSONANT = True
    STEM_SUFFIX_CONSONANT = 'u'
    #
    STEM_SUFFIX = "e"

    #
    STEM_SEPARATOR = "-"
    #
    CORE_SEPARATOR = "+"

    def __init__(self,
                 core, #「溶かす」なら tok
                 transitive_type, #「溶かす」"+as-u" type ["s", "u"]
                 intransitive_type, #「溶ける」"+e-ru" type [0, "ru"]
                 ):
        self._core = core
        self.get_stem_type = self.get_stem_type()
        self._is_transitive = is_transitive
        self._transitive = Transitive()
        return

    def get_core_last(self,):
        core_last = self._core[-1]
        if core_last in ('a', 'i', 'u', 'e', 'o'):
            return self.CORE_LAST_VOWEL
        else:
            return self.CORE_LAST_CONSONANT
    def get_stem_last(self,):
        return self._stem_last
    def get_current_stem_last(self,):
        stem_last = self._stem[-1]
        if stem_last in ('a', 'i', 'u', 'e', 'o'):
            return self.STEM_LAST_VOWEL
        else:
            return self.STEM_LAST_CONSONANT
    """
    終止形
    """
    def get_shuushikei_suffix(self,):
        if self.get_stem_last() == self.STEM_LAST_VOWEL:
            return self.STEM_SUFFIX_VOWEL
        else:# self.get_stem_last() == self.STEM_LAST_CONSONANT:
            return self.STEM_SUFFIX_CONSONANT
    def get_shuushikei(self,):
        return "%s%s%s" %(self._stem, self.STEM_SEPARATOR, self.get_shuushikei_suffix())

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
        self._core = core
        self._transitive_type = transitive_type
        self._stem_last = stem_last
        self.set_stem()
        return

    def set_stem(self,):
        self._stem = self._core
        self._stem += self.CORE_SEPARATOR
        self.set_transitive_suffix()
        # ??
        if self.get_stem_last() == self.STEM_LAST_VOWEL:
            if self.get_current_stem_last() == self.STEM_LAST_CONSONANT:
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
