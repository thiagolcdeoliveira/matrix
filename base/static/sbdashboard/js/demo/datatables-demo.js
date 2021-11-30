// Call the dataTables jQuery plugin
$(document).ready(function() {
  $('#dataTable').DataTable({
   "paging":   false,
    "info":     false,
    "search":     false,
      "language": {
            "search": "Pesquisar",

        }
        });
});
