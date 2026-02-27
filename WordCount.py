#WordCount.py
#Name: Louis Safranek
#Date: 02-26-2026
#Assignment: Lab 6

def main():
  textFile = open("gettysberg.txt", 'r')
  textFile2 = open("fish.txt", 'r')
  lineCount = 0
  lineCount2 = 0
  wordCount = 0
  wordCount2 = 0
  letterCount = 0
  letterCount2 = 0
  for line in textFile:
    lineCount = lineCount + 1
    words = line.split()
    for w in words:
      wordCount = wordCount + 1
    letters = list(line)
    for l in letters:
      letterCount = letterCount + 1
  for line in textFile2:
    lineCount2 = lineCount2 + 1
    words = line.split()
    for w in words:
      wordCount2 = wordCount2 + 1
    letters = list(line)
    for l in letters:
      letterCount2 = letterCount2 + 1
  print("Lines in Gettysberg Address:", lineCount)
  print("Words in Gettysberg Address:", wordCount)
  print("Letters in Gettysberg Address:", letterCount)
  print("Lines in Fish:", lineCount2)
  print("Words in Fish:", wordCount2)
  print("Letters in Fish:", letterCount2)

if __name__ == '__main__':
  main()
