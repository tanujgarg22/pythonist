list1=[{"a":10,"b":50,"c":100},{"a":10,"d":500,"c":100},{"d":900,"a":10,"b":50,"c":100},{"d":500}]
result={}

for d in list1:
    for key,value in d.items():
        if key in result:
            result[key]+=value
        else:
            result[key]=value

print(result)
