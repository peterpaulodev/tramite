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

    // $('#residence-upload').on('change', function () {
    //     $('form#upload-docs').submit();
    // });

    // $('#registration-upload').on('change', function () {
    //     $('form#upload-docs').submit();
    // });
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

function update_field_status($this, event, status) {
    event.preventDefault();

    $($this).parent().find('input').val(status)
    $('#status_doc_update').submit()
}