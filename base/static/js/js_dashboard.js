// Set new default font family and font color to mimic Bootstrap's default styling
//Chart.defaults.global.defaultFontFamily = 'Nunito', '-apple-system,system-ui,BlinkMacSystemFont,"Segoe UI",Roboto,"Helvetica Neue",Arial,sans-serif';
//Chart.defaults.global.defaultFontColor = '#858796';

// Area Chart Example
color=['#4e73df', '#1cc88a', '#36b9cc','#2e59d9', '#17a673', '#2c9faf','green',"#4e73df","#2e59d9","#2e59d9","grey"]
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
                    gerarArea(data)
                    console.log(data);
                } else {
                    $("#modal-object").html(data.html_form);

                }
            }
           });
}




function gerarArea(dados){
var chr = $('#myChart_'+ dados.id);
var myLineChart = new Chart(chr, {
  type: 'line',
  data: {
    labels: dados.x,
    datasets: [{
      label: "Dados ",
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
      data: dados.y,
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
            return value;
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
          return datasetLabel +''+ tooltipItem.yLabel;
        }
      }
    }
  }
});}



function solicitarBar (id) {
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
                    gerarBar(data)
                    console.log(data);
                } else {
                    $("#modal-object").html(data.html_form);

                }
            }
           });
}


function gerarBar(dados){
var chr = $('#myChart_'+ dados.id);
var myBarChart = new Chart(chr, {
  type: 'bar',
  data: {
    labels: dados.x,
    datasets: [{
      label: "Dados ",
//      backgroundColor: ['green',"#4e73df","#2e59d9","#2e59d9","grey"],
      backgroundColor: color,
      hoverBackgroundColor: ["#2e59d9","#2e59d9"],
      borderColor: ["#4e73df"],
      data: dados.y,
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
          unit: 'month'
        },
        gridLines: {
          display: false,
          drawBorder: false
        },
        ticks: {
          maxTicksLimit: 6
        },
        maxBarThickness: 25,
      }],
      yAxes: [{
        ticks: {
          min: 0,

          maxTicksLimit: 5,
          padding: 10,
          // Include a dollar sign in the ticks
          callback: function(value, index, values) {
            return '' + value;
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
      titleMarginBottom: 10,
      titleFontColor: '#6e707e',
      titleFontSize: 14,
      backgroundColor: "rgb(255,255,255)",
      bodyFontColor: "#858796",
      borderColor: '#dddfeb',
      borderWidth: 1,
      xPadding: 15,
      yPadding: 15,
      displayColors: false,
      caretPadding: 10,
      callbacks: {
        label: function(tooltipItem, chart) {
          var datasetLabel = chart.datasets[tooltipItem.datasetIndex].label || '';
          return datasetLabel + '' + (tooltipItem.yLabel);
        }
      }
    },
  }
});


}

function solicitarPie (id) {
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
                    gerarPie(data)
                    console.log(data);
                } else {
                    $("#modal-object").html(data.html_form);

                }
            }
           });
}


function gerarPie(dados){
var chr = $('#myChart_'+ dados.id);

var myPieChart = new Chart(chr, {
  type: 'doughnut',
  data: {
    labels: dados.x,
    datasets: [{
      data: dados.y,
      backgroundColor: ['#4e73df', '#1cc88a', '#36b9cc','#2e59d9', '#17a673', '#2c9faf'],
      backgroundColor: color,
      hoverBackgroundColor: ['#2e59d9', '#17a673', '#2c9faf','#2e59d9', '#17a673', '#2c9faf'],
      hoverBorderColor: "rgba(234, 236, 244, 1)",
    }],
  },
  options: {
    maintainAspectRatio: false,
    tooltips: {
      backgroundColor: "rgb(255,255,255)",
      bodyFontColor: "#858796",
      borderColor: '#dddfeb',
      borderWidth: 1,
      xPadding: 15,
      yPadding: 15,
      displayColors: false,
      caretPadding: 10,
    },
    legend: {
      display: false
    },
    cutoutPercentage: 80,
  },
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
 lista1 ='';
 lista1+='<div class=" table-responsive table "><table class="table table-bordered"  width="100%" cellspacing="0"><thead><tr >'
    console.log(dados.x);
    for (i = 0; i < dados.x.length ;i=i+1){
        lista1+="<th >"+ dados.x[i]+"</th>"
     }

    lista1+="</tr ></thead><tbody>"
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