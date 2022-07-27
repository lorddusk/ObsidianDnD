function session_number(){
	file = fopen('session_number.txt', 0);
	number = fread(file,flength(file));
	newNumber = number + 1;
	file = fopen('session_number.txt', 3);
	fwrite(file, newNumber);
	return newNumber;
}

module.exports = session_number;
