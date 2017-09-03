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
        arr[i][j] = s[ptr++];
        if(ptr==n) break;
    }
    j++;
    while(j<columns) arr[m-1][j++] = 'a';
    for(int i=0;i<columns;i++){
        int swap = pattern[i]-1;
        for(int j=0;j<m;j++) cip[j][i] = arr[j][swap];
    }
    for(int i=0; i<m; i++) for(j=0; j<columns; j++) cout<<cip[i][j];
    return 0;
}