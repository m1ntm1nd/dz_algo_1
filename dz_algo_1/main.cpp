#include <iostream>
#include <utility>

using namespace std;

pair<int, int> solve_du(int a1, int b1, int c1, int a2, int b2, int c2) {
	int y = (c2 * a1 - a2 * c1) / (b2 - b1 * a2);
	int x = (c1 - b1 * y) / a1;
	return make_pair(x, y);
}

int* resheto(int n) {
	int* a = new int[n + 1];
	for (int i = 0; i < n; i++) {
		a[i] = i;
	}
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
		cout<<a[i]<<'\n';
	}
}