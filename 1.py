# class Stack:
#     def __init__(self) -> None:
#         self.sizee = 0
#         self.l = []

#     def push_n(self, n):
#         self.sizee += 1
#         self.l.append(n)
#         print('ok')

#     def size(self):
#         print(self.sizee)

#     def clear(self):
#         self.l = []
#         self.sizee = 0
#         print('ok')

#     def exit()

# cmd = input()
# while cmd != 'exit':
#     cmd


def find_min(l):
    mi = l[0]
    for x, n in l[1:]:
        if x<mi:
            mi = x
    return mi

n = int(input())
l = list(map(int, input().split()))
for i, x in enumerate(l):
    l[0]tmp = min(l[i:])
    x, tmp = tmp, x
print(l)