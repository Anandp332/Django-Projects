function fun1(){
    alert("Welcome to Doctor Page");


}
function checkdata(){
    if(form1.n1.value == ""){
        alert('Doctor Name should not be empty');
    }
    else if(form1.n2.value == ""){
        alert('Doctor Exp should not be empty');
    }
    else{
        alert('Data is accepted')
    }

}
