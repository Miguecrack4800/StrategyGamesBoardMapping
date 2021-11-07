# Strategy Games Board Mapping
This is a simple program that will create a little map with the positions in which you win, the ones where you loose and the ones where it's unknown.
The program assumes both players are perfect and slowly maps out the spots based on the rules.

**Rules**
The program is made for simple games where there are 2 players that take turns moving a piece. The rules are given in the function "can_goto_check", there,
you have to write some code that, given the original position (*source*) and the destination (*dest*) will return *True* or *False*, *True* if the move is
valid and *False* if it's not.

**Usage**
Modify the *rules* and the *board size* and *more* in the configuration. You'll find this in the program itself marked with comments
When using the command you can add *"-c "* followed by *"T"* or *"F"* if you want cashing or not. Cashing is set to *True* by default.

**Remember**: this is a program made for *fun* and is *unoptimazed*.
