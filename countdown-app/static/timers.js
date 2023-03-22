async function refresh_timer_data() {
    let url = 'http://127.0.0.1:5000/live/room-timers';
    let timer_data = await (await fetch(url)).json();
    console.log(timer_data);

    // Loop through all the timers, updating their current time.
    const timers = document.querySelectorAll(".timer");

    // Add 'room-time-expired' class if time_remaining is 0 or 0:00.
}

// Every second, update all the timers on the page.
// TODO - ONLY DO THIS ON THE TIMERS PAGE!
setInterval(function(){
    // Retrieve latest timer info from API.
    refresh_timer_data();
}, 1000);

// TODO REMOVE THIS CODE ONCE I HAVE THE INTERVAL WORKING!
function countdown(timer) {
    // If no timer_id, then set up the countdown.
    if (typeof timer === 'undefined') {
        const timers = document.querySelectorAll(".timer");
        timers.forEach((timer) => {
          time = timer.innerText;
          timeArray = time.split(':');
          seconds = timeToSeconds(timeArray);

          if (seconds == '') {
              temp = document.getElementById(timer.id);
              temp.innerHTML = "0:00";
              temp.classList.add("room-time-expired");

              return;
          }
          seconds--;
          temp = document.getElementById(timer.id);
          temp.innerHTML= secondsToTime(seconds);
          one_second_timeout = setTimeout(countdown, 1000, timer);
        });
    }
    else {
        time = timer.innerText;
        timeArray = time.split(':');
        seconds = timeToSeconds(timeArray);

        if (seconds == '') {
            temp = document.getElementById(timer.id);
            temp.innerHTML = "00:00";
            temp.classList.add("room-time-expired");

            return;
        }
        seconds--;
        temp = document.getElementById(timer.id);
        temp.innerHTML= secondsToTime(seconds);
        one_second_timeout = setTimeout(countdown, 1000, timer);

        // TODO - Use AJAX request to get updated timer data every second?!? Or
        // maybe every 5 seconds? Every 10 seconds?
    }
}

function timeToSeconds(timeArray) {
    var minutes = (timeArray[0] * 1);
    var seconds = (minutes * 60) + (timeArray[1] * 1);
    return seconds;
}

function secondsToTime(secs) {
    var hours = Math.floor(secs / (60 * 60));
    hours = hours < 10 ? '0' + hours : hours;
    var divisor_for_minutes = secs % (60 * 60);
    var minutes = Math.floor(divisor_for_minutes / 60);
    var divisor_for_seconds = divisor_for_minutes % 60;
    var seconds = Math.ceil(divisor_for_seconds);
    seconds = seconds < 10 ? '0' + seconds : seconds;
    return  minutes + ':' + seconds;
}

countdown();
