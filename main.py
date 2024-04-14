from quests import cards
from random import randint

def main():
    slots = (list(cards.items()), [], [])
    box_chance_mul = [4, 2, 1]
    while True:
        wts = [len(i) * box_chance_mul[idx] for idx, i in enumerate(slots)]
        f = randint(1, sum(wts)) - 1
        box_idx = 0
        a = 0
        n = 0
        for idx, i in enumerate(wts):
            a += i
            if f < a:
                box_idx = idx
                n = f - a + i
                break
        box = slots[box_idx]
        q, a = box.pop(n // box_chance_mul[box_idx])
        print(chr(27) + "2J")
        # print(box_idx, f, n)
        print(q)
        print("~" * 10)
        input("The answer is : ")
        o = input(f" The answer was : {a}\n Was the answer correct? (Y/N) : ")
        print("~" * 10)
        if not o or o[0].lower() == "Y":
            box_idx = min(box_idx + 1, len(slots) - 1)
        elif o[0].lower() == "N":
            box_idx = max(box_idx - 1, 0)
        else:
            break
        slots[box_idx].append((q, a))
        if len(cards) == len(slots[-1]):
            print(f" You have memorised all {len(cards)} cards")
            k = input("Do you want to exit? (Y/N) : ")
            if o and o[0].lower() == "Y":
                break

if __name__ == "__main__":
    main()