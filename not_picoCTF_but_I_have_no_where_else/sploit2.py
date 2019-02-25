import math
import string

def function(x) :
	if x <= 1 :
		return x
	else :
		return (function(x-1)+function(x-2))
		
		
flag = ""
result = 0 
resulttrue = 0
key = [104, 116, 116, 112, 115, 58, 47, 47, 119, 119, 119, 46, 121, 111, 117, 116, 117, 98, 101, 46, 99, 111, 109, 47, 119, 97, 116, 99, 104, 63, 118, 61, 100, 81, 119, 52, 119, 57, 87, 103, 88, 99, 81]
ha = "227142283294361239944121842020436314606251027551366252598253848952569754137056719162068186434925671029971182139719658387329553475146831784026958126247778237665988133480298215976588349457119168283551921565256291938518829581694555"
for j in range(len(key)):
	p = function(j+1)
	for i in string.printable:
		result = resulttrue
		magic = int(round(math.exp(math.log(ord(i))+math.log(p))))
		magic = magic ^ key[j]
		result=(result*10)+len(str(magic))
		hooli = magic
		while(hooli > 0):
			hooli = hooli//10
			result = result * 10
		result = result + magic
		if ha.startswith(str(result)):
			flag += i
			print flag
			resulttrue = result
			if "c7f" in flag:
				exit(0)
			break
