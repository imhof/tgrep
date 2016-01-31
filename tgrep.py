#!/usr/bin/env python
#
def main():

#
# This script searches a text file for a given matchcode (like grep)
# and print out the whole paragraph in which the matchcode was found
#
# A paragraph is defind as follows:
#
# 1. Each line beginning with a "non-space" starts a new paragraph
# 2. Each line starting with a space belongs to the current paragraph
# 
# Script has to be called using two cli arguments:
#
#  1. match string
#  2. file to be searched through
#
# tgrep.py matchstring filename  
#

    import argparse, sys, fileinput
    from optparse import OptionParser

#    parser = argparse.ArgumentParser(description="This program provides search features through paragraphs in text files")
#    parser.add_argument("searchpattern", help="string to match in the given file")
#    parser.add_argument("file", help="filename to search through" )
#    args = parser.parse_args()

    parser = OptionParser(usage="Usage: %prog [options] [file, file, ...]")
#    parser.add_option("-a", "--any", dest="match_any", action="store_true", default=False, help="Match ACLs with 'any', too")
    parser.add_option("-m", "--match", dest="matchcode", default=None, help="string to be matched")
#    parser.add_option("-p", "--sport", dest="source_port", default=None, help="Source port to look for")
#    parser.add_option("-I", "--dip", dest="destination_ip", default=None, help="Destination IP to look for")
#    parser.add_option("-P", "--dport", dest="destination_port", default=None, help="Destination port to look for")
#    parser.add_option("-o", "--proto", dest="protocol", default=None, help="Protocol to look for")


    (options, args) = parser.parse_args()

    if len(sys.argv) < 2:
        parser.print_help()
        sys.exit()

    match = options.matchcode

    # ...check all lines in all files (or stdin)
#    for line in fileinput.input(args):
#        if grepper.grep(line):
#            print(line.strip())


#	ifilename = args.file
#    match = match

	
#	ifile = open(ifilename, 'r')


    output = 0
    i = 0
    n = 0
    para = [ '' ]

    for line in fileinput.input(args):

        if line[0] != ' ':    # if begin of new paragraph
            if output == 1:      # eventually print last paragraph and reset paraarray
                while n < len(para):
                    print para[n],
                    n = n + 1
                output = 0
                para = [ '' ]
                i = 0            # (not used)
                n = 0
            else:                # else reset paraarray only
                para = [ '' ]
                i = 0
            if match in line:  # if matchcode found set output flag
                output = 1

        elif line[0] == ' ':   # if line belongs to a paragraph...
            i = i + 1          # (not used)
            if match in line:  # check matchode and set output flag in case
                output = 1
        else:
            print "*** WARNING: Line not classified ***"    # For debug
            print line
        para.append(line)  # save line

main()	
