#include <iostream>
using namespace std;
int main()
{
setlocale(LC_ALL, "RUS");
float x, y, a, b, c, d, e, f;
cout << "Введите коэфициенты первого линейного уравнения один за другим: " << endl;
cin >> a >> b >> c;
cout << "Введите коэфициенты второго линейного уравнения один за другим: " << endl;
cin >> d >> e >> f;
"\n";
if (((((a == 0) && (d == 0)) && (b * f != c * e)) || (((b == 0) && (e == 0)) && (a * f != c * d))) || ((a == 0) && (b == 0) && (c != 0)) || ((d == 0) && (e == 0) && (f != 0)))
{
cout << "Система не имеет решений" << endl;
}
else if ((((a == 0) && (d == 0)) && (b * f == c * e)) || (((b == 0) && (e == 0)) && (a * f == c * d)))
{
cout << "Система имеет бесконечное количество решений" << endl;
}

else if (a * e != d * b)
{
x = (f * b - e * c) / (b * d - e * a);
y = (a * f - d * c) / (a * e - d * b);
cout << "(" << x << ";" << y << ")" << endl;
}
else if (((a != 0) && (b != 0) && (c == 0)) || ((d != 0) && (e != 0) && (f == 0)))
{
cout << "(" << 0 << ";" << 0 << ")" << endl;
}
else if (((a * e == d * b) && (b * f != e * c) && (a * f != d * c))) // (((a == 0) && (d == 0)) && (b * f == c * e)) || (((b == 0) && (e == 0)) && (a * f == c * d)))
{
cout << "Система не имеет решений" << endl;
}
else if ((a * e == d * b) && (c * e == b * f) && (a * f == d * c))
{
cout << "Система имеет бесконечное количество решений" << endl;
}
}