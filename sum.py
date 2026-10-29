

def process_scores():
    scores = list(map(float, input(
        "Enter scores separated by spaces: "
    ).split()))

    if len(scores) == 0:
        print("No scores entered.")
        return

    total = sum(scores)
    average = total / len(scores)

    print("Scores:", scores)
    print("Sum:", total)
    print("Average:", round(average, 2))
    print("Maximum score:", max(scores))
    print("Minimum score:", min(scores))



if __name__ == "__main__":
    process_scores()
