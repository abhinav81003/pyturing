# Compiles Python Code to a Turing Machine
# Last Edit: Feb 27 2023

import TuringMachine

class Compiler:

    def createTM():

        InputSet = {}

        TapeSet = {var for var in InputSet} #all elements in input set exist in tape set
        TapeSet.add('_') #at least has _ 

        TM = TuringMachine() #pass in InputSet
        
        TM.visualize()
