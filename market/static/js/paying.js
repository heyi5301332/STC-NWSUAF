window.onload=function(){


    //document.getElementById("chatbottom").scrollIntoView();
    var div = document.getElementById("chatarea")
    div.scrollTop = div.scrollHeight;
    
    $("#new-message").click(function(){          
　　　　    var content = $("#new-content").val();
        $("#new-content").val("");
        csrf = $("input[name='csrfmiddlewaretoken']").val();
        $.post(url1, {'content':content,'csrfmiddlewaretoken':csrf},
            function(data,status){
                 //window.location.reload();
                 //myFunction();

            });

　　})
    //setInterval(myFunction, 1000);

    var wsURI = "ws://172.29.7.232:8000/market/ws/"+order_id+"/"+uid;

    websocket = new WebSocket(wsURI);

    websocket.onopen = function(evt){
        console.log("Connection open ..."); 
        setInterval("websocket.send('456')", 1000);
    };
     websocket.onclose = function(evt){
         console.log("Connection closed.");
    };
    websocket.onmessage = function(evt){
        //console.log( "Received Message: " + evt.data);
        $('#paycontent').html(evt.data);

        var div = document.getElementById("chatarea")
        div.scrollTop = div.scrollHeight;

    };
    websocket.onerror = function(evt){
        console.log( "Received error: " + evt.data);
    };
}

// function myFunction()
// {
// //$("#chatarea-box").load("/market/paying/"+order_id+" #chatarea", function(){
//     //$("#paycontent").load("/market/paying/"+order_id+" #fresh_area", function(){
//     //document.getElementById("chatbottom").scrollIntoView();
    
// }


