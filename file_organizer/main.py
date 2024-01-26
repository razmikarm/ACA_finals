from file_organizer import FileOrganizer
from controller import Controller

def main():
    path = input('Enter path to your directory: ')
    organizer = FileOrganizer(path)
    controller = Controller(organizer)
    controller.run()

if __name__ == '__main__':
    main()
