
if __name__ == '__main__':
   N = int(input())
   number_list = list(map(float, input().split()))
   sum = 0.00
   maxs = max(number_list)
   for i in range(0, N):
       sum = sum + number_list[i] / maxs * 100

   print(sum /N)