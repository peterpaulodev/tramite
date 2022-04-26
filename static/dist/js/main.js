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
});