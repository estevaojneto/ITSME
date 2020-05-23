//Write a Javascript program for sequential search
//(I know JS has .search() and .indexOf(), but this is an exercise so excuse me!)

function sequential_search(haystack, needle){
	for(l = 0; l < haystack.length; l++){
		if(haystack[l] == needle)
			return l;		
	}
	return false;
}

//As an example, we'll try to find a 8 on this array: it returns the position 
//of the element.
console.log("Position:"+sequential_search([1,2,3,5,8], 8));

//Now we will try to find an element not contained in the array; returns "False" 
//(which we convert to string so we can print it)
console.log("Position:"+sequential_search([1,2,3,5,8], 7));
