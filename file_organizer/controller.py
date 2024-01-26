class Controller:

    def __init__(self, organizer):
        self.organizer = organizer
        self.not_found_msg = (
                "Command '{}' not found\n"
                "For more information enter 'help'"
            )
        self.commands = {
            'exit': 'Exits program',
            'help': 'Shows this message',
            'path': 'Shows path to current directory',
            'trash': 'Shows path to trash directory',
            'clean': self.organizer.clean.__doc__,
            'flatten': self.organizer.flatten.__doc__,
            'restore': self.organizer.restore.__doc__,
            'search': self.organizer.search.__doc__,
            'remove': self.organizer.remove.__doc__,
        }

    def _get_command(self):
        command = input('Please enter your command: ').lower()
        if command not in self.commands:
            print(self.not_found_msg.format(command))
            return ''
        return command

    def run(self):
        while True:
            command = self._get_command()
            match command:
                case '':
                    continue
                case 'exit':
                    exit()
                case 'help':
                    self.help()
                case 'path':
                    print(self.organizer.path)
                case 'trash':
                    print(self.organizer.trash)
                case 'flatten':
                    self.organizer.flatten()
                    print('Successfully flattened')
                case 'clean':
                    self.organizer.clean()
                    print('Successfully cleaned trash')
                case 'restore':
                    files = self.organizer.restore()
                    print('Successfully restored from trash')
                    self.show_files(files)
                case 'search' | 'remove' as func:
                    pattern = input(f'Enter pattern to {func}: ')
                    result = getattr(self.organizer, func)(pattern)
                    self.show_files(result)

    def show_files(self, files):
        if not files:
            print('Info: No any file was found')
            return
        print(*files, sep='\n')

    def help(self):
        msg = '\n'.join([f'{c}: {d}' for c, d in self.commands.items()])
        print(msg)
