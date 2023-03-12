// Allow only one 'live' round.
function onlyAllowOneLive(id) {
    var elements = document.getElementsByClassName("round-live");
    for (i in elements) {
        elements[i].checked = false;
    }
    document.getElementById(id).checked = true;
}

// Allow up to one round to be accepting votes.
function onlyAllowOneAccepting(id) {
    check_me = true;
    if (document.getElementById(id).checked === false) {
        check_me = false;
    }
    var elements = document.getElementsByClassName("round-accepting");
    for (i in elements) {
        elements[i].checked = false;
    }
    if (check_me) {
        document.getElementById(id).checked = true;
    }
}

// Show the 'New Round' form.
function showNewRoundForm() {
    // This is abrupt. Maybe use: https://stackoverflow.com/a/40483232/100134
    document.getElementById('new-row').style.display = "table-row";
    document.getElementById('add-round-button').style.display = "none";
}
