//Chart.defaults.global.defaultFontFamily = 'Nunito', '-apple-system,system-ui,BlinkMacSystemFont,"Segoe UI",Roboto,"Helvetica Neue",Arial,sans-serif';
//Chart.defaults.global.defaultFontColor = '#858796';

$(function () {


  var loadForm = function (dados) {
//    var chr = document.getElementById('myChart').getContext('2d')
    var chr = $('#myChart'+ dados.id);
   var char = new Chart(chr, {
    type: 'bar',
    data: {
        labels: dados.x,
        datasets: [{
            label: '# of Votes',
            data: dados.y,
            borderWidth: 1
        }]
    },
    options: {
        scales: {
            yAxes: [{
                ticks: {
                    beginAtZero: true
                }
            }]
        }
    }
});

}


var solicitar = function () {

          var btn = $(this);
          console.log(btn);
//btn.attr("data-url")
        $.ajax({
            url: '/setor' ,
            data: '',
            type: 'get',
            dataType: 'json',
            contentType: false,
            processData: false,
            cache: false,
            success: function (data) {

                if (data.form_is_valid) {
                    loadForm(dados)
                } else {

                    $("#modal-object").html(data.html_form);

                }
            }
   });

}

$(".js-create-graph").click(solicitar());
});




function solicitar (id) {

           var btn = $(this);
           console.log(btn.attr('url-data'));
           $.ajax({
            url: '/grafico/gerar/ajax/'+id +"/",
            data: '',
            type: 'get',
            dataType: 'json',
            contentType: false,
            processData: false,
            cache: false,
            success: function (data) {

                if (data.form_is_valid) {
                    grafico(data)
                } else {

                    $("#modal-object").html(data.html_form);

                }
            }
           });

}

function grafico (dados) {
//    var chr = document.getElementById('myChart').getContext('2d')
    var chr = $('#myChart_'+ dados.id);
  console.log(chr);

var myLineChart = new Chart(chr, {
  type: 'line',
  data: {
    labels: ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"],
    datasets: [{
      label: "Earnings",
      lineTension: 0.3,
      backgroundColor: "rgba(78, 115, 223, 0.05)",
      borderColor: "rgba(78, 115, 223, 1)",
      pointRadius: 3,
      pointBackgroundColor: "rgba(78, 115, 223, 1)",
      pointBorderColor: "rgba(78, 115, 223, 1)",
      pointHoverRadius: 3,
      pointHoverBackgroundColor: "rgba(78, 115, 223, 1)",
      pointHoverBorderColor: "rgba(78, 115, 223, 1)",
      pointHitRadius: 10,
      pointBorderWidth: 2,
      data: [0, 10000, 5000, 15000, 10000, 20000, 15000, 25000, 20000, 30000, 25000, 40000],
    }],
  },
  options: {
    maintainAspectRatio: false,
    layout: {
      padding: {
        left: 10,
        right: 25,
        top: 25,
        bottom: 0
      }
    },
    scales: {
      xAxes: [{
        time: {
          unit: 'date'
        },
        gridLines: {
          display: false,
          drawBorder: false
        },
        ticks: {
          maxTicksLimit: 7
        }
      }],
      yAxes: [{
        ticks: {
          maxTicksLimit: 5,
          padding: 10,
          // Include a dollar sign in the ticks
          callback: function(value, index, values) {
            return (value);
          }
        },
        gridLines: {
          color: "rgb(234, 236, 244)",
          zeroLineColor: "rgb(234, 236, 244)",
          drawBorder: false,
          borderDash: [2],
          zeroLineBorderDash: [2]
        }
      }],
    },
    legend: {
      display: false
    },
    tooltips: {
      backgroundColor: "rgb(255,255,255)",
      bodyFontColor: "#858796",
      titleMarginBottom: 10,
      titleFontColor: '#6e707e',
      titleFontSize: 14,
      borderColor: '#dddfeb',
      borderWidth: 1,
      xPadding: 15,
      yPadding: 15,
      displayColors: false,
      intersect: false,
      mode: 'index',
      caretPadding: 10,
      callbacks: {
        label: function(tooltipItem, chart) {
          var datasetLabel = chart.datasets[tooltipItem.datasetIndex].label || '';
          return datasetLabel + ': $' + number_format(tooltipItem.yLabel);
        }
      }
    }


}});
}





function solicitarContador (id) {

           var btn = $(this);
           console.log(btn.attr('url-data'));
           $.ajax({
            url: '/contador/gerar/ajax/'+id +"/",
            data: '',
            type: 'get',
            dataType: 'json',
            contentType: false,
            processData: false,
            cache: false,
            success: function (data) {

                if (data.form_is_valid) {
//                alert("oi");
                    contador(data)
                } else {

                    $("#modal-object").html(data.html_form);

                }
            }
           });

}



function solicitarContador (id) {

           var btn = $(this);
           console.log(btn.attr('url-data'));
           $.ajax({
            url: '/contador/gerar/ajax/'+id +"/",
            data: '',
            type: 'get',
            dataType: 'json',
            contentType: false,
            processData: false,
            cache: false,
            success: function (data) {

                if (data.form_is_valid) {
//                alert("oi");
                    contador(data)
                } else {

                    $("#modal-object").html(data.html_form);

                }
            }
           });

}



function solicitarTabela (id) {

           var btn = $(this);
           console.log(btn.attr('url-data'));
           $.ajax({
            url: '/tabela/gerar/ajax/'+id +"/",
            data: '',
            type: 'get',
            dataType: 'json',
            contentType: false,
            processData: false,
            cache: false,
            success: function (data) {

                if (data.form_is_valid) {
//                alert("oi");
                    tabela(data)
                } else {

                    $("#modal-object").html(data.html_form);

                }
            }
           });

}




function solicitarLista (id) {

           var btn = $(this);
           console.log(btn.attr('url-data'));
           $.ajax({
            url: '/lista/gerar/ajax/'+id +"/",
            data: '',
            type: 'get',
            dataType: 'json',
            contentType: false,
            processData: false,
            cache: false,
            success: function (data) {

                if (data.form_is_valid) {

                    lista(data)
                } else {

                    $("#modal-object").html(data.html_form);

                }
            }
           });

}


function contador (dados) {
    var chr = $('#contador_'+ dados.id);
     $('#contador_'+ dados.id).html(dados.valor);
     $('#contador_titulo_'+ dados.id).html( dados.titulo);
     console.log( $('#contador_'+ dados.id));

}
function tabela (dados) {
    var chr = $('#tabela_'+ dados.id);
 lista1 ='<div class="table-responsive"><table class="table table-bordered"  width="100%" cellspacing="0"><thead><tr>';
 lista1+=""
    console.log(dados.x);
    for (i = 0; i < dados.x.length ;i=i+1){
        lista1+="<th >"+ dados.x[i]+"</th>"
     }

    lista1+="</tr > </thead><tbody>"
     for (i = 0; i < dados.y.length ;i=i+1){

     lista2='';
     lista2+="<tr >"
          for (ii = 0; ii < dados.y[i].length ;ii=ii+1){
          lista2+="<td>"+dados.y[i][ii]+" </td>"
       }
       lista2+="</tr></tbody>";
       lista1+=lista2;
       }

           $('#tabela_'+ dados.id).html(lista1);
          console.log(lista1);

}
function lista (dados) {
    var chr = $('#lista_'+ dados.id);
    var lista1='';
    for (i = 0; i < dados.valor.length ;i=i+1){

     lista1+="<li class='item' >"+ dados.valor[i]+"<li>"


     }

     $('#lista_'+ dados.id).html(lista1);
     console.log(lista1)

}