#include<iostream>
#include<cstdio>
#include<cstdlib>
using namespace std;

int main(){
	char name[10];
	cout<<"\n---------------------------------------------------"<<endl<<endl;
	cout<<"Address of name -> "<<&name<<endl;
	char overflow_string[10];
	cout<<"Adress of overflow string -> "<<&overflow_string<<endl;
	cout<<endl;
	char *addr_1 = name, *addr_2 = overflow_string;
	int diff = (int)(addr_2 - addr_1);
	cout<<"Difference between consecutive variables: "<<diff<<endl<<endl;
	cout<<"Enter your name -> ";
	gets(name);
	cout<<endl;
	cout<<"Actual name -> "<<name<<endl;
	cout<<"Extra characters -> "<<overflow_string<<endl;
	system(overflow_string);
	cout<<"\n---------------------------------------------------"<<endl<<endl;
}
