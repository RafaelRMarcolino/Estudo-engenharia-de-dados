# Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score. You are given 
#  scores. Store them in a list and find the score of the runner-up.

# Input Format

# The first line contains . The second line contains an array   of  integers each separated by a space.

# Constraints

# Output Format

# Print the runner-up score.

# Sample Input 0

# 5
# 2 3 6 6 5
# Sample Output 0

# 5
# Explanation 0

# Given list is . The maximum score is , second maximum is . Hence, we print  as the runner-up score.


a = "2 3 6 6 5"

# x = [int(n) for n in a.split()]
# print(max(x))


# list = []
# n = int(input(""))
# arr3=[1, 2, 5, 8]

# for i in range(0, n):

#     ele = int(input())
#     list.append(ele)
#     for i in list:
#         if(i not in arr3):
#             arr3.append(i)
#     arr3.sort()
#     x=len(arr3)
#     print(arr3[x-2])

if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())

my_array = list(arr)

print(
    max([x for x in my_array if x != max(my_array)])
)