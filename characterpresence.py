import string
req_list = range(2,102)
j = 0
check = 2
i = 0
main_dict = {}
removdupli = {}
found = []
notfound = []
product = 1
mainstring = raw_input("Enter the main string :")
substring  = raw_input("Enter the subtring :")
while(check*check <= 102):
	ind = req_list.index(check)+ 1
	while(ind<len(req_list)):
		if req_list[ind]%check == 0:
			del req_list[ind]
		ind+=1
	j+=1
	check = req_list[j]
for each in string.lowercase:
	main_dict[each] = req_list[i]
	i+=1
for each in mainstring:
	product*=main_dict[each]
for each in substring:
	if (product)%(main_dict[each]) == 0 :
		found.append(each)
	else:
		notfound.append(each)
if found:
	for each in found:removdupli[each]=0
	print 'the following characters in the substring were found in mainstring','\n'
	print ''.join(removdupli.keys())
else:
	print 'none found'
