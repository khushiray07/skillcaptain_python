let btn = document.getElementById("locateBtn");

btn.addEventListener("click", function() {
    if ('geolocation' in navigator) {
        navigator.geolocation.getCurrentPosition(position => {
            const { latitude, longitude } = position.coords;
            const message = `My Location:\nLatitude: ${latitude.toFixed(4)}, Longitude: ${longitude.toFixed(4)}`;

            document.getElementById("output").innerText = message;

            if ('Notification' in window) {
                Notification.requestPermission().then(permission => {
                    if (permission === 'granted') {
                        new Notification('My Location', {
                            body: message
                        });
            }
            });
        }
    });
}
});

