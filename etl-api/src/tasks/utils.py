def validate_dni(dni):
  return (len(dni) == 8 and dni.isdigit())

# TODO: implementar handle_invalid_dni()
def handle_invalid_dni(dni):
  with open("invalid_dnis.txt", "a") as f:
    f.write(f"{dni}\n")