#include<iostream>
#include<cmath>
#define columns 5
using namespace std;

int pattern[5] = {4,1,5,3,2};
int main(){
    string s;
    cin>>s;
    int n = s.length();
    int m = ceil((double)n/(double)columns);
    char arr[m][columns], cip[m][columns];
    int j,ptr=0;
    for(int i=0; i<m; i++) for(j=0; j<columns; j++) {
        cip[i][j] = s[ptr++];
    }
    for(int i=0;i<columns;i++){
        int swap = pattern[i]-1;
        for(int j=0;j<m;j++) arr[j][swap] = cip[j][i];
    }
    for(int i=0; i<m; i++) for(j=0; j<columns; j++) cout<<arr[i][j];
    return 0;
}