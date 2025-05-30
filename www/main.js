$(document).ready(function () {


    $('.text').textillate({
        loop: true,
        sync: true,
        in: {
            effect: 'bounceIn',
        },
        out: {
            effect: 'bounceOut',
        }
    });

    // siri configuration
    var siriWave = new SiriWave({
        container: document.getElementById("siri-container"),
        width: 640,
        height: 200,
        style: "ios9",
        amplitude: "1",
        speed: "0.30",
        autostart: true,
    });

    // siri text animation
    $('.siri-message').textillate({
        loop: true,
        sync: true,
        in: {
            effect: 'fadeInUp',
            sync: true,
        },
        out: {
            effect: 'fadeOutUp',
            sync: true,
        }
    });

    //mic button click event
    $('#MicBtn').click(function () {
        eel.playAssisteantSound()
        $("#Oval").attr("hidden", true);
        $("#SiriWave").attr("hidden", false);
        eel.allCommands();
    });

    //hodward key to activate the assistant
    function doc_keyUp(e) {
        if (e.key === 'j' && e.metaKey) {
            eel.playAssisteantSound()
            $("#Oval").attr("hidden", true);
            $("#SiriWave").attr("hidden", false);
            eel.allCommands();
        }
    }
    document.addEventListener('keyup', doc_keyUp, true);

    function PlayAssistant(message) {

        if (message != "") {

            $("#Oval").attr("hidden", true);
            $("#SiriWave").attr("hidden", false);
            eel.allCommands(message);
            $("#chatbox").val("")
            $("#MicBtn").attr("hidden", false);
            $("#SendBtn").attr("hidden", true);

        }
    }

    function showHideButton(message) {
        if (message.length == 0) {
            $("#MicBtn").attr("hidden", false);
            $("#SendBtn").attr("hidden", true);
        }
        else {
            $("#MicBtn").attr("hidden", true);
            $("#SendBtn").attr("hidden", false);
        }
    }

    $("#chatbox").keyup(function (e) {
        let message = $("#chatbox").val();
        showHideButton(message);

        // Submit message when Enter key is pressed
        if (e.keyCode === 13) {
            PlayAssistant(message);
        }
    });

    $("#SendBtn").click(function () {

        let message = $("#chatbox").val();
        PlayAssistant(message);
    });

    $("#chatbox").keypress(function (e) {
        key = e.which;

        if (key == 13) {
            let message = $("#chatbox").val();
            PlayAssistant(message)
        }
    });

});