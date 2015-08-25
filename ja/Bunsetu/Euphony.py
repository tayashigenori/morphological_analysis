# -*- coding: utf-8 -*-

TE_FORMS = {
    u"kyt": u"it", u"gyt": u"id",
    u"syt": u"sit",
    u"tyt": u"tt",
    u"nyt": u"nd",
    u"byt": u"nd",
    u"myt": u"nd",
    u"ryt": u"tt",
    u"wyt": u"tt",
}

def euphony_t(self_stem, dep_prefix, dep_definition):
    (init, euphony_target, last) = (self_stem[:-1],
                                    self_stem[-1] + dep_prefix + dep_definition[0], # "?yt"
                                    dep_definition[1:], # "e-" or "a-"
                                    )
    try:
        r = init + TE_FORMS[euphony_target] + last
    except KeyError:
        raise Exception("Unkown te-form")
    return r
