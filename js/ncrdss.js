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
    this.currentSpc = undefined;

    this.thinningScenario = {A:undefined,B:undefined,C:undefined,D:undefined,E:undefined,F:undefined,G:undefined,H:undefined,I:undefined,X:undefined};
    this.forManPlan = undefined;

    this.spcGrowth = undefined;

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
            if (this.availableSpc.includes(spc))
                continue;
            else
                additionalSpcList.push(spc);
        }
        this.additionalSpc = additionalSpcList;
        this.totalSpc = arrayUnique(this.availableSpc.concat(additionalSpcList));
    }
    this.setBase = function (data) {
        this.numSections = Number(data[0][0]);
        this.numSpecies = Number(data[0][1]);
        this.planningPeriod = Number(data[0][2]);
        this.startYear = Number(data[0][3]);
    }
    this.setSpcClasses = function (data) {
        var result_temp = new Array();
        for (var i=0; i<data.length; i++)
            result_temp.push({class: i+1, speciesID: data[i][0], species:data[i][1]});
        this.spcClasses = result_temp;
        this.spcLists = result_temp.map(a => a.species);
    }
    this.setCurrentSpc = function (data) {
        var result_temp = new Array();
        for (var i=0; i<data.length; i++)
            result_temp.push({section: Number(data[i][0]), species: data[i][1], age: Number(data[i][2]), area: Number(data[i][3]), volume: Number(data[i][4])});
        this.currentSpc = result_temp;
    }
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
    }
    this.setForManPlan = function (data) {
        var result_temp = [];
        for (var i=0; i<data.length; i++) {
            if (data[i][3] == "")
                continue;
            result_temp.push({section: Number(data[i][0].replace("구역 ", "")), species: data[i][1], clearCutYear: Number(data[i][2]), thinningScenario: this.thinningScenario[data[i][3]]});
        }
        this.forManPlan = result_temp;
    }
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
    }

}
var manager = new Manager();

function testDefine() {
    address = "전남 진도군 임회면"
    base = [["2", "3", "4", "5"]];
    spcClasses = [
        [
            "A",
            "육박나무"
        ],
        [
            "B",
            "비목나무"
        ],
        [
            "C",
            "상수리나무"
        ]
    ];
    currentSpc= [
        [
            "1",
            "육박나무",
            "5",
            "20",
            "140"
        ],
        [
            "1",
            "비목나무",
            "4",
            "40",
            "130"
        ],
        [
            "1",
            "비목나무",
            "3",
            "40",
            "150"
        ],
        [
            "2",
            "상수리나무",
            "3",
            "10",
            "160"
        ],
        [
            "2",
            "육박나무",
            "7",
            "30",
            "180"
        ]
    ];

    manager.setAvailableSpc(addressSpecies[address]);
    manager.setAddress(address); // save to manager
    onChangeAddress();
    table_Base.setData(base);
    table_SpcClasses.setData(spcClasses);
    //table_currentSpc.setData(currentSpc);
}


// Keep it global
var chart = null;
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