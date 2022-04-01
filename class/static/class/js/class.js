$(function () {
    // Datatable instance
    if ($("#class-list").length) {
        $("#class-list").DataTable({
            "responsive": true,
            "lengthChange": false,
            "autoWidth": false,
            "buttons": ["copy", "csv", "excel", "pdf", "print", "colvis"]
        }).buttons().container().appendTo('#class-list_wrapper .col-md-6:eq(0)')
    }

    let datepicker_options = {
        format: 'DD/MM/YYYY',
        date: moment().format()
    }

    //Date picker
    $('#initial-date').datetimepicker(datepicker_options)
    $('#final-date').datetimepicker(datepicker_options)

    $('#search-zipcode').click(function (e) {
        e.preventDefault()
        let zipcode = $('#class-zipcode').val()

        if (/^[0-9]{8}$/.test(zipcode)) address_consult(zipcode)
        else alert('Digite um CEP válido!')
    })
})

function address_consult(cep) {
    $.getJSON("https://viacep.com.br/ws/" + cep + "/json/?callback=?", function (dados) {
        if (!("erro" in dados)) {
            //Atualiza os campos com os valores da consulta.
            $("#class-address").val(dados.logradouro)
            $("#class-neighbourhood").val(dados.bairro)
            $("#class-city").val(dados.localidade)
        } else {
            //CEP pesquisado não foi encontrado.
            alert("CEP não encontrado.")
        }
    })
}

function clear_class_form() {
    $('#class-form input').each(
        (index, element) => {
            $(element).val('')
        })
}