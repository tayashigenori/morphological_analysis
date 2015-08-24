# -*- coding: utf-8 -*-

import sys
import re

def is_consonant(s):
    # TODO
    s = re.sub("\+", "", s)
    s = re.sub("-", "", s)
    if s[-1] in ('a', 'i', 'u', 'e', 'o'):
        return False
    else:
        return True

class VerbCore(str):
    SEPARATOR = "+"
    def __init__(self,
                 core, #「溶かす」なら tok
                 ):
        self._surface_form = core
        self._suffix_glue = "a"
        return

    def __add__(self, suffix):
        if isinstance(suffix, VerbCoreSuffix):
            res = self._surface_form + suffix._prefix_glue
            if is_consonant(res) == True:
                res += self._suffix_glue
            return res + self.SEPARATOR + suffix._surface_form
        else:
            raise ValueError("Unexpected type %s of suffix %s\n"
                             %(type(suffix), suffix))

class VerbStem(str):
    SUFFIX_GLUE = "e"
    #
    SEPARATOR = "-"
    def __init__(self,
                 stem, #「溶かす」なら tokas
                 ):
        self._surface_form = stem
        return

    def __add__(self, suffix):
        res = self._surface_form + self.SEPARATOR
        if is_consonant(self._surface_form) == True:
            return res + suffix._surface_form
        else:
            return res + suffix._prefix_glue + suffix._surface_form

class Verb(str):
    def init_with_core(self,
                       core,
                       core_suffix):
        self._core = VerbCore(core)
        self._stem = VerbStem(core + core_suffix)
        self._surface_form = VerbStem(core + core_suffix)
        return self
    def init_with_stem(self,
                       stem):
        self._core = VerbCore(False)
        self._stem = VerbStem(stem)
        self._surface_form = VerbStem(stem)
        return self

    def __add__(self, suffix):
        return self._surface_form + suffix

"""
VerbSuffix
"""
class VerbSuffix:
    def __init__(self,):
        return

class VerbSuffixShuushikei(VerbSuffix):
    def __init__(self,):
        self._prefix_glue = 'r'
        self._surface_form = 'u'
        return

"""
VerbCoreSuffix
"""
class VerbCoreSuffix:
    def __init__(self,):
        return

class VerbCoreSuffixTransitive(VerbCoreSuffix):
    def __init__(self,
                 vowel = False,
                 s = True,
                 ):
        if vowel:
            self._prefix_glue = 'e'
        else:
            self._prefix_glue = ''
        if s:
            self._surface_form = 's'
        else:
            self._surface_form = ''
        return

class VerbCoreSuffixIntransitive(VerbCoreSuffix):
    def __init__(self,
                 vowel = False,
                 r = True,
                 ):
        if vowel:
            self._prefix_glue = 'e'
        else:
            self._prefix_glue = ''
        if r:
            self._surface_form = 'r'
        else:
            self._surface_form = ''
        return

def test():
    # initialize with Stem
    print Verb().init_with_stem(stem = "toke"
                                ) + VerbSuffixShuushikei()
    print Verb().init_with_stem(stem = "tokas"
                                ) + VerbSuffixShuushikei()
    # initialize with Core + VerbCoreSuffix (Transitive / Intransitive)
    print Verb().init_with_core(core = VerbCore("tok"),
                                core_suffix = VerbCoreSuffixTransitive(s = True,
                                                                       vowel = False)
                                ) + VerbSuffixShuushikei()
    print Verb().init_with_core(core = VerbCore("tok"),
                                core_suffix = VerbCoreSuffixIntransitive(r = False,
                                                                         vowel = True)
                                ) + VerbSuffixShuushikei()

def main():
    test()
    return

if __name__ == '__main__':
    main()
