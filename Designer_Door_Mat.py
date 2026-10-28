# Enter your code here. Read input from STDIN. Print output to STDOUT

n, m = map(int, input().split())

# Top half
for i in range(1, n, 2):
    print((".|." * i).center(m, "-"))

# Middle line
print("WELCOME".center(m, "-"))

# Bottom half (mirror of the top)
for i in range(n - 2, 0, -2):
    print((".|." * i).center(m, "-"))
