/*************************************************************************************************
 *                                         Define Variables
 *************************************************************************************************/
/**********************************************************************
 *                         Define Constants
 **********************************************************************/

function LPVariable(siteNumber, periodBorn, currentSpcIndex, periodCut, regenSpcIndex) {
    var periodBornString = String(periodBorn);
    if (periodBorn < 0)
        periodBornString = '.';
    this.name = String(siteNumber) + "_" + periodBornString + String(currentSpcIndex) + String(periodCut) + String(regenSpcIndex);
    return {siteNumber:siteNumber, periodBorn:periodBorn, currentSpcIndex:currentSpcIndex, periodCut:periodCut, regenSpcIndex:regenSpcIndex, name:this.name}
}

var LPVtest = LPVariable(1, -6, 1, 4, 2)

function LinearProgramming() {
    this.variables = [];
    this.variableNames = [];
    // this.testRow = [0, 0, 0, 0, 0, 0];
    this.mxA = math.zeros(); // Ax ≤ B 에서의 A 항
    this.mxB = math.zeros(); // Ax ≤ B 에서의 B 항
    this.addRow = function (line) {
        /* A 행렬에 행을 추가합니다. 아직 값 선언이 안된 경우면 값을 대체합니다.
        * Usage: lp.addRow([1,2,3,4,5])
        * >>> [
        *       [0,0,0,0,0]
        *       [1,2,3,4,5]
        *      ]
        * */
        const mxLine = math.matrix([line]);
        if (this.mxA._size[0] == 0) {
            this.mxA = mxLine;
            return;
        }
        if (this.mxA._size[0] != 0 & mxLine._size[1] != this.mxA._size[1])
            throw '열의 갯수가 맞지 않습니다.';
        this.mxA = math.concat(this.mxA, mxLine, 0);
    };
    this.addColumn = function (line) {
        /* A 행렬에 열을 추가합니다.
        * Usage: lp.addRow([100,200])
        * >>> [
        *       [0,0,0,0,0,100]
        *       [1,2,3,4,5,200]
        *      ]
        * */
        line = line.map(a => [a]);
        const mxLine = math.matrix(line);
        if (mxLine._size[0] != this.mxA._size[0])
            throw '열의 갯수가 맞지 않습니다.';
        this.mxA = math.concat(this.mxA, mxLine, 1);
    };
    this.getNumberOfColumns = function () {
        return {mxA:this.mxA._size[1], mxB:this.mxB._size[1]}
    };
    this.getNumberOfRows = function () {
        return {mxA:this.mxA._size[0], mxB:this.mxB._size[0]}
    };
    this.getMatrices = function () {
        return {mxA: this.mxA, mxB: this.mxB};
    };

    this.defineDecisionVariables = function () {
        const currentSpcData = manager.currentSpc;
        const numSection = manager.numSections;
        const forManPlan = manager.forManPlan;



    }
}

//TODO 수종별 면적당 재적

var lp = new LinearProgramming();


/**********************************************************************
 *                       Accounting Variables
 **********************************************************************/
const TOTAL_PERIOD = 15;


var area_section_spc_period;
var thinning_spc_period;
var clearcut_spc_period;
var area_age_period;
var thinningP_period;
var clearcutP_period;
var combinedP_period;
var carbon_period;
var water_period;
var labor_period;

var Z;

function defineLPVariables() {
    A = math.zeros(manager.numSections.length, manager.spcClasses.length, TOTAL_PERIOD);
}


/**********************************************************************
 *                        Decision Variables
 **********************************************************************/



/*************************************************************************************************
 *                                       Constraints
 *************************************************************************************************/


/*************************************************************************************************
 *                                    Decision Variables
 *************************************************************************************************/








function getCurrentSpc() {

}





// getThinningScenario();


//volume_spc = math.zeros(manager.spcClasses.length, TOTAL_PERIOD);
//area_section_spc_period = math.zeros(manager.numSections.length, manager.spcClasses.length, TOTAL_PERIOD);
//area_age_period = math.zeros(manager.numSections.length, TOTAL_PERIOD, TOTAL_PERIOD); // 면적은 일정해야 하니까?
//TODO 이게 뭐야? 영급별 분기별 면적이 area_age_period
//thinning_spc_period = math.zeros(manager.spcClasses.length, TOTAL_PERIOD);
//clearcut_spc_period = math.zeros(manager.spcClasses.length, TOTAL_PERIOD);
//thinningP_period = math.zeros(TOTAL_PERIOD);
//clearcutP_period = math.zeros(TOTAL_PERIOD);
//combinedP_period = math.zeros(TOTAL_PERIOD);
//carbon_period = math.zeros(TOTAL_PERIOD);
//water_period = math.zeros(TOTAL_PERIOD);
//labor_period = math.zeros(TOTAL_PERIOD);