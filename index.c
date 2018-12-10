#include<stdio.h>
int main()
{
char ch[100];
int k;
clrscr();
printf("Enter string:");
for(k=0;k<100;k++)
{
scanf("%c",&ch[k]);
if(ch[k]=='i')
{
break;
}
}
for(k=0;ch[k]!='\0';k++)
{
printf("%c",ch[k]);
}
getch();
}
