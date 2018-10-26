import visualizer
import logger   

def main():
    bold = "\033[1m"
    ending = "\033[00m"
    eye = "\033[01;37mx{}".format(ending)
    top_mouth = "\033[01;32m/\033[00;32m_____\033[01;32m\\{}".format(ending)
    bot_mouth = "\033[01;32m\_____/{}".format(ending)
    intro = "\033[01;32m({}\033[01;32m)-({}\033[01;32m)\n{}\n{}".format(eye,eye,top_mouth,bot_mouth)
    print(intro)
    cases = {
        'u' : lambda: visualizer.visualize(logger.log()),
        'p' : lambda: visualizer.print_maxs()
    }

    user = input("{}Would you like to update (u), preview (p), or exit (x)?{} ".format(bold, ending))
    while(user != 'x'):
        try:
            cases[user]()
        except KeyError:
            print("Invalid input!")
        user = input("{}Would you like to update (u), preview (p), or exit (x)?{} ".format(bold,ending))
        print()
    


if __name__ == '__main__':
    main()