// console.log('userregister js');

$("#registerForm").on('click', '#RegisterBtn', function() {
    var cur = $(this).closest(".rform");
    var fullname = cur.find("#fullname").val();
    var uname = cur.find("#uname").val();
    var regpass = cur.find("#regpass").val();
    
    $.ajax({
        url: "/register_customer/",
        method: "GET",
        data:{fullname:fullname, uname:uname, regpass:regpass},
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