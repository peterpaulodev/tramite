$(function () {
    $.extend($.validator.messages, {
        required: "Esse campo é obrigatório.",
        password: "Por favor, entre com uma senha válida",
        remote: "Por favor, entre com esse campo válido.",
        email: "Por favor, entre com um email válido.",
        url: "Por favor, entre com uma URL válida.",
        date: "Por favor, entre com uma data válida.",
        dateISO: "Please enter a valid date (ISO).",
        number: "Por favor, entre com um número válido.",
        digits: "Por favor, entre somente com digitos.",
        equalTo: "Os valores não coincidem.",
        accept: "Please enter a value with a valid extension.",
        maxlength: $.validator.format("O valor deve ter no máximo {0} caracteres."),
        minlength: $.validator.format("O valor deve ter no minímo {0} caracteres."),
        rangelength: $.validator.format("O valor deve ter entre {0} e {1} caracteres."),
        range: $.validator.format("O valor deve estar entre {0} e {1}."),
        max: $.validator.format("O valor deve ter no máximo {0}."),
        min: $.validator.format("O valor deve ter no minímo {0}.")
    });

    var custom_messages = {
        password: {
            required: "Por favor, entre com uma senha válida",
            minlength: "Sua senha deve ter no mínimo 5 caracteres"
        },
    }

    $('form:not(.files)').validate({
        rules: {
            email: {
                required: true,
                email: true,
            },
            password: {
                required: true,
                minlength: 5
            },
            terms: {
                required: true
            },
        },
        messages: custom_messages,
        errorElement: 'span',
        errorPlacement: function (error, element) {
            error.addClass('invalid-feedback');
            element.closest('.form-group').append(error);
        },
        highlight: function (element, errorClass, validClass) {
            $(element).addClass('is-invalid');
        },
        unhighlight: function (element, errorClass, validClass) {
            $(element).removeClass('is-invalid');
        }
    });

    bsCustomFileInput.init();

    $('#student-cpf').mask('000.000.000-00');
});


function address_consult(cep) {
    $.getJSON("https://viacep.com.br/ws/" + cep + "/json/?callback=?", function (dados) {
        if (!("erro" in dados)) {
            //Atualiza os campos com os valores da consulta.
            $("[id$='address']").val(dados.logradouro)
            $("[id$='neighbourhood']").val(dados.bairro)
            $("[id$='city']").val(dados.localidade)
            $("[id$='uf']").val(dados.uf)
        } else {
            //CEP pesquisado não foi encontrado.
            alert("CEP não encontrado.")
        }
    })
}

$('#search-zipcode').click(function (e) {
    e.preventDefault()
    let zipcode = $("[id$='zipcode']").val()

    if (/^[0-9]{8}$/.test(zipcode)) address_consult(zipcode)
    else alert('Digite um CEP válido!')
})

$('#administrator-login').click(function (e) {
    $('#selection-card').hide()
    $('#login-card').show()
})

$('.student-login').click(function (e) {
    $('#selection-card').hide()
    $('#student-card').show()
})

