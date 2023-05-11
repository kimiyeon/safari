from animal import Animal

def print_TODO(todo):
    print(f'<<< NOT IMPLEMENTED: {todo} >>>')

class CircleOfLife:
    def __init__(self, world_size, num_zebras, num_lions):
        self.occupancy = [[False for _ in range(world_size)]
                          for _ in range(world_size)]
        print_TODO('get random empty coordinates')
        self.zebras = [Animal(0, 0) for _ in range(num_zebras)]
        self.lions = [Animal(0, 0) for _ in range(num_lions)]
        self.timestep = 0
        print('Welcome to AIE Safari!')
        print(f'\tworld size = {world_size}')
        print(f'\tnumber of zebras = {len(self.zebras)}')
        print(f'\tnumber of lions = {len(self.lions)}')

    def display(self):
        print(f'Clock: {self.timestep}')
        length = 20
        for i in range(length):
            print(i, end = '    ')
        print()            
        grid = []

        # i = int(0)
        # for i in range(length):
        #     grid.append(['*'] * height)
        # for x in grid:
        #     grid = ('  '.join(x))
        #     print(grid)

        for i in range(length):
            grid.append('*')
        for i in range(1, 21, 1):
            print(i, grid)

        print_TODO('display()')
        key = input('enter [q] to quit:')
        if key == 'q':
            exit()

    def step_move(self):
        print_TODO('step_move()')
        for zebra in self.zebras:
            print_TODO('get empty neighbor')
            direction = 'left'
            zebra.move(direction)
        for lion in self.lions:
            print_TODO('get neighboring zebra')
            print_TODO('move to zebra if found, else move to empty')
            print_TODO('get empty neighbor')
            direction = 'left'
            lion.move(direction)
    
    def step_breed(self):
        print_TODO('step_breed()')
        for animal in self.zebras + self.lions:
            print_TODO('get empty neighbor')
            x, y = 0, 0
            animal.breed(x, y)
    
    def run(self, num_timesteps=100):
        self.display()
        for _ in range(num_timesteps):
            self.timestep +=1
            self.step_move()
            self.display()
            self.step_breed()
            self.display()





if __name__ == '__main__':
    safari = CircleOfLife(5, 5, 2)
    safari.run(2)