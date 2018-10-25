import visualizer
import logger   

def main():
    intro = "|~~|~~\|~~  /\  | /  /\  ~~//~~\~|~|~~\ \n|--|__/|-- /__\ |(  /__\  /|    || |   | \n|  |  \|__/    \| \/    \/__\__/_|_|__/ "
    print(intro)
    cases = {
        'u' : lambda: visualizer.visualize(logger.log()),
        'p' : lambda: visualizer.print_maxs()
    }

    user = input("Would you like to update (u), preview (p), or exit (x)? ")
    while(user != 'x'):
        try:
            cases[user]()
        except KeyError:
            print("Invalid input!")
        user = input("Would you like to update (u), preview (p), or exit (x)? ")
        print()
    


if __name__ == '__main__':
    main()