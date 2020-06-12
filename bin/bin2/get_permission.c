#include<stdio.h>
#include<stdlib.h>
#include<string.h>

void flag(int permission, char* s) {
	if(!strcmp(s,"Keys!")) {
		if(permission == 1){
			printf("Alas! you made it!");
			char c;
			FILE * f = fopen("flag1.txt", "r");
        		if(!f) {
	                	printf("file not found");
	                	return;
        		}
	        	while((c = fgetc(f)) != EOF)
                		printf("%c",c);
			        fclose(f);
			        return;

			}
		else
			printf("zenseCTF{S3cur1ty_4rr1v3d_s33ms_y0u_d0n't_h4v3_p3rMission}");
	}
	else
		printf("\n%sWait where are the keys!? :/",s);
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
	printf("Hello %s",name);
	if(!p2 || !p1)
		printf("You can't modify things as you like!\n");
	else
		flag(p5,keys);
}
