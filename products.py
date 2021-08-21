
products = []
while True: # 在不確定重複執行幾次狀況下用 while
    name = input('輸入商品名稱') # 讓使用者輸入商品名稱 用 name變數裝
    if name == 'q': # 如果 name 等於字串 q
        break # 強制退出
    price = input('輸入價格') # 請使用者輸入價格 用 price變數裝
    products.append([name, price]) # 新增 商品名稱與價格的清單到 products清單裡
print(products)
