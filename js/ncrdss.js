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

var ObjectiveCanvas = document.getElementById('ObjectiveBarChart');
var barChart;
var chartOptions = {
    layout: {
        padding: {
            left: 10,
            right: 20,
            top: 0,
            bottom: 0
        },
        margin: {
            top: 15,
        }
    },
    legend: {
        position: "bottom",
        labels: {}
    },
    scales: {
        xAxes: [{
            barPercentage: 1,
            categoryPercentage: 0.6
        }],
        yAxes: [{
            ticks: {
                beginAtZero: true,
                //stepSize: 500000,
                // Return an empty string to draw the tick line but hide the tick label
                // Return `null` or `undefined` to hide the tick line entirely
                userCallback: function(value, index, values) {
                    // Convert the number to a string and split the string every 3 charaters from the end
                    value = value.toString();
                    value = value.split(/(?=(?:...)*$)/);

                    // Convert the array to a string and format the output
                    value = value.join(',');
                    return value + '원';
                }
            },
            id: "axis1",
        }, {
            ticks: {
                beginAtZero: true,
                //stepSize: 500000,
                // Return an empty string to draw the tick line but hide the tick label
                // Return `null` or `undefined` to hide the tick line entirely
                userCallback: function(value, index, values) {
                    // Convert the number to a string and split the string every 3 charaters from the end
                    value = value.toString();
                    value = value.split(/(?=(?:...)*$)/);

                    // Convert the array to a string and format the output
                    value = value.join(',');
                    return value + '명';
                }
            },
            id: "axis2"
        }]
    }
};

var WoodProd = {
    label: '분기별 목재 생산 가치',
    data: [],
    backgroundColor: 'rgba(231, 111, 81, 0.6)',
    borderWidth: 0,
    yAxisID: "axis1"
};
var Carbon = {
    label: '분기별 탄소 저장 가치',
    data: [],
    backgroundColor: 'rgba(38, 70, 83, 0.6)',
    borderWidth: 0,
    yAxisID: "axis1"
};
var WaterSave = {
    label: '분기별 수자원 함양 가치',
    data: [],
    backgroundColor: 'rgba(42, 157, 143, 0.6)',
    borderWidth: 0,
    yAxisID: "axis1"
};
var Labor = {
    label: '분기별 일자리 창출량 (명 / ha)',
    data: [],
    backgroundColor: 'rgba(233, 196, 106, 0.6)',
    borderWidth: 0,
    yAxisID: "axis2"
};

let objectives = {
    WoodProd : WoodProd,
    Carbon : Carbon,
    WaterSave : WaterSave,
    Labor : Labor,
}

const objPrefix = {
    WoodProd : 'f.',
    Carbon : 'g.',
    WaterSave : 'h.',
    Labor : 'J.',
};

function arrayUnique(array) { // removes duplicates
    var a = array.concat();
    for(var i=0; i<a.length; ++i) {
        for(var j=i+1; j<a.length; ++j) {
            if(a[i] === a[j])
                a.splice(j--, 1);
        }
    }
    return a;
}

function Manager() {
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

    var that = this;
    this.setAddress = function (data) {
        this.address = data;
    };
    this.setAvailableSpc = function (data) {
        this.availableSpc = data;
    };
    this.setAdditionalSpc = function () {
        const essentialSpc = ['소나무', '신갈나무', '굴참나무', '리기다소나무', '졸참나무', '곰솔', '상수리나무', '일본잎갈나무', '밤나무', '잣나무', '아까시나무', '갈참나무', '산벚나무', '물푸레나무', '때죽나무', '굴피나무', '떡갈나무'];
        var additionalSpcList = [];
        for (const spc of essentialSpc) {
            if (!this.availableSpc.includes(spc))
                additionalSpcList.push(spc);
        }
        this.additionalSpc = additionalSpcList;
        this.totalSpc = arrayUnique(this.availableSpc.concat(additionalSpcList));
    };
    this.setBase = function (data) {
        this.numSections = Number(data[0][0]);
        this.numSpecies = Number(data[0][1]);
        this.planningPeriod = Number(data[0][2]);
        this.startYear = Number(data[0][3]);
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
            result_temp.push({section: Number(data[i][0]), species: data[i][1], age: Number(data[i][2]), area: Number(data[i][3]), volume: Number(data[i][4])});
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
                    result_temp[index[j]].push(Number(data[k][j].replace('%', '')) / 100);
                }
            }
        }
        this.thinningScenario = result_temp;
    };
    this.setForManPlan = function (data) {
        var result_temp = [];
        for (var i=0; i<data.length; i++) {
            if (data[i][3] == "")
                continue;
            result_temp.push({section: Number(data[i][0].replace("구역 ", "")), species: data[i][1], clearCutYear: Number(data[i][2]), thinningScenario: this.thinningScenario[data[i][3]]});
        }
        this.forManPlan = result_temp;
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
        this.spcGrowth = result_temp;
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

        that.coeffs.initialDensity = 3000;

        manager.coeffs.w1 = 1.0
        manager.coeffs.w2 = 0
        manager.coeffs.w3 = 0
    }
}
var manager = new Manager();

function updateResultPage(solution) {
    if (barChart)
        barChart.destroy();
    console.log(solution);
    const val = solution.value;
    const meta = solution.meta;
    console.log(meta)
    for (let period=1; period<=meta.planningPeriod; period++) {
        for (const key of Object.keys(objectives)) {
            objectives[key].data.push(val[objPrefix[key] + String(period)])
        }
    }
    var objectiveDataset = {
        labels: [...Array(meta.planningPeriod).keys()].map(x => x + 1),
        datasets: Object.values(objectives)
    };

    barChart = new Chart(ObjectiveCanvas, {
        type: 'bar',
        data: objectiveDataset,
        options: chartOptions
    });
}

function showResultPage() {

}

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