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
const style_orig = "1px solid #ccc";
const style_bg_red = "rgba(255,0,0,0.1)"
const style_bg_orig = "rgb(255,255,255)"

function setBgColor(table, style) {
    var numCol = table.colgroup.length;
    var numRow = table.rows.length;
    var dictObj = {};
    var cellName;

    for (var i=0;i<numCol;i++) {
        for (var j=0;j<numRow;j++) {
            cellName = String.fromCharCode(i+'A'.charCodeAt(0)) + String(j+1);
            dictObj[cellName] = new Array();
            dictObj[cellName].push('background-color: ' + style);
        }
    }
    var propObj = {};
    for (key of Object.keys(dictObj)) {
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
        setBgColor(table_base, style_bg_orig);
        // setCellBorderColor(table_base, style_orig)
    else
        setBgColor(table_base, style_bg_red);
        // setCellBorderColor(table_base, style_red)
}