class Editor:
    def functionalities(self):
        self.funcs=["create new file","excute","save"]
        return self.funcs
class Pycharm(Editor):
    def functionalities(self):
        funcs=super().functionalities()
        funcs.append(["debug","version control"])
        return funcs

pyc=Pycharm()
print(pyc.functionalities())