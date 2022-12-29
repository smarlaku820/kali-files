#include <stdio.h>
#include <string.h>

void func(char *v){
	char buffer[10];
	strcpy(buffer, v);
	printf("%s",buffer);
}

void main(int argc, char *argv[]){
	func(argv[1]);
}
