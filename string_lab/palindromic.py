#def is_palidomic_tup():
ip_tuple=(5,1,2,2,1,5)
#ip_tuple2=(5,1,2,2,1,5)

length_v=len(ip_tuple)
result=True
#range_v1=int((length_v-1)/2)
#print(range_v1)

for index in range(length_v//2):
    var_x=ip_tuple[index]
    var_y=ip_tuple[-index -1]
    print(f"index {index} var x {var_x} var y {var_y}")
    if var_x != var_y:
        result = False
        break
    else:
        result=True
#else :#

print(result)


