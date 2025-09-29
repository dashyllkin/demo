from tkinter import ttk
from Controllers.UserController import UserController
from tkinter import *
from datetime import datetime, timedelta

class AdminView(ttk):
    '''
    класс для создания панели администратора
    '''
    def __init__(self):
        super().__init__()
