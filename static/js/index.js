function type(element_id, source_text, speed) {
    var txt = source_text;
    var i = 0
    document.getElementById(element_id).innerHTML = txt.charAt(0);
    function typeWriter() {
        if (i < txt.length) {
            let text = document.getElementById(element_id).innerHTML;

            if (text.length >= 1) {
                text = text.slice(0, -1);
                text += txt.charAt(i)
                text += '#';
            } else {
                text += txt.charAt(i)
            }
            document.getElementById(element_id).innerHTML = text;
            i++;
            setTimeout(typeWriter, speed);
        } else {
            let text = document.getElementById(element_id).innerHTML;
            text = text.slice(0, -1);
            document.getElementById(element_id).innerHTML = text;
        }
    }
    typeWriter();
}


function getSitePath() {
    return window.location.protocol + window.location.host + '/'
}


function openUrl(url, targetBlank = false) {
    if (targetBlank) {
        window.open(url);
    } else {
        window.location.href = url;
    }
}


function copyText(text) {
    const textArea = document.createElement("textarea");
    textArea.value = text;
    document.getElementById('copy').appendChild(textArea);
    textArea.focus();
    textArea.select();
    document.execCommand('copy');
    document.getElementById('copy').removeChild(textArea);

    showNotification("Ссылка скопирована в буфер обмена.")
//    navigator.share({
//        url: link
//    }).then(function () {
//        ShowNotification('ссылка скопирована');
//    })
//    .catch(function () {
//        ShowNotification('ошибка копирования!');
//    })
}


function showNotification(text){
    document.getElementById('notification-message').innerHTML = text;
    let notification = document.getElementById('notification');
    notification.style.display = 'block';

    function notificationOpacity100() {
        notification.style.opacity = '100%';
    }

    setTimeout(notificationOpacity100, 300)
}

function hideNotification(){
    let notification = document.getElementById('notification');
    notification.style.opacity = '0';

    function notificationDisplayNone() {
        notification.style.display = 'none';
        document.getElementById('notification-message').innerHTML = "";
    }

    setTimeout(notificationDisplayNone, 300)
}

