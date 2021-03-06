/************************************ ncrdss.jexcel - model ************************************/
const CELL_WIDTH = 120;
var currentSpeciesSelected = {x1:null,y1:null,x2:null,y2:null}; //

var isBaseCompleted = function () {
    return !table_Base.getData().flat().includes("");
}
var isCurrentSpcCompleted = function () {
    const tableData = table_currentSpc.getData();
    for (const line of tableData) {
        if (line.slice(0, 4).includes("") || (line[4] === "" && line[5] === ""))
            return false;
    }
    return true;
}; // 현재임분정보 테이블이 완료되었는지 확인. 5~6번째 열에 대해서는 둘 중 하나만 채워지면 OK.
var isForManPlanCompleted = function () {
    return !table_ForManPlan.getData().flat().includes("")
}

/************************************ ncrdss.jexcel - controller ************************************/

/************************ jExcel OnChange Events ************************/
function isNumeric(instance, x, y, value) {
    /* 숫자 입력 여부 확인하는 함수.
    *  문자 입력, 혹은 delete 에 의해 공백이 입력되면
    *  해당 table 의 (id_table dictionary 로 참조) cell 을 공백으로
    *  바꾼 뒤에, False 를 출력한다. 숫자 입력일 경우 true */

    // 숫자가 아니거나, 음수이거나, 공백이거나 (지워져서)
    if (Number.isNaN(Number(value)) | Number(value) < 0 && value !== "") {
        // 그런데 만약, 입력된게 간벌시나리오이면서 %가 붙은 경우 (2자리부터 %가 붙어서 문자열로 출력됨 e.g., % 20)
        if (instance.id === 'table_thinning' && String(value).includes('%')) {
            value = Number(value.replace('% ', ''));
            // 숫자로 바꿔주고 100보다 큰지 체크
            if (value > 100 || value < 0) {
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
} // 0을 허용하는 numeric checker
function isNumericButNotZero(instance, x, y, value) {
    /* 숫자 입력 여부 확인하는 함수.
    *  문자 입력, 혹은 delete 에 의해 공백이 입력되면
    *  해당 table 의 (id_table dictionary 로 참조) cell 을 공백으로
    *  바꾼 뒤에, False 를 출력한다. 숫자 입력일 경우 true */

    // 숫자가 아니거나, 0이하이거나, 공백이거나 (지워져서)
    if (Number.isNaN(Number(value)) | Number(value) <= 0 && value !== "") {
        // 그런데 만약, 입력된게 간벌시나리오이면서 %가 붙은 경우 (2자리부터 %가 붙어서 문자열로 출력됨 e.g., % 20)
        if (instance.id === 'table_thinning' && String(value).includes('%')) {
            value = Number(value.replace('% ', ''));
            // 숫자로 바꿔주고 100보다 큰지 체크
            if (value > 100 || value < 0) {
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
} // 0을 허용하지 않는 numeric checker
function onChangeAddress() {
    table_SpcClasses.deleteColumn(1);
    // table_SpcClasses.insertColumn(1, 1, false, [{title:'수종명', type:'dropdown', source: manager.availableSpc, width:CELL_WIDTH}]);
    table_SpcClasses.insertColumn(1, 1, false, [{title:'수종명', type:'dropdown', source: manager.totalSpc, width:CELL_WIDTH}]); // 17개 수종 추가한 것
} // 주소 입력시 spcClasses 업데이트
var onChange_Base = function(instance, cell, x, y, value) {
    /* 임분 기본 정보 입력 테이블 #table_Base
    *  구역 수, 수종 수, 계획 기간, 시작 연도
    *  값이 변경되었을 때 호출되는 함수 */
    if (!isNumeric(instance, x, y, value))
        return false;

    manager.setBase(table_Base.getData()); // manager 값 업데이트
    var cellName = jexcel.getColumnNameFromId([x,y]);
    if (cellName == 'A1')
        updateCurrentSpcTable(manager.spcLists, 'sections');
    if (cellName == 'B1') {
        updateSpcClasses(value); // currentSpc 테이블의 수종 수 업데이트 (열 추가)
        manager.setSpcClasses(table_SpcClasses.getData());
    }
    if (cellName == 'C1')
        ""; //TODO : 계획분기 수 설정시 간벌 시나리오 테이블 재설정하는 함수
    if (isBaseCompleted())  // 전부 채워진 경우
        onCompleteBase();
    else {
        manager.completedFlags.table_base = false;
        setBgColor(table_Base, style_bg_red);
    }
};
var onChange_SpcClasses = function(instance, cell, x, y, value) {
    /* 수종 관련 기본 정보 입력 테이블 #table_SpcClasses
    *  수종 구분명, 수종 종류
    *  값이 변경되었을 때 호출되는 함수 */

    manager.setSpcClasses(table_SpcClasses.getData());
    var cellName = jexcel.getColumnNameFromId([x,y]);
    if (cellName.includes('B')) { // 수종이 추가되면 차트 그리기
        if (!manager.spcLists.includes(value))
            return false;
        else
            manager.setGrowth(); // manager 의 Growth 설정 (예측)
        for (const spc of chart.series.map(a => a.name))
             chart.get(spc).remove();
        for (const spc of manager.spcLists) {
            if (spc == "")
                continue;
            chart.addSeries({
                id: spc,
                name:spc,
                //data: final_volume[target_address + ' ' + value]
                //data: manager.spcGrowth[value].growthCombined
                data: manager.spcGrowth[spc].predictions
            }, false);
        }
        chart.redraw();
    }
    if (!table_SpcClasses.getData().flat().includes(""))  // 전부 채워진 경우
        onCompleteSpcClasses();
    else {
        manager.completedFlags.table_SpcClasses = false;
        setBgColor(table_SpcClasses, style_bg_red);
    }
};
var onChange_currentSpc = function(instance, cell, x, y, value) {
    /* 현재 임분 수종 관련 정보 입력 테이블 #table_currentSpc
    *  영급, 면적, 재적
    *  값이 변경되었을 때 호출되는 함수 */
    manager.setCurrentSpc(table_currentSpc.getData());
    var cellName = jexcel.getColumnNameFromId([x,y]);
    if (!cellName.includes('A') && !cellName.includes('B')) { // C D E F 열의 경우
        if (!isNumericButNotZero(instance, x, y, value))
            return false
    }
    if (isCurrentSpcCompleted()) // 전부 채워진 경우
        onCompleteCurrentSpc();
    else {
        manager.completedFlags.table_currentSpc = false;
        setBgColor(table_currentSpc, style_bg_red);
    }
};
var onChange_Thinning = function(instance, cell, x, y, value) {
    /* 산림시업정보 입력 테이블 #table_thinning
    *  
    *  값이 변경되었을 때 호출되는 함수 */
    if (!isNumeric(instance, x, y, value))
        return;
    manager.setThinningScenario(table_thinning.getData());
    manager.setForManPlan(table_ForManPlan.getData()); // 시업 정보를 입력하고, 시나리오를 입력하는 경우?
};
var onChangeForManPlan = function(instance, cell, x, y, value) {
    /* 산림시업정보 입력 테이블 #table_ForManPlan
    *  구역, 수종명, 수확분기, 간벌시나리오
    *  값이 변경되었을 때 호출되는 함수 */
    var cellName = jexcel.getColumnNameFromId([x,y]);
    if (cellName.includes('C') | cellName.includes('E')) { // C E 열인 경우만 (수확분기 & 밀도)
        if (!isNumeric(instance, x, y, value))
            return false
    }
    manager.setForManPlan(table_ForManPlan.getData());
    if (isForManPlanCompleted())  // 전부 채워진 경우
        onCompleteForManPlan();
    else {
        manager.completedFlags.table_ForManPlan = false;
        setBgColor(table_ForManPlan, style_bg_red);
    }
};
var onChange_carbonCoeffs = function(instance, cell, x, y, value) {
    /* 탄소흡수계수 입력 테이블 #table_carbonCoeffs
    *
    *  값이 변경되었을 때 호출되는 함수 */
    if (!isNumeric(instance, x, y, value))
        return false
};
var onSelectionActive = function(instance, x1, y1, x2, y2, origin) {
    currentSpeciesSelected = Object.assign(currentSpeciesSelected, {x1:x1, y1:y1, x2:x2, y2:y2});
}; // 현재임분 테이블의 선택된 영역

var onCompleteBase = function () {
    manager.completedFlags.table_base = true;
    setBgColor(table_Base, style_bg_orig)
    setBgColor(table_SpcClasses, style_bg_red);
}
var onCompleteCurrentSpc = function () {
    manager.completedFlags.table_currentSpc = true;
    setBgColor(table_currentSpc, style_bg_orig);
    setBgColor(table_ForManPlan, style_bg_red);
    setBgColor(table_thinning, style_bg_red);
};
var onCompleteSpcClasses = function () {
    manager.completedFlags.table_SpcClasses = true;
    updateForManTable(manager.spcLists);
    updateCurrentSpcTable(manager.spcLists, 'species');
    updateCarbonCoeffs(manager.spcLists);

    setBgColor(table_SpcClasses, style_bg_orig);
    setBgColor(table_currentSpc, style_bg_red);
    setBgColor(table_thinning, style_bg_red);
};
var onCompleteForManPlan = function () {
    manager.completedFlags.table_thinning = true;
    manager.completedFlags.table_ForManPlan = true;
    manager.setForManPlan(table_ForManPlan.getData());
    manager.setCoeffs();
    setBgColor(table_thinning, style_bg_orig);
    setBgColor(table_ForManPlan, style_bg_orig);
};

/************************ jExcel OnChange -> Update Table Shapes ************************/
function addCurrentSpcRow() {
    setBgColor(table_currentSpc, style_bg_orig);
    // setCellBorderColor(table_currentSpc, style_orig);
    table_currentSpc.insertRow();
    setBgColor(table_currentSpc, style_bg_red);
    // setCellBorderColor(table_currentSpc, style_red);
}
function deleteCurrentSpcRow() {
    table_currentSpc.deleteRow(currentSpeciesSelected.y1, currentSpeciesSelected.y2 - currentSpeciesSelected.y1 + 1);
    setBgColor(table_currentSpc, style_bg_red);
    // setCellBorderColor(table_currentSpc, style_red);
} // 현재 임분 조건에 대해서, 범위 선택 후 - 를 하면 그 열들을 삭제
function updateSpcClasses(num) {
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
        for (var i=0; i<manager.numSections; i++)
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
    if (table_Base.getCell('A1').innerText != "" & table_Base.getCell('B1').innerText != "") {
        var numSec = Number(table_Base.getCell('A1').innerText);
        var numSpc = Number(table_Base.getCell('B1').innerText);

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
var df_base = [
    [ , , , ],
];
var df_SpcClasses = [
    [ , , ],
];
var df_currentSpc = [
    [ , , , , , ],
];
var df_ForManPlan = [
    [ , , , , , ],
];
var df_carbonCoeffs = [[]];

var table_Base = jexcel(document.getElementById('table_Base'), {
    data:df_base,
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
table_Base.hideIndex();

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
    data:df_SpcClasses,
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

/************************ currentSpc Table ************************/
var table_currentSpc = jexcel(document.getElementById('table_currentSpc'), {
    data:df_currentSpc,
    colHeaders: ['구역번호', '수종명', '영급', '면적 (ha)', '재적 (m³/ha)', '밀도 (본수 /ha)'],
    colWidths: [ CELL_WIDTH, CELL_WIDTH, CELL_WIDTH, CELL_WIDTH, CELL_WIDTH, CELL_WIDTH ],
    columns: [
        { type: 'dropdown'},
        { type: 'dropdown'},
        { type: 'numeric' },
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
    data:df_ForManPlan,
    colHeaders: ['구역', '수종명', '수확분기', '간벌시나리오', '밀도 (본 /ha)'],
    colWidths: [ CELL_WIDTH, CELL_WIDTH, CELL_WIDTH, CELL_WIDTH, CELL_WIDTH ],
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
            source:['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'X']
        },
        { type: 'numeric' },
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
    colHeaders: ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'X'],
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
    data:df_carbonCoeffs,
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
    'table_base':table_Base,
    'table_SpcClasses':table_SpcClasses,
    'table_currentSpc':table_currentSpc,
    'table_thinning':table_thinning,
    'table_ForManPlan':table_ForManPlan,
    'table_carbonCoeffs':table_carbonCoeffs,
};