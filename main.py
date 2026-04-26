import sys
from Md2Hhtml import Md2Html

def isTxt(filename: str):
    return filename.endswith(".txt")

def main():
    args = sys.argv[1:]
    try:
        inputFile = args[0]
        outputFile = args[1]

        if not isTxt(inputFile) or not isTxt(outputFile):
            print("Files must have .txt extension")
            sys.exit()

        mh = Md2Html(args[0], args[1])
        mh.toHtml()
    except IndexError:
        print("It is necessary to specify two files in the arguments: input and output")
        sys.exit()

if __name__ == "__main__":
    main()