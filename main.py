from Player import Player
from TicTacToe import TicTacToe
from Result import Result
from Const import X


def set_player_name1(player, prompt="Enter Player X name: "):
    while not player.is_valid():
        name = input(prompt)
        player.name = name


def set_player_name2(player, prompt="Enter Player O name: "):
    while not player.is_valid():
        name = input(prompt)
        player.name = name


def get_position(player):
    pos = input(f"{player.name} - choose your position number: ")
    if not pos.isdigit():
        print("Invalid value")
        print()
        return get_position(player)
    if int(pos) > 9 or int(pos) < 1:
        print("Invalid value")
        print()
        return get_position(player)
    else:
        return int(pos)


def start_game(game, player_X, player_O):
    set_player_name1(player_X)
    set_player_name2(player_O)
    play_again = "Y"
    while play_again == "Y" or play_again == "y":
        game.print()
        if game.turn == X:
            pos = get_position(player_X)
        else:
            pos = get_position(player_O)
        game.move(pos)
        if game_finished(game) == True:
            game.board_reset()
            play_again = input("Do you want to play again? (Y-Yes/N-No): ")
            if play_again == "n" or play_again == "N":
                return


def game_finished(game):
    result = game.get_result()
    if result == Result.X_Won:
        print(f"{player_X.name} has won!")
        print()
        return True
    elif result == Result.O_Won:
        print(f"{player_O.name} has won!")
        print()
        return True
    elif result == Result.Draw:
        print("The game is a draw")
        print()
        return True
    else:
        return False


player_X = Player(set_player_name1)
player_O = Player(set_player_name2)

game = TicTacToe()

start_game(game, player_X, player_O)

