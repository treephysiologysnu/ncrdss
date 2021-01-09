# -*- coding: utf-8 -*-
import numpy as np


def generate_meta(data):
    copy_keys = ['address', 'availableSpc', 'additionalSpc', 'totalSpc', 'numSections', 'numSpecies', 'planningPeriod',
                 'startYear', 'spcLists', 'spcIDList', 'ID2Spc', 'spc2ID']
    meta = {}
    for key in copy_keys:
        meta[key] = data[key]

    return meta


def get_mortality_rate(period, species):
    """ Returns mortality rate of the target site

    :param period:
    :param species:
    :return: 1 - mortality rate (e.g., 0.9)
    """

    initial_value = 0.05
    mortality_decrease_rate = 0.97  # 0.97 ^ 50 .==' 0.218
    r = initial_value * (mortality_decrease_rate ** period)
    return 1 - r


def get_matching_item(list0, dict0, match_keys):
    for item in list0:
        is_matched = True
        for key in match_keys:
            if item[key] != dict0[key]:
                is_matched = False
                break
        if is_matched:
            return item


def get_index(arr, condition):
    for i in range(len(arr)):
        is_matched = True
        for key in condition:
            if arr[i][key] != condition[key]:
                is_matched = False
                break
        if is_matched:
            return i


def read_environment_data(year, coordinates):
    """

    :param coordinates: tuple (x, y)
    :return: environment data temperature and precipitation
    """
    temperature, precipitation = None, None
    return {'temp': temperature, 'precip': precipitation}  # TODO - 생장식 수정


def get_growth_env_cal_ratio(species, **kwargs):
    """

    :param species:
    :param kwargs:
    :return:
    """
    r_t = 1  # Calibration ratio for temperature
    r_p = 1  # Calibration ratio for precipitation
    if 'density' not in kwargs:
        print('Density has not been input - Setting Rd to 1')
        r_d = None  # Calibration ratio for density
    else:
        r_d = 1 # TODO 수정
    return r_t, r_p, r_d


def filter_indices(arr, condition):
    result_indices = []
    for i in range(len(arr)):
        is_matched = True
        for key in condition:
            if arr[i][key] != condition[key]:
                is_matched = False
                break
        if is_matched:
            result_indices.append(i)
    return result_indices


def NPV(r, t):  # t는 분기 단위로 입력
    return 1 / pow(1 + r, 10*t-5)
