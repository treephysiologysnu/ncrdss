import numpy as np
from utils import *

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
  "startYear": 2020,
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
      "area": 8,
      "volume": 80,
      "density": 800
    },
    {
      "section": 1,
      "species": "일본잎갈나무",
      "age": 5,
      "area": 18,
      "volume": 180,
      "density": 1800
    }
  ],
  "thinningScenario": [],
  "forManPlan": [
    {
      "section": 1,
      "species": "육박나무",
      "spcID": "A",
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
      ],
      "density": 1800
    },
    {
      "section": 1,
      "species": "일본잎갈나무",
      "spcID": "B",
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
      ],
      "density": 2800
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
    "initialDensity": 250,
    "w1": 0.5,
    "w2": 0.5,
    "w3": 0
  },
  "completedFlags": {
    "address": True,
    "table_base": True,
    "table_SpcClasses": True,
    "table_currentSpc": True,
    "table_thinning": True,
    "table_ForManPlan": True
  }
}

# TODO : currentVolumeTable & futureVolumeTable 밀도 파트 추가하기.

w1 = manager['coeffs']['w1']
w2 = manager['coeffs']['w2']
w3 = manager['coeffs']['w3']

DENSITY = manager['coeffs']['initialDensity']


# TODO currentSpc 리스트 안에 density
# TODO forManPlan 리스트 안에 density key 존재

class Manager:
    def __init__(self, obj):
        """

        :param obj: JSON object transferred from the front-end
        """
        self.address = obj['address']
        self.numSections = obj['numSections']
        self.numSpecies = obj['numSpecies']
        self.planningPeriod = obj['planningPeriod']
        self.startYear = obj['startYear']
        self.spcClasses = obj['spcClasses']
        self.spcLists = obj['spcLists']
        self.spc2ID = obj['spc2ID']
        self.ID2Spc = obj['ID2Spc']
        self.spcIDList = obj['spcIDList']
        self.currentSpc = obj['currentSpc']
        self.forManPlan = obj['forManPlan']
        self.regenerationRules = obj['regenerationRules']
        self.spcGrowth = obj['spcGrowth']
        self.coeffs = obj['coeffs']

        self.spc2Growth = dict()  # TODO - 생장식 수정

        self.initialConditions = []
        self.currentVolumeTables = []
        self.futureVolumeTables = []
        self.ageMax = np.max([x['clearCutYear'] for x in self.forManPlan])

        self.generate_initial_conditions()

    def generate_initial_conditions(self):
        """
        
        :return: 
        """
        for currentSpc in self.currentSpc:
            temp_dict = currentSpc.copy()
            temp_dict['spcID'] = self.spc2ID[temp_dict['species']]
            temp_dict['periodBorn'] = 1 - temp_dict['age']  # TODO - periodBorn 정의 식 점검하기

            forManPlan = get_matching_item(self.forManPlan, temp_dict, ['section', 'species'])

            if temp_dict['periodBorn'] + forManPlan['clearCutYear'] <= 0:  # 만약 현재 존재하는 나무들이 주벌시기가 이미 지나버린 경우
                temp_dict['periodDied'] = 1
            else:
                temp_dict['periodDied'] = temp_dict['periodBorn'] + forManPlan['clearCutYear']
            temp_dict['clearCutYear'] = forManPlan['clearCutYear']

            if 'thinningScenario' in forManPlan:  # thinningScenario key 가 존재하면
                temp_dict['thinningScenario'] = forManPlan['thinningScenario']
            else:  # 키가 존재하지 않는 경우 (사용자가 입력 X) 계획 기간 길이만큼 zeros 생성
                temp_dict['thinningScenario'] = [0 for _ in range(self.planningPeriod)]

            temp_dict['spcGrowth'] = self.spcGrowth[temp_dict['species']]

            self.initialConditions.append(temp_dict)


manager = Manager(manager)


class VolumeScenario:
    """
    growth 와 density 를 이용해서 volume 을 계산하는 클래스.
    """
    def __init__(self, decision_var):  # TODO - UNIQUE Decision Variable 에 대한 입력으로 GrowthScenario 를 만들어야 함!
        self.address = manager.address  # TODO - coordinates 변환
        self.coordinates = None
        self.start_year = manager.startYear
        self.planningPeriod = manager.planningPeriod
        self.period_born = decision_var['periodBorn']
        self.spcID = decision_var['spcID']
        self.species = manager.ID2Spc[self.spcID]
        self.forManPlan = get_matching_item(manager.forManPlan, decision_var, ['section', 'spcID'])

        " Define Initial Conditions "
        self.initial_condition = None  # 초기 조건으로 입력되는 initialCondition object
        self.initial_volume = None  # 초기 조건으로 입력된 재적값.
        self.initial_density = None  # 초기 조건으로 입력된 밀도, 혹은 입력되지 않은 경우 산림시업 정보에서 입력된 초기식재밀도.
        self.initial_age = None

        " Define Growth Function and Variables "
        self.predict_growth = None  # 연도를 입력하면 생장량을 반환하는 기본 곡선식
        self.growth_coefficients = None # 기본 생장 곡선식에 들어가는 계수들. 현재 조건 입력시에 보정됨.
        self.growth_env_cal_ratio = None  # 환경에 따른 보정 계수

        " Define Density Function and Variables "
        self.predict_density = None
        self.density_coefficients = 1  # 기본 밀도 감소 곡선을 현재 영급 조건으로 fitting 하기 위한 계수

        " Define Thinning and Clear-cut Plans "
        self.clear_cut_year = self.forManPlan['clearCutYear']
        self.thinning_scenario = self.forManPlan['thinningScenario']


        " Initialize growth and density "
        self.set_growth_function_coeffs()
        self.predict_growth = self.get_growth_base_function()
        self.predict_density = self.get_density_base_function()

        " Initialize variables if initial condition is input "
        if self.period_born < 1:
            self.initial_condition = get_matching_item(manager.initialConditions, decision_var,
                                                       ['section', 'periodBorn', 'spcID'])
            self.initial_volume = self.initial_condition['volume']
            self.initial_density = self.initial_condition['density']
            self.initial_age = self.initial_condition['age']

            self.fit_growth_coefficients()
            self.fit_density_coefficients()

    def fit_growth_coefficients(self):

        temperature, precipitation = read_environment_data(self.start_year, self.coordinates)
        if self.initial_volume and self.initial_density:
            r_t, r_p, r_d = get_growth_env_cal_ratio(self.species, temp=temperature, precp=precipitation, density=self.initial_density)
            update_ratio = self.initial_volume / (self.predict_growth(self.initial_age) * r_t * r_p * r_d)
            self.growth_coefficients = [x * update_ratio for x in self.growth_coefficients]
            
        elif self.initial_volume:
            r_t, r_p, _ = get_growth_env_cal_ratio(self.species, temp=temperature, precp=precipitation) # ignoring density
            update_ratio = self.initial_volume / (self.predict_growth(self.initial_age) * r_t * r_p)
            self.initial_density = update_ratio
            _, _, r_d = get_growth_env_cal_ratio(self.species,
                                                 temp=temperature,
                                                 precp=precipitation,
                                                 density=self.initial_density)

            update_ratio = update_ratio / r_d
            self.growth_coefficients = [x * update_ratio for x in self.growth_coefficients]

    def fit_density_coefficients(self):

        self.density_coefficients = self.initial_density / self.predict_density(self.initial_age)

    def calc_volume(self, period):
        """ 주어진 분기 수를 이용해서, 해당 연도의 재적량을 계산합니다.

        :param period: int.
            재적을 예측하려는 경영 계획 중 p 번째 분기.
        :return: Float.
        """
        year = self.start_year + 10 * period # 그 해가 몇년인지를 찾기
        V = self.predict_growth(period)
        t, p = read_environment_data(year, self.coordinates)
        d = self.predict_density(period)
        r_t, r_p, r_d = get_growth_env_cal_ratio(self.species, temp=t, precp=p,
                                                 density=d)

        return V * r_t * r_p * r_p * d

    def get_growth_base_function(self):
        """
        Sets growth_base_function to an equation function that calculates tree growth by period.
        The equation gets period number (p) as its input.
        :return: None
        """
        coefficients = self.growth_coefficients

        def growth(p):
            g = coefficients[0] * np.log(10 * p) + coefficients[1]
            return g
        return growth  # TODO - 생장식 수정

    def set_growth_function_coeffs(self):
        species = self.species
        # TODO - 생장식 수정: species 조건에 따라 미리 정의된 계수 가져오기.
        # TODO - 해당 기간 평균 환경 인자에 따라 보정하기.
        b, a = manager.spcGrowth[species]['equation']
        self.growth_coefficients = [a, b]

    def get_density_base_function(self):

        mortality = 0.015

        def density(p):
            d = (1 - mortality) ** (10 * p)
            return self.density_coefficients * self.initial_density * d
        return density

    def process_initial_condition(self):
        """
        초기 정보가 입력된 경우, 초기 영급 조건을 입력하고, 재적과 밀도를 설정합니다.
        밀도나 재적의 경우, 입력이 안되었을 때 0으로 주어지게 됩니다.
        :return: None
        """
        self.initial_age = self.initial_condition['age']
        if self.initial_condition:
            self.initial_volume = self.initial_condition['volume']
            self.initial_density = self.initial_condition['density']
        else:
            self.initial_density = self.forManPlan['density']



'''
growth_scenarios = {}
for initCond in manager.initialConditions:
    growth_scenario = {}


# TODO
class DensityScenario:
    def __init__(self, mng):
        self.spcList = mng.spc
        self.planningPeriod = mng.planningPeriod
        self.spcIDList = mng.spcIDList
        self.currentData = dict()
        self.futureData = dict()

    def generate_current_density(self):
        """
        Generates density from currentSpc information

        :return: None
        """
        #  구역 번호, 수종명, 영급

    def generate_future_density(self):
        """
        
        :return: 
        """

    def update(self):
        """
        
        :return: 
        """ 
'''

class DecisionVariablesClass:
    duplicateCheckKeys = ['section', 'spcID', 'periodDied', 'regenSpcID']  # 중복 여부 검사할 딕셔너리 키들

    def __init__(self, mng):
        self.list = list()
        self.manager = mng

    def is_duplicate(self, condition):
        if not self.list:
            return False
        for dv in self.list:
            all_key_matched = False
            for key in self.duplicateCheckKeys:
                if dv[key] != condition[key]:
                    all_key_matched = False
                    break
                all_key_matched = True
            if all_key_matched:
                return True
        return False

    def add(self, condition):
        if self.is_duplicate(condition):
            return
        pd_string = str(condition['periodDied'])
        if condition['periodDied'] > self.manager.planningPeriod:
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
                               e['section'], e['periodBorn'],
                               self.manager.spcIDList.index(e['spcID']),
                               e['periodDied'])
                           )

    def create_variables(self, condition):
        if condition['periodBorn'] > self.manager.planningPeriod:
            return False
        regen_spc_id_list = self.manager.spcIDList
        search_results = [x for x in self.manager.regenerationRules
                          if ((x['section'] == condition['section']) & (x['spcID'] == condition['spcID']))
                          ]
        if search_results:
            regen_spc_id_list = search_results[0]['regenerationRule']

        # 계획기간을 넘어, 주벌 & 갱신을 안하는 경우 한번 추가하고, 이후 반복문은 실행 X
        if condition['periodBorn'] + condition['clearCutYear'] > self.manager.planningPeriod:
            condition['regenSpcID'] = '.'
            self.add(condition)
            return False

        #  계획기간 내, 주벌 & 갱신 모두 함. 수종에 따라, 주벌시기가 계획기간 이상일 수도, 이내일 수도 있으므로 고려.
        for regenSpcID in regen_spc_id_list:
            new_condition = condition.copy()  # To prevent changing of initialCondition values. Making a Copy.
            new_condition['regenSpcID'] = regenSpcID
            self.add(new_condition)  # regenSpcID 만 할당한 뒤에 추가.

            new_condition['spcID'] = regenSpcID
            new_condition['species'] = self.manager.ID2Spc[new_condition['spcID']]
            new_condition['periodBorn'] = new_condition['periodDied']
            new_condition['clearCutYear'] = get_matching_item(self.manager.forManPlan, new_condition, ['section', 'species'])['clearCutYear']
            new_condition['periodDied'] = new_condition['periodBorn'] + new_condition['clearCutYear']
            self.create_variables(new_condition)


DecisionVariables = DecisionVariablesClass(manager)

for initialCondition in manager.initialConditions:
    DecisionVariables.create_variables(initialCondition)
DecisionVariables.sort()


print(DecisionVariables.list[0])
vs0 = VolumeScenario(DecisionVariables.list[0])
print(vs0.initial_condition)
print(vs0.predict_growth(1))

print('=============')

print(DecisionVariables.list[10])
vs1 = VolumeScenario(DecisionVariables.list[3])
print(vs1.initial_condition)
print(vs1.predict_growth(10) * vs1.initial_condition['density'])
exit()




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


for ID in ID2AccVarNameRules:
    for sec in range(manager.numSections):
        sec += 1
        for spcID in manager.spcIDList:
            for age in range(manager.ageMax):
                age += 1
                for per in range(manager.planningPeriod):
                    per += 1
                    AccountingVariables.add({
                        'ID': ID,
                        'section': sec,
                        'spcID': spcID,
                        'age': age,
                        'period': per
                    })

Variables = DecisionVariables.list + AccountingVariables.list

exit()

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
            area = get_matching_item(manager.initialConditions, EqName, ['section', 'spcID', 'periodBorn'])['area']
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
    if ID == 'Vol_SpcPer':  # TODO - 생장 파트 수정
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
                    age_temp = EqName['period'] - V['periodBorn']
                    vol = next(item for item in futureVolumeTables
                               if (item['section'] == V['section']) &
                               (item['spcID'] == V['spcID']))['data'][age_temp]['volume']
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
                    prod = next(item for item in currentVolumeTables
                                if (item['section'] == V['section']) &
                                (item['spcID'] == V['spcID']) &
                                (item['currentAge'] == 1 - V['periodBorn']))['data'][EqName['period']]['produced']
                    line.append(prod)
                else:  # 식재된 나무일 때 면적이 변화) -> futureVolumeTables 에서 참고
                    age_temp = EqName['period'] - V['periodBorn']
                    prod = next(item for item in futureVolumeTables
                                if (item['section'] == V['section']) &
                                (item['spcID'] == V['spcID']))['data'][age_temp]['produced']
                    line.append(prod)
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
                    prod = next(item for item in currentVolumeTables
                                if (item['section'] == V['section']) &
                                (item['spcID'] == V['spcID']) &
                                (item['currentAge'] == 1 - V['periodBorn']))['data'][EqName['period']]['produced']
                    line.append(prod)
                else:  # 식재된 나무일 때 면적이 변화) -> futureVolumeTables 에서 참고
                    age_temp = EqName['period'] - V['periodBorn']
                    prod = next(item for item in futureVolumeTables
                                if (item['section'] == V['section']) &
                                (item['spcID'] == V['spcID']))['data'][age_temp]['produced']
                    line.append(prod)
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
            carbonCoeff = manager.coeffs['volume2Carbon'][manager.ID2Spc[V['spcID']]]

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
                age_temp = EqName['period'] - V['periodBorn']
                waterCoeff = next(item for item in manager.coeffs['waterCoeffs']
                                  if (item['section'] == V['section']) &
                                  (V['spcID'] in item['spcIDs']))['data'][age_temp]
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
                    age_temp = EqName['period'] - V['periodBorn']
                    produced = next(item for item in futureVolumeTables
                                    if (item['section'] == V['section']) &
                                    (item['spcID'] == V['spcID']))['data'][age_temp][
                        'produced']
            if produced != 0:
                if EqName['period'] == V['periodDied']:
                    # clearCut + regen labor. 만약 regeneration = '.' 인 경우 0
                    line.append(
                        manager.coeffs['laborCoeffs']['clearCut'] + manager.coeffs['laborCoeffs']['regeneration'][
                            V['regenSpcID']])
                else:
                    line.append(manager.coeffs['laborCoeffs']['thinning'])
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
                    age_temp = EqName['period'] - V['periodBorn']
                    produced = next(item for item in futureVolumeTables
                                    if (item['section'] == V['section']) &
                                    (item['spcID'] == V['spcID']))['data'][age_temp]['produced']
            if produced != 0:
                line.append(manager.coeffs['costCoeffs']['thinning'])
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
            thinningPrice = manager.coeffs['volume2Price']['thinning'][V['spcID']]
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
            line.append(manager.coeffs['costCoeffs']['clearCut'] + manager.coeffs['costCoeffs']['regeneration'][
                V['regenSpcID']])

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
            clearCutPrice = manager.coeffs['volume2Price']['clearCut'][V['spcID']]
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
        line.append(manager.coeffs['CO2ProcessingCost'] * manager.coeffs['exchangeRate'])

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
        line.append(manager.coeffs['waterSavingCoeff'])

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
        line.append(NPV(manager.coeffs['interestRate'], EqName['period']))

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
        line.append(NPV(manager.coeffs['interestRate'], EqName['period']))

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
        line.append(NPV(manager.coeffs['interestRate'], EqName['period']))

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
