# Defining a Turing Machine
# Last Edit: Feb 27 2023

class TuringMachine:
    
    # essence of a turing machine:
    # set of states (Q), input character set (E), tape character set (T), start, accept and reject states (q0, qa, qr), transitions funciton 
    
    def __init__(self, Q: set, E: set, T: set, q0, qa, qr, ) -> None: #todo: figure out types for q0, qa, and qr, add transitions
        self.stateSet = Q
        self.inputCharacterSet = E
        self.tapeCharacterSet = T
        self.startState = q0
        self.acceptState = qa
        self.rejectState = qr
        self.currentState = qa

        #tra
        pass

    # accepts or rejects
    def compute():
        print("reject")
        return 

    #use some library to make circles for states and arrows for transitions => future: goes through each state in an animation
    def visualize():
        print() 
    
