# sports-lottery-calc


>這支程式是個簡潔的「運彩過關組合計算器」它能根據你下注的場次、賠率（odds）、過關組合（例如兩關、三關...）自動幫你算出總投注金額、總中獎金額與獲利。
我們可以一步步拆解，讓你完全理解怎麼「用」它。

---

## 一、基本概念

在運彩（或博彩）中，「過關組合」是指你把多場比賽組合成一張投注單。
例如你選了 3 場比賽：

 - A 賠率 2.8

 - B 賠率 2.8

 - C 賠率 3.0

你可以：

 - 單場投注（一關）：A、B、C 各自一注。

 - 兩關組合：AB、AC、BC。

 - 三關組合：ABC。

這支程式的目的，就是把這些組合依據你設定的「下注金額」與「賠率」自動算出所有組合的中獎金額總和與總投注成本。

---
## 二、如何使用這支程式
(1) 設定每種組合的投注金額

```python
one_game_combin = GameCombin(bet=100, size=1)  # 一關，每注100元
two_game_combin = GameCombin(bet=10, size=2)   # 兩關，每注10元
three_game_combin = GameCombin(bet=10, size=3) # 三關，每注10元
four_game_combin = GameCombin(bet=0, size=4)   # 四關不玩
five_game_combin = GameCombin(bet=0, size=5)   # 五關不玩
six_game_combin = GameCombin(bet=0, size=6)    # 六關不玩
```
這裡的 `size` 表示幾關（組合幾場），`bet` 是每組合的下注金額。

(2) 設定你的賠率清單
```python
odds_list = [2.8, 2.8, 0]  # 如果輸掉的場次就設定為 0
```
這表示你有三場比賽，賠率分別是 2.8、2.8、0。
0 通常代表這場輸掉或未中。

(3) 計算總結果

程式的核心運算是：
```python
total = sum(multiplication(odds_list, two_game_combin))
total += sum(multiplication(odds_list, three_game_combin))
...
```
這幾行會根據你的設定，逐一跑每種過關組合，把中獎金額加總起來。
同時，`PAYMENT` 這個全域變數會統計你「總共投注了多少金額」。

(4) 最後輸出結果
```python
print(f"總共支付: {PAYMENT}\t中獎金額: {total}\t獲利: {total-PAYMENT}")
```

這行會輸出三個重要數據：

- 總共支付：你總共下注的金額。

- 中獎金額：所有組合中獎後的回報。

- 獲利：中獎金額 - 總投注。
---

⚖️ 授權

本程式採用 MIT License，自由使用與修改。

---

👨‍💻 作者

Jerry Yang

📧 Email: jerry9517538462@gmail.com

📅 2025
