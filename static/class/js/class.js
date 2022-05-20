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

    // if ($("#student-class-list").length) {
    //     $("#student-class-list").DataTable({
    //         "responsive": true,
    //         "lengthChange": false,
    //         "autoWidth": false,
    //     })
    // }

    let datepicker_options = {
        format: 'DD/MM/YYYY',
        date: moment().format()
    }

    set_form_mask()

    let class_id = $('#class_id').val()
    $('#' + class_id).fadeIn()

    //Date picker
    $('#initial-date').datetimepicker(datepicker_options)
    $('#final-date').datetimepicker(datepicker_options)

    $('#class_id').change(function (e) {
        e.preventDefault();
        let id = $(this).val()

        $('.info-class').hide()
        $('#' + id).fadeIn()
    });

})


function clear_class_form() {
    $('#class-form input').each(
        (index, element) => {
            $(element).val('')
        })
}

function set_form_mask() {
    $('#class-zipcode').mask('99999-999');
    $('#class-workload').mask('#', {
        reverse: true
    });
}