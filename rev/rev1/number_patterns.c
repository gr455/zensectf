#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<math.h>

int main() {
	char ans[1024];
	printf("Enter the Key!\n");
	scanf("%s",ans);
	if(strlen(ans) != 45) 
	{
		puts("Get the length right first\n");
		return 0;
	}
	if(ans[44] == 125 && ans[8] == 123) {
		if(ans[1] == 101 && ans[4] == 101  && ans[2] == 110  && ans[3] == 115) {
			if(ans[0] == 122 && ans[5] == 67 && ans[7] == 70 && ans[6] == 84 && ans[26] == 109 && ans[9] == 99) {
				if(ans[14] == 95  && ans[18] == 95  && ans[23] == 95  && ans[31] == 95){
					if(ans[17] == 51 && ans[34] == 51 && ans[28] == 51 && ans[41] == 51 && ans[28] == 51) {
						if(ans[11] == 52 && ans[13] == 53  && ans[15] == 52  && ans[32] == 52){
							if(ans[30] == 53 && ans[21] == 53) {
								if(ans[27] == 98 && ans[9] == 99  && ans[12] == 114 && ans[29] == 114 && ans[33] == 114 && ans[16] == 114) {
									if(ans[19] == 106 && ans[25] == 117 && ans[22] == 116 && ans[39] == 116){ 
										if(ans[35] == 110 && ans[40] == 104){ 
											if(ans[42] == 89 &&  ans[37] == 84 && ans[10] == 72) {
												if(ans[43] == 33 && ans[36] == 95 && ans[24] == 110 && ans[20] == 85){
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
