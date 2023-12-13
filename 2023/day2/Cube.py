import re
def game_calculator(raw):
    global valid_sum
    valid_sum = 0
    #TODO write logic that analyzes if the current line is valid game
    data = raw
    #regex will match each new line, separate ID into group 1 and sets into group 2. technically able to skip looping by making a better regex, but I'm not there yet
    pattern = re.compile(r'Game (\d+):((?:[^;\n]+(?:;\s*)?)+)\n?')
    
    matches = pattern.finditer(data)

    for match in matches:
        game_id = match.group(1)
        sets_str = match.group(2)

        sets = [set.strip() for set in sets_str.split(";")]
        validity = True
        print(f"Game ID: {game_id}")
        print(f"Sets:")

        for s in sets:
            color_counts = {color: int(count) for count, color in (item.split() for item in s.split(','))}
            print (color_counts)
            
            if any(color_counts[color] > valid_cubes.get(color, 0) for color in color_counts):
                print("Invalid set! Breaking.")
                validity = False
                break
        if validity == True:
            valid_sum += int(game_id)
            valid_games.append(game_id)
        else:
            pass
        print("----------")


def cube_conundrum(file):

    with open(file, 'r') as f:
        cube_doc = f.read()
    game_calculator(cube_doc)


def main():
    #TODO run programs
    file = "C:\\Users\\Admin\\Documents\\code\\adventofcode\\2023\\day2\\input.txt"
    cube_conundrum(file)
    print(f"Valid Games: {valid_games}\n Sum of valid IDs: {valid_sum}.")


valid_cubes = {'red': 12, 'green': 13, 'blue': 14}
valid_games = []
if __name__ == "__main__":
    main()
