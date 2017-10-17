Chart.defaults.global.responsive = false;
var ctx = document.getElementById('myChart').getContext('2d');
var myChart = new Chart(ctx, {
    type: 'pie',
    data: {
        labels : [{% for item in labels %}
                       "{{item}}",
                  {% endfor %}],
        datasets: [
            {
                label: [
                    {% for label in labels %}
                        "{{label}}",
                    {% endfor %}
                ],
                data: [
                    {% for value in values %}
                        {{value}},
                    {% endfor %}
                ],
                backgroundColor: [
                    "#ff0000","#0079bf","#DDA0DD","#85bb65","#daa520",
                    "#9b59b6","#f1c40f","#e74c3c","#34495e","#008080",
                    "#ffc0cb","#d3ffce","#ff7373","#ffa500","#e6e6fa",
                    "#2ecc71","#20b2aa","#c6e2ff","#008000"
                ]
            }
        ]
    }
});