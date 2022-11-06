# https://codeforces.com/problemset/problem/1539/B
def Love_Song():
    song_length, questions = input(
        "Enter the length of the song AND THEN Enter the number of questios ").split(" ")
    song = input("Enter the songs lyrics: ")
    result_list = []
    for i in range(0, int(questions)):
        result = 0
        questions_lower_bound, questions_upper_bound = input(
            "Enter the lower bound AND THEN Enter the upper bound: ").split(" ")
        questions_lower_bound = int(questions_lower_bound) - 1
        questions_upper_bound = int(questions_upper_bound)
        for j in range(questions_lower_bound, questions_upper_bound):
            result = result + ord(song[j]) - 96
        result_list.append(result)
    for i in range(0, int(questions)):
        print(result_list[i])


Love_Song()
