def anagrama(palabra1, palabra2):
    palabra1sorted = sorted(palabra1.lower())
    palabra2sorted = sorted(palabra2.lower())
    if palabra1sorted == palabra2sorted:
        return True
    else:
        return False
