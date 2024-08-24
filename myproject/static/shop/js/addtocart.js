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
            console.log(data.status);
            alert(data.status);
            window.setTimeout(function(){ } ,100);
                            location.reload();      
        },
        error:function(){
            alert('Please Login Account');
        },
        
                        
      });//end ajax
});


//update qty
$(".cqty").change(function(){
    var a3=$(this).val();
    var crow = $(this).closest(".cartrow");
    var cpid = crow.find(".crid").val();
    var cartid = crow.find(".cartid").val();
    $.ajax({
    url: "/cart_change_qty/",
    method: "GET",
    data:{cpid:cpid, cartid:cartid, a3:a3},
    success: function(data){
        console.log('h3');

        // window.setTimeout(function(){ } ,100);
        //                     location.reload(); 
             
    },
    error:function(){
        alert('Error contact to 09-969255445');
    },
                    
  });//end ajax
 
});//End update qty


// SaveData
$("#uptcartbtn").click(function(){
    location.reload(true);
});



// // SaveData
// $("#sentorder").click(function(){
//     console.log('cl');
// });


// start order function 
$("#customerdetail").on('click', '#sentorder', function() {
    var cur = $(this).closest("#cdatil");
    var phone = cur.find("#phone").val();
    var caddress = cur.find("#caddress").val();
    var oid = cur.find("#oid").val();

    $.ajax({
        url: "/send_order_to_admin/",
        method: "GET",
        data:{phone:phone, caddress:caddress, oid:oid},
        success: function(data){
            alert('Thank You for your purchase');
            window.location.href = '/';
                     
        },
        error:function(){
            alert('Error contact to 09-969255445');
        },
                        
      });//end ajax
    
});

