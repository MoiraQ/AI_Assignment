
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
    return [ (9708651, 'Christopher', 'O\'Rafferty'), (9400001, 'Moira', 'Quinn'), (1234569, 'Eva', 'Tardos') ]

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

