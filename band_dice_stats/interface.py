import argparse
from band_dice_stats.funcs import validInput, stats
import sys

def parser():
    myparser = argparse.ArgumentParser()
    
    myparser.add_argument(
        'DiceString',
        metavar='[dice_string]',
        type = str,
        help='''enter dice string in dnd/angband style (i.e 2d4+1d8) also
        supports negative dice rolls and modifiers, enter negative rolls and
        modifiers in this form "2d4+-1d8", everydice roll must be separated by
        "+" sign''',
        action='store'
            )

    myparser.add_argument(
        '-w',
        '--width',
        type=int,
        metavar='[width]',
        action='store',
        default=50,
        help='specify width of bar graph'
            )
    return myparser

def main():
    parser0 = parser()
    
    # if no argument is given program shows help and closes
    if len(sys.argv) == 1:
        parser0.print_help()
        sys.exit(0)

    args = parser0.parse_args()
    dice_string = args.DiceString
    width = args.width
    
    termgraph_args = {'stacked':False,'width':width,'no_labels':False,
        'format':'{:<5.2f}','suffix':'','vertical':False
        }
    if validInput(dice_string) == False:
        parser0.error('the dice string you have entered is not valid, be sure to check help for proper usage')
    
    stats(dice_string, termgraph_args=termgraph_args)
    


if __name__ == '__main__':
    main()
