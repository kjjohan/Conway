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

        row = self.position.row
        column = self.position.column

        # Needs to be checked for corned values
        for i in range(row - 1, row + 1):
            for j in range(column - 1, column + 1):
                # If Conway at position = True
                if !(i == row and j == column) and world[i][j]:
                    neighbours += 1
    
    # Updates the life status of the Conway
    def update_life_status(self):

        if (self.neighbours <= 1 or self.neighbours >= 4):
            self.alive = False
        elif self.neighbours == 3:
            self.alive = True


# This class with check the life status of Conways and handle them. It will also handle the initial Conwoys
class Conway_handler():

    # initial_conways is the starting objects
    def __init__(self, initial_positions):

        for pos in initial_positions:
            initial_conways.append(Conway(pos, True))

        self.conway_list = initial_conways
        self.temp_list = []
    
    # Needs some sort of check the cell already has been added
    def spawn_new_conways(self, world):

        self.temp_list = []
        empty_cells = []

        for conway in self.conway_list:
            row = conway.position.row
            column = conway.position.column

            # Checks around every live Conway to see if there are any empty cells to be potentially revived
            # Needs to be checked for corner values
            for i in range(row - 1, row + 1):
                for j in range(column - 1, column + 1): 
                    if(!(world[i][j])):
                        empty_cells.append(Conway(Position(i,j), False))

            # If the empty cell becomes alive it shall be added to the temp list 
            for cell in empty_cells:
                cell.count_neighbours(world)
                cell.update_life_status()
                if cell.alive:
                    self.temp_list.append(cell)
    
    
    def update_conwoys(self):
        # Spawn to a seperate list
        self.spawn_new_conways(world)

        # Kill conways
        for conway in self.conway_list:
            # World needs to be created first
            conway.count_neighbours(world)
            conway.update_life_status():
            if(!(conway.alive)):
                self.conway_list.remove(conway)
        
        # Now add the new Conways
        for new_conway in self.temp_list:
            self.conway_list.append(new_conway)

class Position():
    def __init__(self, row, column):
        self.row = row
        self.column = column


if __name__ = '__main__'():
    # Needs to fix the world thingy

    # Create GUI object
    ###################
    #start_positions = #####
    #handler = Conway_handler(start_positions, True)
