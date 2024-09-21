import time

# PASO 1 : DEFINIR EL STRING

input = "El análisis de texto, también conocido como minería de datos, se refiere al proceso de extraer información significativa de datos textuales."

# PASO 2: DEFINIR LA CLASE Y SUS ATRIBUTOS

def replaceFromList(text, repList = []):
  newText = ''
  repSet = set(repList)
  
  for char in text:
    if char not in repSet:
      newText = newText + char

  return newText


class TextAnalyzer():
  def __init__(self, text = ''):
    # formattedText = text.replace('.', '').replace('!','').replace('?','').replace(',','')

    formattedText = replaceFromList(text, ['.', '!', '?', ','])

    # PASO 3: PASAR EL STRING A MINÚSCULAS
    formattedText = formattedText.lower()

    self.fmtText = formattedText
  
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

analyzed = TextAnalyzer(input)
freqOfAllWords = analyzed.freqAll()

print(freqOfAllWords)
print(f"Occurrences of 'de': {analyzed.freqOf('datos')}")