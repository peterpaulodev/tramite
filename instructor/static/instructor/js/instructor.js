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
})

function clear_instructor_form() {
    $('#instructor-form input').each(
        (index, element) => {
            $(element).val('')
        })
}