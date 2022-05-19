$(function () {
    // Datatable instance
    if ($("#student-list").length) {
        $("#student-list").DataTable({
            "responsive": true,
            "lengthChange": false,
            "autoWidth": false,
            "buttons": ["copy", "csv", "excel", "pdf", "print", "colvis"]
        }).buttons().container().appendTo('#student-list_wrapper .col-md-6:eq(0)')
    }

    $('[data-toggle="tooltip"]').tooltip()

    let datepicker_options = {
        format: 'DD/MM/YYYY',
        date: moment().format()
    }

    set_form_mask()

    //Date picker
    $('#student-birth_date').datetimepicker(datepicker_options)

    $('#in_class').click(function (e) {
        e.preventDefault();
        link_in_class()
    });

    $('#edit-link-class').click(function (e) {
        e.preventDefault();
        $(this).hide()
        $('#link-class-button').slideToggle()
        $('#select-class-div').slideToggle()
    });
})

function set_form_mask() {
    $('#student-primary_phone').mask('(00) 00000-0000');
    $('#student-secondary_phone').mask('(00) 00000-0000');
    $('#student-cpf').mask('000.000.000-00');
    $('#student-rg').mask('#', {
        reverse: true
    });
    $('#student-zipcode').mask('#', {
        reverse: true
    });
}

function edit_student_document(event, div) {
    event.preventDefault();

    $('#div-' + div).slideToggle()
}

function update_field_status(input_id, event, status) {
    event.preventDefault();

    $('select[name="' + input_id + '"]').val(status)
    $('form#status_doc_update').submit()
}

function link_in_class() {
    let selected_class = $('#class-name-select').val()

    $('input[name="classes_name"]').val(selected_class);

    $('form#link_class').submit();
}
