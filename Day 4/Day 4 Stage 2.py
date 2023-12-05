def main():
    with open("input.txt", "r") as f:
        cards = [i for i in f]

    totalCards = [1] * len(cards)

    for idx, card in enumerate(cards):
        cardsWon = 0
        card = card.split(":")[1].strip()
        winningNumbers = card.split("|")[0].split(" ")
        myNumbers = card.split("|")[1].split(" ")
        for num in myNumbers:
            if num and num in winningNumbers:
                cardsWon += 1

        for i in range(cardsWon):
            totalCards[idx + i + 1] += totalCards[idx]

    return sum(totalCards)


if __name__ == "__main__":
    print(main())