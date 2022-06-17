from math import sqrt, gcd
from string import ascii_uppercase

dict_letters_to_int = dict()
dict_int_to_letters = dict()

for number, letter in enumerate(ascii_uppercase, start=2):
    dict_int_to_letters[number] = letter
    dict_letters_to_int[letter] = number

dict_letters_to_int[" "] = 28
dict_int_to_letters[28] = " "


def is_prime(n: int):
    for i in range(2, int(sqrt(n))+1):
        if (n % i) == 0:
            return False

    return True 


def phi(p: int, q: int):
    return (p-1)*(q-1)


def encrypt_message(message: str, e: int, n: int):
    cypher = list()
    for letter in message:
        if letter.upper() not in dict_letters_to_int:
            raise ValueError(f"{letter} não é considerado um caractere válido")

        letter_int = dict_letters_to_int[letter.upper()]
        cypher.append(str(pow(letter_int, e, n)))

    return " ".join(cypher)


def decrypt_message(cypher: str, d: int, n: int):
    message = list()

    for number in cypher.split():
        if not number.isnumeric():
            raise TypeError("Mensagem inválida")

        letter_int = pow(int(number), d, n)
        message.append(dict_int_to_letters[letter_int])

    return "".join(message)


def linear_combination(a, b):
  if b == 0:
      return (a, 1, 0)

  (d, xx, yy) = linear_combination(b, a % b)

  return (d, yy, xx - (a//b)*yy)


def inverse(s, counter, m):
    inv = s + (m*counter)
    
    if inv > 0 and inv < m:
        return inv
    
    elif inv > m:
        return inv % m

    return inverse(s, counter+1, m)


def generate_public_key(p: int, q: int, e: int):
    if not is_prime(p):
        raise ValueError("P informado não é primo.")
    
    if not is_prime(q):
        raise ValueError("Q informado não é primo.")
    
    if gcd(e, phi(p, q)) != 1:
        raise ValueError("E informado não é coprimo a (p-1)*(q-1).")

    n = p*q

    return f"{n} {e}"
