//Write a Javascript program for binary search
//(I know JS has .search() and .indexOf(), but this is an exercise so excuse me!)

function binary_search(haystack, needle){
	var l = 0;
	var r = (haystack.length)-1;
	while(l <= r){
		var m = Math.floor((l+r)/2);
		if(haystack[m] < needle)
			l = m + 1;
		else if(haystack[m] > needle)
			r = m - 1;
		else
			return m;
	}
	return false;
}
    
//As an example, we'll try to find a 3 on this array: it returns the position 
//of the element.
console.log("Position:"+binary_search([1,2,3,5,8], 3));

//Now we will try to find an element not contained in the array; returns "False" 
//(which we convert to string so we can print it)
console.log("Position:"+binary_search([1,2,3,5,8], 7));
