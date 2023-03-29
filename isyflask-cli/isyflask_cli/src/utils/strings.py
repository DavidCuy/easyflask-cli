from re import sub
import random
import string

def camel_case(s: str):
    """
    Convierte un string a su notación UpperCamelCase

    Args:
        s (str): String de entrada

    Returns:
        str: String en formato UpperCamelCase
    """
    s = sub(r"(_|-)+", " ", s).title().replace(" ", "")
    return ''.join([s[0].upper(), s[1:]])

def get_random_string(length = 16):
    """
    Genera una cadena random de longitud variable

    Args:
        length (int, optional): Longitudd de la cadena. Defaults to 16.

    Returns:
        str: Cadena autogenerada
    """
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for i in range(length))
