from Problem import Problem
from Controller import Controller
from UI import UI

problem = Problem()
ctrl = Controller(problem)
ui = UI(ctrl)
ui.mainMenu()
