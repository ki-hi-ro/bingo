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

def main():
  card = generate_card()
  print_card(card)

if __name__ == "__main__":
  main()