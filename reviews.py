
data = []
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

average = sum_len/count
print('留言平均長度 = ', average)

new = []
for d in data:
	if len(d) < 100:
		new.append(d)
print('長度小於100的留言有', len(new), '筆')
print(new[0])