#include<stdio.h>
#include<stdlib.h>
#include<string.h>

int main(){

	char buf1[16]="secret";
	char buf2[16];

	printf("Enter something for buf2:");
	/* scanf is a function which doesn't not give any protection from buffer overflow & we use such as function
	 * here to demonstrate the buffer overflow concept.
	 * In the real world, hackers look into code for such vulnerable functions so that they can exploit
	 * buffer overflow conditions
	 */
	scanf("%s", buf2);

	printf("Value at buf1: %s\n", buf1);
	printf("Value at buf2: %s\n", buf2);
	printf("Address at buf1: %p\n", buf1);
	printf("Address at buf2: %p\n", buf2);

	return 0;

}

