function removeColor() {
    select = document.getElementById("colorSelect");
    
    select.remove(select.value);

    if (select.length == 0) {
        alert("No more items to remove");
    }
}