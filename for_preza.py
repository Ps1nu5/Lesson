import random

score = {'bot': 0, 'player': 0}
player_choice = ''
bot_choice = ''
game_run = True


def get_player_choice():
    global player_choice
    player_choice = input('Ващ выбор[К / Н / Б]: ').lower()


def generate_bot_choice():
    global bot_choice
    bot_choice = random.choice('кнб')


def check_wins():
    if player_choice == bot_choice:
        print('Ничья!\n')

    elif player_choice == 'к' and bot_choice == 'н':
        score['player'] += 1
    elif player_choice == 'к' and bot_choice == 'б':
        score['bot'] += 1

    elif player_choice == 'н' and bot_choice == 'б':
        score['player'] += 1
    elif player_choice == 'н' and bot_choice == 'к':
        score['bot'] += 1

    elif player_choice == 'б' and bot_choice == 'к':
        score['player'] += 1
    elif player_choice == 'б' and bot_choice == 'н':
        score['bot'] += 1


def game():
    global score
    while game_run:
        get_player_choice()
        generate_bot_choice()

        print(f'Ваш выбор: {player_choice}\n'
              f'Выбор бота: {bot_choice}\n')

        check_wins()

        if score['player'] > score['bot']:
            print('Вы ведёте в игре!')
        elif score['bot'] > score['player']:
            print('В игре ведёт бот!')
        else:
            print('Вы сравнялись с ботом!')

        next_turn = input('Продолжить игру?\n'
                          'Введите [Д / Н]').lower()

        if next_turn != 'д':
            print(f'Финальный счёт:\n'
                  f'Ваши очки: {score["player"]}\n'
                  f'Очки бота: {score["bot"]}\n')
            break


game()
