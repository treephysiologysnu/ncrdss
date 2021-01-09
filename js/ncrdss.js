/************************************ ncrdss.main - model ************************************/
// 모델 전반적인 파라미터를 관리하는 Manager (class 처럼 작동) 함수 정의.
function Manager() {
    let that = this;
    this.address = undefined;

    this.availableSpc = undefined;
    this.additionalSpc = undefined;
    this.totalSpc = undefined;

    this.numSections = undefined;
    this.numSpecies = undefined;
    this.planningPeriod = undefined;
    this.startYear = undefined;

    this.spcClasses = undefined;
    this.spcLists = undefined;
    this.spc2ID = undefined;
    this.ID2Spc = undefined;
    this.spcIDList = undefined;

    this.currentSpc = undefined;

    this.thinningScenario = {A:undefined,B:undefined,C:undefined,D:undefined,E:undefined,F:undefined,G:undefined,H:undefined,I:undefined,X:undefined};
    this.forManPlan = undefined;
    this.regenerationRules = []; //TODO: 갱신제한 조건 추가하기

    this.spcGrowth = undefined;

    this.coeffs = undefined;

    this.completedFlags = {
        address: false,
        table_base: false,
        table_SpcClasses: false,
        table_currentSpc: false,
        table_thinning:false,
        table_ForManPlan: false,
    }
    this.setAddress = function (data) {
        that.completedFlags.address = true;
        that.address = data;
    };
    this.setAvailableSpc = function (data) {
        that.availableSpc = data;
    };
    this.setAdditionalSpc = function () {
        const essentialSpc = ['소나무', '신갈나무', '굴참나무', '리기다소나무', '졸참나무', '곰솔', '상수리나무', '일본잎갈나무', '밤나무', '잣나무', '아까시나무', '갈참나무', '산벚나무', '물푸레나무', '때죽나무', '굴피나무', '떡갈나무'];
        var additionalSpcList = [];
        for (const spc of essentialSpc) {
            if (!this.availableSpc.includes(spc))
                additionalSpcList.push(spc);
        }
        that.additionalSpc = additionalSpcList;
        that.totalSpc = arrayUnique(this.availableSpc.concat(additionalSpcList));
    };
    this.setBase = function (data) {
        that.numSections = Number(data[0][0]);
        that.numSpecies = Number(data[0][1]);
        that.planningPeriod = Number(data[0][2]);
        that.startYear = Number(data[0][3]);
    };
    this.setSpcClasses = function (data) {
        var result_temp = new Array();
        for (var i=0; i<data.length; i++)
            result_temp.push({class: i+1, speciesID: data[i][0], species:data[i][1]});
        that.spcClasses = result_temp;
        that.spcLists = result_temp.map(a => a.species);
        that.spc2ID = that.spcClasses.map(s => ({[s.species]: s.speciesID})).reduce(((r, c) => Object.assign(r, c)), {});
        that.ID2Spc = that.spcClasses.map(s => ({[s.speciesID]: s.species})).reduce(((r, c) => Object.assign(r, c)), {});
        that.spcIDList = Object.values(that.spc2ID); // e.g., [ 'O', 'C', 'K', 'L', 'S', 'B' ]
    };
    this.setCurrentSpc = function (data) {
        var result_temp = new Array();
        for (var i=0; i<data.length; i++)
            result_temp.push({section: Number(data[i][0]), species: data[i][1], age: Number(data[i][2]), area: Number(data[i][3]), volume: Number(data[i][4]), density: Number(data[i][5])});
        that.currentSpc = result_temp;
    };
    this.setThinningScenario = function (data) {
        var result_temp = new Array();
        const index = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I'];
        for (const i in index) {
            const cols = data.length;
            const rows = data[0].length;
            for (var j = 0; j < rows; j++) {
                result_temp[index[j]] = Array();
                for (var k = 0; k < cols; k++) {
                    if (typeof data[k][j] === "string") // 문자열일 때만 검사! 백스페이스로 지우면 에러가 나는 것 해결.
                        result_temp[index[j]].push(Number(data[k][j].replace('%', '')) / 100);
                }
            }
        }
        this.thinningScenario = result_temp;
    };
    this.setForManPlan = function (data) {
        var result_temp = [];
        for (var i=0; i<data.length; i++) {
            if (data[i][3] === "")
                continue;
            result_temp.push({
                section: Number(data[i][0].replace("구역 ", "")),
                species: data[i][1],
                spcID: that.spc2ID[data[i][1]],
                clearCutYear: Number(data[i][2]),
                thinningScenario: that.thinningScenario[data[i][3]],
                density: Number(data[i][4]),
            });
        }
        that.forManPlan = result_temp;
    };
    this.setGrowth = function () {
        const speciesArray = this.spcClasses;
        var address = this.address;
        var result_temp = {};
        for (var i=0; i<speciesArray.length; i++) {
            if (speciesArray[i].species == "")
                continue
            if (!manager.availableSpc.includes(speciesArray[i].species))
                address = "전국평균";
            var volumes = final_volume[address + ' ' + speciesArray[i].species];
            var temp = []; // [x, y] 를 담고 있는 리스트
            for (var j=1; j<volumes.length; j++) { // starting from 1 to avoid NaN values
                temp.push([j, volumes[j]]);
            }

            var options = {
                precision: 6,
            }

            var logRegression = regression.logarithmic(temp, options)
            var predictions = [];
            for (var k=1; k<=150; k++) {
                var prd = logRegression.predict(k)[1];
                if (prd < 0)
                    prd = 0
                predictions.push(prd);
                // predictions.push(logRegression.predict(i)); // for [x, y] type array dataset
            }

            var growthCombined = []; // 관측 + 예측 합쳐진 것
            for (var l=1; l<=150; l++) {
                if (volumes[l] != undefined)
                    growthCombined.push(volumes[l]);
                else
                    growthCombined.push(predictions[l]);
            }
            logRegression.predictions = predictions;
            logRegression.growthCombined = growthCombined;
            result_temp[speciesArray[i].species] = logRegression;
        }
        that.spcGrowth = result_temp;
    };
    this.setCoeffs = function (data) {
        that.coeffs = new Object();
        const spcLists = that.spcLists;
        const spcIDList = that.spcIDList;
        const spc2ID = that.spc2ID;
        const ID2Spc = that.ID2Spc;

        // Set volume to carbon coefficients
        let volume2Carbon = {};
        for (const species of spcLists) {
            if (Object.keys(spc2VolumeCarbonCoeffs).includes(species))
                volume2Carbon[species] = spc2VolumeCarbonCoeffs[species];
            else
                volume2Carbon[species] = spc2VolumeCarbonCoeffs['default'];
        }
        that.coeffs.volume2Carbon = volume2Carbon;

        // Set water yield coefficients
        let waterCoeffs = [];
        let defaultWaterCoeffPerPeriod = [];
        for (let per=1; per<=that.planningPeriod; per++)
            defaultWaterCoeffPerPeriod.push(90 * per + 2000);
        for (let sec=1; sec<=that.numSections; sec++) {
            waterCoeffs.push({
                section:sec,
                spcIDs:that.spcIDList,
                data:defaultWaterCoeffPerPeriod
            })
        }
        that.coeffs.waterCoeffs = waterCoeffs;

        let laborCoeffs = {};
        let regenerationLabor = {};
        laborCoeffs.clearCut = 169.858462306131;
        laborCoeffs.thinning = 13.505923710842;
        for (const spcID of spcIDList) {
            if (Object.keys(regenerationLaborCoeffs).includes(spcID))
                regenerationLabor[spcID] = regenerationLaborCoeffs[ID2Spc[spcID]];
            else
                regenerationLabor[spcID] = regenerationLaborCoeffs['default'];
        }
        regenerationLabor["."] = 0;
        laborCoeffs.regeneration = regenerationLabor;
        that.coeffs.laborCoeffs = laborCoeffs;

        let costCoeffs = {};
        let regenerationCost = {};
        costCoeffs.clearCut = 9207.3361732583;
        costCoeffs.thinning = 3017.14924786963;
        for (const spcID of spcIDList) {
            if (Object.keys(regenerationCostCoeffs).includes(spcID))
                regenerationCost[spcID] = regenerationCostCoeffs[ID2Spc[spcID]];
            else
                regenerationCost[spcID] = regenerationCostCoeffs['default'];
        }
        costCoeffs.regeneration = regenerationCost;
        that.coeffs.costCoeffs = costCoeffs;


        let volume2Price = {};
        let thinningPrice = {};
        let clearCutPrice = {};
        for (const spcID of spcIDList) {
            if (Object.keys(spc2VolumePriceCoeffs.thinning).includes(ID2Spc[spcID]))
                thinningPrice[spcID] = spc2VolumePriceCoeffs.thinning[ID2Spc[spcID]];
            else
                thinningPrice[spcID] = spc2VolumePriceCoeffs.thinning['default'];
        }
        for (const species of spcLists) {
            if (Object.keys(spc2VolumePriceCoeffs.clearCut).includes(species))
                clearCutPrice[spc2ID[species]] = spc2VolumePriceCoeffs.clearCut[species];
            else
                clearCutPrice[spc2ID[species]] = spc2VolumePriceCoeffs.clearCut['default'];
        }
        volume2Price.thinning = thinningPrice;
        volume2Price.clearCut = clearCutPrice;
        that.coeffs.volume2Price = volume2Price;

        that.coeffs.CO2ProcessingCost = 50;
        that.coeffs.exchangeRate = 1200;
        that.coeffs.waterSavingCoeff = 959.91;
        that.coeffs.interestRate = 0.015;

        that.coeffs.initialDensity = 250;

        manager.coeffs.w1 = 0.5
        manager.coeffs.w2 = 0.5
        manager.coeffs.w3 = 0
    };
}
var manager = new Manager();


/************************************ ncrdss.main - view ************************************/
var chart = null; // Keep it global
Highcharts.setOptions({
    chart: {
        style: {
            fontFamily: "'Nanum Gothic', sans-serif"
        },
    }
});
chart = new Highcharts.Chart('container', {
    title: {
        text: '수종별 생장량 (m³/ha)',
        x: -20
    },
    subtitle: {
        text: '',
        x: -20
    },
    xAxis: {
        //categories: ['10년', '20년', '30년', '40년', '50년', '60년', '70년', '80년', '90년', '100년', '110년', '120년', '130년', '140년', '150년']
    },
    yAxis: {
        title: false
    },
    tooltip: {
        valueSuffix: 'm³/ha'
    },
    legend: {
        layout: 'vertical',
        align: 'left',
        verticalAlign: 'top',
        borderWidth: 1,
        floating: true,
        backgroundColor: '#FFFFFF',
        x: 50,
        y: 0,
    },
    series: []
});






var solution;
function sendData(data) {
    $.ajax({
        type: 'POST',
        contentType: 'application/json',
        url: '/post/data',
        dataType : 'json',
        data : JSON.stringify(data),
        success : function(res) {
            solution = JSON.parse(res);
            updateResultPage(solution);
            showResultPage();
        }, error : function(res){
            console.log(res);
        }
    });
}