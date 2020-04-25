alert('this works');
let tot = [];
   let calcTotal = document.querySelector(".button-w3ls");
	calcTotal[i].addEventListener("click", function(){
		console.log(calcTotal);
	   let cartTotal = document.querySelector('#price');
			tot.push(parseInt(cartTotal.textContent));
			console.log(cartTotal.textContent);
			console.log('arr ' + tot);
			cartTotal.textContent = tot.reduce(function(x, y){
				return x + y;
	   }, 0);
	   

   });