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

    // CODE TO CHANGE NAME ON CHANGE INPUT FILE
    // $('.custom-file-input').on('change', function(e) {
    //     const input = e.currentTarget
    //     const name = $(input).attr("name")

    //     const previous_file = input.files[0]
    //     const extension = previous_file.type.replace(/(.*)\//g, '')

    //     const new_name = name + '.' + extension
    //     const new_file = new File([previous_file], new_name)

    //     // hack to update the selected file
    //     const dT = new DataTransfer()
    //     dT.items.add(new_file)
    //     input.files = dT.files
    //     console.log('Selected file: ' + input.files.item(0).name)
    // })
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