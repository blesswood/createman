import os
import sys

if 'help' in sys.argv:
    print('->Create manpage:\n-->python3 ctman.py\n--->After choosing manpage name, edit it in current dicrectory, then build.')
    print('\n->Build:\n-->sudo python3 ctman.py\n--->Build using choosed manpage name.')
    sys.exit()

askme = input('1)Build manpage\n2)Create manpage\n')

def build_from_file():
    if(os.getuid()) == 0: #check privileges
        filename = input("->Manpage: ")
        pwd = str(os.popen('pwd').read().split())[2:-2] #current pwd
        r = "cp " +  filename + " /usr/share/man/man1/" + filename + ".1" #copy manpage to /man
        mute = os.popen(r)
        r = 'gzip /usr/share/man/man1/' + filename + '.1' #zip manpage
        mute = os.popen(r)
        print("\n--->Try: man %s\n" % filename)
    else:
        print("\nTry with sudo!")
        sys.exit()

def create_man(filename):
    os.popen("touch  %s" % filename) #create manpage
    manpage = open(filename, "w")

    text = '''.\\" "TITLE"
.TH man 1 "DATE" "VERSION"
'''
    for opt in open("options.txt", "r"):
        text += "\n.SH " + opt #add to manpage additional options from options.txt
    manpage.write(text)
    print("\n--->Edit '%s' in current directory and start ctman.py to build manpage\n" % filename)

if "1" in askme:
    build_from_file() #build manpage
elif "2" in askme:
    filename = input("->Manpage name: ")
    create_man(filename) #create manpage
else:
    print("--->Sorry, incorrect data")
