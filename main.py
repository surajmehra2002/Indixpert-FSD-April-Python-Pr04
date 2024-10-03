# This is main file where all module or package will accessed ,after running only this file you can see overall output...
# Note:- for running this file properly you have to changing some file path accordingly your pc , file path inside "manage_shop.py" which are inside package
# Adding My_folder to the system path
import sys
import os

# Add the path to packages so Python can locate the 'Inventory_management_system' package
sys.path.append(os.path.join(os.path.dirname(__file__), 'packages'))


import Inventory_management_system
Inventory_management_system.dashboard()              