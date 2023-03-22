// See: https://stackoverflow.com/a/39835908/100134
const pluralize = (count, noun, suffix = 's') =>
  `${count} ${noun}${count !== 1 ? suffix : ''}`;

async function refresh_timer_data() {
    // TODO: Change this before pushing to production!
    let url = 'http://127.0.0.1:5000/live/room-timers';
    let timer_data = await (await fetch(url)).json();

    // Loop through all the timers, updating their current time.
    const timers = document.querySelectorAll(".timer");
    timers.forEach((timer) => {
        var timer_room_id = timer.id.slice(6);
        // Why do I have to subtract 1? No clue. But it works, so it ships.
        var time_remaining = timer_data[timer_room_id - 1]['time_remaining'];
        var time_remaining_seconds = timer_data[timer_room_id - 1]['time_remaining_seconds'];
        var press_count = timer_data[timer_room_id - 1]['press_count']
        // If time is expired, add the room-time-expired class.
        if (time_remaining_seconds === 0) {
            // 3 parents up the heirarchy.
            timer.parentNode.parentNode.parentNode.classList.add('room-time-expired');
        }
        // Otherwise, make sure the room-time-expired class is not present.
        else if (time_remaining_seconds > 0) {
            timer.parentNode.parentNode.parentNode.classList.remove('room-time-expired');
        }
        // Update the time remaining.
        timer.innerHTML = time_remaining;
        // Update the press count (parent, then sibling, then span).
        timer.parentNode.nextElementSibling.querySelector('.press-count').innerHTML = pluralize(press_count, 'press', 'es');
    })
}

// Every second, update all the timers on the page.
setInterval(function(){
    refresh_timer_data();
}, 1000);
