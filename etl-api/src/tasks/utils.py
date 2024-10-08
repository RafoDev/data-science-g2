def validate_dni(dni):
  return (len(dni) == 8 and dni.isdigit())

# TODO: implementar handle_invalid_dni()