#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<math.h>

int main() {
	char ans[1024];
	printf("Enter the Key!\n");
	scanf("%s",ans);
	if(strlen(ans) != 45) {
		puts("Get the length right first\n");
		return 0;
	}
	if(abs(ans[44]-ans[8]) == strlen("01\0") && ans[8]/100 + ((ans[8]/10)% 10) == ans[8]%10 && ans[8]%10 + 1 == pow((ans[8]/10)%10,2)) {
		if(ans[1] == ans[4] && ans[4]/100 == ans[4]%100 && (ans[4]%100 * 10) == ans[2]%100 && 5*(ans[4]%100)+(ans[2]%100) == ans[3]%100 && ans[3]) {
			if(ans[0]%10 == (ans[0]/10%10)*ans[0]/100 && ans[5] == 67 && ans[7] == (ans[5]%10)*10 && ans[6] == ans[7]+(ans[7]/10)*2 && ans[26] - 1 == ans[9] + (ans[9]%10)) {
				if(ans[14] == ans[18] && sqrt(ans[14]/10) == sqrt(ans[14]/10 - ans[14]%10)+1 && ans[18] == ans[23] && ans[23] == ans[31] && ans[31] == ans[38]){
					if(ans[17] == ans[34] && ans[34] == ans[28] && ans[41] == ans[28]) {
						if(ans[11] == ans[13]-1 && ans[11] == ans[15] && ans[11] == ans[32]){
							if(ans[13] == ans[21] && ans[30] == ans[21] && pow(ans[30]/10-(ans[30]%10),2) == (ans[30]/10 + (ans[30]%10))/2) {
								if(ans[27] == ans[9] -1 && ans[9] == ans[12]-(12/4)*(12/3+1) && ans[12] == ans[29] && ans[29] == ans[33] && ans[33] == ans[16]) {
									if(ans[19] == ans[9] + ans[7]/10 && ans[25]-ans[29] == sqrt(ans[9]%10) && ans[25]-ans[22] == 1 && ans[22] == ans[39]){ 
										if(ans[35] == ans[26] + 1 && ans[40] == 104 && ans[9]%10 == ans[9]/10 && !(((ans[9]%10)+1)%10)){ 
											if(ans[42]%10 == pow(3,2) && ans[42]/10 == pow(2,3) && ans[37] == ans[20]-1 && ans[37]-ans[10] == 3*4) {
												if(ans[43] == 33 && ans[36] == 39 && ans[24] == 94 && ans[20] + pow(2,2) == ans[42]){
													printf("Hurray! That's right!!\n");
													return 0;
												}
											}	
										}
									}
								}
							}
						}
					}
				}
			}
		}	
	}
	printf("Got lost somewhere :/\n");
	return 0;
}
