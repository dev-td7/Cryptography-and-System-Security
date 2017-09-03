#include<iostream>
#include<cctype>
#include<string>
using namespace std;

int main(){
	string s;
	getline(cin,s);
	for(int i=0;i<s.length();i++){ 
		if(tolower(s[i])>='a' && tolower(s[i])<='z'){
			int c = tolower(s[i]) - 'a';
			c = (c+23)%26;
			char ch = c + 'a';
			cout<<ch;
		}
		else cout<<s[i];
	}
	cout<<endl;
}
