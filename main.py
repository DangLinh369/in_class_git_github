print('Hello từ Vịt Vàng ���')
datas = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
def Numbers(numb):
    results = []
    for i in range(len(datas)):
        if i > 2:
            print(datas[i]) 
        else:
            continue
    return
Numbers(datas)
print(Numbers)



#Bài 1 tuần 2 hoàn chỉnh
num_k_list = []
result_max_list = []

def get_max_list(num_list, k):
    for i in range(len(num_list) - k + 1):
          num_k_list.append(num_list[i:i+k])
          print("Đoạn", i+1, num_k_list)
          result_max_list.append(max(num_k_list[-1]))
          del num_k_list[0]       # Xóa đoạn đầu tiên

num_list = [3, 4, 5, 1, -44, 5, 10, 12, 33, 1]
k = 3
get_max_list(num_list, k)
print('Ket qua cua day so lon nhat trong num list voi k = 3 la:', result_max_list)