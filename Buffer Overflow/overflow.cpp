/*
	Buffer overflow (C++)
	Author: Tejas Dastane.

	Note: 
		* Sorry, not compatible with Turbo C++ compiler! 
		* Try removing namespace declaration, it might work.
		* GNU compiler is recommended. 
*/

#include<iostream> 		// I do cout only :(
#include<cstdio> 		// I have gets() command.
#include<cstdlib> 		// I have the system command B)
using namespace std;	// Without me, program is a waste!

int main(){
	cout<<"\n---------------------------------------------------"<<endl<<endl;
	/*
		# Important:

		Memory handling of g++ compiler is different for UNIX/LINUX/WINDOWS. Please confirm whether the
		difference between the address two variables is positive. 

		If negative, change declaration of the two variables.

		My program worked fine on Windows x64.
	*/

	// Deadly overflow variable.
	char overflow_string[10] = "echo css!";
	cout<<"Adress of overflow string -> "<<&overflow_string<<endl;
	
	// Useless input variable.
	char name[10];
	cout<<"Address of name -> "<<&name<<endl<<endl;
	
	// This tells you how apart are 'name' and 'overflow_string' stored in memory
	char *addr_1 = name, *addr_2 = overflow_string;
	int diff = (int)(addr_2 - addr_1);
	cout<<"Difference between consecutive variables: "<<diff<<endl<<endl;
	cout<<"Enter your name -> ";
	gets(name);		//Enter some garbage for first 'diff' characters, then put actual command.
	cout<<endl;

	// Actual name ends at the provided input, but the start pointer of overflow is within its range.
	cout<<"Actual name -> "<<name<<endl;
	cout<<"Extra characters -> "<<overflow_string<<endl<<endl;

	// And destruction!!
	cout<<"Executing '"<<overflow_string<<"' command..."<<endl;
	system(overflow_string);
	cout<<"\n---------------------------------------------------"<<endl<<endl;
}

/*
Output:

	---------------------------------------------------

	Adress of overflow string -> 0x60ff0a
	Address of name -> 0x60ff00

	Difference between consecutive variables: 10

	Enter your name -> 1234567890echo Hacked!

	Actual name -> 1234567890echo Hacked!
	Extra characters -> echo Hacked!

	Executing 'echo Hacked!' command...
	Hacked!

	---------------------------------------------------

*/