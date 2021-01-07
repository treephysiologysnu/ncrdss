import pandas as pd
import numpy as np
from coeffs import *

ID2AccVarNameRules = {
        'Vol_SpcPer': ['spcID', 'V', '.', 'period'],  # 특정 수종의 분기별 재적
        'Area_SpcSecPer': ['section', 'spcID', 'A', '.', 'period'],  # 2KA.10 => 10분기의 2구역, K 수종의 면적
        'Area_SpcPer': ['spcID', 'A', '.', 'period'],  # KA.10 => 10분기의 K 수종의 면적.
        'Area_AgePer': ['AC', 'age', '.', 'period'],  # AC1.10 => 10분기에 AgeClass 가 1 인 면적
        'Thin_SpcPer': ['spcID', 'T', '.', 'period'],  # KT.10 => 10분기에 K 수종의 간벌량
        'Harv_SpcPer': ['spcID', 'H', '.', 'period'],  # KH.10 => 10분기에 H 수종의 수확량
        'PThin_Per': ['T', '.', 'period'],  # T.10 => 10 분기의 간벌 생산량
        'PHarv_Per': ['H', '.', 'period'],  # H.10 => 10 분기의 주벌 생산량
        'PThinHarv_Per': ['TH', '.', 'period'],
        'Carbon_Per': ['C', '.', 'period'],
        'Water_Per': ['W', '.', 'period'],
        'Labor_Per': ['J', '.', 'period'],
        'TCost_Per': ['TC', '.', 'period'],
        'TRev_Per': ['TR', '.', 'period'],
        'TNet_Per': ['ft', '.', 'period'],
        'HCost_Per': ['HC', '.', 'period'],
        'HRev_Per': ['HR', '.', 'period'],
        'HNet_Per': ['fh', '.', 'period'],
        'f_Per': ['f', '.', 'period'],
        'g_Per': ['g', '.', 'period'],
        'h_Per': ['h', '.', 'period'],
        'NPV_f_Per': ['NPV_f', '.', 'period'],
        'NPV_g_Per': ['NPV_g', '.', 'period'],
        'NPV_h_Per': ['NPV_h', '.', 'period'],
        'NPV_f': ['NPV_f'],
        'NPV_g': ['NPV_g'],
        'NPV_h': ['NPV_h'],
    }

def create_matrix(data):
    manager = data

    w1 = manager['coeffs']['w1']
    w2 = manager['coeffs']['w2']
    w3 = manager['coeffs']['w3']

    DENSITY = manager['coeffs']['initialDensity']
    spc2ID = {obj['species']: obj['speciesID'] for obj in manager['spcClasses']}
    ID2spc = {obj['speciesID']: obj['species'] for obj in manager['spcClasses']}
    spcIDList = list(spc2ID.values())
    regenerationRules = manager['regenerationRules']
    initialConditions = list()
    for currentSpc in manager['currentSpc']:
        temp_dict = currentSpc.copy()
        temp_dict['spcID'] = spc2ID[temp_dict['species']];
        temp_dict['periodBorn'] = 1 - temp_dict['age']

        forManPlan = next(item for item in manager['forManPlan']
                          if (item['section'] == temp_dict['section']) &
                          (item['species'] == temp_dict['species'])
                          )

        if temp_dict['periodBorn'] + forManPlan['clearCutYear'] <= 0:
            temp_dict['periodDied'] = 1
        else:
            temp_dict['periodDied'] = temp_dict['periodBorn'] + forManPlan['clearCutYear']
        temp_dict['clearCutYear'] = forManPlan['clearCutYear']

        if 'thinningScenario' in forManPlan:  # thinningScenario key 가 존재하면
            temp_dict['thinningScenario'] = forManPlan['thinningScenario']
        else:  # 키가 존재하지 않는 경우 계획 기간 길이만큼 zeros 생성
            temp_dict['thinningScenario'] = [0 for _ in range(manager['planningPeriod'])]

        temp_dict['spcGrowth'] = manager['spcGrowth'][temp_dict['species']]

        initialConditions.append(temp_dict)

    currentVolumeTables = list()
    for initialCondition in initialConditions:
        currentVolumeTable = dict()
        currentVolumeTable['section'] = initialCondition['section']
        currentVolumeTable['spcID'] = initialCondition['spcID']
        currentVolumeTable['currentAge'] = initialCondition['age']
        currentVolumeTable['clearCutYear'] = initialCondition['clearCutYear']
        growthData = initialCondition['spcGrowth']['predictions'].copy()

        ratio = initialCondition['volume'] / growthData[10 * initialCondition['age'] - 1]
        growthData = [x * ratio for x in growthData]

        temp_current_volume_data = dict()
        age = 1
        if currentVolumeTable['currentAge'] < initialCondition['clearCutYear']:
            per = 1
            while age < initialCondition['clearCutYear']:
                age = currentVolumeTable['currentAge'] + per - 1
                prod = growthData[10 * age - 1] * initialCondition['thinningScenario'][age - 1]

                if age == initialCondition['clearCutYear']:
                    prod = growthData[10 * age - 1]

                growthData = [x - prod for x in growthData]  # Subtract the amount of thinning from the growth data
                vol = growthData[10 * age - 1]  # Volume after subtracting

                temp_current_volume_data[per] = {
                    'period': per,
                    'age': age,
                    'volume': vol,
                    'produced': prod
                }
                per += 1
        else:  # 현재 영급이 주벌시기를 지나버린 경우
            per = 1
            age = currentVolumeTable['currentAge'] + per - 1
            vol = 0
            prod = growthData[10 * age - 1]
            temp_current_volume_data[per] = {
                'period': per,
                'age': age,
                'volume': vol,
                'produced': prod
            }
        currentVolumeTable['data'] = temp_current_volume_data
        currentVolumeTables.append(currentVolumeTable)

    futureVolumeTables = list()
    for sec in range(manager['numSections']):
        sec += 1
        for spcID in spcIDList:
            growthData = manager['spcGrowth'][ID2spc[spcID]]['predictions'].copy()
            growthData = [x * DENSITY for x in growthData]

            futureVolumeTable = dict()
            futureVolumeTable['section'] = sec
            futureVolumeTable['spcID'] = spcID

            temp_future_volume_data = dict()
            forManPlan = next(item for item in manager['forManPlan']
                              if (item['section'] == sec) &
                              (item['species'] == ID2spc[spcID])
                              )
            clearCutYear = forManPlan['clearCutYear']
            if 'thinningScenario' in forManPlan:
                thinningScenario = forManPlan['thinningScenario']
            else:
                thinningScenario = [0 for _ in range(clearCutYear)]

            for per in range(clearCutYear):
                per += 1  # To start from 1. per => 1, 2, 3 .. 7 (clearCutYear = 7)
                prod = growthData[10 * per - 1] * thinningScenario[per - 1]
                if per == clearCutYear:
                    prod = growthData[10 * per - 1]

                growthData = [x - prod for x in growthData]
                vol = growthData[10 * per - 1]
                temp_future_volume_data[per] = {
                    'period': per,
                    'age': per,
                    'volume': vol,
                    'produced': prod
                }
            futureVolumeTable['data'] = temp_future_volume_data
            futureVolumeTables.append(futureVolumeTable)

    class DecisionVariablesClass:
        duplicateCheckKeys = ['section', 'spcID', 'periodDied', 'regenSpcID']  # 중복 여부 검사할 딕셔너리 키들

        # sortKeys = ['section', 'periodBorn', 'spcID', 'periodDied', regenSpcID']

        def __init__(self):
            self.list = list()

        def is_duplicate(self, condition):
            if self.list == []:
                return False
            for dv in self.list:
                allKeyMatched = False
                for key in self.duplicateCheckKeys:
                    if dv[key] != condition[key]:
                        allKeyMatched = False
                        break
                    allKeyMatched = True
                if allKeyMatched:
                    return True
            return False

        def add(self, condition):
            if self.is_duplicate(condition):
                return
            pd_string = str(condition['periodDied'])
            if condition['periodDied'] > manager['planningPeriod']:
                pd_string = '.'
            self.list.append(dict(
                type='Variable',
                ID='DecisionVariable',
                section=condition['section'],
                spcID=condition['spcID'],
                periodBorn=condition['periodBorn'],
                periodDied=condition['periodDied'],
                regenSpcID=condition['regenSpcID'],
                name=str(condition['section']) +
                     '_' + str(condition['periodBorn']) +
                     condition['spcID'] + pd_string +
                     condition['regenSpcID']
            ))

        def sort(self):
            self.list = sorted(self.list,
                               key=lambda e: (
                               e['section'], e['periodBorn'], spcIDList.index(e['spcID']), e['periodDied']))

    DecisionVariables = DecisionVariablesClass()

    def create_decision_variables(condition):
        if condition['periodBorn'] > manager['planningPeriod']:
            return False
        regenSpcIDList = spcIDList
        search_results = [x for x in regenerationRules
                          if ((x['section'] == condition['section']) & (x['spcID'] == condition['spcID']))
                          ]
        if len(search_results) > 0:
            regenSpcIDList = search_results[0]['regenerationRule']

        # 계획기간을 넘어, 주벌 & 갱신을 안하는 경우 한번 추가하고, 이후 반복문은 실행 X
        if condition['periodBorn'] + condition['clearCutYear'] > manager['planningPeriod']:
            condition['regenSpcID'] = '.'
            DecisionVariables.add(condition)
            return False

        #  계획기간 내, 주벌 & 갱신 모두 함. 수종에 따라, 주벌시기가 계획기간 이상일 수도, 이내일 수도 있으므로 고려.
        for regenSpcID in regenSpcIDList:
            newCondition = condition.copy()  # To prevent changing of initialCondition values. Making a Copy.
            newCondition['regenSpcID'] = regenSpcID
            DecisionVariables.add(newCondition)  # regenSpcID 만 할당한 뒤에 추가.

            newCondition['spcID'] = regenSpcID
            newCondition['species'] = ID2spc[newCondition['spcID']]
            newCondition['periodBorn'] = newCondition['periodDied']
            newCondition['clearCutYear'] = next(item for item in manager['forManPlan']
                                                if (item['section'] == newCondition['section']) &
                                                (item['species'] == newCondition['species']))['clearCutYear']
            newCondition['periodDied'] = newCondition['periodBorn'] + newCondition['clearCutYear']
            create_decision_variables(newCondition)

    for initialCondition in initialConditions:
        create_decision_variables(initialCondition)
    DecisionVariables.sort()

    AccVarIDList = ID2AccVarNameRules.keys()

    class AccountingVariablesClass:
        duplicateCheckKeys = ['name']  # 중복 여부 검사할 딕셔너리 키들

        def __init__(self):
            self.list = list()

        def is_duplicate(self, condition):
            if self.list == []:
                return False
            for av in self.list:
                all_key_matched = False
                for key in self.duplicateCheckKeys:
                    if av[key] != condition[key]:
                        all_key_matched = False
                        break
                    all_key_matched = True
                if all_key_matched:
                    return True
            return False

        def create_name(self, condition):
            name = ''
            for datakey in ID2AccVarNameRules[condition['ID']]:
                if not datakey in condition:
                    name += str(datakey)
                else:
                    name += str(condition[datakey])
            return name

        def add(self, condition):
            condition['name'] = self.create_name(condition)
            if self.is_duplicate(condition):
                return
            temp_dict_accvar = dict(
                type='Variable',
                ID=condition['ID'],
                period=condition['period'],
                name=condition['name']
            )
            if 'section' in ID2AccVarNameRules[temp_dict_accvar['ID']]:
                temp_dict_accvar['section'] = condition['section']
            if 'spcID' in ID2AccVarNameRules[temp_dict_accvar['ID']]:
                temp_dict_accvar['spcID'] = condition['spcID']
            if 'age' in ID2AccVarNameRules[temp_dict_accvar['ID']]:
                temp_dict_accvar['age'] = condition['age']
            self.list.append(temp_dict_accvar)

    AccountingVariables = AccountingVariablesClass()

    ageMax = 0
    for FM_dict in manager['forManPlan']:
        if ageMax < FM_dict['clearCutYear']:
            ageMax = FM_dict['clearCutYear']

    for ID in ID2AccVarNameRules:
        for sec in range(manager['numSections']):
            sec += 1
            for spcID in spcIDList:
                for age in range(ageMax):
                    age += 1
                    for per in range(manager['planningPeriod']):
                        per += 1
                        AccountingVariables.add({
                                                    'ID': ID,
                                                    'section': sec,
                                                    'spcID': spcID,
                                                    'age': age,
                                                    'period': per
                                                })

    Variables = DecisionVariables.list + AccountingVariables.list

    class DecisionVariableEquationNamesClass:
        duplicateCheckKeys = ['section', 'spcID', 'periodBorn']

        def __init__(self):
            self.list = list()

        def is_duplicate(self, condition):
            if self.list == []:
                return False
            for dv in self.list:
                allKeyMatched = False
                for key in self.duplicateCheckKeys:
                    if dv[key] != condition[key]:
                        allKeyMatched = False
                        break
                    allKeyMatched = True
                if allKeyMatched:
                    return True
            return False

        def add(self, condition):
            if self.is_duplicate(condition):
                return
            self.list.append(dict(
                type='EquationName',
                ID='DecisionVariable',
                section=condition['section'],
                spcID=condition['spcID'],
                periodBorn=condition['periodBorn'],
                name=str(condition['section']) +
                     '_' + str(condition['periodBorn']) +
                     condition['spcID']
            ))

    DecisionVariableEquationNames = DecisionVariableEquationNamesClass()
    for dv in DecisionVariables.list:
        DecisionVariableEquationNames.add(dv)

    AccountingVariableEquationNames = list()
    for av in AccountingVariables.list:
        AccVarEqName = av.copy()
        AccVarEqName['type'] = "EquationName"
        AccountingVariableEquationNames.append(AccVarEqName)

    EquationNames = DecisionVariableEquationNames.list + AccountingVariableEquationNames

    def get_index(arr, condition):
        for i in range(len(arr)):
            is_matched = True
            for key in condition:
                if arr[i][key] != condition[key]:
                    is_matched = False
                    break
            if is_matched:
                return i

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

    LHSMatrix = np.zeros((len(EquationNames), len(Variables)))
    RHSMatrix = np.zeros((1, len(EquationNames)))

    for rowNum in range(len(EquationNames)):
        indices = []
        line = []
        EqName = EquationNames[rowNum]
        ID = EqName['ID']
        if ID == "DecisionVariable":
            # DecisionVariable: {'type':'Variable','ID':'DecisionVariable','section':1,'spcID':'K','periodBorn':-7,'periodDied':1,'regenSpcID':'O','name':'1_-7K1O'}
            if EqName['periodBorn'] < 1:  # 기존에 있던 나무인 경우 (0분기 이하)
                indices = filter_indices(Variables, {
                    'ID': 'DecisionVariable',
                    'section': EqName['section'],
                    'spcID': EqName['spcID'],
                    'periodBorn': EqName['periodBorn']
                })
                line = [1 for _ in range(len(indices))]
                area = next(item for item in initialConditions
                            if (item['section'] == EqName['section']) &
                            (item['spcID'] == EqName['spcID']) &
                            (item['periodBorn'] == EqName['periodBorn']))['area']
                RHSMatrix[0, rowNum] = area  # 우변에 각 영역 값을 할당
            else:  # 기존에 있던 나무가 아니고 식재된 경우
                indices = filter_indices(Variables, {
                    'ID': ID,
                    'section': EqName['section'],
                    'regenSpcID': EqName['spcID'],
                    'periodDied': EqName['periodBorn']  # 갱신 대상 수종과 갱신 분기를 통해 검색
                })
                line = [1 for _ in range(len(indices))]

                # RHS
                indices_temp = filter_indices(Variables, {
                    'ID': EqName['ID'],
                    'section': EqName['section'],
                    'spcID': EqName['spcID'],
                    'periodBorn': EqName['periodBorn']
                })  # 갱신된 현 상태의 수종 정보 (-1값 대입용)
                line2 = [-1 for _ in range(len(indices_temp))]
                indices = indices + indices_temp
                line = line + line2
                RHSMatrix[0, rowNum] = 0  # 우변에 0을 할당 (Equation 이기 때문에)
        if ID == 'Vol_SpcPer':
            # Vol_SpcPer EqName : {'type':'EquationName','ID':'Vol_SpcPer','section':1,'spcID':'C','period':12,'name':'CV.12'}
            indices = filter_indices(Variables, {  # 수종 조건이 맞는 indices 는 우선 전부 다 불러오기.
                'ID': 'DecisionVariable',
                'spcID': EqName['spcID'],
            })
            for i in indices:  # 각각의 indices 에 대해서 Variable 을 불러온 뒤, 조건에 맞게 처리.
                V = Variables[i]
                if (V['periodBorn'] < EqName['period']) & (
                        EqName['period'] <= V['periodDied']):  # 특정 period 에 그 나무가 살아있는 경우
                    if V['periodBorn'] <= 0:  # 원래 있던 나무일 때 currentVolumeTables 에서 참고
                        vol = next(item for item in currentVolumeTables
                                   if (item['section'] == V['section']) &
                                   (item['spcID'] == V['spcID']) &
                                   (item['currentAge'] == 1 - V['periodBorn']))['data'][EqName['period']]['volume']
                        line.append(vol)
                    else:  # 식재된 나무일 때 면적이 변화) -> futureVolumeTables 에서 참고
                        vol = next(item for item in futureVolumeTables
                                   if (item['section'] == V['section']) &
                                   (item['spcID'] == V['spcID']))['data'][EqName['period'] - V['periodBorn']][
                            'produced']
                        line.append(vol)
                else:
                    line.append(0)

            # RHS
            index = get_index(Variables, {
                'ID': EqName['ID'],
                'name': EqName['name'],
            })
            indices.append(index)
            line.append(-1)
            RHSMatrix[0, rowNum] = 0  # 우변에 0을 할당 (Equation 이기 때문에)
        if ID == 'Area_SpcSecPer':
            # Area_SpcSecPer EqName : {ID: 'Area_SpcSecPer', name: '1OA.1', period: 1, section: 1, spcID: 'O', type: 'Variable'}
            indices = filter_indices(Variables, {  # 수종 조건이 맞는 indices 는 우선 전부 다 불러오기.
                'ID': 'DecisionVariable',
                'spcID': EqName['spcID'],
                'section': EqName['section'],
            })
            for i in indices:  # 각각의 indices 에 대해서 Variable 을 불러온 뒤, 조건에 맞게 처리.
                V = Variables[i]
                if (V['periodBorn'] <= EqName['period']) & (EqName['period'] < V['periodDied']):
                    line.append(1)
                else:
                    line.append(0)

            # RHS
            index = get_index(Variables, {
                'ID': EqName['ID'],
                'name': EqName['name'],
            })
            indices.append(index)  # 우항에 해당,
            line.append(-1)
            RHSMatrix[0, rowNum] = 0  # 우변에 0을 할당 (Equation 이기 때문에)
        if ID == 'Area_SpcPer':
            # Area_SpcPer EqName : {'type':'EquationName','ID':'Area_SpcPer','period':1,'spcID':'O','name':'OA.1'}
            indices = filter_indices(Variables, {  # 조건이 맞는 indices 는 우선 전부 다 불러오기.
                'ID': 'Area_SpcSecPer',
                'spcID': EqName['spcID'],
                'period': EqName['period']
            })
            line = [1 for _ in range(len(indices))]

            # RHS
            index = get_index(Variables, {
                'ID': EqName['ID'],
                'name': EqName['name'],
            })
            indices.append(index)  # 우항에 해당,
            line.append(-1)
            RHSMatrix[0, rowNum] = 0  # 우변에 0을 할당 (Equation 이기 때문에)
        if ID == 'Area_AgePer':
            # Area_AgePer EqName : {'type':'EquationName','ID':'Area_AgePer','period':1,'age':1,'name':'AC1.1'}
            indices = filter_indices(Variables, {  # 조건이 맞는 indices 는 우선 전부 다 불러오기.
                'ID': 'DecisionVariable',
                'periodBorn': EqName['period'] - EqName['age'],
            # 다영이가 만든 것과 Variation => 0분기때 태어난 애들은 1분기 때 1살(1영급) 이어야 하는 것 아닌가? 다영이 방식은 0때 바로 1분기로 계산된다. 지금 있는 식에 +1 하면 됨.
            })
            del_indices = []  # indices to delete from the above indices array (filtering out dead trees)
            for i in indices:
                V = Variables[i]
                if V['periodDied'] <= EqName['period']:
                    del_indices.append(i)
            indices = [i for j, i in enumerate(indices) if j not in del_indices]
            line = [1 for _ in range(len(indices))]

            # RHS
            index = get_index(Variables, {
                'ID': EqName['ID'],
                'name': EqName['name'],
            })
            indices.append(index)  # 우항에 해당,
            line.append(-1)
            RHSMatrix[0, rowNum] = 0  # 우변에 0을 할당 (Equation 이기 때문에)
        if ID == 'Thin_SpcPer':
            # Thin_SpcPer EqName : {'type':'EquationName','ID':'Thin_SpcPer','period':1,'spcID':'O','name':'OT.1'}
            indices = filter_indices(Variables, {  # 수종 조건이 맞는 indices 는 우선 전부 다 불러오기.
                'ID': 'DecisionVariable',
                'spcID': EqName['spcID'],
            })
            for i in indices:  # 각각의 indices 에 대해서 Variable 을 불러온 뒤, 조건에 맞게 처리.
                V = Variables[i]
                if (V['periodBorn'] < EqName['period']) & (
                        EqName['period'] < V['periodDied']):  # periodDied = 주벌시기 이므로, 해당 분기를 제외한 기간 동안 생존한 나무
                    if V['periodBorn'] <= 0:  # 원래 있던 나무일 때 currentVolumeTables 에서 참고
                        vol = next(item for item in currentVolumeTables
                                   if (item['section'] == V['section']) &
                                   (item['spcID'] == V['spcID']) &
                                   (item['currentAge'] == 1 - V['periodBorn']))['data'][EqName['period']]['produced']
                        line.append(vol)
                    else:  # 식재된 나무일 때 면적이 변화) -> futureVolumeTables 에서 참고
                        vol = next(item for item in futureVolumeTables
                                   if (item['section'] == V['section']) &
                                   (item['spcID'] == V['spcID']))['data'][EqName['period'] - V['periodBorn']][
                            'produced']
                        line.append(vol)
                else:
                    line.append(0)

            # RHS
            index = get_index(Variables, {
                'ID': EqName['ID'],
                'name': EqName['name'],
            })
            indices.append(index)
            line.append(-1)
            RHSMatrix[0, rowNum] = 0  # 우변에 0을 할당 (Equation 이기 때문에)
        if ID == 'Harv_SpcPer':
            # Thin_SpcPer EqName : {'type':'EquationName','ID':'Harv_SpcPer','period':1,'spcID':'O','name':'OH.1'}
            indices = filter_indices(Variables, {  # 수종 조건이 맞는 indices 는 우선 전부 다 불러오기.
                'ID': 'DecisionVariable',
                'spcID': EqName['spcID'],
            })
            for i in indices:  # 각각의 indices 에 대해서 Variable 을 불러온 뒤, 조건에 맞게 처리.
                V = Variables[i]
                if EqName['period'] == V['periodDied']:  # 주벌시기에 해당하는 나무
                    if V['periodBorn'] <= 0:  # 원래 있던 나무일 때 currentVolumeTables 에서 참고
                        vol = next(item for item in currentVolumeTables
                                   if (item['section'] == V['section']) &
                                   (item['spcID'] == V['spcID']) &
                                   (item['currentAge'] == 1 - V['periodBorn']))['data'][EqName['period']]['produced']
                        line.append(vol)
                    else:  # 식재된 나무일 때 면적이 변화) -> futureVolumeTables 에서 참고
                        vol = next(item for item in futureVolumeTables
                                   if (item['section'] == V['section']) &
                                   (item['spcID'] == V['spcID']))['data'][EqName['period'] - V['periodBorn']][
                            'produced']
                        line.append(vol)
                else:
                    line.append(0)

            # RHS
            index = get_index(Variables, {
                'ID': EqName['ID'],
                'name': EqName['name'],
            })
            indices.append(index)
            line.append(-1)
            RHSMatrix[0, rowNum] = 0  # 우변에 0을 할당 (Equation 이기 때문에)
        if ID == 'PThin_Per':
            # PThin_Per EqName : {'type':'EquationName','ID':'PThin_Per','period':1,'name':'T.1'}
            indices = filter_indices(Variables, {  # 조건이 맞는 indices 는 우선 전부 다 불러오기.
                'ID': 'Thin_SpcPer',
                'period': EqName['period'],
            })
            line = [1 for _ in range(len(indices))]

            # RHS
            index = get_index(Variables, {
                'ID': EqName['ID'],
                'name': EqName['name'],
            })
            indices.append(index)  # 우항에 해당,
            line.append(-1)
            RHSMatrix[0, rowNum] = 0  # 우변에 0을 할당 (Equation 이기 때문에)
        if ID == 'PHarv_Per':
            # PThin_Per EqName : {'type':'EquationName','ID':'PHarv_Per','period':1,'name':'H.1'}
            indices = filter_indices(Variables, {  # 조건이 맞는 indices 는 우선 전부 다 불러오기.
                'ID': 'Harv_SpcPer',
                'period': EqName['period'],
            })
            line = [1 for _ in range(len(indices))]

            # RHS
            index = get_index(Variables, {
                'ID': EqName['ID'],
                'name': EqName['name'],
            })
            indices.append(index)  # 우항에 해당,
            line.append(-1)
            RHSMatrix[0, rowNum] = 0  # 우변에 0을 할당 (Equation 이기 때문에)
        if ID == 'PThinHarv_Per':
            # PThin_Per EqName : {'type':'EquationName','ID':'PHarv_Per','period':1,'name':'H.1'}
            indices.append(get_index(Variables, {  # TH = _T_ + H
                'ID': 'PThin_Per',
                'period': EqName['period'],
            }))
            indices.append(get_index(Variables, {  # TH = T + _H_
                'ID': 'PHarv_Per',
                'period': EqName['period'],
            }))
            line = [1 for _ in range(len(indices))]  # = [1, 1]

            # RHS
            index = get_index(Variables, {
                'ID': EqName['ID'],
                'name': EqName['name'],
            })
            indices.append(index)  # 우항에 해당,
            line.append(-1)
            RHSMatrix[0, rowNum] = 0  # 우변에 0을 할당 (Equation 이기 때문에)
        if ID == 'Carbon_Per':
            # Carbon_Per EqName : {'type':'EquationName','ID':'Carbon_Per','period':1,'name':'C.1'}
            indices = filter_indices(Variables, {  # 수종 조건이 맞는 indices 는 우선 전부 다 불러오기.
                'ID': 'Vol_SpcPer',
                'period': EqName['period'],
            })
            for i in indices:  # 각각의 indices 에 대해서 Variable 을 불러온 뒤, 조건에 맞게 처리.
                V = Variables[i]
                carbonCoeff = manager['coeffs']['volume2Carbon'][ID2spc[V['spcID']]]

                line.append(carbonCoeff)

            # RHS
            index = get_index(Variables, {
                'ID': EqName['ID'],
                'name': EqName['name'],
            })
            indices.append(index)
            line.append(-1)
            RHSMatrix[0, rowNum] = 0  # 우변에 0을 할당 (Equation 이기 때문에)
        if ID == 'Water_Per':
            # Water_Per EqName : {'type':'EquationName','ID':'Water_Per','period':1,'name':'W.1'}
            indices = filter_indices(Variables, {  # 수종 조건이 맞는 indices 는 우선 전부 다 불러오기.
                'ID': 'DecisionVariable',
            })
            for i in indices:  # 각각의 indices 에 대해서 Variable 을 불러온 뒤, 조건에 맞게 처리.
                V = Variables[i]
                if (V['periodBorn'] <= EqName['period']) & (EqName['period'] <= V['periodDied']):
                    waterCoeff = next(item for item in manager['coeffs']['waterCoeffs']
                                  if (item['section'] == V['section']) &
                                  (V['spcID'] in item['spcIDs']))['data'][EqName['period'] - V['periodBorn']]
                    if (V['periodBorn'] == EqName['period']) | (EqName['period'] == V['periodDied']):
                        waterCoeff = waterCoeff / 2
                    line.append(waterCoeff)
                else:
                    line.append(0)

            # RHS
            index = get_index(Variables, {
                'ID': EqName['ID'],
                'name': EqName['name'],
            })
            indices.append(index)
            line.append(-1)
            RHSMatrix[0, rowNum] = 0  # 우변에 0을 할당 (Equation 이기 때문에)
        if ID == 'Labor_Per':
            # Labor_Per EqName : {'type':'EquationName','ID':'Labor_Per','period':1,'name':'J.1'}
            indices = filter_indices(Variables, {  # 수종 조건이 맞는 indices 는 우선 전부 다 불러오기.
                'ID': 'DecisionVariable',
            })
            for i in indices:  # 각각의 indices 에 대해서 Variable 을 불러온 뒤, 조건에 맞게 처리.
                V = Variables[i]
                produced = 0
                if (V['periodBorn'] < EqName['period']) & (
                        EqName['period'] <= V['periodDied']):  # 주벌분기를 포함한 기간 동안 생존한 나무만 선택
                    if V['periodBorn'] <= 0:  # 원래 있던 나무일 때 currentVolumeTables 에서 참고
                        produced = next(item for item in currentVolumeTables
                                        if (item['section'] == V['section']) &
                                        (item['spcID'] == V['spcID']) &
                                        (item['currentAge'] == 1 - V['periodBorn']))['data'][EqName['period']][
                            'produced']
                    else:  # 식재된 나무일 때 -> futureVolumeTables 에서 참고
                        produced = next(item for item in futureVolumeTables
                                        if (item['section'] == V['section']) &
                                        (item['spcID'] == V['spcID']))['data'][EqName['period'] - V['periodBorn']][
                            'produced']
                if produced != 0:
                    if EqName['period'] == V['periodDied']:
                        # clearCut + regen labor. 만약 regeneration = '.' 인 경우 0
                        line.append(manager['coeffs']['laborCoeffs']['clearCut'] + manager['coeffs']['laborCoeffs']['regeneration'][V['regenSpcID']])
                    else:
                        line.append(manager['coeffs']['laborCoeffs']['thinning'])
                else:
                    line.append(0)

            # RHS
            index = get_index(Variables, {
                'ID': EqName['ID'],
                'name': EqName['name'],
            })
            indices.append(index)
            line.append(-1)
            RHSMatrix[0, rowNum] = 0  # 우변에 0을 할당 (Equation 이기 때문에)
        if ID == 'TCost_Per':
            # TCost_Per EqName : {'type':'EquationName','ID':'TCost_Per','period':1,'name':'TC.1'}
            indices = filter_indices(Variables, {  # 수종 조건이 맞는 indices 는 우선 전부 다 불러오기.
                'ID': 'DecisionVariable',
            })
            for i in indices:  # 각각의 indices 에 대해서 Variable 을 불러온 뒤, 조건에 맞게 처리.
                V = Variables[i]
                produced = 0
                if (V['periodBorn'] < EqName['period']) & (
                        EqName['period'] < V['periodDied']):  # 주벌분기를 포함한 기간 동안 생존한 나무만 선택
                    if V['periodBorn'] <= 0:  # 원래 있던 나무일 때 currentVolumeTables 에서 참고
                        produced = next(item for item in currentVolumeTables
                                        if (item['section'] == V['section']) &
                                        (item['spcID'] == V['spcID']) &
                                        (item['currentAge'] == 1 - V['periodBorn']))['data'][EqName['period']][
                            'produced']
                    else:  # 식재된 나무일 때 -> futureVolumeTables 에서 참고
                        produced = next(item for item in futureVolumeTables
                                        if (item['section'] == V['section']) &
                                        (item['spcID'] == V['spcID']))['data'][EqName['period'] - V['periodBorn']][
                            'produced']
                if produced != 0:
                    line.append(manager['coeffs']['costCoeffs']['thinning'])
                else:
                    line.append(0)

            # RHS
            index = get_index(Variables, {
                'ID': EqName['ID'],
                'name': EqName['name'],
            })
            indices.append(index)
            line.append(-1)
            RHSMatrix[0, rowNum] = 0  # 우변에 0을 할당 (Equation 이기 때문에)
        if ID == 'TRev_Per':
            # TRev_Per EqName : {'type':'EquationName','ID':'TRev_Per','period':1,'name':'TR.1'}
            indices = filter_indices(Variables, {  # 수종별 간벌량 변수 불러오기
                'ID': 'Thin_SpcPer',
                'period': EqName['period']
            })
            for i in indices:  # 각각의 indices 에 대해서 Variable 을 불러온 뒤, 조건에 맞게 처리.
                V = Variables[i]
                thinningPrice = manager['coeffs']['volume2Price']['thinning'][V['spcID']]
                line.append(thinningPrice)

            # RHS
            index = get_index(Variables, {
                'ID': EqName['ID'],
                'name': EqName['name'],
            })
            indices.append(index)
            line.append(-1)
            RHSMatrix[0, rowNum] = 0  # 우변에 0을 할당 (Equation 이기 때문에)
        if ID == 'TNet_Per':
            # TNet_Per EqName : {'type':'EquationName','ID':'TNet_Per','period':1,'name':'ft.1'}
            indices.append(get_index(Variables, {  # ft = *-TC* + TR
                'ID': 'TCost_Per',
                'period': EqName['period'],
            }))
            line.append(-1)
            indices.append(get_index(Variables, {  # ft = -TC + *TR*
                'ID': 'TRev_Per',
                'period': EqName['period'],
            }))
            line.append(1)  # [-1, 1]

            # RHS
            index = get_index(Variables, {
                'ID': EqName['ID'],
                'name': EqName['name'],
            })
            indices.append(index)
            line.append(-1)
            RHSMatrix[0, rowNum] = 0  # 우변에 0을 할당 (Equation 이기 때문에)
        if ID == 'HCost_Per':
            # HCost_Per EqName : {'type':'EquationName','ID':'HCost_Per','period':1,'name':'HC.1'}
            indices = filter_indices(Variables, {  # 수종 조건이 맞는 indices 는 우선 전부 다 불러오기.
                'ID': 'DecisionVariable',
                'periodDied': EqName['period'],
            })
            for i in indices:  # 각각의 indices 에 대해서 Variable 을 불러온 뒤, 조건에 맞게 처리.
                V = Variables[i]
                line.append(manager['coeffs']['costCoeffs']['clearCut'] + manager['coeffs']['costCoeffs']['regeneration'][V['regenSpcID']])

            # RHS
            index = get_index(Variables, {
                'ID': EqName['ID'],
                'name': EqName['name'],
            })
            indices.append(index)
            line.append(-1)
            RHSMatrix[0, rowNum] = 0  # 우변에 0을 할당 (Equation 이기 때문에)
        if ID == 'HRev_Per':
            # HRev_Per EqName : {'type':'EquationName','ID':'HRev_Per','period':1,'name':'HR.1'}
            indices = filter_indices(Variables, {  # 수종별 주벌량 변수 불러오기
                'ID': 'Harv_SpcPer',
                'period': EqName['period']
            })
            for i in indices:  # 각각의 indices 에 대해서 Variable 을 불러온 뒤, 조건에 맞게 처리.
                V = Variables[i]
                clearCutPrice = manager['coeffs']['volume2Price']['clearCut'][V['spcID']]
                line.append(clearCutPrice)

            # RHS
            index = get_index(Variables, {
                'ID': EqName['ID'],
                'name': EqName['name'],
            })
            indices.append(index)
            line.append(-1)
            RHSMatrix[0, rowNum] = 0  # 우변에 0을 할당 (Equation 이기 때문에)
        if ID == 'HNet_Per':
            # HNet_Per EqName : {'type':'EquationName','ID':'HNet_Per','period':1,'name':'fh.1'}
            indices.append(get_index(Variables, {  # fh = *-HC* + HR
                'ID': 'HCost_Per',
                'period': EqName['period'],
            }))
            line.append(-1)
            indices.append(get_index(Variables, {  # fh = *-HC* + *HR*
                'ID': 'HRev_Per',
                'period': EqName['period'],
            }))
            line.append(1)  # [-1, 1]

            # RHS
            index = get_index(Variables, {
                'ID': EqName['ID'],
                'name': EqName['name'],
            })
            indices.append(index)
            line.append(-1)
            RHSMatrix[0, rowNum] = 0  # 우변에 0을 할당 (Equation 이기 때문에)
        if ID == 'f_Per':
            # f_Per EqName : {'type':'EquationName','ID':'f_Per','period':1,'name':'f.1'}
            indices.append(get_index(Variables, {  # f = *ft* + fh
                'ID': 'TNet_Per',
                'period': EqName['period'],
            }))
            indices.append(get_index(Variables, {  # f = ft + *fh*
                'ID': 'HNet_Per',
                'period': EqName['period'],
            }))
            line = [1 for _ in range(len(indices))]  # = [1, 1]

            # RHS
            index = get_index(Variables, {
                'ID': EqName['ID'],
                'name': EqName['name'],
            })
            indices.append(index)  # 우항에 해당,
            line.append(-1)
            RHSMatrix[0, rowNum] = 0  # 우변에 0을 할당 (Equation 이기 때문에)
        if ID == 'g_Per':
            # g_Per EqName : {'type':'EquationName','ID':'g_Per','period':1,'name':'g.1'}
            indices.append(get_index(Variables, {  # g = *C* x 처리비용 x 환율
                'ID': 'Carbon_Per',
                'period': EqName['period'],
            }))
            line.append(manager['coeffs']['CO2ProcessingCost'] * manager['coeffs']['exchangeRate'])

            # RHS
            index = get_index(Variables, {
                'ID': EqName['ID'],
                'name': EqName['name'],
            })
            indices.append(index)  # 우항에 해당,
            line.append(-1)
            RHSMatrix[0, rowNum] = 0  # 우변에 0을 할당 (Equation 이기 때문에)
        if ID == 'h_Per':
            # h_Per EqName : {'type':'EquationName','ID':'h_Per','period':1,'name':'h.1'}
            indices.append(get_index(Variables, {  # h.per = WaterCoeff * Water.per
                'ID': 'Water_Per',
                'period': EqName['period'],
            }))
            line.append(manager['coeffs']['waterSavingCoeff'])

            index = get_index(Variables, {
                'ID': EqName['ID'],
                'name': EqName['name'],
            })
            indices.append(index)  # 우항에 해당,
            line.append(-1)
            RHSMatrix[0, rowNum] = 0  # 우변에 0을 할당 (Equation 이기 때문에)
        if ID == 'NPV_f_Per':
            # NPV_f_Per EqName : {'type':'EquationName','ID':'NPV_f_Per','period':1,'name':'NPV_f.1'}
            indices.append(get_index(Variables, {  # NPV_f = *f* x 1/(1+r)^t
                'ID': 'f_Per',
                'period': EqName['period'],
            }))
            line.append(NPV(manager['coeffs']['interestRate'], EqName['period']))

            # RHS
            index = get_index(Variables, {
                'ID': EqName['ID'],
                'name': EqName['name'],
            })
            indices.append(index)  # 우항에 해당,
            line.append(-1)
            RHSMatrix[0, rowNum] = 0  # 우변에 0을 할당 (Equation 이기 때문에)
        if ID == 'NPV_g_Per':
            # NPV_g_Per EqName : {'type':'EquationName','ID':'NPV_g_Per','period':1,'name':'NPV_g.1'}
            indices.append(get_index(Variables, {  # NPV_f = *f* x 1/(1+r)^t
                'ID': 'g_Per',
                'period': EqName['period'],
            }))
            line.append(NPV(manager['coeffs']['interestRate'], EqName['period']))

            # RHS
            index = get_index(Variables, {
                'ID': EqName['ID'],
                'name': EqName['name'],
            })
            indices.append(index)  # 우항에 해당,
            line.append(-1)
            RHSMatrix[0, rowNum] = 0  # 우변에 0을 할당 (Equation 이기 때문에)
        if ID == 'NPV_h_Per':
            # NPV_h_Per EqName : {'type':'EquationName','ID':'NPV_h_Per','period':1,'name':'NPV_h.1'}
            indices.append(get_index(Variables, {  # NPV_f = *f* x 1/(1+r)^t
                'ID': 'h_Per',
                'period': EqName['period'],
            }))
            line.append(NPV(manager['coeffs']['interestRate'], EqName['period']))

            # RHS
            index = get_index(Variables, {
                'ID': EqName['ID'],
                'name': EqName['name'],
            })
            indices.append(index)  # 우항에 해당,
            line.append(-1)
            RHSMatrix[0, rowNum] = 0  # 우변에 0을 할당 (Equation 이기 때문에)
        if ID == 'NPV_f':
            # NPV_f EqName : {'type':'EquationName','ID':'NPV_f','name':'NPV_f'}
            indices = filter_indices(Variables, {  # NPV_f = ∑ NPV_f_Per
                'ID': 'NPV_f_Per',
            })
            line = [1 for _ in range(len(indices))]

            # RHS
            index = get_index(Variables, {
                'ID': EqName['ID'],
                'name': EqName['name'],
            })
            indices.append(index)  # 우항에 해당,
            line.append(-1)
            RHSMatrix[0, rowNum] = 0  # 우변에 0을 할당 (Equation 이기 때문에)
        if ID == 'NPV_g':
            # NPV_g EqName : {'type':'EquationName','ID':'NPV_g','name':'NPV_g'}
            indices = filter_indices(Variables, {  # NPV_g = ∑ NPV_g_Per
                'ID': 'NPV_g_Per',
            })
            line = [1 for _ in range(len(indices))]

            # RHS
            index = get_index(Variables, {
                'ID': EqName['ID'],
                'name': EqName['name'],
            })
            indices.append(index)  # 우항에 해당,
            line.append(-1)
            RHSMatrix[0, rowNum] = 0  # 우변에 0을 할당 (Equation 이기 때문에)
        if ID == 'NPV_h':
            # NPV_h EqName : {'type':'EquationName','ID':'NPV_h','name':'NPV_h'}
            indices = filter_indices(Variables, {  # NPV_h = ∑ NPV_h_Per
                'ID': 'NPV_h_Per',
            })
            line = [1 for _ in range(len(indices))]

            # RHS
            index = get_index(Variables, {
                'ID': EqName['ID'],
                'name': EqName['name'],
            })
            indices.append(index)  # 우항에 해당,
            line.append(-1)
            RHSMatrix[0, rowNum] = 0  # 우변에 0을 할당 (Equation 이기 때문에)

        if indices:  # if not empty
            # replace specific rowNum and col indices to new values
            LHSMatrix[rowNum, np.array(indices)] = line

    z = [0 for _ in range(LHSMatrix.shape[1] - 3)] + [w1, w2, w3]

    return LHSMatrix, RHSMatrix, z, Variables

def process_output(lp_results, variables):
    variable_name_list = [x['name'] for x in variables]
    sol = lp_results
    df = pd.DataFrame(sol, columns=['value'], index=variable_name_list)

    keys = set()
    for var in variables:
        keys.update(var.keys())

    for key in keys:
        temp_dict = dict()
        for var in variables:
            try:
                temp_dict[var['name']] = var[key]
            except KeyError:
                temp_dict[var['name']] = np.nan

        df[key] = df.index.map(temp_dict)
    return df

def solve(data, solver='scipy-ipm'):
    LHSMatrix, RHSMatrix, z, variables = data
    z = np.array(z)
    if solver == 'highs-ds':
        from scipy.optimize import linprog
        results = linprog(c=-z, A_eq=LHSMatrix, b_eq=RHSMatrix, method=solver, options={
            'disp': True,
            'presolve': False
        })
    if solver == 'highs-ipm':
        from scipy.optimize import linprog
        results = linprog(c=-z, A_eq=LHSMatrix, b_eq=RHSMatrix, method=solver, options={
            # 'disp': True,
            'presolve': False
        })
    if solver == 'scipy-ipm':
        from scipy.optimize import linprog
        results = linprog(c=-z, A_eq=LHSMatrix, b_eq=RHSMatrix, options={
            # 'disp': True,
            'presolve': False
        })
    if solver == 'simplex':
        from scipy.optimize import linprog
        results = linprog(c=-z, A_eq=LHSMatrix, b_eq=RHSMatrix, method=solver, options={
            # 'disp': True,
            'presolve': False
        })
    if solver == 'cylp':
        from cylp.cy import CyClpSimplex
        from cylp.py.modeling.CyLPModel import CyLPArray
        s = CyClpSimplex()
        x = s.addVariable('x', len(LHSMatrix.shape[1]))
        A = CyLPArray(LHSMatrix)
        b = CyLPArray(np.transpose(RHSMatrix))

        # Add constraints
        s += ((A * x) == b)
        s += (x >= 0)
        c = CyLPArray(z)  # Set the objective function
        s.objective = c * x

        # Solve using primal Simplex
        s.primal()
        results = s.primalVariableSolution['x']
    else:
        results = results['x']
    return process_output(results, variables)
