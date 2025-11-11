# sum_avg_file.py
f = open("numbers.txt", "r")
nums = f.read().split()
nums = [int(x) for x in nums]
total = sum(nums)
avg = total / len(nums)
print("Sum:", total)
print("Average:", avg)
f.close()
