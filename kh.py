#ovoj program e  so uvoz na sys elename ucese za argv 
import sys

if (len(sys.argv) < 3):
    print("you gave too little", len(sys.argv), "commandline arguments. Should be 3, but if it is les or more then answer should be given")
    sys.exit()
elif (len(sys.argv) > 3):
    print("you gave too many commandline argumrnts. should be 3")
    sys.exit()
print("Hello {}. Welcome to {} tutorial".format(sys.argv[1], sys.argv[2]))
print(len(sys.argv))
print(len(sys.argv[0]) + len(sys.argv[1]) + len(sys.argv[2]))
