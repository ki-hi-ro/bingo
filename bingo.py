import random

class BingoCard:
    def __init__(self):
        self.card = self.generate_card()
        self.marked = [[False] * 5 for _ in range(5)]  # 数字のマーク状態を保持

    def generate_card(self):
        # 各列 (B, I, , G, O) ごとに範囲内のランダムな数字を選ぶ
        card = []
        ranges = [(1, 15), (16, 30), (31, 45), (46, 60), (61, 75)]
        for start, end in ranges:
            column = random.sample(range(start, end + 1), 5)
            card.append(column)

        card[2][2] = "FREE"  # 中央のフリー枠
        return card

    def mark_number(self, number):
        for i in range(5):
            for j in range(5):
                if self.card[i][j] == number:
                    self.card[i][j] = "✖️"
                    self.marked[i][j] = True

    def check_bingo(self):
        # 行と列でビンゴかどうかをチェック
        for i in range(5):
            if all(self.marked[i]):  # 行のビンゴ
                return True
            if all([self.marked[j][i] for j in range(5)]):  # 列のビンゴ
                return True

        # 対角線のビンゴをチェック
        if all([self.marked[i][i] for i in range(5)]):  # 左上から右下
            return True
        if all([self.marked[i][4 - i] for i in range(5)]):  # 右上から左下
            return True

        return False

    def display_card(self):
        print("\nB  I  N  G  O")
        for i in range(5):
            for j in range(5):
                value = self.card[j][i]  # 列ごとに表示
                if isinstance(value, int):
                    print(f"{value:2d}", end=" ")
                else:
                    print(f"{value:>2}", end=" ")
            print()

def play_bingo():
    card = BingoCard()
    card.display_card()

    drawn_numbers = set()
    while True:
        input("Enterで次の番号を引きます...")
        number = random.randint(1, 75)
        while number in drawn_numbers:  # 重複しないようにする
            number = random.randint(1, 75)
        drawn_numbers.add(number)

        print(f"引かれた番号: {number}")
        card.mark_number(number)
        card.display_card()

        if card.check_bingo():
            print("ビンゴ！おめでとうございます！")
            break

# ゲームを開始
play_bingo()