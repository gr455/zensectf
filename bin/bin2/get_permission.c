#include<stdio.h>
#include<stdlib.h>
#include<string.h>

void flag(int permission, char* s) {
	if(!strcmp(s,"Keys")) {
		if(permission == 1){
			printf("Alas! you made it!\n");
			char c;
			FILE * f = fopen("flag1.txt", "r");
        		if(!f) {
	                	printf("file not found\n");
	                	return;
        		}
	        	while((c = fgetc(f)) != EOF)
                		printf("%c",c);
			        fclose(f);
			        return;

			}
		else
			printf("zenseCTF{S3cur1ty_4rr1v3d_s33ms_y0u_d0n't_h4v3_p3rMission}\n");
	}
	else
		printf("Wait where are the keys!? :/\n");
}

int main() {
	long long int p1 = 0;
	unsigned int p2 = 0;
	int *p3;
	char keys[6];
	int p5 = 0;
	unsigned long long p6 = 0;
	short p4 = 0;
	char name[128];
	gets(name);
	printf("Hello %s\n",name);
	if(p2 != p1 || p1 != 0)
		printf("You can't modify things as you like!\n");
	else
		flag(p5,keys);
	return 0;
}
