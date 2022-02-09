

def add_score(difficulty):
    points_of_winning = (difficulty * 3) + 5
    points = 0

    try:
        file = open("Scores.txt", "r")
        print('reading')
        points = file.read()
        if points == "":
            points = points_of_winning
        else:
            points = int(points) + points_of_winning

    except FileNotFoundError:
        print("File not found")
        points = points_of_winning

    finally:
        file = open("Scores.txt", "w")
        file.write(str(points))
        file.close()


def read_score():
    file = open("Scores.txt", "r")
    points = file.read()
    file.close()
    return points




