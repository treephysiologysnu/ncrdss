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


var seed = 1;
function resetSeed() {
    seed = 1;
}


function random() {
    var x = Math.sin(seed++) * 10000;
    return x - Math.floor(x);
}


var dynamicColors = function() {
    var r = Math.floor(random() * 255);
    var g = Math.floor(random() * 255);
    var b = Math.floor(random() * 255);
    return "rgba(" + r + "," + g + "," + b + ", 0.6)";
};


var format3DigitWithCommas = function (x) {
    var parts = x.toString().split(".");
    parts[0] = parts[0].replace(/\B(?=(\d{3})+(?!\d))/g, ",");
    return parts.join(".");
}