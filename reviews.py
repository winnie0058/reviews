
data = []
# datalen = []
count = 0
sum_len = 0

with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		sum_len += len(line)
		count += 1
		# if count % 10000 == 0:
		# 	print(len(data))
# print(len(data))
print('檔案讀取完成，總共有', count, '筆留言')

# tot = 0
# for l in datalen:
# 	tot += l
average = sum_len/count
print('留言平均長度 = ', average)
