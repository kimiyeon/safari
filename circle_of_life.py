from animal import Animal

def print_TODO(todo):
    print(f'<<< NOT IMPLEMENTED: {todo} >>>')

class CircleOfLife:
    def __init__(self, world_size, num_zebras, num_lions):
        self.occupancy = [[' ' for _ in range(world_size)]
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
        for i in range(len(self.occupancy)):
            print(i, end = '  ')     
        print()     
        # grid = []
        # i = int(0)
        # for i in range(length):
        #     grid.append(['*'] * height)

        # for i in range(len(self.occupancy)):
        #     grid.append(' ')
        for i, x in zip(range(1, 21, 1),(self.occupancy)):
            print(i, x)
        # for i in range(len(self.occupancy)):
        # grid = [[ _ for i in range(1, 21, 1)
        #     for x in self.occupancy]
        #     print(grid)
                
        # for i in grid:
        #     grid[i+1] = 'L'
        # for i in world_size:
        #     animal[i][i] = 'A'
        # print('\n'.join(' '.join(row) for row in animal))
        # for i in range(len(grid)):
        #     grid[i] = 'L'
        # for i in self.lions:
        #     grid.append('L')
        # for line in grid:
        #     print(line)

        # top_coord_str = ' '.join([f'{coord}' for coord in range(len(self.occupancy))])
        # print(top_coord_str)
        # world_size = 20
        # for i in range(world_size):
        #     print(i)
        for animal in self.zebras:
            self.occupancy[animal.y][animal.x] = 'Z'
        for animal in self.lions:
            self.occupancy[animal.y][animal.x] = 'L'
      
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
    safari = CircleOfLife(20, 5, 2)
    safari.run(2)