from app.commands import Command
class AdditionCommand(Command):
    def execute(self, args):
        if args:
            a = float(args[0])
            b = float(args[1])
            print (a+b)
        else:
            print ("nothing to add")