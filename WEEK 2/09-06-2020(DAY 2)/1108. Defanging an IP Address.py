# Given a valid (IPv4) IP address, return a defanged version of that IP address.
# A defanged IP address replaces every period "." with "[.]".
# Example 1:
# Input: address = "1.1.1.1"
# Output: "1[.]1[.]1[.]1"
address="1.1.1.1"
ans=''
for char in address:
    if(char=='.'):
        ans=ans+''.join('[.]') 
    else:
        ans=ans+''.join(char)
print(ans)