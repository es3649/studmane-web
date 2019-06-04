
var mischeifManaged = false;
    
function doMischief() {
    if (!mischeifManaged) {
        document.getElementById("mischiefBox").style.display = "block";
        mischeifManaged = true;
    } else {
        document.getElementById("mischiefBox").style.display = "none";
        mischeifManaged = false;
    }
}
