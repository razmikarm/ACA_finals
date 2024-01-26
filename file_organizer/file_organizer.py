from os import sep
from pathlib import Path


class FileOrganizer:

    def __init__(self, path):
        self.__path = Path(path)
        if not self.__path.is_dir():
            raise Exception(f"Directory '{path}' was not found")
        self.__trash = self.__path / 'Recycle Bin'
        if not self.__trash.exists():
            self.__trash.mkdir()

    @property
    def path(self) -> Path:
        return self.__path.absolute()

    @property
    def trash(self) -> Path:
        return self.__trash.absolute()

    def flatten(self) -> None:
        """
        Moving all files in subdirectories into `self.path`
        > !IMPORTANT: This action can't be undone
        """
        for file in self.path.rglob('*'):
            if file.is_dir() or file.parent in (self.trash, self.path):
                continue
            target = self.path / file.name
            if target.exists():
                name = file.stem
                ext = file.suffix
                mark = f"({str(file.parent).replace(sep, '~')})"
                target = self.path / f"{name}{mark}{ext}"
            file.rename(target)

        # Cleaning empty subdirectories
        for file in self.path.rglob('*'):
            if file.is_dir() and file != self.trash:
                self.clear_directory(file)
                file.rmdir()

    @staticmethod
    def clear_directory(directory: Path) -> None:
        """
        Deletes everything in directory recursively
        """
        for file in directory.rglob('*'):
            if file.is_dir():
                FileOrganizer.clear_directory(file)
                file.rmdir()
            else:
                file.unlink(missing_ok=True)

    def search(self, filename: str, recursive: bool = True) -> list[Path]:
        """
        Searching for a file inside a directory

        :param filename: Name of the file to be searched (can include extension)
        :param recursive: Also searching child directories if `True`
        :return: List of matched files
        """
        subdirs = f'**{sep}' if recursive else ''
        return list(self.path.glob(f'{subdirs}{filename}'))

    def remove(self, ext: str, recursive: bool = True) -> list[Path]:
        """
        Removing files with given extension
        > Actually moving into `Recycle Bin` directory

        :param ext: Extension of files to be removed
        :return: List of removed files
        """
        subdirs = f'**{sep}' if recursive else ''
        result = []
        for file in self.path.glob(f'{subdirs}*.{ext}'):
            if file.parent == self.trash:
                continue
            suffix = str(file.parent).replace(sep, '~')
            target = self.trash / f"({suffix}){file.name}"
            file.rename(target)
            result.append(target)
        return result

    def clean(self) -> None:
        """
        Removes files in the trash (`Recycle Bin` directory) permanently
        > !IMPORTANT: This action can't be undone
        """
        for file in self.trash.iterdir():
            file.unlink(missing_ok=True)

    def restore(self) -> list[Path]:
        """
        Restores files from `Recycle Bin` into their previous diretories
        Will create directories, if they does not exist

        :return: List of restored files
        """
        result = []
        for file in self.trash.iterdir():
            dir_name, _, filename = file.name.partition(')')
            dir_name = dir_name[1:].replace('~', sep)
            dir_path = Path(dir_name)
            if not dir_path.exists():
                dir_path.mkdir()
            new_file = dir_path / filename
            file.rename(new_file)
            result.append(new_file)
        return result
