str=input(" enter the string")
str=str.lower()
str1=str.split(" ")
ans=""
for word in str1:
    val=word[0]
    i=0
    for j in range(1,len(word)):
        if word[i]!=word[j]:
            val=val+word[j]
        i+=1
    ans=ans+val+" "
print(ans)