$(function () {
    // Datatable instance
    if ($("#instructor-list").length) {
        $("#instructor-list").DataTable({
            "responsive": true,
            "lengthChange": false,
            "autoWidth": false,
            "buttons": ["copy", "csv", "excel", "pdf", "print", "colvis"]
        }).buttons().container().appendTo('#instructor-list_wrapper .col-md-6:eq(0)')
    }

    $('[data-toggle="tooltip"]').tooltip()

    set_form_mask()
})

function clear_instructor_form() {
    $('#instructor-form input').each(
        (index, element) => {
            $(element).val('')
        })
}

function set_form_mask() {
    $('#instructor-phone1').mask('(00) 00000-0000');
    $('#instructor-phone2').mask('(00) 00000-0000');
    $('#instructor-cpf').mask('000.000.000-00');
    $('#instructor-rg').mask('00.000.000-0');
}