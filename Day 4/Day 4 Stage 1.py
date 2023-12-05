def main():
    with open("input.txt", "r") as f:
        cards = [i for i in f]

    totalValue = 0
    for card in cards:
        cardValue = 0
        card = card.split(":")[1].strip()
        winningNumbers = card.split("|")[0].split(" ")
        myNumbers = card.split("|")[1].split(" ")
        for i in myNumbers:
            if i and i in winningNumbers:
                if cardValue == 0:
                    cardValue += 1
                else:
                    cardValue *= 2
        totalValue += cardValue
    return totalValue

if __name__ == "__main__":
    print(main())