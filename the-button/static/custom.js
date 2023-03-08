// Allow only one 'live' round.
function onlyAllowOneActive(id) {
    var elements = document.getElementsByClassName("round-live");
    console.log(elements);
    for (i in elements) {
        elements[i].checked = false;
    }
    document.getElementById(id).checked = true;
}

// Show the 'New Round' form.
function showNewRoundForm() {
    // This is abrupt. Maybe use: https://stackoverflow.com/a/40483232/100134
    document.getElementById('new-row').style.display = "table-row";
    document.getElementById('add-round-button').style.display = "none";
}
