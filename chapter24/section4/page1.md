##  Question 8

Add the commands TEST, IFTRUE (abbreviation IFT), and IFFALSE (abbreviation
IFF). These are alternatives to the IF/IFELSE style of conditional evaluation,
provided in Logo because an IFELSE that carries out several conditional
instructions can lead to one very long instruction line, hard to read and hard
to edit. Here's how it works:

The command TEST takes one argument, which must be TRUE or FALSE. It remembers
the value for later, and does nothing else. Note: If TEST is called inside a
procedure, the argument value is remembered locally, but does not modify the
caller's test result (or the global one).

The command IFTRUE takes one argument, an instruction list. If the remembered
TEST value is TRUE, then the instruction list is run. If the remembered value
is FALSE, nothing happens. The command IFFALSE is the same only backwards. It
is an error if IFTRUE or IFFALSE is used before any TEST has been done. Note:
It is *not* an error to use IFTRUE or IFFALSE inside a procedure, before the
procedure does a TEST, provided that a TEST has been done by the caller. That
is, each procedure call inherits its caller's test flag.

Suggestion: Put a variable with an untypeable-in name, such as the string "
TEST", in every frame.

**When your partner is done with question 8 as well, move on to part 9!**

