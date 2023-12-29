import sys
import platform
import time
from PyQt5.QtWidgets import QApplication as qapp, QMainWindow as qmain, QLabel as qlab, QVBoxLayout as qvbox, QWidget, QPushButton, QEvent as qeve      
from PyQt5.QtGui import QIcon
import subprocess as sp

app = qapp(sys.argv)

class Install(qmain):
    def __init__(self):
        super().__init__()
        self.setWindowIcon(QIcon("K:\Dont_Bother\Icon-Taskbar-window.png"))
        

        if platform.system() != "Windows":
            # If your OS isn't Windows it will execute this code:
            self.setWindowTitle('--NotWindowsError')
            self.setGeometry(100, 100, 800, 600)  # Adjusted size

            # Create a central widget to hold the layout
            central_widget = QWidget(self)

            layout = qvbox()
            label = qlab(f"OS must be Windows 10, 8.1 or 11, this OS is using {platform.system()}")
            layout.addWidget(label)

            # Set the layout for the central widget
            central_widget.setLayout(layout)

            # Set the central widget for the main window
            self.setCentralWidget(central_widget)
        else:
            # If your OS is Windows it will execute this code:
            self.setWindowTitle('Dont_Bother')
            self.setGeometry(100, 100, 800, 600)  # Adjusted size

            central_widget = QWidget(self)

            layout = qvbox()
            label = qlab("OS is windows... Do you wish to continue?")
            layout.addWidget(label)

            # Create a label to display the user's input
            input_label = qlab()

            # Create a function to handle the user's input
            def handle_input():
                user_input = input_label.text()
                if user_input.lower() == "yes":
                    layout.addWidget(input_label)

                else:
                    sys.exit()
                    
            # if the user wants to continue.
            button = QPushButton("Continue to Dont_Bother?")
            

            # Create a button to get the user's input
            if button.clicked:
                sp.run(['python', 'ExecutableBuilder.py'])
                layout2 = qvbox()
                label2 = qlab('Welcome, This is the Executable Builder running.')
                layout2.addWidget(label2)
                
                
                    
                
            
            button.clicked.connect(handle_input)
                
            
            layout.addWidget(button)

            central_widget.setLayout(layout)

            self.setCentralWidget(central_widget)

# Create an instance of the Install class
install_window = Install()

# Show the window
install_window.show()

# Start the application's event loop
sys.exit(app.exec_())

