#include <stdio.h>

int main(void) {
	int b[10];
	int k;
	for(k=0;k<10;k++)
	{
	scanf("%d",&b[k]);
	}
	int min=b[0];
	for(k=0;k<10;k++)
	{
		if(min>b[k])
		{
			min=b[k];
		}
	}
	printf("%d",min);
}
