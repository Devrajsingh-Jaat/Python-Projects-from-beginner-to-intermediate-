file = "true"
file2 = "love"

def calculate_love_score(firstname, secondname):
    fullname = (firstname + secondname).lower()
    true_count = 0
    love_count = 0
    for i in fullname:
        if i in file:
            true_count += 1
        if i in file2:
            love_count += 1

    score = int(str(true_count) + str(love_count))
    print(score)


calculate_love_score("rutu", "lomo")



