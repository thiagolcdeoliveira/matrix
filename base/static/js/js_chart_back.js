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
//
//x =['Red', 'Blue', 'Yellow', 'Green', 'Purple', 'Orange'];
//y =[12, 19, 3, 5, 2, 3];
//id = 1;
//dados = {'x':x,'y':y, 'id':id};

//$("#js-create-graph").click(loadForm(dados));
//$("#js-create-graph").click(loadForm(dados));
//$(".js-create-graph").click(solicitar());
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
   var char = new Chart(chr, {
    type: dados.tipo,
    data: {
        labels: dados.x,
        datasets: [{
            label: dados.titulo,
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
 lista1 ='';
 lista1+="<tr >"
    console.log(dados.x);
    for (i = 0; i < dados.x.length ;i=i+1){
        lista1+="<th >"+ dados.x[i]+"</th>"
     }
//      lista1+="</tr><tr>"

//lista2='';
    lista1+="</tr >"
     for (i = 0; i < dados.y.length ;i=i+1){

     lista2='';
     lista2+="<tr >"
          for (ii = 0; ii < dados.y[i].length ;ii=ii+1){
          lista2+="<td>"+dados.y[i][ii]+" </td>"
       }
       lista2+="</tr>";
       lista1+=lista2;
       }

           $('#tabela_'+ dados.id).html(lista1);
          console.log(lista1);

}
function lista (dados) {
    var chr = $('#lista_'+ dados.id);
    var lista1='';
    for (i = 0; i < dados.valor.length ;i=i+1){
//     lista="<li>"+dados.valor+"<li>"
//     lista="<li>"+ dados.valor[i]+"<li>"
//     lista+="<li>"+ dados.valor[i]+"<li>"
     lista1+="<li class='item' >"+ dados.valor[i]+"<li>"
//         console.log( $('#lista_'+ dados.valor[i]));
//         console.log(  dados.valor[i]);

     }
//    $('#lista_'+ dados.id).html( dados.valor);
//     $('#lista_titulo_'+ dados.id).html(dados.titulo);
//     $('#lista_'+ dados.id).html(dados.titulo);
     $('#lista_'+ dados.id).html(lista1);
     console.log(lista1)

//    console.log( $('#lista_'+ dados.id));
//    console.log( $('#lista_'+ lista));
//    console.log( $('#lista_'+ dados.titulo));

}


/*

function EnviarMensagem (id) {

//          var form = $(this);
//        e.preventDefault();
//        form = $(this)
//        preventDefault();
        var form = $(this);

        var formdata = new FormData(this);
//         $("#load-modal").addClass("active");
//         $("#submit_json").prop("disabled", true);
        console.log(form.getAll);

        $.ajax({
            url: form.attr("action"),
            data: formdata,
            type: form.attr("method"),
            dataType: 'json',
            contentType: false,
            processData: false,
            cache: false,

              timeout: 600000,
                          mimeType: "multipart/form-data",
//                          async: true

            success: function (data) {

                if (data.form_is_valid) {
                    mensagem(data);
                    }
                } else {
//                    $("#modal-object").modal("hide");
//                    $("#modal-object").html(data.html_form);
//                    $("#modal-object").modal("show");
                }
            }

        });
        return false;
//    }
}


function mensagem (dados) {
    var chr = $('#mensagem');
//     $('#contador_'+ dados.id).html(dados.valor);
//     $('#contador_titulo_'+ dados.id).html( dados.titulo);
//     console.log( $('#contador_'+ dados.id));

        $('#mensagem').html(dados.html_form);
        console.log(dados.html_form);
}*/