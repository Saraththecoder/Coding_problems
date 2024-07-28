sarath=[1,2,3,4,6]
n=len(sarath)
miss=(n+1)*(n+2)/2
add=sum(sarath)
missing=miss-add
print(f"The missing number is {missing}")
sarath=[1,2,3,4,6,int(missing)]
sarath.sort()
print(f"Finally the updated list is {sarath}")