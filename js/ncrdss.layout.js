const body = document.body;
const collapseBtn = document.querySelector(".admin-menu .collapse-btn");
const collapsedClass = "collapsed";

collapseBtn.addEventListener("click", function() {
    this.getAttribute("aria-expanded") == "true"
        ? this.setAttribute("aria-expanded", "false")
        : this.setAttribute("aria-expanded", "true");
    this.getAttribute("aria-label") == "collapse menu"
        ? this.setAttribute("aria-label", "expand menu")
        : this.setAttribute("aria-label", "collapse menu");
    body.classList.toggle(collapsedClass);
});




var addr_complete = false;
var base_complete = false;
var spcClass_complete = false;
var currentSpc_complete = false;
var forManPlan_complete = false;


const style_red = "2px solid red";
var style_orig = '1px solid #ccc';

function setCellBorderColor(table, style) {
    var numCol = table.colgroup.length;
    var numRow = table.rows.length;
    var dictObj = {};
    var cellName;

    for (var i=0;i<numCol;i++) {
        for (var j=0;j<numRow;j++) {
            cellName = String.fromCharCode(i+'A'.charCodeAt(0)) + String(j+1);
            dictObj[cellName] = new Array();
            if (i==0)
                dictObj[cellName].push('border-left: ' + style);
            if (i==numCol-1)
                dictObj[cellName].push('border-right: ' + style);
            if (j==0)
                dictObj[cellName].push('border-top: ' + style);
            if (j==numRow-1)
                dictObj[cellName].push('border-bottom: ' + style);
        }
    }
    var propObj = {};
    for (key of Object.keys(dictObj)) {
        //console.log(dictObj[key])
        if (dictObj[key].length == 0)
            continue;
        var propString = "";
        for (const property of dictObj[key]) {
            propString += property + ';'
        }
        propObj[key] = propString;
    }
    table.setStyle(propObj);
}

function updateAddressInput() {
    if (addr_complete)
        return;
    addr_complete = true;
    updateBaseInput(false);
}

function updateBaseInput(completed) {
    if (completed)
        setCellBorderColor(table_base, style_orig)
    else {
        setCellBorderColor(table_base, style_red)
        /*table_base.setStyle({
            A1:'border-left: ' + style_red + '; border-top: ' + style_red + '; border-bottom: ' + style_red,
            B1:'border-top: ' + style_red + '; border-bottom: ' + style_red,
            C1:'border-top: ' + style_red + '; border-bottom: ' + style_red,
            D1:'border-right: ' + style_red + '; border-top: ' + style_red + '; border-bottom: ' + style_red,
        });*/
    }
}