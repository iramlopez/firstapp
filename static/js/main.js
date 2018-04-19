$(document).ready(function(){


	function setSwitch(id,state){

        var app_url=$('#serverip').val();
		var dataset={
					'port':id,
					'status':state
					};
            console.log(dataset);
	        $.ajax({
	        url : app_url+'set/switch',
	        dataType : 'application/json',
	        contentType: 'application/json; charset=UTF-8',
	        data:dataset,
	        type : 'POST',
	        crossDomain:true,
	        data : JSON.stringify(dataset),
	        success : function(response) {
	        	    $("#resultdiv").val(response);
	            },
	        error:function(error){

	        }
	    }); //end of ajax
    }


    $(".switch").on("click",function(elem){

        id_text=this.id;
        id=id_text.replace("btn_","");
        $('#'+id_text).toggleClass('btn-warning');
        setSwitch(id,0);
        if($('#'+id_text).hasClass('btn-warning')){
          console.log("set button on");
          setSwitch(id,1);
        } else {
          console.log("set button off");
          setSwitch(id,0);
        }
    }); //end on reqbtn


});