$(document).ready(function(){

    var socket=io.connect('http://192.168.0.28:5000');

    socket.on('connect',function(){
        socket.send('User has connected! ');
    });

    socket.on('message',function(msg){
        $('#messages').append(msg+'</br>');
        console.log('Received Message');
    });

    $('#sendbutton').on('click',function(){
        socket.send($('#myMessage').val());
    });

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
