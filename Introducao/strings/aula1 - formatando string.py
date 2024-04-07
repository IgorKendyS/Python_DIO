curso = "PytHoN"

print(curso.upper())

print(curso.lower())

print(curso.title())


# remove espaço, esquerda, direita
curso ="  Python "

print(curso.strip())

print(curso.lstrip())

print(curso.rstrip())

# centralização e junção
print(curso.center(10,"_"))

# adiciona . entre cada caractere
# é possivel usar com lista
print(".".join(curso))