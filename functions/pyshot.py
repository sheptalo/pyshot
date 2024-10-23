import random
import sys
import time


class Game:
    def __init__(self, name):
        self.health_model = '⚡'
        self.ammo_symbols = ['📗', '♦️']
        self.user_name = name
        self.player = 4
        self.dealer = 4
        self.ammo = []
        self.current = 0
        self.damage = 1
        self.match = 1
        self.player_items = {
            'med': 0,
            'Krit': 0,
            'inspect': 0
        }

    def game_process(self):
        if len(self.get_ammo_list()) == 0 or '📗' not in self.ammo or '♦️' not in self.ammo:
            self.generate_ammo()
            new_items = self.give_items()
            game.current = 0
            for i in new_items:
                self.get_item(input(f'Взять {i}?\n1-Да\n2-Нет'), i)


        print(' '.join(self.get_ammo_list()))

        if self.current == 0:
            print('Ваш ход')
            action = input('В кого стрелять? '
                           + '\n1 - в себя'
                           + '\n2 - в DEALER'
                           + ('\n5-Использовать пилу' if self.player_items['Krit'] > 0 else '')
                           + ('\n6-Использовать лупу' if self.player_items['inspect'] > 0 else '')
                           + ('\n7-вылечиться' if self.player_items['med'] > 0 else ''))
            if action in '12':
                self.shoot(action, 'player')
            elif action in '567':
                self.use_item(int(action))
            time.sleep(3)
        elif game.current == 1:
            print('Ходит дилер')
            self.shoot(game.dealer_ai(), '')
            time.sleep(3)

    @property
    def game(self):
        if not (game.dealer > 0 and game.player > 0):
            if self.match == 3:
                return False

            self.player_items = {
                'med': 0,
                'Krit': 0,
                'inspect': 0
            }
            self.match += 1

            self.player = 4 * self.match
            self.dealer = 4 * self.match
            print(f'Начинаем новый раунд {self.match}')
        return True

    def print_health(self):
        dealer = self.health_model * self.dealer
        player = self.health_model * self.player
        if game.game:
            self.print_blink(f'Ваше здоровье {player[:-1]}', player[-1])
            self.print_blink(f'Здорорвье дилера {dealer[:-1]}', dealer[-1])
            print('\n\n\n\n\n')

    def generate_ammo(self):
        amount = random.randint(3, 10)
        self.ammo = [random.choice(self.ammo_symbols) for _ in range(amount)]

    def get_ammo_list(self):
        return sorted(self.ammo)

    def shoot(self, x, who):
        if x == '1':
            if self.ammo[0] == '♦️':
                if who == 'player':
                    self.player -= self.damage
                    self.current = 1
                    print('Вы выстрелили в себя')

                else:
                    self.dealer -= self.damage
                    self.current = 0
                    print('Дилер выстрелил в себя')
                self.print_health()

            else:
                print('к счастью обошлось без выстрела')
        else:
            if self.ammo[0] == '♦️':
                if who == 'player':
                    self.dealer -= self.damage
                else:
                    self.player -= self.damage
                print('Выстрел произошел')
                self.print_health()

            else:
                if who == 'player':
                    self.current = 1
                else:
                    self.current = 0
        self.ammo.pop(0)
        print('\n\n\n\n')
        self.damage = 1

    def dealer_ai(self):
        if '📗' not in self.ammo:
            return '2'

        green_count = self.ammo.count('📗')
        red_count = self.ammo.count('♦️')
        if green_count == red_count:
            return random.randint(1, 2)
        elif green_count > red_count:
            return '1'
        else:
            return '2'

    def give_items(self):
        items = ['Krit', 'inspect', 'med']
        return [random.choice(items) for _ in range(random.randint(0, 3))]

    def get_item(self, take, item):
        if take == '1':
            self.player_items[item] += 1

    def use_item(self, item, user='player'):
        items = ['Krit', 'inspect', 'med']
        item -= 5

        if self.player_items[items[item]] >= 1:
            self.player_items[items[item]] -= 1
        item = items[item]

        if item == 'Krit':
            self.damage = 2
        if item == 'inspect':
            print(self.ammo[0])
        if item == 'med':
            if user == 'player':
                self.player += 1
            else:
                self.dealer += 1

    def print_blink(self, text, text_to_blink):
        for i in range(4):
            sys.stdout.write('\r' + text + text_to_blink)
            sys.stdout.flush()
            time.sleep(.3)
            sys.stdout.write('\r' + text)
            sys.stdout.flush()
            time.sleep(.3)


if __name__ == '__main__':
    game = Game(input('Введите ваше имя ->'))
    game.generate_ammo()

    while game.game:
        game.game_process()
