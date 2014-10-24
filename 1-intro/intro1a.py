import string
import random

RUN_COUNTER = 0


def generate_string():
    char_options = string.letters + ' '
    random_string = ''

    while len(random_string) <= 27:
        random_string += random.choice(char_options)

    return random_string


def levenshtein(random_string, goal_string):
    # From wikipedia article on Levenshtein distance
    previous_row = xrange(len(goal_string) + 1)

    for i, c1 in enumerate(random_string):
        current_row = [i + 1]
        for j, c2 in enumerate(goal_string):
            insertions = previous_row[j + 1] + 1 # j+1 instead of j since previous_row and current_row are one character longer
            deletions = current_row[j] + 1       # than s2
            substitutions = previous_row[j] + (c1 != c2)
            current_row.append(min(insertions, deletions, substitutions))
        previous_row = current_row

    return previous_row[-1]


def get_score(goalstring, teststring):
    numSame = 0

    for i in range(len(goalstring)):
        if goalstring[i] == teststring[i]:
            numSame += 1

    score = (float(numSame) / float(len(goalstring))) * 100
    # print 'numSame / len(goalstring): %s' % (score)

    return score


def run(counter):
    goal_string = "methinks it is like a weasel"
    best_score = 0  # Best score in this case will be lowest number
    best_match = ""

    for i in range(1000):
        current_string = generate_string()
        score = get_score(current_string, goal_string)

        # Use number of same letters per string
        if score == 'Perfect match':
            print score
            break
        else:
            if i == 0 or score > best_score:
                best_score = score
                best_match = current_string


        counter += 1

    # Print results & go again.
    print 'Best match after %d runs: %s' % (counter, best_match)
    print 'Score: %.2f' % best_score

    # Kill after 20 times through.
    if counter < 20000:
        run(counter)


run(RUN_COUNTER)

# sample = 'methinks it is like a monkey'
# goal = "methinks it is like a weasel"