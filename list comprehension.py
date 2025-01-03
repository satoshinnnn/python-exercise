# Đề bài: yêu cầu nhập vào 4 giá trị x, y, z ,n (biết x, y , z là độ dài của hình hộp chữ nhật)
#         yêu cầu in ra những kết quả của của tọa độ của [i,j,k] trên trục 3D vs i + j + k != n
#         (biết i thuộc x, j thuộc y, k thuộc z)
# GỢI Ý: dùng công thức tạo list " list = [i,j,k] " ~ các giá trị được đặt cùng tên với i, j, k sẽ tự động được đưa vào list đó
# CT của LIST COMPREHENSION: dùng để tạo list theo mong muốn hoặc những giá trị trong list mang giá trị được tính theo công thức
#                   [biểu thức for sth in range() if điều kiện] /
#                   [ biểu thức for sth1 in range1
#                               for sth2 in range2
#                               for sth3 in range3
#                               ...etc
#                               if điều kiện]
x = int(input())
y = int(input())
z = int(input())
n = input()
results = [[i,j,k] for i in range(0,x+1)
                   for j in range(0,y+1)
                   for k in range(0,z+1)
                   if i + j + k != n]
print(results)
