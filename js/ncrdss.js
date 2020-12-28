var manager = {
    numSection:null,
    numSpecies:null,
    planningPeriod:null,
    startYear:null,
    spcClasses:null,
    spcLists:null,
};

function setAddress(data) {
    manager.address = data;
}
function setBase(data) {
    var result_temp = {};
    result_temp.numSection = Number(data[0][0]);
    result_temp.numSpecies = Number(data[0][1]);
    result_temp.planningPeriod = Number(data[0][2]);
    result_temp.startYear = Number(data[0][3]);

    manager = Object.assign(manager, result_temp);
    }
function setSpcClasses(data) {
    var result_temp = new Array();
    for (var i=0; i<data.length; i++)
        result_temp.push({class: i+1, speciesID: data[i][0], species:data[i][1]});
    manager.spcClasses = result_temp;
    manager.spcLists = result_temp.map(a => a.species);
}
function setCurrentSpc(data) {
    var result_temp = new Array();
    for (var i=0; i<data.length; i++)
        result_temp.push({section: Number(data[i][0]), species: data[i][1], age: Number(data[i][2]), area: Number(data[i][3]), volumn: Number(data[i][4])});
    manager.currentSpc = result_temp;
    }
function setThinningScenario(data) {
    var result_temp = new Array();
    const index = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I'];
    for (const i in index) {
        const cols = data.length;
        const rows = data[0].length;
        for (var j=0; j<rows; j++) {
            result_temp[index[j]] = Array();
            for (var k=0; k<cols; k++) {
                result_temp[index[j]].push(Number(data[k][j].replace('%', ''))/100);
            }
        }
    }
    manager.thinningScenario = result_temp;
}
function setForManPlan(data) {
    var result_temp = new Array();
    for (var i=0; i<data.length; i++)
        result_temp.push({section: Number(data[i][0].replace("구역 ", "")), species: Number(data[i][1]), clearCutYear: Number(data[i][2]), thinningScenarioID: data[i][3]});
    manager.forManPlan = result_temp;
}
function setGrowth() {
    const speciesArray = manager.spcClasses;
    var result_temp = {};
    for (var i=0; i<speciesArray.length; i++) {
        console.log(speciesArray[i].species);
        if (speciesArray[i].species == "") {
            console.log("Continue", i)
            continue
        }
        var volumns = final_volumn[manager.address + ' ' + speciesArray[i].species]
        var temp = []; // [x, y] 를 담고 있는 리스트
        for (var j=1; j<volumns.length; j++) { // starting from 1 to avoid NaN values
            temp.push([j, volumns[j]]);
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
            if (volumns[l] != undefined)
                growthCombined.push(volumns[l]);
            else
                growthCombined.push(predictions[l]);
        }
        logRegression.predictions = predictions;
        logRegression.growthCombined = growthCombined;
        result_temp[speciesArray[i].species] = logRegression;
    }
    manager.spcGrowth = result_temp;
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

function update_option(arr){ // 주소 입력시에
    table_SpcClasses.deleteColumn(1);
    table_SpcClasses.insertColumn(1, 1, false, [{title:'수종명', type:'dropdown', source: arr, width:CELL_WIDTH}]);
}