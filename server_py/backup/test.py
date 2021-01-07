import numpy as np

arr = [{'section': 1, 'spcID': 'O', 'data': {1: {'period': 1, 'age': 1, 'volume': 235.05, 'produced': 0.0}, 2: {'period': 2, 'age': 2, 'volume': 238.5432, 'produced': 102.2328}, 3: {'period': 3, 'age': 3, 'volume': 300.3882, 'produced': 0.0}, 4: {'period': 4, 'age': 4, 'volume': 240.98844000000003, 'produced': 103.28076}, 5: {'period': 5, 'age': 5, 'volume': 275.02344, 'produced': 0.0}, 6: {'period': 6, 'age': 6, 'volume': 302.83344, 'produced': 0.0}, 7: {'period': 7, 'age': 7, 'volume': 0.0, 'produced': 326.34443999999996}}}, {'section': 1, 'spcID': 'C', 'data': {1: {'period': 1, 'age': 1, 'volume': 66.384, 'produced': 0.0}, 2: {'period': 2, 'age': 2, 'volume': 72.7167, 'produced': 31.164299999999997}, 3: {'period': 3, 'age': 3, 'volume': 94.6527, 'produced': 0.0}, 4: {'period': 4, 'age': 4, 'volume': 0.0, 'produced': 110.2167}}}, {'section': 1, 'spcID': 'K', 'data': {1: {'period': 1, 'age': 1, 'volume': 520.143, 'produced': 0.0}, 2: {'period': 2, 'age': 2, 'volume': 579.1884, 'produced': 248.2236}, 3: {'period': 3, 'age': 3, 'volume': 758.9304, 'produced': 0.0}, 4: {'period': 4, 'age': 4, 'volume': 620.5222799999999, 'produced': 265.93811999999997}, 5: {'period': 5, 'age': 5, 'volume': 719.4412799999998, 'produced': 0.0}, 6: {'period': 6, 'age': 6, 'volume': 800.2642799999999, 'produced': 0.0}, 7: {'period': 7, 'age': 7, 'volume': 0.0, 'produced': 868.5982799999999}}}, {'section': 1, 'spcID': 'L', 'data': {1: {'period': 1, 'age': 1, 'volume': 576.522, 'produced': 0.0}, 2: {'period': 2, 'age': 2, 'volume': 741.9740999999999, 'produced': 317.9889}, 3: {'period': 3, 'age': 3, 'volume': 1024.7691, 'produced': 0.0}, 4: {'period': 4, 'age': 4, 'volume': 857.7905699999999, 'produced': 367.62453}, 5: {'period': 5, 'age': 5, 'volume': 1013.4245699999999, 'produced': 0.0}, 6: {'period': 6, 'age': 6, 'volume': 0.0, 'produced': 1140.5855699999997}}}, {'section': 1, 'spcID': 'S', 'data': {1: {'period': 1, 'age': 1, 'volume': 201.9, 'produced': 0.0}, 2: {'period': 2, 'age': 2, 'volume': 237.5121, 'produced': 101.7909}, 3: {'period': 3, 'age': 3, 'volume': 317.8881, 'produced': 0.0}, 4: {'period': 4, 'age': 4, 'volume': 262.44057, 'produced': 112.47452999999997}, 5: {'period': 5, 'age': 5, 'volume': 306.6755700000001, 'produced': 0.0}, 6: {'period': 6, 'age': 6, 'volume': 342.81657000000007, 'produced': 0.0}, 7: {'period': 7, 'age': 7, 'volume': 0.0, 'produced': 373.37457000000006}}}, {'section': 1, 'spcID': 'B', 'data': {1: {'period': 1, 'age': 1, 'volume': 94.90799999999999, 'produced': 0.0}, 2: {'period': 2, 'age': 2, 'volume': 84.8862, 'produced': 36.3798}, 3: {'period': 3, 'age': 3, 'volume': 100.30319999999999, 'produced': 0.0}, 4: {'period': 4, 'age': 4, 'volume': 77.87093999999999, 'produced': 33.373259999999995}, 5: {'period': 5, 'age': 5, 'volume': 86.35494, 'produced': 0.0}, 6: {'period': 6, 'age': 6, 'volume': 93.28793999999999, 'produced': 0.0}, 7: {'period': 7, 'age': 7, 'volume': 0.0, 'produced': 99.14993999999999}}}, {'section': 2, 'spcID': 'O', 'data': {1: {'period': 1, 'age': 1, 'volume': 235.05, 'produced': 0.0}, 2: {'period': 2, 'age': 2, 'volume': 238.5432, 'produced': 102.2328}, 3: {'period': 3, 'age': 3, 'volume': 210.27174, 'produced': 90.11645999999999}, 4: {'period': 4, 'age': 4, 'volume': 177.90691800000002, 'produced': 76.245822}, 5: {'period': 5, 'age': 5, 'volume': 211.94191799999996, 'produced': 0.0}, 6: {'period': 6, 'age': 6, 'volume': 0.0, 'produced': 239.75191800000002}}}, {'section': 2, 'spcID': 'C', 'data': {1: {'period': 1, 'age': 1, 'volume': 66.384, 'produced': 0.0}, 2: {'period': 2, 'age': 2, 'volume': 72.7167, 'produced': 31.164299999999997}, 3: {'period': 3, 'age': 3, 'volume': 0.0, 'produced': 94.6527}}}, {'section': 2, 'spcID': 'K', 'data': {1: {'period': 1, 'age': 1, 'volume': 520.143, 'produced': 0.0}, 2: {'period': 2, 'age': 2, 'volume': 579.1884, 'produced': 248.2236}, 3: {'period': 3, 'age': 3, 'volume': 531.25128, 'produced': 227.67911999999998}, 4: {'period': 4, 'age': 4, 'volume': 461.14689599999997, 'produced': 197.63438399999998}, 5: {'period': 5, 'age': 5, 'volume': 560.0658959999998, 'produced': 0.0}, 6: {'period': 6, 'age': 6, 'volume': 0.0, 'produced': 640.8888959999999}}}, {'section': 2, 'spcID': 'L', 'data': {1: {'period': 1, 'age': 1, 'volume': 576.522, 'produced': 0.0}, 2: {'period': 2, 'age': 2, 'volume': 741.9740999999999, 'produced': 317.9889}, 3: {'period': 3, 'age': 3, 'volume': 717.3383699999999, 'produced': 307.43073}, 4: {'period': 4, 'age': 4, 'volume': 642.5890589999999, 'produced': 275.39531099999994}, 5: {'period': 5, 'age': 5, 'volume': 0.0, 'produced': 798.2230589999999}}}, {'section': 2, 'spcID': 'S', 'data': {1: {'period': 1, 'age': 1, 'volume': 201.9, 'produced': 0.0}, 2: {'period': 2, 'age': 2, 'volume': 237.5121, 'produced': 101.7909}, 3: {'period': 3, 'age': 3, 'volume': 222.52167000000003, 'produced': 95.36643}, 4: {'period': 4, 'age': 4, 'volume': 195.68406899999997, 'produced': 83.86460099999998}, 5: {'period': 5, 'age': 5, 'volume': 239.9190690000001, 'produced': 0.0}, 6: {'period': 6, 'age': 6, 'volume': 0.0, 'produced': 276.06006900000006}}}, {'section': 2, 'spcID': 'B', 'data': {1: {'period': 1, 'age': 1, 'volume': 94.90799999999999, 'produced': 0.0}, 2: {'period': 2, 'age': 2, 'volume': 84.8862, 'produced': 36.3798}, 3: {'period': 3, 'age': 3, 'volume': 70.21224, 'produced': 30.090959999999995}, 4: {'period': 4, 'age': 4, 'volume': 56.80726799999999, 'produced': 24.345972}, 5: {'period': 5, 'age': 5, 'volume': 65.291268, 'produced': 0.0}, 6: {'period': 6, 'age': 6, 'volume': 0.0, 'produced': 72.224268}}}, {'section': 3, 'spcID': 'O', 'data': {1: {'period': 1, 'age': 1, 'volume': 235.05, 'produced': 0.0}, 2: {'period': 2, 'age': 2, 'volume': 238.5432, 'produced': 102.2328}, 3: {'period': 3, 'age': 3, 'volume': 300.3882, 'produced': 0.0}, 4: {'period': 4, 'age': 4, 'volume': 240.98844000000003, 'produced': 103.28076}, 5: {'period': 5, 'age': 5, 'volume': 275.02344, 'produced': 0.0}, 6: {'period': 6, 'age': 6, 'volume': 0.0, 'produced': 302.83344}}}, {'section': 3, 'spcID': 'C', 'data': {1: {'period': 1, 'age': 1, 'volume': 66.384, 'produced': 0.0}, 2: {'period': 2, 'age': 2, 'volume': 103.881, 'produced': 0.0}, 3: {'period': 3, 'age': 3, 'volume': 0.0, 'produced': 125.817}}}, {'section': 3, 'spcID': 'K', 'data': {1: {'period': 1, 'age': 1, 'volume': 520.143, 'produced': 0.0}, 2: {'period': 2, 'age': 2, 'volume': 579.1884, 'produced': 248.2236}, 3: {'period': 3, 'age': 3, 'volume': 758.9304, 'produced': 0.0}, 4: {'period': 4, 'age': 4, 'volume': 620.5222799999999, 'produced': 265.93811999999997}, 5: {'period': 5, 'age': 5, 'volume': 719.4412799999998, 'produced': 0.0}, 6: {'period': 6, 'age': 6, 'volume': 0.0, 'produced': 800.2642799999999}}}, {'section': 3, 'spcID': 'L', 'data': {1: {'period': 1, 'age': 1, 'volume': 576.522, 'produced': 0.0}, 2: {'period': 2, 'age': 2, 'volume': 741.9740999999999, 'produced': 317.9889}, 3: {'period': 3, 'age': 3, 'volume': 1024.7691, 'produced': 0.0}, 4: {'period': 4, 'age': 4, 'volume': 857.7905699999999, 'produced': 367.62453}, 5: {'period': 5, 'age': 5, 'volume': 0.0, 'produced': 1013.4245699999999}}}, {'section': 3, 'spcID': 'S', 'data': {1: {'period': 1, 'age': 1, 'volume': 201.9, 'produced': 0.0}, 2: {'period': 2, 'age': 2, 'volume': 237.5121, 'produced': 101.7909}, 3: {'period': 3, 'age': 3, 'volume': 317.8881, 'produced': 0.0}, 4: {'period': 4, 'age': 4, 'volume': 262.44057, 'produced': 112.47452999999997}, 5: {'period': 5, 'age': 5, 'volume': 306.6755700000001, 'produced': 0.0}, 6: {'period': 6, 'age': 6, 'volume': 0.0, 'produced': 342.81657000000007}}}, {'section': 3, 'spcID': 'B', 'data': {1: {'period': 1, 'age': 1, 'volume': 94.90799999999999, 'produced': 0.0}, 2: {'period': 2, 'age': 2, 'volume': 84.8862, 'produced': 36.3798}, 3: {'period': 3, 'age': 3, 'volume': 100.30319999999999, 'produced': 0.0}, 4: {'period': 4, 'age': 4, 'volume': 77.87093999999999, 'produced': 33.373259999999995}, 5: {'period': 5, 'age': 5, 'volume': 86.35494, 'produced': 0.0}, 6: {'period': 6, 'age': 6, 'volume': 0.0, 'produced': 93.28793999999999}}}, {'section': 4, 'spcID': 'O', 'data': {1: {'period': 1, 'age': 1, 'volume': 235.05, 'produced': 0.0}, 2: {'period': 2, 'age': 2, 'volume': 238.5432, 'produced': 102.2328}, 3: {'period': 3, 'age': 3, 'volume': 300.3882, 'produced': 0.0}, 4: {'period': 4, 'age': 4, 'volume': 240.98844000000003, 'produced': 103.28076}, 5: {'period': 5, 'age': 5, 'volume': 275.02344, 'produced': 0.0}, 6: {'period': 6, 'age': 6, 'volume': 0.0, 'produced': 302.83344}}}, {'section': 4, 'spcID': 'C', 'data': {1: {'period': 1, 'age': 1, 'volume': 66.384, 'produced': 0.0}, 2: {'period': 2, 'age': 2, 'volume': 103.881, 'produced': 0.0}, 3: {'period': 3, 'age': 3, 'volume': 0.0, 'produced': 125.817}}}, {'section': 4, 'spcID': 'K', 'data': {1: {'period': 1, 'age': 1, 'volume': 520.143, 'produced': 0.0}, 2: {'period': 2, 'age': 2, 'volume': 579.1884, 'produced': 248.2236}, 3: {'period': 3, 'age': 3, 'volume': 758.9304, 'produced': 0.0}, 4: {'period': 4, 'age': 4, 'volume': 620.5222799999999, 'produced': 265.93811999999997}, 5: {'period': 5, 'age': 5, 'volume': 719.4412799999998, 'produced': 0.0}, 6: {'period': 6, 'age': 6, 'volume': 0.0, 'produced': 800.2642799999999}}}, {'section': 4, 'spcID': 'L', 'data': {1: {'period': 1, 'age': 1, 'volume': 576.522, 'produced': 0.0}, 2: {'period': 2, 'age': 2, 'volume': 741.9740999999999, 'produced': 317.9889}, 3: {'period': 3, 'age': 3, 'volume': 1024.7691, 'produced': 0.0}, 4: {'period': 4, 'age': 4, 'volume': 857.7905699999999, 'produced': 367.62453}, 5: {'period': 5, 'age': 5, 'volume': 0.0, 'produced': 1013.4245699999999}}}, {'section': 4, 'spcID': 'S', 'data': {1: {'period': 1, 'age': 1, 'volume': 201.9, 'produced': 0.0}, 2: {'period': 2, 'age': 2, 'volume': 237.5121, 'produced': 101.7909}, 3: {'period': 3, 'age': 3, 'volume': 317.8881, 'produced': 0.0}, 4: {'period': 4, 'age': 4, 'volume': 262.44057, 'produced': 112.47452999999997}, 5: {'period': 5, 'age': 5, 'volume': 306.6755700000001, 'produced': 0.0}, 6: {'period': 6, 'age': 6, 'volume': 0.0, 'produced': 342.81657000000007}}}, {'section': 4, 'spcID': 'B', 'data': {1: {'period': 1, 'age': 1, 'volume': 94.90799999999999, 'produced': 0.0}, 2: {'period': 2, 'age': 2, 'volume': 84.8862, 'produced': 36.3798}, 3: {'period': 3, 'age': 3, 'volume': 100.30319999999999, 'produced': 0.0}, 4: {'period': 4, 'age': 4, 'volume': 77.87093999999999, 'produced': 33.373259999999995}, 5: {'period': 5, 'age': 5, 'volume': 86.35494, 'produced': 0.0}, 6: {'period': 6, 'age': 6, 'volume': 0.0, 'produced': 93.28793999999999}}}]


print([x for x in arr if (x['section'] == 1) & (x['spcID'] == 'O')][0]['data'][6])