$(function(){
   //aqui van los mensajer por error
   	$("erroremail").hide();
    $("errorRunUsuario").hide();
    $("errorNombre").hide();
    $("errorFechaDeNacimiento").hide();
    $("errorTelefono").hide();

    //variables indicando su estado de validacion antes del evento
    var error_email = false;
    var error_RunUsuario = false;
	var error_nombre = false;
	var error_fecha = false;
	var error_Telefono= false;

	$("#email").focusout(function() {//llamamos a los id del html

        check_email();//le entrgo la funcion
		
	});
	$("#RunUsuario").focusout(function() {
		
		check_RunUsuario();
		
	});
    //lo mimso a los demas 
    $("#nombreUsuario").focusout(function() {

		check_username();
		
	});

    $("#Fecha").focusout(function() {

        check_fecha();
		
	});

 $("#Telefono").focusout(function() {

        check_Telefono();
		
	});

	function check_email() {//creo la funcion para el correo

		var pattern = new RegExp(/^[+a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}$/i);//aqui se valida el formato del corro electronico
	
		if(pattern.test($("#email").val())) {
			$("#erroremail").hide();
		} else {
			$("#erroremail").html("ERROR, Correo electronico valido");
			$("#erroremail").show();
			error_email = true;//si esta erroeno tira el error
		}
	
	}
	 function check_RunUsuario() {
	
		var RunUsuario_length = $("#RunUsuario").val().length;
		
		if(RunUsuario_length < 10 || RunUsuario_length > 12) {//aqui valido que el minimo de caracteres para el rut deve ser 10 y el maximo 12
			$("#errorRunUsuario").html("ERROR, Run invalido");
			$("#errorRunUsuario").show();//si el no cumple con lo aterior saldra el mensaje de error
			error_RunUsuario = true;//llamando al error
		} else {
			$("#errorRunUsuario").hide();//llamo al  error del html
		}
	
	}


	function check_username() {
	
		var nombre_length = $("#nombreUsuario").val().length;
		
		if(nombre_length < 10 ) {//aqui le dico que el nombre debe ser mayor a 10 caracteres
			$("#errorNombre").html("ERROR, El nombre debe ser mayor a 10");
			$("#errorNombre").show();//y si no cumple con la restriccion mandara mensaje de alerta
			error_nombrecompleto = true;
		} else {
			$("#errorNombre").hide();
		}
	
	}
  
  function check_fecha() {

      var patron=new RegExp(/^\d{1,2}\/\d{1,2}\/\d{2,4}$/);//aqui le paso el parameto a la fecha
      var fecha = "2001";
//la idea es que si la fecha es inferior a 2001 mande un mensaje de error
      if ((patron.test($("#Fecha").val())) && ($("#Fecha").val() < fecha)) {
            $("#errorFecha").hide();
      } else {
               $("#errorFecha").html("ERROR, Año de nacimiento anterior a 2001");
            $("#errorFecha").show();
            error_fecha = true;
      }

    }


function check_Telefono() {//creo la funcion que le dara al telefono un formato
	
		var tefcontac_length = $("#Telefono").val().length;
		
		if(tefcontac_length < 9 || tefcontac_length > 9) {//aui indico que el los numeros no deven ser mas que 9 dijitos
			$("#errorTelefono").html("ERROR, ingrese un numero valido");
			$("#errorTelefono").show();
			error_tefcontac = true;
		} else {
			$("#errorTelefono").hide();
		}
	}

		//Este es el boton eviar aqui se envian todas las validaciones y les envia verdadero si el error existe y si no retorna true 


	$("#registration_form").submit(function() {
		
											
		 error_email = false;
         error_RunUsuario = false;
	     error_nombre = false;
	     error_fecha = false;
	     error_Telefono =false;
		
		check_email();
		check_RunUsuario();									
		check_username();
		check_fecha();
		check_Telefono();
		//toma las variables y las funciones y cuando algna no se cumpla llamara al error
		
		if(error_nombre == false && error_RunUsuario == false  && error_email == false && error_fecha == false && error_Telefono == false)  {
			return true;
		} else {
			return false;	
		}

	});



});