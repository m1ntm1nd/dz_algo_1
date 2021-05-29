#include <iostream>
#include <vector>
#include <cmath>
#include <algorithm>
#include <fstream>

using namespace std;
float mathoj(vector<int> x, int N)
{
	float s = 0;
	for (int i = 0; i < N; i++)
	{
		s = s + x[i];
	}
	return s / N;
}
float Disp(vector<int> x, int N)
{
	float d = 0;
	float M = mathoj(x, N);
	for (int i = 0; i < N; i++)
	{
		d = d + (x[i]-M)*(x[i]-M);
	}
	return d / N;
}
float sredn(vector<int> x, int N)
{
	return sqrt(Disp(x, N));
}
float xisqr(vector<int> x, int N,int max)
{
	int interv = 70;
	float k = max / interv;
	double p = (1.0/interv);
	vector<double> ivl(interv);
	ivl[0] = 0;
	vector<double> gg(interv);
	for (int i = 1; i<interv; i++)
	{
		ivl[i] = ivl[i-1]+k;
	}
	for (int i = 1; i < interv; i++)
	{
		for (int j = 0; j < N; j++)
		{
			if (x[j] >= ivl[i - 1] && x[j] < ivl[i])
			{
				gg[i] += 1.0;
			}
		}
	}

	float sum = 0;
	for (int i = 0; i < interv; i++)
	{
		double kekw = p * N;
		if (gg[i] != 0)
		{
			sum += pow((gg[i] - kekw), 2);
		}
	}
	return (sum/(p*N));
}
int main()
{
	int a, b, c, m,N;
	a = 3;
	b = 5;
	c = 1;
	m = 2048;
	N = 100;
	//cin >> a >> b >> c >> m >> N;	
	vector<int> x1(N);
	int tmp = 0;
	for (int i = 0;i<N;i++)
	{
		x1[i] = abs(((a * (tmp *tmp) + b * tmp + c) % m ));
		tmp = x1[i];
	}
	std::ofstream out;          // ïîòîê äëÿ çàïèñè
	out.open("D:\\hello.txt"); // îêðûâàåì ôàéë äëÿ çàïèñè
	if (out.is_open())
	{
		for (int i = 0; i < N; i++)
		{
			out << x1[i] << endl;
		}
	}
	for (int i = 0; i < N; i++)
	{
		cout << x1[i] << endl;
	}
	sort(x1.begin(), x1.end());
	int g = x1[x1.size() - 1];
    out.close();
	cout << "      " << endl;
	cout << "Math oj = " << mathoj(x1, N) << endl;
	cout << "Disp = " <<Disp(x1, N) << endl;
	cout << "Srednekvadr = "<<sredn(x1, N) << endl;
}