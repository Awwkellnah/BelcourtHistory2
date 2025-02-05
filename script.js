

$(document).ready(function() {
   
   
    function format (rowData) {
        return '<div><strong>Company:</strong> ' + rowData['Company'] + 
               '<br /><strong>Opening Date:</strong> ' + rowData['Opening Date'] + 
               '<br /><strong>Closing Date:</strong> ' + rowData['Closing Date'] +
               '<br /><strong>Days Played:</strong> ' + rowData['Days Played'] +
               '<br /><strong>Lost:</strong> ' + rowData['Lost'] + '</div>';
    }


    // Load and parse the CSV file
    Papa.parse("https://raw.githubusercontent.com/Awwkellnah/belcourthistoryfile/refs/heads/main/Database.csv",{
    // Papa.parse("http://127.0.0.1:5500/Full Database - Sheet1.csv", {
        download: true,
        header: true, // assuming the first row is a header
        complete: function(results) {
            var csvData = results.data;
            // Initialize DataTable and populate data
           table = $('#myTable').DataTable({
                data: csvData,
                
                columns: [
                    {
                        className: 'dt-control',
                        orderable: false,
                        data: null,
                        defaultContent: '',

                    },
                    { data: 'Title' }, // Match these to your CSV column names
                    { data: 'Opening Date' },
                    { data: 'Closing Date' },
                    { data: 'Days Played' },
                    { data: 'Company' },
                    { data: 'Series' },
                    { data: 'Category' },
                    { data: 'Year' },
                    { data: 'Season' },
                    { data: 'Notes' },
                    { data: 'Lost' },
                    { data: 'Country' },
                    { data: 'Genre' },
                    // Add more columns as needed
                ],
              
                responsive: {
                    details: {
                        display: DataTable.Responsive.display.childRow,
                        type: 'column'
                    }
                },
                order: [[2, 'asc']],
                // caption: 'Table 1: Pupil averages',
                pageLength: 25,
                columnDefs: [
                    {
                        target: [6,8,9,10,11,12,13],
                        visible: false,
                        searchable: false
                    },
                    { className: 'boldTitle', targets: [1] },
                    { width: '35%', targets: 1 },
                    { width: '2%', targets: 0 },
                    
                ],
                // searchPanes: {
                //     options: [
                //         {
                //             label: 'Hillsboro',
                //             value: function (rowData, rowIdx) {
                //                 return rowData[5] == 'Hillsboro Theatre';
                //             }
                //         },
                //         {
                //             label: 'Little Theatre Guild',
                //             value: function (rowData, rowIdx) {
                //                 return rowData[6] == 'Little Theatre Guild';
                //             }
                //         }
                //     ],
                //     combiner: 'and'
                // },
                // targets: [4],
                // layout: {
                //     top1: {
                //         searchPanes: {
                //             viewTotal: true,
                //             columns: [1, 3, 4]
                //         }
                //     }
                // },
            
            });
        
        // Add event listener for opening and closing details
        table.on('click', 'td.dt-control', function (e) {
            
            let tr = e.target.closest('tr');
            let row = table.row(tr);
        
            if (row.child.isShown()) {
                // This row is already open - close it
                row.child.hide();
            }
            else {
                // Open this row
                row.child(format(row.data())).show();
                // row.child(format(row.data())).show();
                // console.log(row.child())
            }
         });
           
        }

        
    });

});

        