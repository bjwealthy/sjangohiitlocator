
function getLocation(username) {
    if (!username || username.length < 3) {
        alert('please enter a valid username')
        return
    }
    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(showPosition);
    } else {
        console.log("Geolocation is not supported by this browser.")
    }
    function showPosition(position) {
        console.log(position.coords.latitude)
        console.log(position.coords.longitude)
        document.getElementById('text').value = `[{lat: ${position.coords.latitude},long: ${position.coords.longitude}, date: ${Number(new Date())}}]`
        document.getElementById('submitAA').click();
    
    }
}


