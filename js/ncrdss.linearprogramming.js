/*************************************************************************************************
 *                                         Define Variables
 *************************************************************************************************/
/**********************************************************************
 *                         Define Constants
 **********************************************************************/

//TODO 수종별 면적당 재적



/**********************************************************************
 *                       Accounting Variables
 **********************************************************************/
const TOTAL_PERIOD = 15;
var A = {
    // {section:##, species:##, period:##}: {age:##, area:##},
}; // Main Accounting Variable (면적)



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
    A = math.zeros(manager.numSection.length, manager.spcClasses.length, TOTAL_PERIOD);
}
manager.spcClasses.map(a => a.species);


/**********************************************************************
 *                        Decision Variables
 **********************************************************************/
var X_section_target_period = math.zeros(manager.numSection.length, manager.spcClasses.length, TOTAL_PERIOD);




/*************************************************************************************************
 *                                       Constraints
 *************************************************************************************************/


/*************************************************************************************************
 *                                    Decision Variables
 *************************************************************************************************/








function getCurrentSpc() {

}





// getThinningScenario();




const spcList = managger.spcClasses.map(a => a.species);


volumn_spc = math.zeros(manager.spcClasses.length, TOTAL_PERIOD);
area_section_spc_period = math.zeros(manager.numSection.length, manager.spcClasses.length, TOTAL_PERIOD);
area_age_period = math.zeros(manager.numSection.length, TOTAL_PERIOD, TOTAL_PERIOD); // 면적은 일정해야 하니까?
//TODO 이게 뭐야? 영급별 분기별 면적이 area_age_period
thinning_spc_period = math.zeros(manager.spcClasses.length, TOTAL_PERIOD);
clearcut_spc_period = math.zeros(manager.spcClasses.length, TOTAL_PERIOD);
thinningP_period = math.zeros(TOTAL_PERIOD);
clearcutP_period = math.zeros(TOTAL_PERIOD);
combinedP_period = math.zeros(TOTAL_PERIOD);
carbon_period = math.zeros(TOTAL_PERIOD);
water_period = math.zeros(TOTAL_PERIOD);
labor_period = math.zeros(TOTAL_PERIOD);