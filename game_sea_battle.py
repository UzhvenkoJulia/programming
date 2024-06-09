import random

HORIZONTAL = 0
VERTICAL = 1

class Entity:
    def __init__(self, position):
        self.position = position

    def get_body(self):
        pass

    def get_area(self):
        pass

class Vessel(Entity):
    def __init__(self, position, orientation, length):
        super().__init__(position)
        self.length = length
        self.orientation = orientation
        self.health = length

    def get_body(self):
        body = []
        if self.orientation == VERTICAL:
            for i in range(self.length):
                body.append((self.position[0] + i, self.position[1]))
        else:
            for i in range(self.length):
                body.append((self.position[0], self.position[1] + i))
        return body

    def get_area(self):
        body = self.get_body()
        area = set() # порожня множина буде використовуватися для зберігання координат клітинок, які оточують тіло об'єкта (судна чи міни).
        # Вона буде використовуватися для позначення зони навколо судна або міни, де не можуть знаходитися інші судна чи міни
        for x, y in body:
            for dx in [-1, 0, 1]:
                for dy in [-1, 0, 1]:
                    new_xy = (x + dx, y + dy)
                    if new_xy not in body:
                        area.add(new_xy)
        return area

    @classmethod
    def generate(cls, shape, length): # cls - вказує на сам клас, а не на конкретний екземпляр класу
        max_x, max_y = shape
        '''generate створює випадкове розташування корабля на мапі, враховуючи його довжину та розмір мапи'''
        for _ in range(100):
            x, y = random.randrange(max_x), random.randrange(max_y)
            orientation = random.choice([HORIZONTAL, VERTICAL])
            if orientation == VERTICAL and x + length <= max_x:
                return cls((x, y), orientation=orientation, length=length)
            elif orientation == HORIZONTAL and y + length <= max_y:
                return cls((x, y), orientation=orientation, length=length)
        raise ValueError("створити судно не вдалося")

    def __repr__(self):
        return 'Vessel'

class Mine(Entity):
    def __init__(self, position):
        super().__init__(position)

    def get_body(self):
        return [self.position]

    def get_area(self):
        body = self.get_body()
        area = set()
        for x, y in body:
            for dx in [-1, 0, 1]:
                for dy in [-1, 0, 1]:
                    new_xy = (x + dx, y + dy)
                    if new_xy != (x, y):  # перевірка, щоб уникнути додавання початкової позиції
                        area.add(new_xy)
        return area

    @classmethod
    def generate(cls, shape, vessels):
        potential_positions = set()
        for vessel in vessels:
            for x, y in vessel.get_area():
                for dx in [-1, 0, 1]:
                    for dy in [-1, 0, 1]:
                        possible_position = (x + dx, y + dy)
                        if 0 <= possible_position[0] < shape[0] and 0 <= possible_position[1] < shape[1]:
                            potential_positions.add(possible_position)
        if not potential_positions:
            raise ValueError("доступних позицій для міни нема")
        return cls(random.choice(list(potential_positions)))

    def __repr__(self):
        return 'Mine'

class Map:
    config = {
        'vessels': {
            1: 4,  # 4 канонерські човни - 1 клітинка
            2: 3,  # 3 бриги - 2 клітинки
            3: 2,  # 2 фрегати - 3 клітинки
            4: 1   # 1 лінійний корабель - 4 клітинки
        },
        'mine': {
            1: 2   # 2 міни
        }
    }

    def __init__(self, shape):
        self.shape = shape
        self.entities = []

        # сітка з неприсвоєними значеннями для кожної клітинки
        self.grid = [[None for _ in range(self.shape[1])] for _ in range(self.shape[0])]
        # масив для відстеження промахів пострілів, де 0 відповідає промаху
        self.misses = [[0 for _ in range(self.shape[1])] for _ in range(self.shape[0])]
        # масив для відстеження областей, які можуть бути зайняті кораблями
        self.areas = [[None for _ in range(self.shape[1])] for _ in range(self.shape[0])]
        # масив для відстеження зайнятих клітинок на карті, де 0 відповідає вільній клітинці
        self.occupied = [[0 for _ in range(self.shape[1])] for _ in range(self.shape[0])]

    def add_vessel(self, vessel):
        for x, y in vessel.get_body():
            if x < 0 or x >= self.shape[0] or y < 0 or y >= self.shape[1]:
                raise ValueError("судно поза картою")
            if self.occupied[x][y]:
                raise ValueError("ця позиція вже зайнята")
        self._add_entity(vessel, area_occupied=True)

    def add_mine(self, mine):
        for x, y in mine.get_body():
            if x < 0 or x >= self.shape[0] or y < 0 or y >= self.shape[1]:
                raise ValueError("міна поза картою")
            if self.occupied[x][y]:
                raise ValueError("ця позиція вже зайнята")
        self._add_entity(mine, area_occupied=False)

    # _add_entity використовується лише всередині класу Map для додавання об'єктів на ігрове поле - метод приватний
    def _add_entity(self, entity, area_occupied):
        body_coords = entity.get_body()
        area_coords = entity.get_area()

        # оновлення зайнятості та сітки для кожної клітинки тіла нашого
        for x, y in body_coords:
            self.occupied[x][y] = 1
            self.grid[x][y] = entity # комірці grid за координатами (x, y) значення entity;
            # grid відображає ігрове поле, а entity представляє собою об'єкт (або екземпляр класу),
            # який розміщується на цій комірці поля. Таким чином, коли гравець розміщає корабель або міну на полі,
            # йде оновлення значення комірки grid, вказуючи на те, що на цій комірці знаходиться відповідний об'єкт

        # оновлення зайнятості та області для кожної клітинки області
        for x, y in area_coords:
            if 0 <= x < self.shape[0] and 0 <= y < self.shape[1]:
                if area_occupied:
                    self.occupied[x][y] = 1
                self.areas[x][y] = entity

        self.entities.append(entity)

    @classmethod
    def generate(cls, shape, max_tries=100):
        instance = cls(shape)
        vessels = []

        for length, amount in cls.config['vessels'].items(): # ітерація по елементам словника cls.config['vessels']; ключ-значення (ключ є довжиною корабля, а значення - кількістю кораблів такої довжини)
            for _ in range(amount):
                for _ in range(max_tries):
                    try:
                        vessel = Vessel.generate(shape, length)
                        instance.add_vessel(vessel)
                        vessels.append(vessel)
                        break
                    except ValueError:
                        continue
                else:
                    raise ValueError("не вдалося створити карту")

        for _ in range(cls.config['mine'][1]):
            for _ in range(max_tries):
                try:
                    mine = Mine.generate(shape, vessels)
                    instance.add_mine(mine)
                    break
                except ValueError:
                    continue
            else:
                raise ValueError("не вдалося створити карту")

        return instance

    def show(self, show_all=True):
        board = [[' '] * self.shape[1] for _ in range(self.shape[0])] #  двовимірний список board, який представляє собою дошку або поле з певними розмірами
        # self.shape[0] визначає кількість рядків у дошці
        # self.shape[1] визначає кількість стовпців у дошці

        for entity in self.entities:
            if show_all or isinstance(entity, Mine):
                for (x, y) in entity.get_area():
                    if 0 <= x < self.shape[0] and 0 <= y < self.shape[1]:
                        board[x][y] = '.'
            for (x, y) in entity.get_body():
                if isinstance(entity, Mine):
                    board[x][y] = 'o' if show_all else ' '
                else:
                    board[x][y] = 'x' if show_all else ' '

        for x in range(self.shape[0]):
            for y in range(self.shape[1]):
                if self.misses[x][y] == '.':
                    board[x][y] = '.'  # пропущений удар
                elif self.misses[x][y] == 'x':
                    board[x][y] = 'x'  # підбити, знищити судно
                elif self.misses[x][y] == 'o':
                    board[x][y] = 'o'  # міна підірвалася

        '''фрагмент коду виводить горизонтальні лінії та зміст board у вигляді матриці
        print('-' * (self.shape[1] * 2 + 3)) виводить горизонтальну риску, яка відокремлює верхню частину матриці від нижньої. 
        Довжина цієї риски залежить від ширини board та добавлена додаткова ширина для лівого та правого бордерів
        
        потім кожен рядок row у board виводиться окремо
        
        у кожному рядку виводяться елементи, розділені пробілами, за допомогою методу join. 
        Перед кожним рядком та після нього виводиться вертикальна риска |, що відокремлює клітинки від бордерів
        
        print('-' * (self.shape[1] * 2 + 3)) виводить горизонтальну риску, аналогічну першій, розділяючи нижню частину матриці'''

        print('-' * (self.shape[1] * 2 + 3))
        for row in board:
            print('|', ' '.join(row), '|')
        print('-' * (self.shape[1] * 2 + 3))

    def show_for_user(self):
        board = [[' '] * self.shape[1] for _ in range(self.shape[0])]

        for x in range(self.shape[0]):
            for y in range(self.shape[1]):
                if self.misses[x][y] == '.':
                    board[x][y] = '.'
                elif self.misses[x][y] == 'x':
                    board[x][y] = 'x'
                elif self.misses[x][y] == 'o':
                    board[x][y] = 'o'
                elif isinstance(self.grid[x][y], Mine):
                    board[x][y] = 'o'  # показати міни на карті гравця
                elif isinstance(self.grid[x][y], Vessel):
                    board[x][y] = 'x'  # показати кораблі на карті гравця

        print('-' * (self.shape[1] * 2 + 3))
        for row in board:
            print('|', ' '.join(row), '|')
        print('-' * (self.shape[1] * 2 + 3))

    def show_for_enemy(self):
        board = [[' '] * self.shape[1] for _ in range(self.shape[0])]

        for x in range(self.shape[0]):
            for y in range(self.shape[1]):
                if self.misses[x][y] == '.':
                    board[x][y] = '.'
                elif self.misses[x][y] == 'x':
                    board[x][y] = 'x'
                elif self.misses[x][y] == 'o':
                    board[x][y] = 'o'

        print('-' * (self.shape[1] * 2 + 3))
        for row in board:
            print('|', ' '.join(row), '|')
        print('-' * (self.shape[1] * 2 + 3))

    def hit(self, x, y):
        if not (0 <= x < self.shape[0] and 0 <= y < self.shape[1]):
            raise ValueError("координати недійсні")

        entity = self.grid[x][y]
        if entity:
            if isinstance(entity, Vessel):
                self.misses[x][y] = 'x'
                entity.health -= 1
                print(f"судно постраждало на координатах {(x, y)}!")
                if entity.health == 0:
                    print("судно затонуло")
                    self._sink(entity)
            elif isinstance(entity, Mine):
                self.misses[x][y] = 'o'
                print(f"міну здетоновано на координатах {(x, y)}!")
                self._detonate(entity)
        else:
            self.misses[x][y] = '.'
            print(f"пропущений удар на координатах {(x, y)}.")

    def _sink(self, vessel): # функція призначена для позначення підбитого судна на карті гравця
        for (x, y) in vessel.get_body():
            self.misses[x][y] = 'x'

    def _detonate(self, mine): # функція відповідає за вибух міни на карті гравця
        for (x, y) in mine.get_area():
            if 0 <= x < self.shape[0] and 0 <= y < self.shape[1]:
                if isinstance(self.grid[x][y], Vessel):
                    self.grid[x][y].health -= 1
                    self.misses[x][y] = 'x'
                    print(f"потрапило в судно через міну на координатах {(x, y)}!")
                    if self.grid[x][y].health == 0:
                        print("судно затонуло через міни!")
                        self._sink(self.grid[x][y])
                elif isinstance(self.grid[x][y], Mine):
                    self.misses[x][y] = 'o'
                    print(f"ланцюгова реакція, міна на координатах {(x, y)}!")

class Game:
    def __init__(self, shape):
        self.player_map = Map.generate(shape)
        self.bot_map = Map.generate(shape)
        self.shape = shape

    def player_turn(self):
        x, y = self.get_player_input()
        print(f"хід гравця.., стрільба на координатах ({x}, {y})")
        self.bot_map.hit(x, y)
        print("можливість гравця подивитися на карту бота")
        self.bot_map.show_for_enemy()

    def bot_turn(self):
        x, y = self.get_bot_input()
        print(f"черга бота.., стрільба на координатах ({x}, {y})")
        self.player_map.hit(x, y)
        print("карта гравця після ходу бота:")
        self.player_map.show_for_user()

    def get_player_input(self):
        while True:
            try:
                coords = input("введіть координати для удару (x y): ")
                # х - горизонталь, у - вертикаль
                x, y = map(int, coords.split())
                if 0 <= x < self.shape[0] and 0 <= y < self.shape[1]:
                    return x, y
                else:
                    print(f"координати мають бути в межах розміру карти {self.shape}.")
            except ValueError:
                print("неправильні дані.., введіть два цілі числа, розділені пробілом!!")

    def get_bot_input(self):
        return random.randint(0, self.shape[0] - 1), random.randint(0, self.shape[1] - 1)

    def check_winner(self):
        player_vessels = [v for v in self.player_map.entities if isinstance(v, Vessel) and v.health > 0]
        bot_vessels = [v for v in self.bot_map.entities if isinstance(v, Vessel) and v.health > 0]

        if not player_vessels:
            return "Bot"
        if not bot_vessels:
            return "Player"
        return None

    def run(self):
        turn = 0
        while True:
            print(f"\nTurn {turn + 1}")
            if turn % 2 == 0:
                self.player_turn()
            else:
                self.bot_turn()

            winner = self.check_winner()
            if winner:
                print(f"\n{winner} wins!")
                break

            turn += 1

shape = (10, 10)
game = Game(shape)
game.run()
