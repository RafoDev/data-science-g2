import time

# PASO 1 : DEFINIR EL STRING

# PASO 2: DEFINIR LA CLASE Y SUS ATRIBUTOS

def replaceFromList(text, repList = []):
  newText = ''
  repSet = set(repList)
  
  for char in text:
    if char not in repSet:
      newText = newText + char

  return newText


class TextAnalyzer():
  def __init__(self, filename = ''):
    # formattedText = text.replace('.', '').replace('!','').replace('?','').replace(',','')
    self.fmtText = ''
    self.inputFilename = filename

    try: 
      file = open(filename)
      text = file.read()
      file.close()

      formattedText = replaceFromList(text, ['.', '!', '?', ','])

      # PASO 3: PASAR EL STRING A MINÚSCULAS
      formattedText = formattedText.lower()

      self.fmtText = formattedText
      
    except Exception as error:
      print(f"Error: {error}")

  # PASO 4: CONTAR LA FRECUENCIA DE TODAS LAS PALABRAS ÚNICAS
  def freqAll(self):
    wordList = self.fmtText.split(' ')

    freqMap = {}
    for word in set(wordList):
      freqMap[word] = wordList.count(word)

    return freqMap


  # PASO 5: CONTAR LA FRECUENCIA DE UNA PALABRA EN ESPECÍFICO
  def freqOf(self, word):

    freqDict = self.freqAll()

    if word in freqDict:
      return freqDict[word]
    else:
      return 0
  
  def writeFreqInAFile(self):
    freqDict = self.freqAll()
  
    with open(self.inputFilename + '_output.txt', 'w') as outputFile:
      for word, freq in freqDict.items():
        outputFile.write(f"{word} : {freq}\n")


filename = 'file.txt'
analyzed = TextAnalyzer(filename)
analyzed.writeFreqInAFile()
freqOfAllWords = analyzed.freqAll()


print(freqOfAllWords)
print(f"Occurrences of 'de': {analyzed.freqOf('de')}")
