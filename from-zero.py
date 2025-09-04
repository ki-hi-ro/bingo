import random

B_RANGES = [(1, 15), (16, 30), (31, 45), (46, 60), (61, 75)]

def generate_card():
  cols = [random.sample(range(lo, hi + 1), 5) for lo, hi in B_RANGES]
  card = [[cols[c][r] for c in range(5)] for r in range(5)]
  card[2][2] = "FR"
  return card

def print_card(card):
  print('B  I  N  G  O')
  for row in card:
    row_str = ""
    for v in row:
      if v == "FR":
        row_str += " FR "
      else:
        row_str += f"{v:>3} "
    print(row_str)

def main():
  card = generate_card()
  print_card(card)

if __name__ == "__main__":
  main()