/************************************ ncrdss.results - model ************************************/
function ResultManager() {
    let that = this;
    this.optimizedResults = undefined;
    this.metadata = undefined;
    this.periodArray = undefined;

    this.WoodProd = {
        label: '분기별 목재 생산 가치',
        data: [],
        backgroundColor: 'rgba(231, 111, 81, 0.6)',
        borderWidth: 0,
        yAxisID: "axis1"
    };
    this.Carbon = {
        label: '분기별 탄소 저장 가치',
        data: [],
        backgroundColor: 'rgba(38, 70, 83, 0.6)',
        borderWidth: 0,
        yAxisID: "axis1"
    };
    this.WaterSave = {
        label: '분기별 수자원 함양 가치',
        data: [],
        backgroundColor: 'rgba(42, 157, 143, 0.6)',
        borderWidth: 0,
        yAxisID: "axis1"
    };
    this.Labor = {
        label: '분기별 일자리 창출량 (명 / ha)',
        data: [],
        backgroundColor: 'rgba(233, 196, 106, 0.6)',
        borderWidth: 0,
        yAxisID: "axis2"
    };
    this.objectiveFunctionData = {
        WoodProd : that.WoodProd,
        Carbon : that.Carbon,
        WaterSave : that.WaterSave,
        Labor : that.Labor,
    };
    this.volumeGrowthPerSpcData = {};

    this.objectiveFunctionPrefix = {
        WoodProd : 'f.',
        Carbon : 'g.',
        WaterSave : 'h.',
        Labor : 'J.',
    }; // 각 결과 변수의 ID의 접두어. JSON 에서 읽어올 때 활용

    this.updateData = function (data) {
        that.optimizedResults = data.value;
        that.metadata = data.meta;
    }; // 전송된 JSON Response 로부터 본 객체의 optimizedResults 와 metadata 를 업데이트.
    this.createPeriodArray = function () {
        that.periodArray = [...Array(that.metadata.planningPeriod).keys()].map(x => x + 1)
    }; // 1 부터 계획기간까지의 배열을 생성합니다.
    this.updateObjectiveFunctions = function () {
        for (let period=1; period<=that.metadata.planningPeriod; period++) {
            for (const key of Object.keys(that.objectiveFunctionData)) {
                that.objectiveFunctionData[key].data.push(that.optimizedResults[that.objectiveFunctionPrefix[key] + String(period)])
            }
        }
    };
    this.updateVolumeGrowthPerSpc = function () {
        let key;
        resetSeed()
        for (const spcID of that.metadata.spcIDList) {
            let tempObject = {
                label: that.metadata.ID2Spc[spcID],
                data: [],
                borderWidth: 0,
                backgroundColor: dynamicColors(),
                yAxisID: "axis1"
            }; // 임시 객체를 하나 만들고, data 안에 데이터를 집어넣습니다.

            for (let period=1; period<=that.metadata.planningPeriod; period++) {
                key = spcID + 'V.' + String(period); // 참조할 key 를 생성하고
                tempObject.data.push(that.optimizedResults[key]);
            }
            that.volumeGrowthPerSpcData[spcID] = tempObject;
        }
    }
}

resultManager = new ResultManager();

/************************************ ncrdss.results - view ************************************/
var objectiveFunctionCanvas = document.getElementById('objectiveFunctionsCanvas');
var volumeGrowthCanvas = document.getElementById('volumeGrowthCanvas');

var priceSplitCallback = function(value, index, values) {
    // Convert the number to a string and split the string every 3 charaters from the end
    let suffix = '원';
    if (value >= 100000000) {
        value = value / 100000000;
        suffix = ' 억원'
    }
    if (value >= 10000000) {
        value = value / 10000000;
        suffix = ' 천만원';
    }
    if (value >= 10000) {
        value = value / 10000;
        suffix = ' 만원';
    }
    value = format3DigitWithCommas(value);
    return value + suffix;
}; // Value to proper digits in Korean Won

var objectiveFunctionChart;
var volumeGrowthChart;

var objectiveFunctionChartOptions = {
    layout: {
        padding: {
            left: 10,
            right: 20,
            top: 30,
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
    tooltips: {
        callbacks: {
            label: function(tooltipItems, data) {
                let value = tooltipItems.yLabel;
                let suffix = '원';
                if (tooltipItems.datasetIndex === 3) { // 일자리창출량인 경우
                    value = Math.round(value);
                    suffix = '명';
                }
                else {
                    suffix = '원';
                    if (value >= 100000000) {
                        value = value / 100000000;
                        suffix = ' 억원'
                    }
                    if (value >= 1000000) {
                        value = value / 1000000;
                        suffix = ' 백만원';
                    }
                    if (value >= 10000) {
                        value = value / 10000;
                        suffix = ' 만원';
                    }
                    value = Math.round(value*10)/10;
                }

                value = format3DigitWithCommas(value);
                return value + suffix;
            }
        }
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
                userCallback: priceSplitCallback,
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
                    value = format3DigitWithCommas(value);
                    return value + '명';
                }
            },
            id: "axis2"
        }]
    }
};
var volumeGrowthChartOptions = {
    layout: {
        padding: {
            left: 10,
            right: 20,
            top: 30,
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
                    value = Math.round(value*10)/10;
                    value = format3DigitWithCommas(value);
                    return value + ' m³';
                }
            },
            id: "axis1"
        }]
    }
};
/************************************ ncrdss.results - controller ************************************/


const chartShowBtnClick = ({ target }) => {
    for (let element of document.getElementsByClassName("chart-showBtn")) {
        if (element.dataset.id === target.dataset.id)
            target.classList.add('selected');
        else
            element.classList.remove('selected');
    }
    for (let element of document.getElementsByClassName("chart-canvas")) {
        if (element.dataset.id === target.dataset.id)
            element.classList.remove('hidden');
        else
            element.classList.add('hidden');
    }
    //document.getElementById(target.id).style.display = 'auto';

    //target.classList.add('selected');
    //document.querySelectorAll('.page-content').forEach(t => t.classList.add('hidden'));
    //document.querySelector(`#${id}`).classList.remove('hidden');

};
const bindClickListenerToChartBtn = () => {
    document.querySelectorAll('.chart-showBtn').forEach(btn => {
        btn.addEventListener('click', chartShowBtnClick);
    })
};
document.addEventListener('DOMContentLoaded', () => {
    bindClickListenerToChartBtn();
});


function updateResultPage(responseJSON) {
    if (objectiveFunctionChart)
        objectiveFunctionChart.destroy();
    if (volumeGrowthChart)
        volumeGrowthChart.destroy();

    resultManager.updateData(responseJSON);
    resultManager.createPeriodArray();
    resultManager.updateObjectiveFunctions();
    resultManager.updateVolumeGrowthPerSpc();


    let objectiveDataset = {
        labels: resultManager.periodArray,
        datasets: Object.values(resultManager.objectiveFunctionData)
    };
    let volumeGrowthDataset = {
        labels: resultManager.periodArray,
        datasets: Object.values(resultManager.volumeGrowthPerSpcData)
    };
    console.log(volumeGrowthDataset)

    objectiveFunctionChart = new Chart(objectiveFunctionCanvas, {
        type: 'bar',
        data: objectiveDataset,
        options: objectiveFunctionChartOptions
    });
    volumeGrowthChart = new Chart(volumeGrowthCanvas, {
        type: 'bar',
        data: volumeGrowthDataset,
        options: volumeGrowthChartOptions
    });
}

function showResultPage() {

}