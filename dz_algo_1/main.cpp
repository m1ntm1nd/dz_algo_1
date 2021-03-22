#include <iostream>
#include <utility>
#include <math.h>
using namespace std;

pair<int, int> solve_du(int a1, int b1, int c1, int a2, int b2, int c2) {
	int den = b2 - b1 * a2;
	if  (a1 == 0){
		if ((a2 == 0) || (b1 == 0)){
			return make_pair(-404,-404);
		}
		int y = c1/b1;
		int x = (c2 - y*b2)/a2;
		return make_pair(x,y);
	}
	if  (a2 == 0){
		if ((a1 == 0) || (b2 == 0)){
			return make_pair(-404,-404);
		}
		int y = c2/b2;
		int x = (c1 - y*b1)/a1;
		return make_pair(x,y);
	}
	if  (b1 == 0){
		if ((a1 == 0) || (b2 == 0)){
			return make_pair(-404,-404);
		}
		int x = c1/a1;
		int y = (c2 - x*a2)/a1;
		return make_pair(x,y);
	}  
	if  (b2 == 0){
		if ((a2 == 0) || (b1 == 0)){
			return make_pair(-404,-404);
		}
		int x = c2/a2;
		int y = (c1 - x*a1)/a2;
		return make_pair(x,y);
	}    
	int y = (c2 * a1 - a2 * c1) / (b2 - b1 * a2);
	int x = (c1 - b1 * y) / a1;
	return make_pair(x, y);
}

int* resheto(int n) {
	int* a = new int[n + 1];
	for (int i = 0; i <= n; i++) {
		a[i] = i;
	}
	cout<<a[n]<<endl;
	for (int i = 2; i < sqrt(n); i++) {
		int k = i * i;
		a[k] = 0;
		for (int j = k; j < n; j+=i) {
			a[j] = 0;
		}
	}
	return a;
}

int gcd(int a, int b) {
	if (b == 0)
		return a;
	else
		return gcd(b, a % b);
}

int main(){
	int n = 1000;
	int* a = resheto(n);
	for (int i = 2; i < n; i++) {
		if (a[i] != 0){
			cout<<a[i]<<'\n';
		}
	}
}