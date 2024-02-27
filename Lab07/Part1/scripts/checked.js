function getChecked() {
    count = 0
    nodes = document.querySelectorAll("input");
    for (i = 0; i < nodes.length; i++) {
        if (nodes[i].checked == true) {
            count ++;
        } 
    }
    
    p = document.getElementsByTagName("p");
    if (count != 0) {
        p[0].innerHTML = count + " are checked.";
    }
    else {
        p[0].innerHTML = "";
    }
}