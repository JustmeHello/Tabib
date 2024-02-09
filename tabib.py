#import cmd 
import cmd
"""
"""

class tabib(cmd.Cmd):
    intro = "welcome Sir, type help or ? to list commands.\n"
    prompt = "(Tabib)"
    
    # commands
    def do_quit(self, arg):
        return True


if __name__ == '__main__':
    tabib().cmdloop()
