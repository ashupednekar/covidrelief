// jQuery(document).ready(function($) {
//     'use strict';
//
// });

function loaddatatable(){
    'use strict';
    if ($("table.first").length) {

        $(document).ready(function() {
            $('table.first').DataTable();
        });
    }

    /* Calender jQuery **/

    if ($("table.second").length) {

        $(document).ready(function() {
            var table = $('table.second').DataTable({
                lengthChange: false,
                buttons: ['copy', 'excel', 'pdf', 'print', 'colvis']
            });

            table.buttons().container()
                .appendTo('#example_wrapper .col-md-6:eq(0)');
        });
    }


    if ($("#example2").length) {

        $(document).ready(function() {
            $(document).ready(function() {
                var groupColumn = 2;
                var table = $('#example2').DataTable({
                    "columnDefs": [
                        { "visible": false, "targets": groupColumn }
                    ],
                    "order": [
                        [groupColumn, 'asc']
                    ],
                    "displayLength": 25,
                    "drawCallback": function(settings) {
                        var api = this.api();
                        var rows = api.rows({ page: 'current' }).nodes();
                        var last = null;

                        api.column(groupColumn, { page: 'current' }).data().each(function(group, i) {
                            if (last !== group) {
                                $(rows).eq(i).before(
                                    '<tr class="group"><td colspan="5">' + group + '</td></tr>'
                                );

                                last = group;
                            }
                        });
                    }
                });

                // Order by the grouping
                $('#example2 tbody').on('click', 'tr.group', function() {
                    var currentOrder = table.order()[0];
                    if (currentOrder[0] === groupColumn && currentOrder[1] === 'asc') {
                        table.order([groupColumn, 'desc']).draw();
                    } else {
                        table.order([groupColumn, 'asc']).draw();
                    }
                });
            });
        });
    }

    if ($("#example3").length) {

        $('#example3').DataTable({
            select: {
                style: 'multi'
            }
        });

    }
    if ($("#example4").length) {

        $(document).ready(function() {
            var table = $('#example4').DataTable({
                fixedHeader: true
            });
        });
    }

    jQuery.ajax({
            "method": "GET",
            "url": "{{ host }}/getcurrententries",
            "headers": {"X-CSRFToken": "{{ csrf_token }}"},
            "success": function (res1) {
            jQuery('#table_body').html('');
            for(var i=0; i<res1.length; i++){
                if(res1[i]['closed'] == 'Y') {
                    jQuery('#table_body').append(
                        "<tr>" +
                        "<td>" + (i + 1).toString() + "</td>" +
                        "<td>" + res1[i]['name'] + "</td>" +
                        "<td>" + res1[i]['mobile'] + "</td>" +
                        "<td>" + res1[i]['address'] + "</td>" +
                        "<td>" + res1[i]['landmark'] + "</td>" +
                        "<td>" + res1[i]['center'] + "</td>" +
                        "<td>" + res1[i]['remark'] + "</td>" +
                        "<td>" + res1[i]['actor'] + "</td>" +
                        "<td>Done <i class='fa fa-check-circle'></i></td>" +
                        "</tr>"
                    );
                }else{
                    jQuery('#table_body').append(
                        "<tr>" +
                        "<td>"+(i+1).toString()+"</td>" +
                        "<td>"+res1[i]['name']+"</td>" +
                        "<td>"+res1[i]['mobile']+"</td>" +
                        "<td>"+res1[i]['address']+"</td>" +
                        "<td>"+res1[i]['landmark']+"</td>" +
                        "<td>"+res1[i]['center']+"</td>" +
                        "<td>"+res1[i]['remark']+"</td>" +
                        "<td>"+res1[i]['actor']+"</td>" +
                        "<td>Pending <i class='fa fa-warning'></i></td>" +
                        "</tr>"
                    );
                }
            }
        }
    });
}