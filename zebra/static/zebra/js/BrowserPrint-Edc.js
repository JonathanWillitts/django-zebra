var selected_device;
function setup() {
    // Get the default device from the application.
    BrowserPrint.getDefaultDevice("printer", function(device) {
        selected_device = device;

        // Display default device on page
        var default_device_display = document.getElementById("default-device-display");
        default_device_display.innerHTML = `${device.name} (${device.uid})`;
        default_device_display.className = "default-device-found";

    }, function(error) {
        alert(`Error getting default device, details: ${error}`);
    })
}

function getConfig() {
    BrowserPrint.getApplicationConfiguration(function(config){
        alert(`Config: ${JSON.stringify(config)}`)
    }, function(error) {
        alert(`Config error, details: ${JSON.stringify(new BrowserPrint.ApplicationConfiguration())}, error: ${error}`);
    })
}

function writeToSelectedPrinter(dataToWrite) {
    selected_device.send(dataToWrite, undefined, errorCallback);
}

var errorCallback = function(errorMessage) {
    alert("Error, details: " + errorMessage);
}

window.onload = setup;
