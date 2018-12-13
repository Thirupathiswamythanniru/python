#include <stdio.h>

int main(void) {
	int b[10];
	int k;
	for(k=0;k<10;k++)
	{
	scanf("%d",&b[k]);
	}
	int max=b[0];
	for(k=0;k<10;k++)
	{
		if(max<b[k])
		{
			max=b[k];
		}
	}
	printf("%d",max);
}
