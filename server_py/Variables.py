# -*- coding: utf-8 -*-
from utils import *
from coeffs import *
import numpy as np

DENSITY = 3000


manager = {
  "address": "전남 진도군 임회면",
  "availableSpc": [
    "육박나무",
    "참식나무",
    "비목나무",
    "굴참나무",
    "곰솔",
    "상수리나무"
  ],
  "additionalSpc": [
    "소나무",
    "신갈나무",
    "리기다소나무",
    "졸참나무",
    "일본잎갈나무",
    "밤나무",
    "잣나무",
    "아까시나무",
    "갈참나무",
    "산벚나무",
    "물푸레나무",
    "때죽나무",
    "굴피나무",
    "떡갈나무"
  ],
  "totalSpc": [
    "육박나무",
    "참식나무",
    "비목나무",
    "굴참나무",
    "곰솔",
    "상수리나무",
    "소나무",
    "신갈나무",
    "리기다소나무",
    "졸참나무",
    "일본잎갈나무",
    "밤나무",
    "잣나무",
    "아까시나무",
    "갈참나무",
    "산벚나무",
    "물푸레나무",
    "때죽나무",
    "굴피나무",
    "떡갈나무"
  ],
  "numSections": 1,
  "numSpecies": 2,
  "planningPeriod": 10,
  "startYear": 0,
  "spcClasses": [
    {
      "class": 1,
      "speciesID": "A",
      "species": "육박나무"
    },
    {
      "class": 2,
      "speciesID": "B",
      "species": "일본잎갈나무"
    }
  ],
  "spcLists": [
    "육박나무",
    "일본잎갈나무"
  ],
  "spc2ID": {
    "육박나무": "A",
    "일본잎갈나무": "B"
  },
  "ID2Spc": {
    "A": "육박나무",
    "B": "일본잎갈나무"
  },
  "spcIDList": [
    "A",
    "B"
  ],
  "currentSpc": [
    {
      "section": 1,
      "species": "육박나무",
      "age": 3,
      "area": 10,
      "volume": 140
    },
    {
      "section": 1,
      "species": "일본잎갈나무",
      "age": 3,
      "area": 10,
      "volume": 140
    }
  ],
  "thinningScenario": [],
  "forManPlan": [
    {
      "section": 1,
      "species": "육박나무",
      "clearCutYear": 6,
      "thinningScenario": [
        0,
        0.3,
        0,
        0.3,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0
      ]
    },
    {
      "section": 1,
      "species": "일본잎갈나무",
      "clearCutYear": 6,
      "thinningScenario": [
        0,
        0.3,
        0,
        0.3,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0
      ]
    }
  ],
  "regenerationRules": [],
  "spcGrowth": {
    "육박나무": {
      "points": [
        [
          1,
          -0.002509
        ],
        [
          2,
          0.010021
        ],
        [
          3,
          0.017351
        ],
        [
          4,
          0.022551
        ],
        [
          5,
          0.026585
        ],
        [
          6,
          0.029881
        ],
        [
          7,
          0.032667
        ],
        [
          8,
          0.035081
        ],
        [
          9,
          0.03721
        ],
        [
          10,
          0.039115
        ],
        [
          11,
          0.040838
        ],
        [
          12,
          0.042411
        ],
        [
          13,
          0.043858
        ],
        [
          14,
          0.045197
        ],
        [
          15,
          0.046444
        ],
        [
          16,
          0.047611
        ],
        [
          17,
          0.048707
        ],
        [
          18,
          0.04974
        ],
        [
          19,
          0.050718
        ],
        [
          20,
          0.051645
        ],
        [
          21,
          0.052527
        ],
        [
          22,
          0.053368
        ],
        [
          23,
          0.054171
        ],
        [
          24,
          0.054941
        ],
        [
          25,
          0.055679
        ],
        [
          26,
          0.056388
        ],
        [
          27,
          0.05707
        ],
        [
          28,
          0.057727
        ]
      ],
      "equation": [
        -0.002509,
        0.018077
      ],
      "string": "y = -0.002509 + 0.018077 ln(x)",
      "r2": 0.948627,
      "predictions": [
        0,
        0.010021,
        0.017351,
        0.022551,
        0.026585,
        0.029881,
        0.032667,
        0.035081,
        0.03721,
        0.039115,
        0.040838,
        0.042411,
        0.043858,
        0.045197,
        0.046444,
        0.047611,
        0.048707,
        0.04974,
        0.050718,
        0.051645,
        0.052527,
        0.053368,
        0.054171,
        0.054941,
        0.055679,
        0.056388,
        0.05707,
        0.057727,
        0.058362,
        0.058974,
        0.059567,
        0.060141,
        0.060697,
        0.061237,
        0.061761,
        0.06227,
        0.062766,
        0.063248,
        0.063717,
        0.064175,
        0.064621,
        0.065057,
        0.065482,
        0.065898,
        0.066304,
        0.066701,
        0.06709,
        0.067471,
        0.067843,
        0.068209,
        0.068567,
        0.068918,
        0.069262,
        0.0696,
        0.069932,
        0.070257,
        0.070577,
        0.070892,
        0.071201,
        0.071504,
        0.071803,
        0.072097,
        0.072386,
        0.072671,
        0.072951,
        0.073227,
        0.073499,
        0.073767,
        0.074031,
        0.074291,
        0.074547,
        0.0748,
        0.07505,
        0.075296,
        0.075538,
        0.075778,
        0.076014,
        0.076247,
        0.076478,
        0.076705,
        0.076929,
        0.077151,
        0.07737,
        0.077587,
        0.077801,
        0.078012,
        0.078221,
        0.078428,
        0.078632,
        0.078834,
        0.079034,
        0.079231,
        0.079427,
        0.07962,
        0.079811,
        0.080001,
        0.080188,
        0.080373,
        0.080557,
        0.080739,
        0.080919,
        0.081097,
        0.081273,
        0.081448,
        0.081621,
        0.081792,
        0.081962,
        0.08213,
        0.082296,
        0.082462,
        0.082625,
        0.082787,
        0.082948,
        0.083107,
        0.083265,
        0.083422,
        0.083577,
        0.083731,
        0.083883,
        0.084034,
        0.084185,
        0.084333,
        0.084481,
        0.084627,
        0.084772,
        0.084916,
        0.085059,
        0.085201,
        0.085342,
        0.085481,
        0.08562,
        0.085757,
        0.085894,
        0.086029,
        0.086164,
        0.086297,
        0.086429,
        0.086561,
        0.086691,
        0.086821,
        0.08695,
        0.087077,
        0.087204,
        0.08733,
        0.087455,
        0.08758,
        0.087703,
        0.087826,
        0.087947,
        0.088068
      ],
      "growthCombined": [
        0,
        0.0116,
        0.0177,
        0.0237,
        0.0278,
        0.0305,
        0.0332,
        0.0342,
        0.0367,
        0.0385,
        0.0393,
        0.0415,
        0.0416,
        0.0421,
        0.0427,
        0.0435,
        0.0445,
        0.0451,
        0.0464,
        0.0479,
        0.0506,
        0.0525,
        0.0547,
        0.057,
        0.0595,
        0.0622,
        0.065,
        0.067,
        0.058974,
        0.059567,
        0.060141,
        0.060697,
        0.061237,
        0.061761,
        0.06227,
        0.062766,
        0.063248,
        0.063717,
        0.064175,
        0.064621,
        0.065057,
        0.065482,
        0.065898,
        0.066304,
        0.066701,
        0.06709,
        0.067471,
        0.067843,
        0.068209,
        0.068567,
        0.068918,
        0.069262,
        0.0696,
        0.069932,
        0.070257,
        0.070577,
        0.070892,
        0.071201,
        0.071504,
        0.071803,
        0.072097,
        0.072386,
        0.072671,
        0.072951,
        0.073227,
        0.073499,
        0.073767,
        0.074031,
        0.074291,
        0.074547,
        0.0748,
        0.07505,
        0.075296,
        0.075538,
        0.075778,
        0.076014,
        0.076247,
        0.076478,
        0.076705,
        0.076929,
        0.077151,
        0.07737,
        0.077587,
        0.077801,
        0.078012,
        0.078221,
        0.078428,
        0.078632,
        0.078834,
        0.079034,
        0.079231,
        0.079427,
        0.07962,
        0.079811,
        0.080001,
        0.080188,
        0.080373,
        0.080557,
        0.080739,
        0.080919,
        0.081097,
        0.081273,
        0.081448,
        0.081621,
        0.081792,
        0.081962,
        0.08213,
        0.082296,
        0.082462,
        0.082625,
        0.082787,
        0.082948,
        0.083107,
        0.083265,
        0.083422,
        0.083577,
        0.083731,
        0.083883,
        0.084034,
        0.084185,
        0.084333,
        0.084481,
        0.084627,
        0.084772,
        0.084916,
        0.085059,
        0.085201,
        0.085342,
        0.085481,
        0.08562,
        0.085757,
        0.085894,
        0.086029,
        0.086164,
        0.086297,
        0.086429,
        0.086561,
        0.086691,
        0.086821,
        0.08695,
        0.087077,
        0.087204,
        0.08733,
        0.087455,
        0.08758,
        0.087703,
        0.087826,
        0.087947,
        0.088068,
      ]
    },
    "일본잎갈나무": {
      "points": [
        [
          1,
          -0.343145
        ],
        [
          2,
          -0.181998
        ],
        [
          3,
          -0.087733
        ],
        [
          4,
          -0.020851
        ],
        [
          5,
          0.031027
        ],
        [
          6,
          0.073414
        ],
        [
          7,
          0.109252
        ],
        [
          8,
          0.140296
        ],
        [
          9,
          0.167679
        ],
        [
          10,
          0.192174
        ],
        [
          11,
          0.214332
        ],
        [
          12,
          0.234561
        ],
        [
          13,
          0.25317
        ],
        [
          14,
          0.270399
        ],
        [
          15,
          0.286439
        ],
        [
          16,
          0.301443
        ],
        [
          17,
          0.315537
        ],
        [
          18,
          0.328826
        ],
        [
          19,
          0.341396
        ],
        [
          20,
          0.353321
        ],
        [
          21,
          0.364664
        ],
        [
          22,
          0.375479
        ],
        [
          23,
          0.385814
        ],
        [
          24,
          0.395708
        ],
        [
          25,
          0.405199
        ],
        [
          26,
          0.414317
        ],
        [
          27,
          0.423091
        ],
        [
          28,
          0.431546
        ],
        [
          29,
          0.439704
        ],
        [
          30,
          0.447586
        ],
        [
          31,
          0.455209
        ],
        [
          32,
          0.46259
        ],
        [
          33,
          0.469744
        ],
        [
          34,
          0.476684
        ],
        [
          35,
          0.483424
        ],
        [
          36,
          0.489973
        ],
        [
          37,
          0.496343
        ],
        [
          38,
          0.502543
        ],
        [
          39,
          0.508582
        ],
        [
          40,
          0.514468
        ],
        [
          41,
          0.520209
        ]
      ],
      "equation": [
        -0.343145,
        0.232486
      ],
      "string": "y = -0.343145 + 0.232486 ln(x)",
      "r2": 0.69078,
      "predictions": [
        0,
        0,
        0,
        0,
        0.031027,
        0.073414,
        0.109252,
        0.140296,
        0.167679,
        0.192174,
        0.214332,
        0.234561,
        0.25317,
        0.270399,
        0.286439,
        0.301443,
        0.315537,
        0.328826,
        0.341396,
        0.353321,
        0.364664,
        0.375479,
        0.385814,
        0.395708,
        0.405199,
        0.414317,
        0.423091,
        0.431546,
        0.439704,
        0.447586,
        0.455209,
        0.46259,
        0.469744,
        0.476684,
        0.483424,
        0.489973,
        0.496343,
        0.502543,
        0.508582,
        0.514468,
        0.520209,
        0.525811,
        0.531281,
        0.536626,
        0.541851,
        0.546961,
        0.55196,
        0.556855,
        0.561649,
        0.566346,
        0.570949,
        0.575464,
        0.579892,
        0.584238,
        0.588504,
        0.592693,
        0.596808,
        0.600851,
        0.604825,
        0.608733,
        0.612576,
        0.616356,
        0.620076,
        0.623737,
        0.627342,
        0.630891,
        0.634387,
        0.637831,
        0.641225,
        0.644571,
        0.647868,
        0.65112,
        0.654327,
        0.65749,
        0.660611,
        0.66369,
        0.666729,
        0.669729,
        0.67269,
        0.675615,
        0.678503,
        0.681356,
        0.684174,
        0.686958,
        0.689709,
        0.692428,
        0.695116,
        0.697773,
        0.7004,
        0.702998,
        0.705567,
        0.708108,
        0.710621,
        0.713107,
        0.715568,
        0.718002,
        0.720411,
        0.722796,
        0.725156,
        0.727493,
        0.729806,
        0.732096,
        0.734365,
        0.736611,
        0.738836,
        0.741039,
        0.743222,
        0.745385,
        0.747528,
        0.749651,
        0.751755,
        0.75384,
        0.755906,
        0.757955,
        0.759985,
        0.761998,
        0.763994,
        0.765972,
        0.767934,
        0.76988,
        0.771809,
        0.773723,
        0.77562,
        0.777503,
        0.77937,
        0.781223,
        0.783061,
        0.784884,
        0.786693,
        0.788489,
        0.79027,
        0.792038,
        0.793793,
        0.795534,
        0.797263,
        0.798978,
        0.800682,
        0.802373,
        0.804051,
        0.805718,
        0.807372,
        0.809015,
        0.810647,
        0.812267,
        0.813876,
        0.815474,
        0.817061,
        0.818637,
        0.820202,
        0.821758
      ],
      "growthCombined": [
        0,
        0.013,
        0.0209,
        0.0263,
        0.0306,
        0.0336,
        0.037,
        0.0407,
        0.0497,
        0.0609,
        0.0744,
        0.0842,
        0.0983,
        0.118,
        0.1341,
        0.1564,
        0.1764,
        0.1953,
        0.2136,
        0.232,
        0.2547,
        0.2697,
        0.2888,
        0.3193,
        0.3457,
        0.375,
        0.4038,
        0.4274,
        0.4582,
        0.4842,
        0.504,
        0.5371,
        0.5707,
        0.6056,
        0.6345,
        0.6488,
        0.6631,
        0.6858,
        0.6996,
        0.7219,
        0.7491,
        0.531281,
        0.536626,
        0.541851,
        0.546961,
        0.55196,
        0.556855,
        0.561649,
        0.566346,
        0.570949,
        0.575464,
        0.579892,
        0.584238,
        0.588504,
        0.592693,
        0.596808,
        0.600851,
        0.604825,
        0.608733,
        0.612576,
        0.616356,
        0.620076,
        0.623737,
        0.627342,
        0.630891,
        0.634387,
        0.637831,
        0.641225,
        0.644571,
        0.647868,
        0.65112,
        0.654327,
        0.65749,
        0.660611,
        0.66369,
        0.666729,
        0.669729,
        0.67269,
        0.675615,
        0.678503,
        0.681356,
        0.684174,
        0.686958,
        0.689709,
        0.692428,
        0.695116,
        0.697773,
        0.7004,
        0.702998,
        0.705567,
        0.708108,
        0.710621,
        0.713107,
        0.715568,
        0.718002,
        0.720411,
        0.722796,
        0.725156,
        0.727493,
        0.729806,
        0.732096,
        0.734365,
        0.736611,
        0.738836,
        0.741039,
        0.743222,
        0.745385,
        0.747528,
        0.749651,
        0.751755,
        0.75384,
        0.755906,
        0.757955,
        0.759985,
        0.761998,
        0.763994,
        0.765972,
        0.767934,
        0.76988,
        0.771809,
        0.773723,
        0.77562,
        0.777503,
        0.77937,
        0.781223,
        0.783061,
        0.784884,
        0.786693,
        0.788489,
        0.79027,
        0.792038,
        0.793793,
        0.795534,
        0.797263,
        0.798978,
        0.800682,
        0.802373,
        0.804051,
        0.805718,
        0.807372,
        0.809015,
        0.810647,
        0.812267,
        0.813876,
        0.815474,
        0.817061,
        0.818637,
        0.820202,
        0.821758,
      ]
    }
  },
  "coeffs": {
    "volume2Carbon": {
      "육박나무": 2,
      "일본잎갈나무": 1.431354293
    },
    "waterCoeffs": [
      {
        "section": 1,
        "spcIDs": [
          "A",
          "B"
        ],
        "data": [
          2090,
          2180,
          2270,
          2360,
          2450,
          2540,
          2630,
          2720,
          2810,
          2900
        ]
      }
    ],
    "laborCoeffs": {
      "clearCut": 169.858462306131,
      "thinning": 13.505923710842,
      "regeneration": {
        "A": 15,
        "B": 15,
        ".": 0
      }
    },
    "costCoeffs": {
      "clearCut": 9207.3361732583,
      "thinning": 3017.14924786963,
      "regeneration": {
        "A": 2000,
        "B": 2000
      }
    },
    "volume2Price": {
      "thinning": {
        "A": 50000,
        "B": 79176
      },
      "clearCut": {
        "A": 70000,
        "B": 68905
      }
    },
    "CO2ProcessingCost": 50,
    "exchangeRate": 1200,
    "waterSavingCoeff": 959.91,
    "interestRate": 0.015,
    "initialDensity": 3000,
    "w1": 0.5,
    "w2": 0.5,
    "w3": 0
  }
}



########################################################################
#              Define Initial Conditions From Manager                  #
########################################################################
spc2ID = {obj['species']: obj['speciesID'] for obj in manager['spcClasses']}
'''
{
    '소나무': 'O',
    '리기다소나무': 'C',
    '잣나무': 'K',
    '일본잎갈나무': 'L',
    '상수리나무': 'S',
    '신갈나무': 'B'
}
'''  # spc_to_ID: 전체 수종명을 입력하면 수종 ID로 바꿔주는 딕셔너리

ID2spc = {obj['speciesID']: obj['species'] for obj in manager['spcClasses']}
'''
{
    'O': '소나무',
    'C': '리기다소나무',
    'K': '잣나무',
    'L': '일본잎갈나무',
    'S': '상수리나무',
    'B': '신갈나무'
}
'''  # ID_to_spc: spcID를 입력하면 전체 수종명으로 바꿔주는 딕셔너리

spcIDList = list(spc2ID.values())
'''
['O', 'C', 'K', 'L', 'S', 'B']
'''  # spcIDList: 사용자가 순서대로 입력한 spcID 리스트

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
'''
{
     'section': 1,
     'species': '잣나무',
     'spcID': 'K',
     'age': 8,
     'area': 208.7,
     'volume': 394.7714,
     'periodBorn': -7,
     'periodDied': 1,
     'clearCutYear': 7,
     'thinningScenario': [0, 0.3, 0, 0.3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     'spcGrowth': {
         'points': [[1, -0.166863], [2, -0.064439], [3, -0.004525], [4, 0.037984], [5, 0.070957], [6, 0.097898],
                    [7, 0.120676], [8, 0.140408], [9, 0.157812], [10, 0.173381], [11, 0.187464], [12, 0.200322],
                    [13, 0.212149], [14, 0.2231], [15, 0.233295], [16, 0.242831], [17, 0.25179], [18, 0.260236],
                    [19, 0.268225], [20, 0.275804], [21, 0.283014], [22, 0.289888], [23, 0.296456], [24, 0.302745]],
         'equation': [-0.166863, 0.147766],
         'string': 'y = -0.166863 + 0.147766 ln(x)',
         'r2': 0.680663,
         'predictions': [0, 0, 0, 0.037984, 0.070957, 0.097898, 0.120676, 0.140408, 0.157812, 0.173381, 0.187464,
                         0.200322, 0.212149, 0.2231, 0.233295, 0.242831, 0.25179, 0.260236, 0.268225, 0.275804,
                         0.283014, 0.289888, 0.296456, 0.302745, 0.308777, 0.314573, 0.32015, 0.325524, 0.330709,
                         0.335718, 0.340564, 0.345255, 0.349802, 0.354213, 0.358497, 0.362659, 0.366708, 0.370649,
                         0.374487, 0.378228, 0.381877, 0.385437, 0.388914, 0.392312, 0.395632, 0.39888, 0.402058,
                         0.405169, 0.408216, 0.411201, 0.414127, 0.416996, 0.419811, 0.422573, 0.425285, 0.427947,
                         0.430563, 0.433132, 0.435658, 0.438142, 0.440584, 0.442987, 0.445351, 0.447679, 0.44997,
                         0.452226, 0.454448, 0.456637, 0.458794, 0.46092, 0.463016, 0.465083, 0.467121, 0.469131,
                         0.471115, 0.473072, 0.475004, 0.47691, 0.478793, 0.480652, 0.482487, 0.4843, 0.486091,
                         0.487861, 0.48961, 0.491338, 0.493046, 0.494735, 0.496405, 0.498056, 0.499689, 0.501304,
                         0.502901, 0.504481, 0.506045, 0.507592, 0.509124, 0.510639, 0.512139, 0.513625, 0.515095,
                         0.516551, 0.517992, 0.51942, 0.520834, 0.522235, 0.523622, 0.524997, 0.526359, 0.527708,
                         0.529045, 0.530371, 0.531684, 0.532986, 0.534277, 0.535556, 0.536824, 0.538082, 0.539329,
                         0.540566, 0.541792, 0.543008, 0.544214, 0.545411, 0.546598, 0.547775, 0.548943, 0.550102,
                         0.551252, 0.552393, 0.553525, 0.554649, 0.555764, 0.556871, 0.55797, 0.55906, 0.560143,
                         0.561218, 0.562284, 0.563344, 0.564395, 0.56544, 0.566477, 0.567506, 0.568529, 0.569545,
                         0.570553, 0.571555, 0.57255, 0.573539],
         'growthCombined': [0, 0.0092, 0.0145, 0.0177, 0.0212, 0.0276, 0.0391, 0.0532, 0.0685, 0.0851, 0.1002, 0.1177,
                            0.1406, 0.1623, 0.1875, 0.2188, 0.2493, 0.2721, 0.3064, 0.3481, 0.3813, 0.4066, 0.4261,
                            0.4375, 0.314573, 0.32015, 0.325524, 0.330709, 0.335718, 0.340564, 0.345255, 0.349802,
                            0.354213, 0.358497, 0.362659, 0.366708, 0.370649, 0.374487, 0.378228, 0.381877, 0.385437,
                            0.388914, 0.392312, 0.395632, 0.39888, 0.402058, 0.405169, 0.408216, 0.411201, 0.414127,
                            0.416996, 0.419811, 0.422573, 0.425285, 0.427947, 0.430563, 0.433132, 0.435658, 0.438142,
                            0.440584, 0.442987, 0.445351, 0.447679, 0.44997, 0.452226, 0.454448, 0.456637, 0.458794,
                            0.46092, 0.463016, 0.465083, 0.467121, 0.469131, 0.471115, 0.473072, 0.475004, 0.47691,
                            0.478793, 0.480652, 0.482487, 0.4843, 0.486091, 0.487861, 0.48961, 0.491338, 0.493046,
                            0.494735, 0.496405, 0.498056, 0.499689, 0.501304, 0.502901, 0.504481, 0.506045, 0.507592,
                            0.509124, 0.510639, 0.512139, 0.513625, 0.515095, 0.516551, 0.517992, 0.51942, 0.520834,
                            0.522235, 0.523622, 0.524997, 0.526359, 0.527708, 0.529045, 0.530371, 0.531684, 0.532986,
                            0.534277, 0.535556, 0.536824, 0.538082, 0.539329, 0.540566, 0.541792, 0.543008, 0.544214,
                            0.545411, 0.546598, 0.547775, 0.548943, 0.550102, 0.551252, 0.552393, 0.553525, 0.554649,
                            0.555764, 0.556871, 0.55797, 0.55906, 0.560143, 0.561218, 0.562284, 0.563344, 0.564395,
                            0.56544, 0.566477, 0.567506, 0.568529, 0.569545, 0.570553, 0.571555, 0.57255, 0.573539,
                            None]
     }
 }
'''  # initialConditions: 초기 조건값들

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
'''
{
     'section': 1,
     'spcID': 'K',
     'currentAge': 6,
     'data': {
         1: {
             'period': 1,
             'age': 6,
             'volume': 167.12,
             'produced': 0.0
         },
         2: {
             'period': 2,
             'age': 7,
             'volume': 0.0,
             'produced': 175.80818638706174
         },
         3: {
             'period': 3,
             'age': 8,
             'volume': 7.526354104377134,
             'produced': 0.0
         },
         4: {
             'period': 4,
             'age': 9,
             'volume': 14.164741841686038,
             'produced': 0.0
         },
         5: {
             'period': 5,
             'age': 10,
             'volume': 20.103207635880608,
             'produced': 0.0
         },
         6: {
             'period': 6,
             'age': 11,
             'volume': 25.474870156250688,
             'produced': 0.0
         }
     }
 }
'''  # currentVolumeTables: 현재 존재하는 나무들에 대한


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
'''
{
     'section': 1,
     'spcID': 'O',
     'data': {
         1: {
             'period': 1,
             'age': 1,
             'volume': 235.05,
             'produced': 0.0
         },
         2: {
             'period': 2,
             'age': 2,
             'volume': 238.5432,
             'produced': 102.2328
         },
         3: {
             'period': 3,
             'age': 3,
             'volume': 300.3882,
             'produced': 0.0
         },
         4: {
             'period': 4,
             'age': 4,
             'volume': 240.98844000000003,
             'produced': 103.28076
         },
         5: {
             'period': 5,
             'age': 5,
             'volume': 275.02344,
             'produced': 0.0
         },
         6: {
             'period': 6,
             'age': 6,
             'volume': 302.83344,
             'produced': 0.0
         },
         7: {
             'period': 7,
             'age': 7,
             'volume': 0.0,
             'produced': 326.34443999999996
         }
     }
 }
'''

print(futureVolumeTables)

########################################################################
#                      Create Decision Variables                       #
########################################################################
regenerationRules = [
    {'section': 1, 'spcID': 'B', 'regenerationRule': ['S', 'B']},
    {'section': 1, 'spcID': 'S', 'regenerationRule': ['S', 'B']},
]  # 1 구역의 B는 S, B 로만 갱신


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
                 '_'+str(condition['periodBorn']) +
                 condition['spcID']+pd_string +
                 condition['regenSpcID']
        ))

    def sort(self):
        self.list = sorted(self.list,
                           key=lambda e: (e['section'], e['periodBorn'], spcIDList.index(e['spcID']), e['periodDied']))


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

########################################################################
#                     Create Accounting Variables                      #
########################################################################
# Naming Rules: 각 요소의 순서대로 이름을 생성. undefined 인 경우 그 key 를 그대로 이름에 활용.
ID2AccVarNameRules = {
    'Vol_SpcPer': ['spcID', 'V', '.', 'period'],  # 특정 수종의 분기별 재적
    'Area_SpcSecPer': ['section', 'spcID', 'A',  '.', 'period'],  # 2KA.10 => 10분기의 2구역, K 수종의 면적
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
                    AccountingVariables.add({'ID': ID, 'section': sec, 'spcID': spcID, 'age': age, 'period': per})

Variables = DecisionVariables.list + AccountingVariables.list

########################################################################
#              Create Decision Variables' Equation Names               #
########################################################################


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
                 '_'+str(condition['periodBorn']) +
                 condition['spcID']
        ))

DecisionVariableEquationNames = DecisionVariableEquationNamesClass()
for dv in DecisionVariables.list:
    DecisionVariableEquationNames.add(dv)
########################################################################
#             Create Accounting Variables' Equation Names              #
########################################################################
AccountingVariableEquationNames = list()
for av in AccountingVariables.list:
    AccVarEqName = av.copy()
    AccVarEqName['type'] = "EquationName"
    AccountingVariableEquationNames.append(AccVarEqName)

EquationNames = DecisionVariableEquationNames.list + AccountingVariableEquationNames
########################################################################
#          Create Matrix from defined Variables Equation Names         #
########################################################################



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
                               (item['spcID'] == V['spcID']))['data'][EqName['period'] - V['periodBorn']]['volume']
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
                               (item['spcID'] == V['spcID']))['data'][EqName['period'] - V['periodBorn']]['produced']
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
                               (item['spcID'] == V['spcID']))['data'][EqName['period'] - V['periodBorn']]['produced']
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
            carbonCoeff = volume2Carbon[ID2spc[V['spcID']]]
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
                waterCoeff = next(item for item in waterCoeffs
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
                                    (item['currentAge'] == 1 - V['periodBorn']))['data'][EqName['period']]['produced']
                else:  # 식재된 나무일 때 -> futureVolumeTables 에서 참고
                    produced = next(item for item in futureVolumeTables
                                    if (item['section'] == V['section']) &
                                    (item['spcID'] == V['spcID']))['data'][EqName['period'] - V['periodBorn']][
                        'produced']
            if produced != 0:
                if EqName['period'] == V['periodDied']:
                    line.append(laborCoeffs['clearCut'] + laborCoeffs['regeneration'][
                        V['regenSpcID']])  # clearCut + regen labor. 만약 regeneration = '.' 인 경우 0
                else:
                    line.append(laborCoeffs['thinning'])
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
                                    (item['currentAge'] == 1 - V['periodBorn']))['data'][EqName['period']]['produced']
                else:  # 식재된 나무일 때 -> futureVolumeTables 에서 참고
                    produced = next(item for item in futureVolumeTables
                                    if (item['section'] == V['section']) &
                                    (item['spcID'] == V['spcID']))['data'][EqName['period'] - V['periodBorn']][
                        'produced']
            if produced != 0:
                line.append(costCoeffs['thinning'])
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
            thinningPrice = volume2Price['thinning'][V['spcID']]
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
            line.append(costCoeffs['clearCut'] + costCoeffs['regeneration'][V['regenSpcID']])

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
            clearCutPrice = volume2Price['clearCut'][V['spcID']]
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
        line.append(CO2ProcessingCost * exchangeRate)

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
        line.append(waterSavingCoeff)

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
        line.append(NPV(interestRate, EqName['period']))

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
        line.append(NPV(interestRate, EqName['period']))

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
        line.append(NPV(interestRate, EqName['period']))

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

VariableNameList = [x['name'] for x in Variables]
equation_comparisons = ['=' for _ in range(len(VariableNameList))]
Z = [0 for _ in range(len(VariableNameList) - 3)] + [w1, w2, w3]


print(len(Variables))