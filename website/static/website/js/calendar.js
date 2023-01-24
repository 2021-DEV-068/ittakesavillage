document.addEventListener('DOMContentLoaded', function() {
    const calendarEl = document.getElementById('calendar');
    if (calendarEl !== null){
        const eventsUrl = calendarEl.dataset.eventsUrl;
        const calendar = new FullCalendar.Calendar(calendarEl, {
            initialView: 'timeGridWeek',
            themeSystem: 'bootstrap5',
            height: "auto",
            allDaySlot: false,
            slotMinTime: '6:00',
            slotMaxTime: '20:00',
            nowIndicator: true,
            events: eventsUrl,
            headerToolbar: {
                end: 'prev,next'
            }
        });
        calendar.render();
    }
});

