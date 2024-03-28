from app.commands import Command

class DivisionCommand(Command):
    def execute(self, args):
        if args:
            a = float(args[0])
            b = float(args[1])
            try:
                result = a/b
                print (f" Division result : {result}")
            except:
                print ("division by zero error ")
        else:
            print ("nothing to Divide")