# 建立記帳程式
# 二為清單建立
products = []
while True:
    name = input('輸入品名: ')
    if name == 'q':
        break
    price = input('輸入價格$: ')
    p = []
    # p = [name, price] 比較快的寫法
    p.append(name)
    p.append(price)
    products.append(p) # 更快寫法 products.append([name, price]) 省略上面三行
print(products)

products[0][0] # 存取二為清單