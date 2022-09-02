function limpiarFormulario(){
	document.getElementById("factura").reset();
}
function calculo(){
	var nombre1= document.getElementById("i1");
	var producto1= document.getElementById("i2");
	var precio1= document.getElementById("i3");
	var cantidad1= document.getElementById("i4");
	var subtotal1= document.getElementById("i5");
	var iva1= document.getElementById("i6");
	var totalpagar= document.getElementById("i7");

	var precio= parseFloat(precio1.value);
	var cantidad=parseInt(cantidad1.value);
	var subtotal=0,iva=0,total=0;
	subtotal=(precio*cantidad);
	iva=(subtotal*0.12);
	totalpagar=(subtotal+iva);
	if(cantidad1.value.length==0 || precio1.value.length==0){
	validar();
	}else{
		document.getElementById("precio").value=precio;
		document.getElementById("cantidad").value=cantidad;
		document.getElementById("totalapagar").value=totalpagar;
	}
	}
function validar(){
	var subtotal1= document.getElementById("i5");
	var iva1= document.getElementById("i6");
	var totalpagar= document.getElementById("i7");
	subtotal1.value="0.00";
	iva1.value="0.00";
	total1.value="0.00";
	}