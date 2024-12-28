README

I was inspired by the British game show "Countdown" to create this Python program which randomly generates configurations for the show's 'letters' and 'numbers' rounds. Rules for Countdown's letters and numbers rounds can be found on the show's Wikipedia page: https://en.wikipedia.org/wiki/Countdown_(game_show)#Format

After the user types in one of two commands (which can be seen below), the program displays either a string of nine letters (for the 'letters' round) or seven numbers: a three-digit 'target' number and six smaller numbers below it (for the 'numbers' round). It then waits for 30 seconds as the user attempts to play the game (no additional functionality for this has been implemented as of now), before the program finishes its execution.


INSTRUCTIONS

This program has two run commands: one of the letters round and one for the numbers round.

To run the letters round, type:
python3 countdown.py letters

To run the numbers round, type:
python3 countdown.py numbers


NOTES

Not all configurations of letters are considered valid by the show's rules. For example, 'O U A I D C L I E' is a possible configuration for a letters round in this program, but would not be considered valid in the show as there are not enough consonants.
