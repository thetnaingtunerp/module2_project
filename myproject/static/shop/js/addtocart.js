console.log('add to cart');

// start btn 
$("#itmdetail").on('click', '.addtobtn', function() {
    var cur = $(this).closest(".itmlist");
    var itmname = cur.find(".itmname").html();
    var itmid = cur.find(".itmid").val();
    var price = cur.find(".pric").val();
    var isize = cur.find(".si").val();
    var icl = cur.find(".icl").val();
    var qty = cur.find(".num-product").val();
    // alert(qty);
    $.ajax({
        url: "/addtocart/",
        method: "GET",
        data:{itmid:itmid, isize:isize, icl:icl, qty:qty},
        success: function(data){
      
            alert('Add to Cart Successfully');
            window.setTimeout(function(){ } ,100);
                            location.reload();      
        },
        error:function(){
            alert('Error contact to 09-969255445');
        },
                        
      });//end ajax
});