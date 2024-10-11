def remove_chars(text, rem_list = []):
  new_text = ""
  rem_set = set(rem_list)

  for char in text:
    if char not in rem_set:
      new_text = new_text + char

  return new_text

def remove_list_elements(list, remList = []):
  new_list = []
  remSet = set(remList)

  for e in list:
    if e not in remSet:
      new_list.append(e)

  return new_list  

def get_text_from_file(filename):
  text = ""
  with open(filename) as file:
    text = file.read()

  return text

def write_text_to_file(text, filename):
  with open(filename, "w") as file:
    file.writelines(text)

class TextProcessor:
  def __init__(self, stop_words_filename):
    self.stop_words = get_text_from_file(stop_words_filename).split()

  def clean_text(self, text):
    text = text.lower()
    text = remove_chars(text, ['(',')','.', '¡','!', '¿', '?', ',', '/n'])
    text = remove_chars(text, [str(i) for i in range(10)])
    return text

  def tokenize(self, text):
    return text.split()

  def remove_stop_words(self, tokens):
    return remove_list_elements(tokens, self.stop_words)

  def process_file(self, raw_filename, proc_filename):
    raw_text = get_text_from_file(raw_filename)

    clean_text = self.clean_text(raw_text)
    tokens = self.tokenize(clean_text)
    clean_tokens = self.remove_stop_words(tokens)

    proc_text = "\n".join(clean_tokens)

    write_text_to_file(proc_text, proc_filename)

    print(f"INFO | Se procesó el archivo '{raw_filename}' y el resultado se guardó en '{proc_filename}'")

  def process_text(self, raw_text):
    clean_text = self.clean_text(raw_text)
    tokens = self.tokenize(clean_text)
    clean_tokens = self.remove_stop_words(tokens)

    proc_text = ' '.join(clean_tokens)

    return proc_text


filenames = {
  "raw" : "raw-text.txt",
  "processed": "processed-text.txt",
  "stop_words": "stop-words.txt",
}

# Procesamiento de un archivo

processor = TextProcessor(filenames["stop_words"])
processor.process_file(filenames["raw"], filenames["processed"])

# Procesamiento de texto

text = """El curso de Python cuesta 100 soles y es excelente. ¡Lo recomiendo!"""

processed_text = processor.process_text(text)

print(f"Texto sin procesar: {text}")
print(f"Texto procesado   : {processed_text}")