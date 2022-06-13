import sys, getopt

def main(argv):
   global count
   global inputfile
   global outputfile
   try:
      opts, args = getopt.getopt(argv,"hi:l:o:",["ifile=","length=","ofile="])
   except getopt.GetoptError:
      print ('makecsv.py -i <inputfile> -o <outputfile> -l <length (words) of string>')
      sys.exit(2)
   for opt, arg in opts:
      if opt == '-h':
         print ('makecsv.py -i <inputfile> -o <outputfile>')
         sys.exit()
      elif opt in ("-i", "--ifile"):
         inputfile = arg
      elif opt in ("-l","--length"):
          count = int(arg)
      elif opt in ("-o", "--ofile"):
         outputfile = arg

if __name__ == '__main__':

    # get arguments
    main(sys.argv[1:])
    # open file
    filein = open(f'{inputfile}', 'r')
    # read lines
    lines = filein.readlines()

    # Create blank document
    fileout = ''

    # iterate x times
    while lines:
        newline = ''
        for x in range(count):
            newline = newline + lines.pop(0).strip() + ','
        fileout = fileout + newline[:-1] + "\n"
    
    file2 = open(outputfile, 'a')
    file2.writelines(fileout)
