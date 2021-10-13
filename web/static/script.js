$(function() {
    $("td.position-grid-cell-div").on("click", function(e) {
        //e.preventDefault()
        var positionId = $(this).attr("id").match(/\d+/g);
        
        $.ajax({
        type: "PUT",
        url: "/index",
        data: { position: JSON.stringify(positionId) },
        dataType: "json",
        error: function(xhr,status,error){
            alert("ERROR: " + xhr.status + ": " + xhr.statusText + "\n" + status + "\n" + error);
        },
        success: function(result,status,xhr){
            console.log(result);
            var debug = result["debug"];
            var grid = result["grid"];
            $('#debug-text').html(debug);
            drawBoard(grid);
        }
        });
        
        return false;
    });
});
