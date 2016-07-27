#include<stdio.h>
#include<string.h>
char* reverseString(char* s){
	char tem;
	for(int i = 0; i < strnlen(s)/2 ; i++){
		tem = s[i];
		s[i] = s[strlen(s)-1-i];
		s[strlen(s)-1-i] = tem;
	}
	return s;
}