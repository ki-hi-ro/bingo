import random

B_RANGES = [(1, 15), (16, 30), (31, 45), (46, 60), (61, 75)]
CELL_W = 4

def generate_card():
  cols = [random.sample(range(lo, hi + 1), 5) for lo, hi in B_RANGES]
  card = [[cols[c][r] for c in range(5)] for r in range(5)]
  card[2][2] = "FR"
  return card

def print_card(card, marked=None):
  header = "".join(f"{ch:^{CELL_W}}" for ch in "BINGO")
  print(header)

  for r in range(5):
    cells = []
    for c in range(5):
      v = card[r][c]
      if v == "FR":
        s = "[FR]"
      elif marked and marked[r][c]:
        s = f"[{str(v).rjust(2)}]"  
      else:
        s = f"{str(v).rjust(2)}"

      cells.append(f"{s:^{CELL_W}}")

    print("".join(cells))

def new_marked():
  m = [[False]*5 for _ in range(5)]
  m[2][2] = True # FREEは最初からマーク
  return m

def mark_number(card, marked, n):
  for r in range(5):
    for c in range(5):
      if card[r][c] == n:
        marked[r][c] = True
        return True
  return False

def count_lines(marked):
  lines = 0
  for r in range(5):
    if all(marked[r][c] for c in range(5)): lines += 1
  for c in range(5):
    if all(marked[r][c] for r in range(5)): lines += 1  
  if all(marked[i][i] for i in range(5)): lines += 1
  if all(marked[i][4-i] for i in range(5)): lines += 1  
  return lines

def main():
  card = generate_card()
  marked = new_marked()
  pool = list(range(1, 76))
  random.shuffle(pool)
  history = []
  turn = 0

  print_card(card, marked)
  print("Enter=next  h=history  q=quit") 
  
  while True:
    cmd = input("> ").strip().lower()
    
    if cmd == "q":
      print("Bye!")
      break
    if cmd == "h":
      print(f"Called: {', '.join(map(str, history)) or '(none)'}")
      continue
    # Enter(空文字)以外は無視して続行
    if cmd not in ("",):
      continue

    if not pool:
      print("No numbers left. Draw game.")
      break

    # ここから1ターン進行
    n  = pool.pop()
    history.append(n)
    turn += 1

    mark_number(card, marked, n)
    lines = count_lines(marked)

    print(f"\nTurn {turn}  Called: {n}  Remaining: {len(pool)}  Lines: {lines}")
    print_card(card, marked)

    if lines >= 1:
      print("\nBINGO! congrats!")
      break

if __name__ == "__main__":
  main()