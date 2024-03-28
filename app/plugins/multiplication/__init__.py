from app.commands import Command

class MultiplicationCommand(Command):
    def execute(self, args):
        if args:
            a = float(args[0])
            b = float(args[1])
            print (f"multiplication result : { a * b }")
        else:
            print ("nothing to multiply")