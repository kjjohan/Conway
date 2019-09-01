# Class for positions of conways
class Position():
    def __init__(self, row, column):
        self.row = row
        self.column = column

    def print_pos(self):
        print("Position is: [{},{}]".format(self.row, self.column))

# Class for creating Conway object
class Conway():

    # Position is position of Conway
    def __init__ (self, position, alive):
        self.position = position
        self.alive = alive
        self.neighbours = 0
    
    # Counts neighbours 
    # World is a two dimensional array of bool
    def count_neighbours(self, world):

        #Reset the counter to have fresh start
        self.neighbours = 0

        row = self.position.row
        column = self.position.column

        for i in range(row - 1, row + 2):
            if not i < 0 or i > (len(world) - 1):

                for j in range(column - 1, column + 2):
                    if not j < 0 or j > (len(world[0]) - 1):

                        # If Conway at position = True
                        if not(i == row and j == column) and world[i][j]:
                            self.neighbours += 1
    
    # Updates the life status of the Conway
    def update_life_status(self):

        if (self.neighbours <= 1 or self.neighbours >= 4):
            self.alive = False
        elif self.neighbours == 3:
            self.alive = True


# This class with check the life status of Conways and handle them. It will also handle the initial Conwoys
# Only this class should update the world
class Conway_handler():

    # Appends all the starting conways
    # Correct the world
    # initial_conways is the starting objects
    def __init__(self, initial_positions, world):

        initial_conways = []

        for pos in initial_positions:
            initial_conways.append(Conway(pos, True))
            # Have in mind if row or column should be first
            world[pos.row][pos.column] = True

        self.conway_list = initial_conways
        self.world = world 
        self.temp_list = []
    
    # Checks around all the alive conways and determine if the dead one should be spawned
    def spawn_new_conways(self):

        self.temp_list = []
        empty_cells = []
        visited_list = []

        # For every conway alive, check for surrounding dead cells, and check if they should be spawned
        for conway in self.conway_list:
            row = conway.position.row
            column = conway.position.column

            # Checks around every live Conway to see if there are any empty cells to be potentially revived

            for i in range(row - 1, row + 2):
                if not i < 0 or i > (len(world) - 1):

                    for j in range(column - 1, column + 2): 
                        if not j < 0 or j > (len(world[0]) - 1):

                            # This works but should be made nicer
                            new_str = str(i) + str(j)
                            if new_str not in visited_list:
                                # If the cell is false
                                if(not(self.world[i][j])):
                                    empty_cells.append(Conway(Position(i,j), False))

                                visited_list.append(new_str)
            
        # If the empty cell becomes alive it shall be added to the temp list 
        for cell in empty_cells:
            cell.count_neighbours(self.world)
            cell.update_life_status()
            if cell.alive:
                self.temp_list.append(cell)
    
    
    def update_conwoys(self):
        killed_conways = []
        
        # Update temp_list
        self.spawn_new_conways()

        # Update all alive conways
        for conway in self.conway_list:
            conway.count_neighbours(self.world)
            conway.update_life_status()
        
        # Kill conways
        for conway in self.conway_list:    
            conway.position.print_pos()
            print("Neighbours nr: {}".format(conway.neighbours))
            print(conway.alive)
            if(not(conway.alive)):
                killed_conways.append(conway)
                self.world[conway.position.row][conway.position.column] = False

        for killed in killed_conways:
            self.conway_list.remove(killed)
        
        print("\n")
        # Now add the new Conways
        for new_conway in self.temp_list:
            #print("Conway nr: {}".format(conway.neighbours))
            self.conway_list.append(new_conway)
            self.world[new_conway.position.row][new_conway.position.column] = True



if __name__ == '__main__':
    start_positions = []
    world_width = 10
    world_height = 10

    # Creates a world 10x10 of False bool
    world = [[False for x in range(world_width)] for y in range(world_height)]    

    # Append start objects to list
    start_positions.append(Position(0,0))
    start_positions.append(Position(0,2))
    start_positions.append(Position(2,0))
    start_positions.append(Position(2,2))
    start_positions.append(Position(1,1))

   

    # Create handler with start objects and a specific world
    handler = Conway_handler(start_positions, world)
    
    for i in range(10):
        print(handler.world[i]) 

    handler.spawn_new_conways()
    handler.update_conwoys()

    print("\n")
    for i in range(10):
        print(handler.world[i])

