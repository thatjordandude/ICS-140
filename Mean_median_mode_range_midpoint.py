
data = [30,20,40,10,60,90,50]

# Mean

print('Mean:', sum(data)/len(data))

# median

data.sort()
middle_index = len(data) // 2 
if len(data) % 2 == 0:
    median = (data[middle_index - 1] + data[middle_index]) / 2
else:
    median = data[middle_index]

print('Median:',median)

# mode
mode_count = {}
for item in data:
    if item in mode_count:
        mode_count[item]+=1
    else:
        mode_count[item]=1
mode=[]
max_count = max(mode_count.values())
for item, count in mode_count.items():
    if count == max_count:
        mode.append(item)
print('Modes(s) is/are:', mode)

# midrange

midrange = (min(data) + max(data)) / 2
print('Midrange is:', midrange)

