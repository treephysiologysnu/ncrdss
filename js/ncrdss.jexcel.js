const CELL_WIDTH = 120;
const CARBONCOEFFS = [1.433102, 1.667497, 1.738947, 1.431354, 2.516572, 2.704444];

var currentSpeciesSelected = {x1:null,y1:null,x2:null,y2:null}

/*************************************************************************************************
 *                              jExcel OnChange Events
 *************************************************************************************************/
function checkNumeric(instance, x, y, value) {
    /* 숫자 입력 여부 확인하는 함수.
    *  문자 입력, 혹은 delete 에 의해 공백이 입력되면
    *  해당 table 의 (id_table dictionary 로 참조) cell 을 공백으로
    *  바꾼 뒤에, False 를 출력한다. 숫자 입력일 경우 true */

    // 숫자가 아니거나, 음수이거나, 공백이거나 (지워져서)
    if (Number.isNaN(Number(value)) | Number(value) <= 0 && value!='') {
        // 그런데 만약, 입력된게 간벌시나리오이면서 %가 붙은 경우 (2자리부터 %가 붙어서 문자열로 출력됨 e.g., % 20)
        if (instance.id == 'table_thinning' & String(value).includes('%')) {
            value = Number(value.replace('% ', ''));
            // 숫자로 바꿔주고 100보다 큰지 체크
            if (value >= 100 | value < 0) {
                id_table[instance.id].setValueFromCoords(x, y, '');
                return false
            } else {
                return true
            }
        } else {
            id_table[instance.id].setValueFromCoords(x, y, '');
            return false
        }
    } else
        return true
}
var onChange_Base = function(instance, cell, x, y, value) {
    /* 임분 기본 정보 입력 테이블 #table_base
    *  구역 수, 수종 수, 계획 기간, 시작 연도
    *  값이 변경되었을 때 호출되는 함수 */
    if (!checkNumeric(instance, x, y, value))
        return

    setBase(table_base.getData()); // manager 값 업데이트
    var cellName = jexcel.getColumnNameFromId([x,y]);
    if (cellName == 'A1')
        updateCurrentSpcTable(manager.spcLists, 'sections');
    if (cellName == 'B1') {
        updateNumSpc(value); // currentSpc 테이블의 수종 수 업데이트 (열 추가)
        setSpcClasses(table_SpcClasses.getData());
    }
    if (cellName == 'C1')
        ""; //TODO : 계획분기 수 설정시 간벌 시나리오 테이블 재설정하는 함수
    if (!table_base.getData().flat().includes("")) { // 전부 채워진 경우

        setBgColor(table_base, style_bg_orig)
        setBgColor(table_SpcClasses, style_bg_red);
        //setCellBorderColor(table_base, style_orig); // BaseTable 레이아웃 업데이트
        //setCellBorderColor(table_SpcClasses, style_red);
    }
};
var onChange_SpcClasses = function(instance, cell, x, y, value) {
    /* 수종 관련 기본 정보 입력 테이블 #table_SpcClasses
    *  수종 구분명, 수종 종류
    *  값이 변경되었을 때 호출되는 함수 */
    setSpcClasses(table_SpcClasses.getData());
    var cellName = jexcel.getColumnNameFromId([x,y]);
    if (cellName.includes('B')) { // 수종이 추가되면 차트 그리기
        setGrowth(); // Growth 예측하고
        chart.addSeries({
            id: value,
            name:value,
            //data: final_volumn[target_address + ' ' + value]
            //data: manager.spcGrowth[value].growthCombined
            data: manager.spcGrowth[value].predictions
        }, false);
        chart.redraw();
    }
    if (!table_SpcClasses.getData().flat().includes("")) { // 전부 채워진 경우
        updateForManTable(manager.spcLists);
        updateCurrentSpcTable(manager.spcLists, 'species');
        updateCarbonCoeffs(manager.spcLists);

        setBgColor(table_SpcClasses, style_bg_orig);
        setBgColor(table_currentSpc, style_bg_red);
        setBgColor(table_thinning, style_bg_red);
        //setCellBorderColor(table_SpcClasses, style_orig); // SpcClass Input 레이아웃 업데이트
        //setCellBorderColor(table_currentSpc, style_red);
        //setCellBorderColor(table_thinning, style_red);
    }
};
var onChange_currentSpc = function(instance, cell, x, y, value) {
    /* 현재 임분 수종 관련 정보 입력 테이블 #table_currentSpc
    *  영급, 면적, 재적
    *  값이 변경되었을 때 호출되는 함수 */
    setCurrentSpc(table_currentSpc.getData());
    var cellName = jexcel.getColumnNameFromId([x,y]);
    if (!cellName.includes('A') & !cellName.includes('B')) { // C D E 열의 경우
        console.log(cellName);
        if (!checkNumeric(instance, x, y, value))
            return false
    }
    if (!table_currentSpc.getData().flat().includes("")) { // 전부 채워진 경우
        setBgColor(table_currentSpc, style_bg_orig);
        setBgColor(table_ForManPlan, style_bg_red);
        setBgColor(table_thinning, style_bg_red);
        //setCellBorderColor(table_currentSpc, style_orig);
        //setCellBorderColor(table_ForManPlan, style_red);
        //setCellBorderColor(table_thinning, style_red);
    }
};
var onChange_Thinning = function(instance, cell, x, y, value) {
    /* 산림시업정보 입력 테이블 #table_thinning
    *  
    *  값이 변경되었을 때 호출되는 함수 */
    if (!checkNumeric(instance, x, y, value))
        return
    setThinningScenario(table_thinning.getData());
};
var onChangeForManPlan = function(instance, cell, x, y, value) {
    /* 산림시업정보 입력 테이블 #table_ForManPlan
    *  구역, 수종명, 수확분기, 간벌시나리오
    *  값이 변경되었을 때 호출되는 함수 */
    var cellName = jexcel.getColumnNameFromId([x,y]);
    if (cellName.includes('C')) { // C 열인 경우만 (수확분기)
        if (!checkNumeric(instance, x, y, value))
            return false
    }
    setForManPlan(table_ForManPlan.getData());
    if (!table_ForManPlan.getData().flat().includes("")) { // 전부 채워진 경우
        setBgColor(table_thinning, style_bg_orig);
        setBgColor(table_ForManPlan, style_bg_orig);
        // setCellBorderColor(table_ForManPlan, style_orig);
    }
};
var onChange_carbonCoeffs = function(instance, cell, x, y, value) {
    /* 탄소흡수계수 입력 테이블 #table_carbonCoeffs
    *
    *  값이 변경되었을 때 호출되는 함수 */
    if (!checkNumeric(instance, x, y, value))
        return false
};
var onSelectionActive = function(instance, x1, y1, x2, y2, origin) {
    currentSpeciesSelected = Object.assign(currentSpeciesSelected, {x1:x1, y1:y1, x2:x2, y2:y2});
}; // 현재임분 테이블의 선택된 영역
/*************************************************************************************************
 *                            jExcel OnChange -> Update Table Shapes
 *************************************************************************************************/
function addCurrentSpcRow() {
    setBgColor(table_currentSpc, style_bg_orig);
    // setCellBorderColor(table_currentSpc, style_orig);
    table_currentSpc.insertRow();
    setBgColor(table_currentSpc, style_bg_red);
    // setCellBorderColor(table_currentSpc, style_red);
}
function delecteCurrentSpcRow() {
    table_currentSpc.deleteRow(currentSpeciesSelected.y1, currentSpeciesSelected.y2 - currentSpeciesSelected.y1 + 1);
    setBgColor(table_currentSpc, style_bg_red);
    // setCellBorderColor(table_currentSpc, style_red);
}
function updateNumSpc(num) {
    index_SpcClasses.deleteRow(1,index_SpcClasses.rows.length);
    table_SpcClasses.deleteRow(1,table_SpcClasses.rows.length);
    for (var i=1;i<num;i++) {
        index_SpcClasses.insertRow(['수종 ' + String(i+1)]);
        table_SpcClasses.insertRow();
    }
}
function updateCurrentSpcTable(species, flag) {
    if (flag == 'sections') {
        var sectionArray = new Array();
        for (var i=0; i<manager.numSection; i++)
            sectionArray.push(String(i+1));
        table_currentSpc.deleteColumn(0);
        table_currentSpc.insertColumn(1, 0, true, [{title:'구역 번호', type:'dropdown', source: sectionArray, width:CELL_WIDTH}]);
    }
    if (flag == 'species') {
        table_currentSpc.deleteColumn(1);
        table_currentSpc.insertColumn(1, 1, true, [{title:'수종명', type:'dropdown', source: species, width:CELL_WIDTH}]);
    }
}
function updateForManTable(species) {
    if (table_base.getCell('A1').innerText != "" & table_base.getCell('B1').innerText != "") {
        var numSec = Number(table_base.getCell('A1').innerText);
        var numSpc = Number(table_base.getCell('B1').innerText);

        index_ForManPlan.deleteRow(1,index_ForManPlan.rows.length)
        table_ForManPlan.deleteRow(1,table_ForManPlan.rows.length);
        for (var i=0;i<numSec;i++) {
            for (var j=0;j<numSpc;j++) {
                index_ForManPlan.insertRow();
                table_ForManPlan.insertRow(['구역 ' + String(i+1), species[j]]);
            }
        }
        index_ForManPlan.deleteRow(0, 1);
        table_ForManPlan.deleteRow(0, 1);
    };
}
function updateCarbonCoeffs(species) {
    index_carbonCoeffs.deleteRow(1,index_carbonCoeffs.rows.length);
    table_carbonCoeffs.deleteRow(1,table_carbonCoeffs.rows.length);

    for (var i=0; i<species.length; i++) {
        index_carbonCoeffs.insertRow([species[i]]);
        table_carbonCoeffs.insertRow();
    }
    index_carbonCoeffs.deleteRow(0);
    table_carbonCoeffs.deleteRow(0);
}
/*************************************************************************************************
*                                  jExcel Chart Initialization
*************************************************************************************************/
var dataframe_base = [
    [ , , , ],
];
var dataframe_SpcClasses = [
    [ , , ],
];
var dataframe_currentSpc = [
    [ , , , , ],
];
var dataframe_ForManPlan = [
    [ , , , , ],
];
var dataframe_carbonCoeffs = [[]];

var table_base = jexcel(document.getElementById('table_base'), {
    data:dataframe_base,
    colHeaders: ['구역 수', '고려할 수종 수', '계획 분기수', '시작 연도'],
    colWidths: [ CELL_WIDTH, CELL_WIDTH, CELL_WIDTH, CELL_WIDTH ],
    columns: [
        { type: 'numeric' },
        { type: 'numeric' },
        { type: 'numeric' },
        { type: 'numeric' },
    ],
    onchange: onChange_Base,
    allowManualInsertRow:false,
    allowManualInsertColumn: false,
});
table_base.hideIndex();

var index_SpcClasses = jexcel(document.getElementById('index_SpcClasses'), {
    data:[['수종 1']],
    colHeaders:['수종구분정보'],
    colWidths: [ CELL_WIDTH ],
    columns: [
        {
            type: 'text',
            readOnly:true,
        },
    ],
    allowManualInsertRow:false,
    allowManualInsertColumn: false,
});
index_SpcClasses.hideIndex();
var table_SpcClasses = jexcel(document.getElementById('table_SpcClasses'), {
    data:dataframe_SpcClasses,
    colHeaders: ['수종 구분명', '수종명'],
    colWidths: [ CELL_WIDTH, CELL_WIDTH],
    columns: [
        { type: 'text' },
        { type: 'dropdown', source:[] },
    ],
    onchange: onChange_SpcClasses,
    rowResize: true,
    allowManualInsertRow:false,
    allowManualInsertColumn: false,
});
table_SpcClasses.hideIndex();

/*
var index_currentSpc = jexcel(document.getElementById('index_currentSpc'), {
    data:[['구역 1']],
    colHeaders:['현재임분정보'],
    colWidths: [ CELL_WIDTH ],
    columns: [
        {
            type: 'text',
            readOnly:true,
        },
    ],
    allowManualInsertRow:false,
    allowManualInsertColumn: false,
});
index_currentSpc.hideIndex();*/
var table_currentSpc = jexcel(document.getElementById('table_currentSpc'), {
    data:dataframe_currentSpc,
    colHeaders: ['구역번호', '수종명', '영급', '면적 (ha)', '재적 (m³/ha)'],
    colWidths: [ CELL_WIDTH, CELL_WIDTH, CELL_WIDTH, CELL_WIDTH, CELL_WIDTH ],
    columns: [
        { type: 'dropdown'},
        { type: 'dropdown'},
        { type: 'numeric' },
        { type: 'numeric' },
        { type: 'numeric' },
    ],
    rowResize: true,
    onchange:onChange_currentSpc,
    onselection:onSelectionActive,
    allowManualInsertRow:false,
    allowManualInsertColumn: false,
});
table_currentSpc.hideIndex();


var index_ForManPlan = jexcel(document.getElementById('index_ForManPlan'), {
    data:[[]],
    colHeaders:['산림시업정보'],
    colWidths: [ CELL_WIDTH ],
    columns: [
        {
            type: 'text',
            readOnly:true,
        },
    ],
    allowManualInsertRow:false,
    allowManualInsertColumn: false,
});
index_ForManPlan.hideIndex();
var table_ForManPlan = jexcel(document.getElementById('table_ForManPlan'), {
    data:dataframe_ForManPlan,
    colHeaders: ['구역', '수종명', '수확분기', '간벌시나리오'],
    colWidths: [ CELL_WIDTH, CELL_WIDTH, CELL_WIDTH, CELL_WIDTH ],
    columns: [
        {
            type: 'text',
            readOnly:true,
        },
        {
            type: 'text',
            readOnly:true,
        },
        { type: 'numeric' },
        { type: 'dropdown',
            source:['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I',]
        },
    ],
    onchange:onChangeForManPlan,
    rowResize: true,
    allowManualInsertRow:false,
    allowManualInsertColumn: false,
});
table_ForManPlan.hideIndex();

var index_thinning = jexcel(document.getElementById('index_thinning'), {
    data:[['10년']],
    colHeaders:['연도'],
    colWidths: [ CELL_WIDTH / 10 * 4.5 ],
    columns: [
        {
            type: 'text',
        },
    ],
    allowManualInsertRow:false,
    allowManualInsertColumn: false,
});
for (const year of ['20년','30년','40년','50년','60년','70년','80년','90년','100년','110년','120년','130년','140년','150년']) {
    index_thinning.insertRow([year]);
}
index_thinning.hideIndex();
var table_thinning = jexcel(document.getElementById('table_thinning'), {
    data:[[]],
    colHeaders: [],
    columns: [
        { type: 'numeric', mask: '% #'},
        { type: 'numeric', mask: '% #'},
        { type: 'numeric', mask: '% #'},
        { type: 'numeric', mask: '% #'},
        { type: 'numeric', mask: '% #'},
        { type: 'numeric', mask: '% #'},
        { type: 'numeric', mask: '% #'},
        { type: 'numeric', mask: '% #'},
        { type: 'numeric', mask: '% #'},
    ],
    defaultColWidth:CELL_WIDTH / 10 * 4.999,
    onchange:onChange_Thinning,
    rowResize: true,
    allowManualInsertRow:false,
    allowManualInsertColumn: false,
});
table_thinning.hideIndex();
for (i=0;i<14;i++)
    table_thinning.insertRow();



var index_carbonCoeffs = jexcel(document.getElementById('index_carbonCoeffs'), {
    data:[[]],
    colHeaders:['탄소흡수계수'],
    colWidths: [ CELL_WIDTH ],
    columns: [
        {
            type: 'text',
            readOnly:true,
        },
    ],
    allowManualInsertRow:false,
    allowManualInsertColumn: false,
});
index_carbonCoeffs.hideIndex();
var table_carbonCoeffs = jexcel(document.getElementById('table_carbonCoeffs'), {
    data:dataframe_carbonCoeffs,
    colHeaders: ['coeffs'],
    colWidths: [ CELL_WIDTH ],
    columns: [
        { type: 'numeric' },
    ],
    onchange: onChange_carbonCoeffs,
    rowResize: true,
    allowManualInsertRow:false,
    allowManualInsertColumn: false,
});
table_carbonCoeffs.hideIndex();

var id_table = {
    'table_base':table_base,
    'table_SpcClasses':table_SpcClasses,
    'table_currentSpc':table_currentSpc,
    'table_thinning':table_thinning,
    'table_ForManPlan':table_ForManPlan,
    'table_carbonCoeffs':table_carbonCoeffs,
};