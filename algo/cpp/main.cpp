#include <iostream>
using namespace std;
int main()
{
setlocale(LC_ALL, "RUS");
double x, y, a1, b1, h1, a2, b2, h2;
cout << "Введите коэфициенты первого линейного уравнения один за другим: " << endl;
cin >> a1 >> b1 >> h1;
cout << "Введите коэфициенты второго линейного уравнения один за другим: " << endl;
cin >> a2 >> b2 >> h2;
"\n";

double delta = a1 * b2 - b1 * a2;
double deltax = h1 * b2 - h1 * b1;
double deltay = a1 * h1 - a2 * h1;

if (delta != 0){
    x = deltax / delta;
    y = deltay / delta;
    cout << "(" << x << ";" << y << ")" << endl;    
}else{
    if ((deltax != 0) || (deltay != 0)){
        cout << "Система не имеет решений" << endl;
    } else{
        if ((a1 / a2 ) == (b1/b2) == (h1/h2)){
            if (b1 == 0){
                cout << "Задайте x произвольно:" << endl;
                cin >> x;
                cout << "x = " << x << endl;
                y = (h2 - a2*x) / b2;
                cout << "y = " << y << endl;
                string value = '(' + to_string(h2) + '-' + to_string(a2) + '*' + to_string(x) + ')' + '/' + to_string(b2);
                cout << "Y задается формулой: (h2 - a2*x) / b2" << endl;
                cout << "Пересчет y при заданном х: "<< value << endl;
                cout<< endl;
                cout<< endl;
            }else{
                cout << "Задайте x произвольно:" << endl;
                cin >> x;
                cout << "x = " << x << endl;
                y = (h1 - a1*x) / b1;
                cout << "y = " << y << endl;
                string value = '(' + to_string(h1) + '-' + to_string(a1) + '*' + to_string(x) + ')' + '/' + to_string(b1);
                cout << "Y задается формулой: (h1 - a1*x) / b1" << endl;
                cout << "Пересчет y при заданном х: "<< value << endl;
                cout<< endl;
                cout<< endl;
            }
        }else{
            if (h1 == h2 == 0){
                
            }
        }
    }
        
    }
}

// cout << "Система имеет бесконечное количество решений" << endl;
//         if (((b1 == 0) && (b2 == 0)) && (a1 == 0)&& (a2 == 0)){
//             cout << "Y определяется произвольно:" << endl;
//             cout << "Y = (-inf, + inf)"<< endl;
//         } else{
//             if (b1 == 0){
//                 cout << "Задайте x произвольно:" << endl;
//                 cin >> x;
//                 cout << "x = " << x << endl;
//                 y = (h2 - a2*x) / b2;
//                 cout << "y = " << y << endl;
//                 string value = '(' + to_string(h2) + '-' + to_string(a2) + '*' + to_string(x) + ')' + '/' + to_string(b2);
//                 cout << "Y задается формулой: (h2 - a2*x) / b2" << endl;
//                 cout << "Пересчет y при заданном х: "<< value << endl;
//                 cout<< endl;
//                 cout<< endl;
//             }else{
//                 cout << "Задайте x произвольно:" << endl;
//                 cin >> x;
//                 cout << "x = " << x << endl;
//                 y = (h1 - a1*x) / b1;
//                 cout << "y = " << y << endl;
//                 string value = '(' + to_string(h1) + '-' + to_string(a1) + '*' + to_string(x) + ')' + '/' + to_string(b1);
//                 cout << "Y задается формулой: (h1 - a1*x) / b1" << endl;
//                 cout << "Пересчет y при заданном х: "<< value << endl;
//                 cout<< endl;
//                 cout<< endl;
//             }
//         }
        
//     }
// if (((((a == 0) && (d == 0)) && (b * f != c * e)) || (((b == 0) && (e == 0)) && (a * f != c * d))) || ((a == 0) && (b == 0) && (c != 0)) || ((d == 0) && (e == 0) && (f != 0)))
// {
// cout << "Система не имеет решений" << endl;
// }
// else if ((((a == 0) && (d == 0)) && (b * f == c * e)) || (((b == 0) && (e == 0)) && (a * f == c * d)))
// {
// cout << "Система имеет бесконечное количество решений" << endl;
// }

// else if (a * e != d * b)
// {
// x = (f * b - e * c) / (b * d - e * a);
// y = (a * f - d * c) / (a * e - d * b);
// cout << "(" << x << ";" << y << ")" << endl;
// }
// else if (((a != 0) && (b != 0) && (c == 0)) || ((d != 0) && (e != 0) && (f == 0)))
// {
// cout << "(" << 0 << ";" << 0 << ")" << endl;
// }
// else if (((a * e == d * b) && (b * f != e * c) && (a * f != d * c))) // (((a == 0) && (d == 0)) && (b * f == c * e)) || (((b == 0) && (e == 0)) && (a * f == c * d)))
// {
// cout << "Система не имеет решений" << endl;
// }
// else if ((a * e == d * b) && (c * e == b * f) && (a * f == d * c))
// {
// cout << "Система имеет бесконечное количество решений" << endl;
//}
}