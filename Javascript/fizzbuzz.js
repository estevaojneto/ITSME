//"Make a program that prints numbers from 0 to 1000, prints "fizz" when a number divisible by 3 and "buzz" when a number is divisible by 5"
//Coded by Estevao Neto
function fizzbuzz(){
	var i;
	  for(i = 0; i < 1001; i++){
			if(i%(3*5)==0) console.log("fizzbuzz\t");
			  else if(i%3==0) console.log("fizz\t");
			  else if(i%5==0) console.log("buzz\t");
		  else console.log(i);
	  }
  }
  
  fizzbuzz();