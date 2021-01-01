const spcClassesData = [
    {
        "class": 1,
        "speciesID": "O",
        "species": "소나무"
    },
    {
        "class": 2,
        "speciesID": "C",
        "species": "리기다소나무"
    },
    {
        "class": 3,
        "speciesID": "K",
        "species": "잣나무"
    },
    {
        "class": 4,
        "speciesID": "L",
        "species": "일본잎갈나무"
    },
    {
        "class": 5,
        "speciesID": "S",
        "species": "상수리나무"
    },
    {
        "class": 6,
        "speciesID": "B",
        "species": "신갈나무"
    }
]; // manager.spcClasses
const currentSpcData = [
        {
            "section": 1,
            "species": "잣나무",
            "age": 8,
            "area": 208.7,
            "volume": 394.7714
        },
        {
            "section": 1,
            "species": "일본잎갈나무",
            "age": 8,
            "area": 5,
            "volume": 272.264
        },
        {
            "section": 1,
            "species": "잣나무",
            "age": 7,
            "area": 2,
            "volume": 185.77
        },
        {
            "section": 1,
            "species": "잣나무",
            "age": 6,
            "area": 13,
            "volume": 167.12
        },
        {
            "section": 1,
            "species": "일본잎갈나무",
            "age": 6,
            "area": 1,
            "volume": 238.46
        },
        {
            "section": 1,
            "species": "잣나무",
            "age": 5,
            "area": 200.1,
            "volume": 280.2216
        },
        {
            "section": 1,
            "species": "일본잎갈나무",
            "age": 5,
            "area": 7,
            "volume": 373.03
        },
        {
            "section": 1,
            "species": "신갈나무",
            "age": 5,
            "area": 31,
            "volume": 208.6839
        },
        {
            "section": 1,
            "species": "잣나무",
            "age": 4,
            "area": 368,
            "volume": 276.128
        },
        {
            "section": 1,
            "species": "일본잎갈나무",
            "age": 4,
            "area": 41,
            "volume": 339.6974
        },
        {
            "section": 1,
            "species": "신갈나무",
            "age": 4,
            "area": 9,
            "volume": 204.21
        },
        {
            "section": 1,
            "species": "잣나무",
            "age": 3,
            "area": 35,
            "volume": 202.397
        },
        {
            "section": 1,
            "species": "일본잎갈나무",
            "age": 3,
            "area": 14,
            "volume": 119.9014
        },
        {
            "section": 1,
            "species": "신갈나무",
            "age": 3,
            "area": 7,
            "volume": 142.37
        },
        {
            "section": 1,
            "species": "일본잎갈나무",
            "age": 2,
            "area": 3,
            "volume": 0
        },
        {
            "section": 1,
            "species": "잣나무",
            "age": 2,
            "area": 13,
            "volume": 29.3833
        },
        {
            "section": 1,
            "species": "상수리나무",
            "age": 2,
            "area": 2,
            "volume": 0
        },
        {
            "section": 1,
            "species": "일본잎갈나무",
            "age": 1,
            "area": 35,
            "volume": 115.22
        },
        {
            "section": 1,
            "species": "잣나무",
            "age": 1,
            "area": 1,
            "volume": 0
        },
        {
            "section": 1,
            "species": "상수리나무",
            "age": 1,
            "area": 12,
            "volume": 0
        },
        {
            "section": 1,
            "species": "신갈나무",
            "age": 1,
            "area": 21,
            "volume": 5.1048
        },
        {
            "section": 2,
            "species": "잣나무",
            "age": 5,
            "area": 33,
            "volume": 160.7384
        },
        {
            "section": 2,
            "species": "일본잎갈나무",
            "age": 5,
            "area": 37,
            "volume": 358.0718919
        },
        {
            "section": 2,
            "species": "신갈나무",
            "age": 5,
            "area": 32.5,
            "volume": 194.13
        },
        {
            "section": 2,
            "species": "일본잎갈나무",
            "age": 4,
            "area": 3,
            "volume": 172.44
        },
        {
            "section": 2,
            "species": "신갈나무",
            "age": 4,
            "area": 9,
            "volume": 118.66
        },
        {
            "section": 2,
            "species": "잣나무",
            "age": 4,
            "area": 34,
            "volume": 267.2690647
        },
        {
            "section": 2,
            "species": "일본잎갈나무",
            "age": 4,
            "area": 11,
            "volume": 172.16
        },
        {
            "section": 2,
            "species": "신갈나무",
            "age": 4,
            "area": 5,
            "volume": 93.73
        },
        {
            "section": 2,
            "species": "신갈나무",
            "age": 3,
            "area": 20,
            "volume": 90.666
        },
        {
            "section": 2,
            "species": "잣나무",
            "age": 2,
            "area": 36,
            "volume": 54.74
        },
        {
            "section": 2,
            "species": "일본잎갈나무",
            "age": 2,
            "area": 6,
            "volume": 18.82
        },
        {
            "section": 2,
            "species": "잣나무",
            "age": 1,
            "area": 2,
            "volume": 0
        },
        {
            "section": 2,
            "species": "일본잎갈나무",
            "age": 1,
            "area": 2,
            "volume": 0
        },
        {
            "section": 3,
            "species": "잣나무",
            "age": 8,
            "area": 14,
            "volume": 179.2786
        },
        {
            "section": 3,
            "species": "일본잎갈나무",
            "age": 7,
            "area": 2,
            "volume": 279.85
        },
        {
            "section": 3,
            "species": "일본잎갈나무",
            "age": 6,
            "area": 2,
            "volume": 115.65
        },
        {
            "section": 3,
            "species": "일본잎갈나무",
            "age": 6,
            "area": 4,
            "volume": 178.88
        },
        {
            "section": 3,
            "species": "신갈나무",
            "age": 6,
            "area": 61.9,
            "volume": 117.2601454
        },
        {
            "section": 3,
            "species": "신갈나무",
            "age": 5,
            "area": 13,
            "volume": 279.643
        },
        {
            "section": 3,
            "species": "잣나무",
            "age": 5,
            "area": 137.8,
            "volume": 318.417237
        },
        {
            "section": 3,
            "species": "일본잎갈나무",
            "age": 5,
            "area": 160.3,
            "volume": 374.632258
        },
        {
            "section": 3,
            "species": "신갈나무",
            "age": 5,
            "area": 182.4,
            "volume": 207.9909371
        },
        {
            "section": 3,
            "species": "신갈나무",
            "age": 4,
            "area": 71,
            "volume": 261.4693
        },
        {
            "section": 3,
            "species": "잣나무",
            "age": 4,
            "area": 364,
            "volume": 266.1554439
        },
        {
            "section": 3,
            "species": "일본잎갈나무",
            "age": 4,
            "area": 193,
            "volume": 327.1993325
        },
        {
            "section": 3,
            "species": "신갈나무",
            "age": 4,
            "area": 116,
            "volume": 192.5432645
        },
        {
            "section": 3,
            "species": "일본잎갈나무",
            "age": 3,
            "area": 1,
            "volume": 53.87
        },
        {
            "section": 3,
            "species": "잣나무",
            "age": 3,
            "area": 77,
            "volume": 172.49097
        },
        {
            "section": 3,
            "species": "일본잎갈나무",
            "age": 3,
            "area": 22,
            "volume": 215.0725
        },
        {
            "section": 3,
            "species": "상수리나무",
            "age": 3,
            "area": 5,
            "volume": 64.77
        },
        {
            "section": 3,
            "species": "신갈나무",
            "age": 3,
            "area": 8,
            "volume": 77.8925
        },
        {
            "section": 3,
            "species": "잣나무",
            "age": 2,
            "area": 16,
            "volume": 52.44365222
        },
        {
            "section": 3,
            "species": "일본잎갈나무",
            "age": 2,
            "area": 48,
            "volume": 53.05604167
        },
        {
            "section": 3,
            "species": "상수리나무",
            "age": 2,
            "area": 2,
            "volume": 31.55
        },
        {
            "section": 3,
            "species": "신갈나무",
            "age": 2,
            "area": 5,
            "volume": 23.716
        },
        {
            "section": 3,
            "species": "일본잎갈나무",
            "age": 1,
            "area": 6,
            "volume": 0
        },
        {
            "section": 3,
            "species": "잣나무",
            "age": 1,
            "area": 15.1,
            "volume": 0
        },
        {
            "section": 3,
            "species": "일본잎갈나무",
            "age": 1,
            "area": 10,
            "volume": 0
        },
        {
            "section": 3,
            "species": "상수리나무",
            "age": 1,
            "area": 4,
            "volume": 0
        },
        {
            "section": 4,
            "species": "잣나무",
            "age": 8,
            "area": 34,
            "volume": 204.4741176
        },
        {
            "section": 4,
            "species": "잣나무",
            "age": 7,
            "area": 4,
            "volume": 183.91
        },
        {
            "section": 4,
            "species": "일본잎갈나무",
            "age": 7,
            "area": 3,
            "volume": 279.85
        },
        {
            "section": 4,
            "species": "일본잎갈나무",
            "age": 5,
            "area": 13,
            "volume": 119.5492308
        },
        {
            "section": 4,
            "species": "잣나무",
            "age": 5,
            "area": 50,
            "volume": 305.6047429
        },
        {
            "section": 4,
            "species": "일본잎갈나무",
            "age": 5,
            "area": 26,
            "volume": 188.7784615
        },
        {
            "section": 4,
            "species": "신갈나무",
            "age": 5,
            "area": 231.3,
            "volume": 252.3812077
        },
        {
            "section": 4,
            "species": "신갈나무",
            "age": 4,
            "area": 15,
            "volume": 317.1681818
        },
        {
            "section": 4,
            "species": "잣나무",
            "age": 4,
            "area": 300,
            "volume": 300.5181462
        },
        {
            "section": 4,
            "species": "일본잎갈나무",
            "age": 4,
            "area": 296,
            "volume": 350.543884
        },
        {
            "section": 4,
            "species": "상수리나무",
            "age": 4,
            "area": 7,
            "volume": 133.24
        },
        {
            "section": 4,
            "species": "잣나무",
            "age": 3,
            "area": 9,
            "volume": 183.738
        },
        {
            "section": 4,
            "species": "일본잎갈나무",
            "age": 3,
            "area": 32,
            "volume": 126.193125
        },
        {
            "section": 4,
            "species": "잣나무",
            "age": 2,
            "area": 10,
            "volume": 77.51833333
        },
        {
            "section": 4,
            "species": "일본잎갈나무",
            "age": 2,
            "area": 23,
            "volume": 119.4336364
        },
        {
            "section": 4,
            "species": "일본잎갈나무",
            "age": 1,
            "area": 3,
            "volume": 0
        },
        {
            "section": 4,
            "species": "일본잎갈나무",
            "age": 1,
            "area": 2,
            "volume": 0
        },
        {
            "section": 4,
            "species": "상수리나무",
            "age": 1,
            "area": 4,
            "volume": 11.73
        },
        {
            "section": 5,
            "species": "일본잎갈나무",
            "age": 4,
            "area": 4,
            "volume": 93.73
        },
        {
            "section": 5,
            "species": "잣나무",
            "age": 4,
            "area": 122,
            "volume": 265.3024912
        },
        {
            "section": 5,
            "species": "일본잎갈나무",
            "age": 4,
            "area": 134,
            "volume": 314.8127545
        },
        {
            "section": 5,
            "species": "신갈나무",
            "age": 4,
            "area": 130,
            "volume": 140.7911905
        },
        {
            "section": 5,
            "species": "잣나무",
            "age": 3,
            "area": 11,
            "volume": 116.0973
        },
        {
            "section": 5,
            "species": "일본잎갈나무",
            "age": 3,
            "area": 18,
            "volume": 258.7087286
        },
        {
            "section": 5,
            "species": "일본잎갈나무",
            "age": 2,
            "area": 10,
            "volume": 12.54
        },
        {
            "section": 5,
            "species": "잣나무",
            "age": 2,
            "area": 27,
            "volume": 3.92
        },
        {
            "section": 5,
            "species": "일본잎갈나무",
            "age": 2,
            "area": 14,
            "volume": 12.97714286
        },
        {
            "section": 5,
            "species": "상수리나무",
            "age": 2,
            "area": 24,
            "volume": 51.69454545
        },
        {
            "section": 5,
            "species": "신갈나무",
            "age": 2,
            "area": 3,
            "volume": 10
        },
        {
            "section": 5,
            "species": "일본잎갈나무",
            "age": 1,
            "area": 27,
            "volume": 0
        },
        {
            "section": 5,
            "species": "잣나무",
            "age": 1,
            "area": 21.3,
            "volume": 0
        },
        {
            "section": 5,
            "species": "일본잎갈나무",
            "age": 1,
            "area": 9,
            "volume": 0
        },
        {
            "section": 5,
            "species": "상수리나무",
            "age": 1,
            "area": 2,
            "volume": 0
        },
        {
            "section": 5,
            "species": "신갈나무",
            "age": 1,
            "area": 28,
            "volume": 7.932142857
        }
    ]; // manager.currentSpc
const forManPlanData = [
    {
        "section": 1,
        "species": "소나무",
        "clearCutYear": 7,
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
        "species": "리기다소나무",
        "clearCutYear": 4,
        "thinningScenario": [
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
            0,
            0,
            0
        ]
    },
    {
        "section": 1,
        "species": "잣나무",
        "clearCutYear": 7,
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
    },
    {
        "section": 1,
        "species": "상수리나무",
        "clearCutYear": 7,
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
        "species": "신갈나무",
        "clearCutYear": 7,
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
        "section": 2,
        "species": "소나무",
        "clearCutYear": 6,
        "thinningScenario": [
            0,
            0.3,
            0.3,
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
        "section": 2,
        "species": "리기다소나무",
        "clearCutYear": 3,
        "thinningScenario": [
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
            0,
            0,
            0
        ]
    },
    {
        "section": 2,
        "species": "잣나무",
        "clearCutYear": 6,
        "thinningScenario": [
            0,
            0.3,
            0.3,
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
        "section": 2,
        "species": "일본잎갈나무",
        "clearCutYear": 5,
        "thinningScenario": [
            0,
            0.3,
            0.3,
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
        "section": 2,
        "species": "상수리나무",
        "clearCutYear": 6,
        "thinningScenario": [
            0,
            0.3,
            0.3,
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
        "section": 2,
        "species": "신갈나무",
        "clearCutYear": 6,
        "thinningScenario": [
            0,
            0.3,
            0.3,
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
        "section": 3,
        "species": "소나무",
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
        "section": 3,
        "species": "리기다소나무",
        "clearCutYear": 3
    },
    {
        "section": 3,
        "species": "잣나무",
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
        "section": 3,
        "species": "일본잎갈나무",
        "clearCutYear": 5,
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
        "section": 3,
        "species": "상수리나무",
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
        "section": 3,
        "species": "신갈나무",
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
        "section": 4,
        "species": "소나무",
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
        "section": 4,
        "species": "리기다소나무",
        "clearCutYear": 3
    },
    {
        "section": 4,
        "species": "잣나무",
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
        "section": 4,
        "species": "일본잎갈나무",
        "clearCutYear": 5,
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
        "section": 4,
        "species": "상수리나무",
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
        "section": 4,
        "species": "신갈나무",
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
        "section": 5,
        "species": "소나무",
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
        "section": 5,
        "species": "리기다소나무",
        "clearCutYear": 3
    },
    {
        "section": 5,
        "species": "잣나무",
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
        "section": 5,
        "species": "일본잎갈나무",
        "clearCutYear": 5,
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
        "section": 5,
        "species": "상수리나무",
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
        "section": 5,
        "species": "신갈나무",
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
]; // manager.forManPlan
const numSection = 5;
const numPeriods = 15;


//var spc2ID = manager.spcClasses.map(s => ({[s.species]: s.speciesID})).reduce(((r, c) => Object.assign(r, c)), {});
var spc2ID = spcClassesData.map(s => ({[s.species]: s.speciesID})).reduce(((r, c) => Object.assign(r, c)), {});
var ID2Spc = spcClassesData.map(s => ({[s.speciesID]: s.species})).reduce(((r, c) => Object.assign(r, c)), {});
var spcIDList = Object.values(spc2ID); // e.g., [ 'O', 'C', 'K', 'L', 'S', 'B' ]

var initialConditions = []; // e.g., [{ section: 1, periodBorn: -7, spcID: 'K', periodDied: 1, clearCutYear: 7 } ... ]
for (let i=0; i<currentSpcData.length; i++) {
    const obj_temp = {};
    obj_temp.section = currentSpcData[i].section;
    obj_temp.periodBorn = 1 - currentSpcData[i].age;
    obj_temp.spcID = spc2ID[currentSpcData[i].species];

    /*** obj_temp.periodDied ***/
    const forManPlan = forManPlanData.find(x => x.section === currentSpcData[i].section & x.species === currentSpcData[i].species); // 해당하는 산림시업 정보를 찾습니다.

    if (obj_temp.periodBorn + forManPlan.clearCutYear <= 0)
        obj_temp.periodDied = 1;
    else
        obj_temp.periodDied = obj_temp.periodBorn + forManPlan.clearCutYear;
    obj_temp.clearCutYear = forManPlan.clearCutYear;
    initialConditions.push(obj_temp);
}





/*****************************************************************************************
 * ***********************************************************************************
 *                         Create Decision Variables
 *
 *    현재 임분 정보를 참고해서, 지속적으로 파생되는 일련의 DV 리스트를 만듭니다.
 *    우선 정의부터 하고, 엑셀 양식에 맞게 정렬하는건 나중에.
 *    참고로 엑셀에는 section, periodBorn, speciesID (ABC 순서가 아닌 사용자 입력순서)
 *    순서로 정렬되어 있습니다.
 ****************************************************************************************/
const regenerationRules = [
    {section:1, spcID:'B', regenerationRule:['S', 'B']},
    {section:1, spcID:'S', regenerationRule:['S', 'B']},
]; // 1 구역의 B는 S, B 로만 갱신.
var DecisionVariable = function (condition) {
    this.ID = "DecisionVariable";
    this.section = condition.section;
    this.spcID = condition.spcID;
    this.periodBorn = condition.periodBorn;
    this.periodDied = condition.periodDied;
    this.regenSpcID = condition.regenSpcID;
    this.name = String(this.section) + "_" + String(this.periodBorn) + this.spcID + String(this.periodDied) + this.regenSpcID; // 1_1K7K
};
var DecisionVariables = [];
DecisionVariables.checkDuplicate = function(condition) {
    const searchResult = this.find(x => x.section === condition.section & x.spcID === condition.spcID & x.periodDied === condition.periodDied & x.regenSpcID === condition.regenSpcID);
    return searchResult !== undefined;
};
DecisionVariables.add = function (condition) {
    if (!this.checkDuplicate(condition))
        this.push(new DecisionVariable(condition));
};
/*****************************************************************************************
 * ***********************************************************************************
 *                         Create Decision Variables' Equations
 *
 *    파생된 DecisionVariable 에서, 각각에 대한 면적의 Equation 을 생성합니다.
 *    면적은 section, periodBorn & spcID 의 조합으로 만들어집니다. 예를 들어,
 *    {"section":1,"spcID":"K","periodBorn":1,"periodDied":7,"regenSpcID":"C","name":"1_1K7C"}
 *    와 같은 입력을 받으면, 1_-7K 로 하나의 Equation 을 만듭니다.
 ****************************************************************************************/
var DecisionVariableEquation = function (condition) {
    this.type = "DecisionVariableEquation";
    this.section = condition.section;
    this.spcID = condition.spcID;
    this.periodBorn = condition.periodBorn;
    this.name = String(this.section) + "_" + String(this.periodBorn) + this.spcID // 1_-7K
};
var DecisionVariableEquations = [];
DecisionVariableEquations.checkDuplicate = function(condition) {
    const searchResult = this.find(x => x.section === condition.section & x.spcID === condition.spcID & x.periodBorn === condition.periodBorn);
    return searchResult !== undefined;
};
DecisionVariableEquations.add = function (condition) {
    if (!this.checkDuplicate(condition))
        this.push(new DecisionVariableEquation(condition));
};
/*****************************************************************************************
 *****************************************************************************************/
var createDecisionVariable = function (initialCondition) {
    /*****************************************************************************************************
     *        input: { section: 1, periodBorn: -7, spcID: 'K', periodDied: 1, clearCutYear: 7 }
     *****************************************************************************************************/
    //console.log("--------현재 조건 출력-------");
    //
    //
    // if (initialCondition.section === 1)
    //    console.log(JSON.stringify(initialCondition));
    //console.log("차원 수" + String(dim))
    //console.log("-----------------------------");
    if (initialCondition.periodBorn > numPeriods)
        return false;

    DecisionVariableEquations.add(initialCondition); // 중복을 없애기 위해 반복문 들어가기 전에 Initial Condition 에서 Equation 추가
    let regenSpcIDList = spcIDList;

    const searchResults = regenerationRules.find(x => x.section === initialCondition.section & x.spcID === initialCondition.spcID);
    if (searchResults !== undefined) // 갱신 제한 수종 있는지 검사. 해당하는 결과가 나오면
        regenSpcIDList = searchResults.regenerationRule;
    if (initialCondition.periodBorn + initialCondition.clearCutYear > numPeriods) { // 계획기간을 넘어, 주벌 & 갱신을 안하는 경우 한번 추가하고, 이후 반복문은 실행 X
        initialCondition.regenSpcID = ".";
        initialCondition.periodDied = ".";
        DecisionVariables.add(initialCondition);
        return false;
    }

    for (const regenSpcID of regenSpcIDList) { // 계획기간 내, 주벌 & 갱신 모두 함. 수종에 따라, 주벌시기가 계획기간 이상일 수도, 이내일 수도 있으므로 고려.
        let newCondition = JSON.parse(JSON.stringify(initialCondition)); // newCondition = initialCondition 으로 하면 initialCondition 값이 바뀌어버림. Copy 를 만듦.
        newCondition.clearCutYear = forManPlanData.find(x => x.section === newCondition.section & x.species === ID2Spc[newCondition.spcID]).clearCutYear;
        newCondition.regenSpcID = regenSpcID;

        DecisionVariables.add(newCondition); // regenSpcID 만 할당한 뒤에 추가.

        newCondition.spcID = regenSpcID;
        newCondition.periodBorn = newCondition.periodDied;
        newCondition.periodDied = newCondition.periodBorn + newCondition.clearCutYear;
        if (newCondition.periodDied <= 0) // 이미 initialCondition 을 만들 때 고려되었으므로 필요는 X
            newCondition.periodDied = 1;
        createDecisionVariable(newCondition);
        /*
        console.log("----반복문 내 상황----");
        console.log(JSON.stringify(initialCondition));
        console.log(JSON.stringify(newCondition));
        console.log("반복 수" + String(iter))
        console.log("----------------------");
        iter += 1
        */

    }
};
/*****************************************************************************************
 *****************************************************************************************/
for (const initialCondition of initialConditions)
    createDecisionVariable(initialCondition)
DecisionVariables.sort(function(a,b){
    if (a.section !== b.section)
        return a.section - b.section;
    if (a.periodBorn !== b.periodBorn)
        return a.periodBorn - b.periodBorn;
    if (spcIDList.indexOf(a.spcID) !== spcIDList.indexOf(b.spcID))
        return spcIDList.indexOf(a.spcID) - spcIDList.indexOf(b.spcID);
    return a.periodDied - b.periodDied;
});
///////////////////////////////////////////////////////////////////////////////////////////
///////////////////////////////////////////////////////////////////////////////////////////
/******************************************************************************************
 * ************************************************************************************
 *                          Create Accounting Variables
 *
 *                        Accounting Variable 를 만듭니다.
 *****************************************************************************************/
/*
const ID2DataKeys = { // Accounting Variable 의 이름을 지정할 때 필요한 변환 변수
    Vol_SpcPer:["spcID", "period"], // KV.10 => 10분기의 K 수종의 전체 재적
    Area_SpcSecPer:["spcID", "section", "period"], // 2KA.10 => 10분기의 2구역, K 수종의 면적
    Area_AgePer:["age", "period"], // AC1.10 => 10분기에 AgeClass 가 1 인 애들
    Thin_SpcPer:["spcID", "period"], // KT.10 => 10분기에 K 수종의 간벌량
    Harv_SpcPer:["spcID", "period"], // KH.10 => 10분기에 H 수종의 수확량
    PThin_Per:["period"], // T.10 => 10 분기의 간벌 생산량
    PHarv_Per:["period"],
    PThinHarv_Per:["period"],
    Carbon_Per:["period"],
    Water_Per:["period"],
    Labor_Per:["period"],
    TCost_Per:["period"],
    TRev_Per:["period"],
    TNet_Per:["period"],
    HCost_Per:["period"],
    HRev_Per:["period"],
    HNet_Per:["period"],
    f_Per:["period"],
    g_Per:["period"],
    h_Per:["period"],
    NPV_f_Per:["period"],
    NPV_g_Per:["period"],
    NPV_h_Per:["period"],
};
*/
const ID2NameRules = {
    Vol_SpcPer:["spcID", "V", ".", "period"], // 각 배열의 요소를 key 로 참조하면서, undefined 인 경우 그 key 를 그대로 이름에 활용.
    Area_SpcSecPer:["spcID", "A", "section", ".", "period"], // 2KA.10 => 10분기의 2구역, K 수종의 면적
    Area_AgePer:["AC", "age", ".", "period"], // AC1.10 => 10분기에 AgeClass 가 1 인 애들
    Thin_SpcPer:["spcID", "T", ".", "period"], // KT.10 => 10분기에 K 수종의 간벌량
    Harv_SpcPer:["spcID", "H", ".", "period"], // KH.10 => 10분기에 H 수종의 수확량
    PThin_Per:["TH", ".", "period"], // T.10 => 10 분기의 간벌 생산량
    PHarv_Per:["H", ".", "period"], // H.10 => 10 분기의 주벌 생산량
    PThinHarv_Per:["TH", ".", "period"],
    Carbon_Per:["C", ".", "period"],
    Water_Per:["W", ".", "period"],
    Labor_Per:["J", ".", "period"],
    TCost_Per:["TC", ".", "period"],
    TRev_Per:["TR", ".", "period"],
    TNet_Per:["ft", ".", "period"],
    HCost_Per:["HC", ".", "period"],
    HRev_Per:["HR", ".", "period"],
    HNet_Per:["fh", ".", "period"],
    f_Per:["f", ".", "period"],
    g_Per:["g", ".", "period"],
    h_Per:["h", ".", "period"],
    NPV_f_Per:["NPV_f", ".", "period"],
    NPV_g_Per:["NPV_g", ".", "period"],
    NPV_h_Per:["NPV_h", ".", "period"],
}; // Naming Rules: 각 요소의 순서대로

var AccountingVariable = function (condition) {
    // ID => V_Spc,
    // data => {spcID:"K", period:15}
    // this.type = "AccountingVariable";
    this.ID = condition.ID;
    this.section = condition.section;
    this.spcID = condition.spcID;
    this.period = condition.period;
    this.name = condition.name;
};
var AccountingVariables = [];
AccountingVariables.createName = function (condition) {
    let name = "";
    for (const DataKey of ID2NameRules[condition.ID]) {
        if (condition[DataKey] === undefined)
            name += String(DataKey);
        else
            name += String(condition[DataKey]);
    }
    return name;
};
AccountingVariables.checkDuplicate = function (condition) {
    const searchResult = this.find(x => x.name === condition.name);
    return searchResult !== undefined;
}; // 같은 name 을 가진 계산 변수가 없을 경우
AccountingVariables.add = function (condition) {
    condition.name = this.createName(condition);
    if (!this.checkDuplicate(condition))
        this.push(new AccountingVariable(condition));
};
/******************************************************************************************
 *                            최대 영급을 계산합니다. (주벌시기 중 최대값)
 *****************************************************************************************/
let ageMax = 0;
for (const obj of forManPlanData.values())
    if (ageMax < obj.clearCutYear)
        ageMax = obj.clearCutYear;
/******************************************************************************************
 *                 가능한 모든 조합에 대해서 중복을 고려하면서 계산 변수를 추가합니다.
 *****************************************************************************************/
for (const ID of Object.keys(ID2NameRules)) {
    for (let period=1; period<=numPeriods; period++)
        for (const spcID of spcIDList)
            for (let section=1; section<=numSection; section++)
                AccountingVariables.add({ID:ID, period:period, spcID:spcID, section:section});
}
var Variables = DecisionVariables.concat(AccountingVariables);

///////////////////////////////////////////////////////////////////////////////////////////
///////////////////////////////////////////////////////////////////////////////////////////
/******************************************************************************************
 * ************************************************************************************
 *                                   Creating Equations
 *
 *                              정의된 각 변수들을 활용해서, 식을 구성합니다.
 *            곱하기로 연결된 경우 배열을 만들고, 값을 참조해야 하는 경우 Object 를 선언합니다.
 *            Vol_SpcPer:{variables:["period", "spcID"], LHS:[[{ID:area2Volume, spcID:spcID, period:period}, {ID:DecisionVariable, period:period, spcID:spcID}], [C]]} // RHS 는 자동으로 해당 period 와 spcID 에 해당하는 값으로
 *****************************************************************************************/
test = {
    variables:["period", "spcID"],
    LHS:[
        [{ID:area2Volume, spcID:spcID, period:period}, {ID:DecisionVariable, period:period, spcID:spcID}],
        [C]
    ]
}

let equations = {
    Vol_SpcPer: [
        [T],
        [1,{}]
    ]
};







//for (dv of DecisionVariables.sort())
//    console.log(JSON.stringify(dv));
//for (av of AccountingVariables.sort())
//    console.log(JSON.stringify(av));
for (v of Variables)
    console.log(JSON.stringify(v));
console.log(Variables.length);
//console.log(AccountingVariables);
//console.log(DecisionVariableEquations.length);