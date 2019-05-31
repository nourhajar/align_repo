$(document).ready(function(){
    $('form').hide();
    $('#loghead').mouseover(function(){
        $('#logform').slideDown( 'slow' );
        $('#regform').hide();
    });
    $('#reghead').mouseover(function(){
    $('#regform').slideDown( 'slow' );
        $('#logform').hide();
    });
    $('.out').mouseover(function(){
        $('form').hide();
    });
})