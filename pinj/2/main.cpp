#include <stdio.h>

#include <string.h>

 

int n;

int dp[100001];

 

int f(int n)

{

  if (n == 1) return 2;

  if (n == 2) return 4;

  if (n == 3) return 7;

  if (dp[n] != -1) return dp[n];

  return dp[n] = (f(n-1) + f(n-2) + f(n-3));

}

 

int main(void)

{

  memset(dp,-1,sizeof(dp));

  scanf("%d",&n);

  printf("%d\n",f(n));

  return 0;

}