
// send email alerts
success = document.getElementsByClassName('alert-success-contact')
error = document.getElementsByClassName('alert-error-contact')


if(success.length > 0){
    window.onload = function(){
                M.toast({html: 'Mensaje enviado <i style="margin-left:5px" class="material-icons">check</i> ',
                         classes: 'rounded cyan darken-3'})
            }
}

if(error.length > 0){
    window.onload = function(){
        M.toast({html: 'Error al enviar mensaje, intenta de nuevo <i style="margin-left:3px" class="material-icons">error_outline</i>',
                classes: 'rounded red lighten-1'})
    }
}
