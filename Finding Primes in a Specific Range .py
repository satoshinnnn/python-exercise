# finding primes in a specific range
primes = []
for x in range(3,20):
    for i in range(2,x):
        if x % i == 0:    # nếu x không phải số nguyên tố thì nó sẽ chia hết cho một số nào đó nhỏ hơn nó trước khi x có thể gặp chính bản thân mình
            break
    else:      # else sẽ được thực thi nếu vòng lặp kết thúc một cách tự nhiên, tức là không gặp câu lệnh break.
        primes.append(x)
print(primes)

# summary: tóm lại là vòng lặp i sẽ kiểm tra các số đến khi nào gặp x chia hết cho i sẽ loại luôn và chạy vòng mới nếu x không chia hết cho bất kì i nào thì tìm ra được một số nguyên tố, và yên tâm kết quả tìm số nguyên tố sẽ luôn đúng vì x chỉ có thể chia hết các số nhỏ hơn nó 
