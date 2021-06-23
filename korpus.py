from collections import Counter
banned_letters = '".,(){}[];?!*+/ \n–'
word_counts = Counter()

def clean_word(word):
  for sign in banned_letters:
    word = word.replace(sign, '')
  if word == '-':
    return ''
  return word

def print_counter(counter):
  for entry in counter.most_common(100):
    print(f'{entry[0]}: {entry[1]}')

def analyze_file(file_name):
  with open(file_name, 'r') as input_file:
    line_number = 0
    for line in input_file:
      line_number += 1
      words = line.split(' ')
      for word in words:
        cleaned_word = clean_word(word)
        if (len(cleaned_word) == 0):
          continue
        word_counts[cleaned_word] += 1
      if (line_number % 1000 == 0):
        print(line_number)
      if (line_number == 100000):
        break
  print_counter(word_counts)


analyze_file('/share/home/profesori/spanel/public/SIVT2020/SEPTIMA/cs.txt')
