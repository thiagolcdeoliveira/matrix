
$(function () {

    /* Functions */

    var loadForm = function () {
        var btn = $(this);
        $.ajax({
            url: btn.attr("data-url"),
            type: 'get',
            dataType: 'json',
            beforeSend: function () {
                $("#modal-object").html("");
            },
            success: function (data) {
                console.log(data);
                $("#modal-object").html(data.html_form);
                $("#modal-object").modal("show");
            }
        });
    };

    var saveForm = function () {
        var form = $(this);
        var formdata = new FormData(this);
        $("#load-modal").addClass("active");
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
            success: function (data) {
                if (data.form_is_valid) {
                    $("#modal-object").modal("hide");
                    if (data.sucesso){
                        $('#'+data.campo_alterar).append('<option value =' + data.id_alterar + '>' + data.nome_alterar + '</option>');
                        $('#'+data.campo_alterar).val(data.id_alterar).attr('selected','selected');
                    }
                } else {
                    $("#load-modal").removeClass("active");
                    $("#modal-object").html(data.html_form);
                    $("#modal-object").modal("show");
                }
            }

        });
        return false;
    };


    $(".js-create-object").click(loadForm);
    $("#modal-object").on("submit", ".js-object-create-form", saveForm);


    var loadFormgrafico = function () {
            var btn = $(this);
             var form = $('#formgrafico');
             var formdata = {'tipo_grafico':$('#id_tipo_grafico').val(),'nome': $('#id_nome').val(),'consulta':$('#id_consulta').val()};
             console.log(formdata);
//            var formdata = new FormData('#formgrafico');
             $.ajax({
                url: btn.attr("data-url"),
                type: 'get',
                data: formdata,
                dataType: 'json',
                beforeSend: function () {
                    $("#modal-object").html("");
                },
                success: function (data) {
                    console.log(data);
                    $("#modal-object").html(data.html_form);
                    $("#modal-object").modal("show");
                }
            });
        };
    $(".js-create-object-grafico").click(loadFormgrafico);

});



function adicionarServidor(id,username,campo_alterar){

 $("#modal-object").modal("hide");

 $('#'+campo_alterar).append('<option value =' + id + '>' + username + '</option>');
 $('#'+campo_alterar).val(id).attr('selected','selected');

}
