function populate(s1,s2){
	var s1 = document.getElementById(s1);
	var s2 = document.getElementById(s2);
	s2.innerHTML = "";
	if(s1.value == "Arica"){
		var optionArray = ["|","Arica|Arica"];
	} else if(s1.value == "Tarapaca"){
		var optionArray = ["|","Tarapaca|Tarapaca"];
	} else if(s1.value == "Antofagasta"){
		var optionArray = ["|","Antofagasta|Antofagasta"];
	}
	
	for(var option in optionArray){
		var pair = optionArray[option].split("|");
		var newOption = document.createElement("option");
		newOption.value = pair[0];
		newOption.innerHTML = pair[1];
		s2.options.add(newOption);
	}
}
//cuando se seleciona una opcion de las regions el combobox de abajo se llama con lo que trae dentro de los checkbox 