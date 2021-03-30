#include <stdio.h>
 
#include <string.h>
 
 
 

 
 
 
int f(int n)
 
{
 
 return 0;
}
 
 
 
int main(void)
 
{
  int n,m;
  scanf("%d%d",&n,&m);
  int dp[n][m];
  for (int i = 0;i<n;i++){
    for (int j = 0;j<n;j++){
      printf("%d",dp[i][j]);
    }
    printf("\n");
  }
 
 
  return 0;
 
}