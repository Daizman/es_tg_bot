import model.Shell as ShellModel


class Shell:
    def __init__(self):
        self.__model = ShellModel.Shell

    def consult(self):
        pass

    def load(self, path):
        if not path or not path.strip():
            raise ValueError('Не найден файл с БЗ')
        self.__model.load(path)

    def backup(self, path):
        pass

    def __take_goal(self):
        pass

    def __ask_question(self):
        pass
