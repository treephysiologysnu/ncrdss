# -*- coding: utf-8 -*-


def generate_meta(data):
    copy_keys = ['address', 'availableSpc', 'additionalSpc', 'totalSpc', 'numSections', 'numSpecies', 'planningPeriod',
                 'startYear', 'spcLists', 'spcIDList']
    meta = {}
    for key in copy_keys:
        meta[key] = data[key]

    return meta
