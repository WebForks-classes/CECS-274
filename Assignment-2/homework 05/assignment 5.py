def hanoi(n, beginning, auxillary, end):
    if n > 0:
        hanoi(n - 1, beginning, end, auxillary)
        if beginning:
            end.append(beginning.pop())
        hanoi(n - 1, auxillary, beginning, end)
        
beginning = [6,5,4,3,2,1]
end = []
auxillary = []
print(beginning, auxillary, end)

hanoi(len(beginning),beginning,auxillary,end)

print(beginning, auxillary, end)