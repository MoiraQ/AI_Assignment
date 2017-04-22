
'''

The partially defined functions and classes of this module 
will be called by a marker script. 

You should complete the functions and classes according to their specified interfaces.
 

'''

import search

import sokoban



# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -


def my_team():
    '''
    Return the list of the team members of this assignment submission as a list
    of triplet of the form (student_number, first_name, last_name)
    
    '''
    return [ (9708651, 'Christopher', 'O\'Rafferty'), (9400001, 'Moira', 'Quinn'), (7226209, 'Maurice', 'Cafun') ]

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

def taboo_cells(warehouse):
    '''  
    Identify the taboo cells of a warehouse. A cell is called 'taboo' 
    if whenever a box get pushed on such a cell then the puzzle becomes unsolvable.  
    When determining the taboo cells, you must ignore all the existing boxes, 
    simply consider the walls and the target  cells.  
    Use only the following two rules to determine the taboo cells;
     Rule 1: if a cell is a corner and not a target, then it is a taboo cell.
     Rule 2: all the cells between two corners along a wall are taboo if none of 
             these cells is a target.
    
    @param warehouse: a Warehouse object

    @return
       A string representing the puzzle with only the wall cells marked with 
       an '#' and the taboo cells marked with an 'X'.  
       The returned string should NOT have marks for the worker, the targets,
       and the boxes.  
    '''
     # Variables 
    left_walls = []
    right_walls = []
    deviation_left = []
    deviation_right = []
    legal_area = []
    current_cell = 0
    
    # Get Warehouse as String and Format
    wh = warehouse.__str__()
    # Get Length of Warehouse 
    wh_length = wh.find('\n')
    # Get Cell Where Top Wall Starts
    wall_start_top = wh.find('#') - wh_length

    # Convert Warehouse to List and Format
    # Note: Am Using a list so data can be manipulated
    wh = list(wh)
    # Remove first blank line on warehouse (occurs on import)
    del wh[0:wh_length]; 

    # Variable for Search
    j = wall_start_top+1
    
    # Find ALl Cells Between the Walls of the Warehouse
    for i in range(0,len(wh)):
        # All the Left Walls
        if(wh[i] == '#' and len(left_walls) <= int(i/(wh_length+1))):
            left_walls.append(i)
        # All the Right Walls
        if(i > (wh_length+1) and i%(wh_length+1) == 0 and i-((i/(wh_length+1))*(wh_length+1)) == 0):
            while True:
                if(wh[i-j] == '#'):
                  right_walls.append(i-j)
                  break
                else:
                    j -= 1
        # Reset Offset Variable
        j = wall_start_top+1

    # Format Left Walls to Only Include Playable Area
    del left_walls[0]
    del left_walls[-1]

    # Get the Legal Area (Between the Walls)
    for i in range(0,len(left_walls)):
        for j in range(1,right_walls[i]-left_walls[i]):
            if(wh[left_walls[i]+j] != '#'):
                legal_area.append(left_walls[i]+j)

    # Get Cells Where Wall Deviates on the Left Side
    for i in range(1,len(left_walls)):
        if(left_walls[i]-left_walls[i-1] != wh_length+1):
            deviation_left.append(left_walls[i])

    # Get Cells Where Wall Deviates on the Right Side
    for i in range(1,len(right_walls)):
        if(right_walls[i]-right_walls[i-1] != wh_length+1):
            deviation_right.append(right_walls[i])


##    j = 0
    # Search through each cell of the warehouse
    for i in wh:
        # Check Cell is in Legal Area
        if(current_cell in legal_area):
            # Top Corners on Left Side
            if(wh[current_cell-1] == '#' and wh[current_cell] != '#' and  wh[current_cell] != '.' and wh[current_cell-wh_length-1] == '#'):
                wh[current_cell] = 'X'
                
            # Top Corners on Right Side
            if(wh[current_cell+1] == '#' and wh[current_cell] != '#' and wh[current_cell] != '.' and wh[current_cell-wh_length-1] == '#'):
                wh[current_cell] = 'X'
                
            # Bottom Corners on Left Side
            if(wh[current_cell-1] == '#' and wh[current_cell] != '#' and  wh[current_cell] != '.' and wh[current_cell+wh_length+1] == '#'):
                wh[current_cell] = 'X'
                
            # Bottom Corners on Right Side
            if(wh[current_cell+1] == '#' and wh[current_cell] != '#' and  wh[current_cell] != '.' and wh[current_cell+wh_length+1] == '#'):
                wh[current_cell] = 'X'
                
##            # Check Rule 2 on Left Side
##            if(len(deviation_left) == 1 and is_between(deviation_left[0]+1,current_cell-wh_length-1,current_cell)
##               and wh[current_cell-1] == '#' and wh[current_cell] != '.' and wh[current_cell] != '#'):
##                wh[current_cell] = 'X'     
##            elif(len(deviation_left) > 1 and is_between(deviation_left[j]+1,current_cell-wh_length-1,current_cell)
##                 and wh[current_cell-1] == '#' and wh[current_cell] != '.' and wh[current_cell] != '#'):
##                wh[current_cell] = 'X'
##                if(j+1 < len(deviation_left)):
##                   j += 1
##
##            # Check Rule 2 on Right Side
##            if(len(deviation_right) == 1 and is_between(deviation_right[0]-1,current_cell-wh_length-1,current_cell)
##               and wh[current_cell+1] == '#' and wh[current_cell] != '.' and wh[current_cell] != '#'):
##                wh[current_cell] = 'X'
##            elif(len(deviation_right) > 1 and is_between(deviation_right[j]-1,current_cell-wh_length-1,current_cell)
##               and wh[current_cell+1] == '#' and wh[current_cell] != '.' and wh[current_cell] != '#' and wh[current_cell-wh_length-1] == '#'):
##                wh[current_cell] = 'X'
##                if(j+1 < len(deviation_right)):
##                   j += 1

        # Increment Counter
        current_cell += 1

    # Reset Counter
    current_cell = 0
    # Remove Other Symbols in Warehouse
    for i in wh:
        # Replace Player, Box and Target With Blank Space
        if(i == '@' or i == '$' or i == '.' or i == '*'):
            wh[current_cell] = ' '
        # Increment Counter
        current_cell += 1

    # Convert Taboo Warehouse from List to String
    wh = ''.join(wh)
##    print(wh)
    return wh
    raise NotImplementedError()

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -


class SokobanPuzzle(search.Problem):
    '''
    Class to represent a Sokoban puzzle.
    Your implementation should be compatible with the
    search functions of the provided module 'search.py'.
    
    Use the sliding puzzle and the pancake puzzle for inspiration!
    
    '''
    ##         "INSERT YOUR CODE HERE"
    
    def __init__(self, warehouse):
        self.warehouse = warehouse        

    def actions(self, state):
        """
        Return the list of actions that can be executed in the given state 
        if these actions do not push a box in a taboo cell.
        The actions must belong to the list ['Left', 'Down', 'Right', 'Up']        
        """
        _actions = []

        if (tuple((state.worker[0]-1, state.worker[1])) not in state.walls):
            if (tuple((state.worker[0]-1, state.worker[1])) in state.boxes):
                if (tuple((state.worker[0]-2, state.worker[1])) not in state.boxes + state.walls):
                    _actions.append('Left')
            else:
                _actions.append('Left')
            
        if (tuple((state.worker[0], state.worker[1]+1)) not in state.walls):
            if (tuple((state.worker[0], state.worker[1]+1)) in state.boxes):
                if (tuple((state.worker[0], state.worker[1]+2)) not in state.boxes + state.walls):
                    _actions.append('Down')
            else:
                _actions.append('Down')
            
        if (tuple((state.worker[0]+1, state.worker[1])) not in state.walls):
            if (tuple((state.worker[0]+1, state.worker[1])) in state.boxes):
                if (tuple((state.worker[0]+2, state.worker[1])) not in state.boxes + state.walls):
                    _actions.append('Right')
            else:
                _actions.append('Right')
            
        if (tuple((state.worker[0], state.worker[1]-1)) not in state.walls):
            if (tuple((state.worker[0], state.worker[1]-1)) in state.boxes):
                if (tuple((state.worker[0], state.worker[1]-2)) not in state.boxes + state.walls):
                    _actions.append('Up')
            else:
                _actions.append('Up')

            
        return _actions

    def result(self, state, action):
        """
        Return the state that results from executing the given
        action in the given state. The action must be one of
        self.actions(state).
        """
        if (action in self.actions(state)):
            worker = list(state.worker)
            
            if (action == "Left"):                
                worker[0] -= 1
                if (tuple(worker) in state.boxes):
                    index = state.boxes.index(tuple(worker))             
                    box = list(state.boxes[index])
                    box[0] -= 1
                    state.boxes[index] = tuple(box)
            if (action == "Right"):                
                worker[0] += 1
                if (tuple(worker) in state.boxes):
                    index = state.boxes.index(tuple(worker))             
                    box = list(state.boxes[index])
                    box[0] += 1
                    state.boxes[index] = tuple(box)
            if (action == "Up"):                
                worker[1] -= 1
                if (tuple(worker) in state.boxes):
                    index = state.boxes.index(tuple(worker))             
                    box = list(state.boxes[index])
                    box[1] -= 1
                    state.boxes[index] = tuple(box)
            if (action == "Down"):                
                worker[1] += 1
                if (tuple(worker) in state.boxes):
                    index = state.boxes.index(tuple(worker))             
                    box = list(state.boxes[index])
                    box[1] += 1
                    state.boxes[index] = tuple(box)

            state.worker = tuple(worker)

        return state

    
    def goal_test(self, state):
        """Return True if the state is a goal. The default method compares the
        state to self.goal, as specified in the constructor. Override this
        method if checking against a single self.goal is not enough."""
        for box in state.boxes:
            if box not in state.targets:
                return False

        return True
        

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

def check_action_seq(warehouse, action_seq):
    '''
    
    Determine if the sequence of actions listed in 'action_seq' is legal or not.
    
    Important notes:
      - a legal sequence of actions does not necessarily solve the puzzle.
      - an action is legal even if it pushes a box onto a taboo cell.
        
    @param warehouse: a valid Warehouse object

    @param action_seq: a sequence of legal actions.
           For example, ['Left', 'Down', Down','Right', 'Up', 'Down']
           
    @return
        The string 'Failure', if one of the action was not successul.
           For example, if the agent tries to push two boxes at the same time,
                        or push one box into a wall.
        Otherwise, if all actions were successful, return                 
               A string representing the state of the puzzle after applying
               the sequence of actions.  This must be the same string as the
               string returned by the method  Warehouse.__str__()
    '''
    
    ##         "INSERT YOUR CODE HERE"
    
    raise NotImplementedError()


# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

def solve_sokoban_elem(warehouse):
    '''    
    This function should solve using elementary actions 
    the puzzle defined in a file.
    
    @param warehouse: a valid Warehouse object

    @return
        A list of strings.
        If puzzle cannot be solved return ['Impossible']
        If a solution was found, return a list of elementary actions that solves
            the given puzzle coded with 'Left', 'Right', 'Up', 'Down'
            For example, ['Left', 'Down', Down','Right', 'Up', 'Down']
            If the puzzle is already in a goal state, simply return []
    '''
    
    ##         "INSERT YOUR CODE HERE"
    
    raise NotImplementedError()

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

def can_go_there(warehouse, dst):
    '''    
    Determine whether the worker can walk to the cell dst=(row,col) 
    without pushing any box.
    
    @param warehouse: a valid Warehouse object

    @return
      True if the worker can walk to cell dst=(row,col) without pushing any box
      False otherwise
    '''
    
    ##         "INSERT YOUR CODE HERE"
    
    raise NotImplementedError()

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

def solve_sokoban_macro(warehouse):
    '''    
    Solve using macro actions the puzzle defined in the warehouse passed as
    a parameter. A sequence of macro actions should be 
    represented by a list M of the form
            [ ((r1,c1), a1), ((r2,c2), a2), ..., ((rn,cn), an) ]
    For example M = [ ((3,4),'Left') , ((5,2),'Up'), ((12,4),'Down') ] 
    means that the worker first goes the box at row 3 and column 4 and pushes it left,
    then goes the box at row 5 and column 2 and pushes it up, and finally
    goes the box at row 12 and column 4 and pushes it down.
    
    @param warehouse: a valid Warehouse object

    @return
        If puzzle cannot be solved return ['Impossible']
        Otherwise return M a sequence of macro actions that solves the puzzle.
        If the puzzle is already in a goal state, simply return []
    '''
    
    ##         "INSERT YOUR CODE HERE"
    
    raise NotImplementedError()

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

