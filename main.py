from tests.test import *
from models.number import *
from utils.random import *
from ui.console import Console


def main():
    try:
        Test().testEverything()
    except:
        exit(0)

    app = Console()
    app.run()

if __name__ == '__main__':
    main()
