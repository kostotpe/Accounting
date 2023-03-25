# 建立記帳程式
# 二為清單建立
# 寫入檔案
# 加入欄位名稱
products = []
while True:
    name = input('輸入品名: ')
    if name == 'q':
        break
    price = input('輸入價格$: ')
    p = []
    # p = [name, price] 比較快的寫法
    p.append(name)
    p.append(price) # 存取二為清單 products[0][0]
    products.append(p) # 更快寫法 products.append([name, price]) 省略上面三行
print(products)

for p in products:
    print(p[0], '的價格是', p[1])

# 字串可以用+跟* 如 'ab' + 'ab'= 'abab' 'ab' * 3 = 'ababab'

with open ('products.csv', 'w', encoding='utf-8') as f: # 文字讀取編碼要在這加入
    f.write('品名,價格\n' )
    for p in products:
        f.write(p[0] + ',' + p[1] + '\n') # 有','excel才會不同格 \n生成後會自動換行

# 練習寫入檔案
data = [1, 3, 5, 7, 9]
with open('test.txt', 'w') as test:
    for c in data:
        test.write(str(c) + '\n')
# 解答寫法
# data = [1, 3, 5, 7, 9]
# with open('file.txt', 'w') as f:
    # for d in data:
        # f.write(str(d) + '\n')