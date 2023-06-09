# 把所有程式碼改成function 專有名詞叫做 refactor 重構
# 建立記帳程式
# 二為清單建立
# 寫入檔案
# 加入欄位名稱
# 加入可讀取檔案及split切割功能
# continue 跳到下一迴的意思，但必須在迴圈內才能作用，不會跳出迴圈
# 檢查檔案在不在
# function內部最好只執行一件事，不要過於複雜。
import os #operating system

#讀取檔案
def read_file(filename):
    products = []
    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            if '品名,價格' in line:
                continue # 繼續，不會跳出迴圈
            name, price = line.strip().split(',') # split 切割的意思,分行之類的,如例子遇','換行
            products.append([name, price])
    return products

# 讓使用者輸入
def user_input(products):     
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
    return products

# 印出所有購買紀錄
def print_products(products):
    for p in products:
        print(p[0], '的價格是', p[1])

# 字串可以用+跟* 如 'ab' + 'ab'= 'abab' 'ab' * 3 = 'ababab'

#寫入檔案
def write_file(filename, products):
    with open (filename, 'w', encoding='utf-8') as f: # 文字讀取編碼要在這加入
        f.write('品名,價格\n' )
        for p in products:
            f.write(p[0] + ',' + p[1] + '\n') # 有','excel才會不同格 \n生成後會自動換行

#檢查檔案在不在 & 主要執行程式main function寫法
def main(): # 寫程式常用寫法main function 來裝主要執行程式碼
    filename = 'products.csv'
    if os.path.isfile(filename):
        print('有')
        products = read_file(filename)
    else:
        print('找不到檔案')

    products = user_input(products)
    print_products(products)
    write_file('products.csv', products)

main()

# # 練習寫入檔案
# data = [1, 3, 5, 7, 9]
# with open('test.txt', 'w') as test:
#     for c in data:
#         test.write(str(c) + '\n')
# # 解答寫法
# # data = [1, 3, 5, 7, 9]
# # with open('file.txt', 'w') as f:
#     # for d in data:
#         # f.write(str(d) + '\n')