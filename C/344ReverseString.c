#include<stdio.h>
#include<string.h>

int main()
{
    char* reverseString(char* s)
    {
        char tem;
        int i = 0;
        int j = strlen(s);
        for(i = 0; i < j/2 ; i++)
            {
                tem = s[i];
                s[i] = s[j-1-i];
                s[j-1-i] = tem;
            }
        return s;
    }
    char* s;
    char* t;
    scanf("%s",s);
    t = reverseString( s);
    printf("%s/n",s);
    return 0;
}
