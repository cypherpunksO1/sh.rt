async function cutLink() {
    let link = document.getElementById('link').value;
    document.getElementById('link').value = "";

    let response = await fetch('/api/v1/cutLink/', {
        method: 'POST',
        headers: {
            'X-CSRFToken': getCookie('csrftoken'),
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            'link': link,
        })
    });
    let result = await response.json();

    if (result['error'] === false) {
        let link = getSitePath() + result['data']['key'];
        document.getElementById('last-link').style.display = 'block';
        document.getElementById('old-link').innerHTML = result['data']['link'];
        document.getElementById('new-link').innerHTML = link;

        document.getElementById('copy').onclick = function () {
            copyText(link);
        }
        document.getElementById('link-statistics').onclick = function() {
            openUrl(result['data']['key'] + '/statistics/', true);
        }
    } else {
        showNotification(result['link'][0])
    }
}

async function updateStatistics() {
    let response = await fetch('/api/v1/allStatistics/', {
        method: 'GET',
        headers: {
            'X-CSRFToken': getCookie('csrftoken'),
            'Content-Type': 'application/json'
        }
    });
    let result = await response.json();

    if (result['error'] === false) {
        document.getElementById('links-count').innerHTML = result['data']['count'];
    }
}


async function setLinkPassedGraphic(key) {
    let response = await fetch('/api/v1/link/' + key + '/passed/', {
        method: 'GET',
        headers: {
            'X-CSRFToken': getCookie('csrftoken'),
            'Content-Type': 'application/json'
        }
    });
    let result = await response.json();

    console.log(result);

    let dates = new Array();
    let colors = new Array();

    for (date in result['data']) {
        dates.push(date);
        colors.push("#9664fa");
    }

    let passed = new Array();

    for (date in result['data']) {
        passed.push(result['data'][date]);
    }

    console.log(passed);


    new Chart(document.getElementById("bar-chart"), {
        type: 'bar',
            data: {
                labels: dates,
                datasets: [
                    {
                        label: "Переходов по ссылке",
                        backgroundColor: colors,
                        data: passed
                    }
                ]
            },
            options: {
            legend: { display: false },
        }
    });
}

async function setLinkStatistics(key) {
    let response = await fetch('/api/v1/link/' + key, {
        method: 'GET',
        headers: {
            'X-CSRFToken': getCookie('csrftoken'),
            'Content-Type': 'application/json'
        }
    });
    let result = await response.json();

    if (result['error'] === false) {
        console.log(result);

        let link = getSitePath() + key
        link = link.slice(0, 25) + '...';

        document.getElementById('link').innerHTML = link;
        document.getElementById('passed').innerHTML = result['data']['passed'];
        document.getElementById('uniquePassed').innerHTML = result['data']['unique_passed'];

        setLinkPassedGraphic(key);
    }
}

