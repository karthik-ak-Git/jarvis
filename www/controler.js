$(document).ready(function () {
    //display message from python to html page
    eel.expose(DisplayMessage)
    function DisplayMessage(message) {

        $(".siri-message li:first").text(message);
        $(".siri-message").textillate('start');
    }
    //display hood

    eel.expose(ShowHood)
    function ShowHood() {
        $("#Oval").attr("hidden", false);
        $("#SiriWave").attr("hidden", true);
    }

    eel.expose(senderText)
    function senderText(message) {
        var charBox = document.getElementById("chat-canvas-body");
        if (message.trim() !== "") {
            charBox.innerHTML += `<div class="row justify-content-end mb-4">
                <div class="width-size">
                <div class="sender_message">${message}</div>
                </div>`;

            charBox.scrollTop = charBox.scrollHeight;
        }
    }
    eel.expose(recieverText)
    function recieverText(message) {
        var charBox = document.getElementById("chat-canvas-body");
        if (message.trim() !== "") {
            charBox.innerHTML += `<div class="row justify-content-start mb-4">
                <div class="width-size">
                <div class="receiver_message">${message}</div>
                </div>
                </div>`;

            charBox.scrollTop = charBox.scrollHeight;
        }
    }


});