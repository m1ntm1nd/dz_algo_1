
print("Введите коэфициенты первого линейного уравнения один за другим:")
a, b, c = (map(int, input().split()))
print("Введите коэфициенты второго линейного уравнения один за другим:")
d, e, f = (map(int, input().split()))

if((a*e-b*d)==0):
    if(a==b==0):
        if(c!=0):
            print(f"Нет решений")
        else:
            if(d==e==0):
                print("X,Y - любое число")
            elif(d==0):
                print(f"X -  любое число, Y = {f/e}")
            elif(e==0):
                      print(f"X ={f/d},Y любое число")
            else:
                print(f"{d}X+{e}Y = {f}")
    elif(a==0):
        try:
            if(c/b!=f/e):
                print("Нет решений")
            else:
                print(f"X -  любое число, Y = {c/b}")
        except ZeroDivisionError:
            if(f!=0):
                print(f"Нет решений")
            else:
                print(f"X любое число, Y={c/b}")
    elif(b==0):
        try:
            if(c/a!=f/d):
                print("Нет решений")
            else:
                print(f"X={c/a},Y любое число")
        except ZeroDivisionError:
            if(f!=0):
                print(f"Нет решений")
            else:
                print(f"X ={c/a}, Y любое число")
    elif(b*f!=e*c and a*f!=d*c):
        print(f"Нет решений.")
    else:
        print(f"{a}x+{b}y={c}")
else:
    print(f"Y={(c*d-f*a)/(b*d-e*a)}, X={(f*b-c*e)/(b*d-a*e)}")