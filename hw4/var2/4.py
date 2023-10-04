with open('class_scores.txt', 'r') as input_file, open('scores2.txt', 'w') as output_file:
    for line in input_file:
        username, score_str = line.strip().split()

        score = int(score_str)
        new_score = score + 5

        output_file.write(f'{username} {new_score}\n')