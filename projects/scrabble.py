letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]


letter_to_points = dict(zip(letters, points))

letter_to_points[" "] = 0

def score_word(word):
    point_total = 0
    for letter in word:
        point_total += letter_to_points.get(str.capitalize(letter), 0)
    return point_total

brownie_points = score_word("Brownie")

player_to_words = {"player1": ["Blue", "Tennis", "Exit"], "wordNerd": ["Earth", "Eyes", "Machien"], "LexiCon": ["Eraser", "Belly", "Husky"], "ProfReader": ["Zap", "Coma", "Period"]}

player_to_points = {}

for player, words in player_to_words.items():
    player_points = 0
    for word in words:
        word_point = 0
        word_point = score_word(word)
        player_points += word_point
    player_to_points[player] = player_points

print(player_to_points)
print(score_word("exit"))