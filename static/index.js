$(document).ready(function(){
    console.log("pronto")
    var socket = io.connect('ws://wflasksocketio.herokuapp.com');
    socket.on('connect', function(){
        socket.send('User has connected!');
    });

    var x = 0;
    $('#sendbutton').click(function(){
        for(var x = 0; x < 10; x += 1){
            console.log("enviando: world");
            socket.emit('evento', { hello: x});
        }
     });
    socket.on('message', function(data){
        console.log(data);
    });
});