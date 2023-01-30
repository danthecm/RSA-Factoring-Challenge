#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <string.h>

int main(int argc, char * argv[])
{
	if (argc < 2) {
		return (1);
	}
	char * filename = argv[1];
	FILE * fp = fopen(filename, "r");

	if (fp == NULL) {
		return (1);
	}
	char * string = malloc(sizeof(char) * 1000000000000000000000000);
	while(fgets(string, 10000000000000000000000, fp) != NULL) {
		signed int len = atoi(string);
		printf("%d\n", len);
	}
	string = NULL;
	free(string);
	printf("Argument 0: %d\n", argc);
	printf("Arguments: %s\n", filename);
}
