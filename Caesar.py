from typing import List

def encryptUpper(ch: chr, key: int) -> chr:
    """
    This function encrypts a single uppercase character using a caesar cipher key and outputs the encrypted character.

    Params
    ------
    ch : chr
        The uppercase character being encrypted with the given key.
    key : int
        The key value being used in the caesar cipher.

    Returns
    -------
    chr
        The caesar encrypted character.
    """

    ch = chr(ord(ch) + key)

    #Check to see that the new character still exists within the range of capital letters 90 being capital 'Z'
    #If character exceeds these bounds subtract 26 to wrap around the alphabet and maintain a capital letter
    if ord(ch) > 90:
        ch = chr(ord(ch) - 26)

    return ch

def encryptLower(ch: chr, key: int) -> chr:
    """
    This function encrypts a single lowercase character using a caesar cipher key and outputs the encrypted character.

    Params
    ------
    ch : chr
        The lowercase character being encrypted with the given key.
    key : int
        The key value being used in the caesar cipher.

    Returns
    -------
    chr
        The caesar encrypted character.
    """

    ch = chr(ord(ch) + key)

    #Check to see that the new character still exists within the range of lowercase letters 122 being lowercase 'z'
    #If character exceeds these bounds subtract 26 to wrap around the alphabet and maintain a capital letter
    if ord(ch) > 122:
        ch = chr(ord(ch) - 26)

    return ch


def decryptUpper(ch: chr, key: int) -> chr:
    """
    This function decrypts a single uppercase character using a caesar cipher key and outputs the decrypted character.

    Params
    ------
    ch : chr
        The uppercase character being decrypted with the given key.
    key : int
        The key value being used in the caesar cipher.

    Returns
    -------
    chr
        The caesar decrypted character.
    """

    ch = chr(ord(ch) - key)

    #Check to see that the new character still exists within the range of capital letters 65 being capital 'A'
    #If character exceeds these bounds add 26 to wrap around the alphabet and maintain a capital letter
    if ord(ch) < 65:
        ch = chr(ord(ch) + 26)

    return ch

def decryptLower(ch, key):
    """
    This function decrypts a single lowercase character using a caesar cipher key and outputs the decrypted character.

    Params
    ------
    ch : chr
        The lowercase character being decrypted with the given key.
    key : int
        The key value being used in the caesar cipher.

    Returns
    -------
    chr
        The caesar decrypted character.
    """

    ch = chr(ord(ch) - key)

    # Check to see that the new character still exists within the range of capital letters 65 being capital 'A'
    # If character exceeds these bounds add 26 to wrap around the alphabet and maintain a capital letter
    if ord(ch) < 97:
        ch = chr(ord(ch) + 26)

    return ch

def caesarEncryption(plainText: str, key: int) -> str:
    """
    This function encrypts a given plaintext to a caesar cipher based on a passed key.

    Parameters
    ----------
    plainText : str
        The plaintext being encrypted.
    key : int
        The key being used in the caesar cipher.

    Returns
    -------
    str
        The caesar cipher after encryption.
    """

    cipher = ''

    for ch in plainText:
        if ch.isupper():
            cipher += encryptUpper(ch, key)

        elif ch.islower():
            cipher += encryptLower(ch, key)

        else:
            cipher += ch

    return cipher

def caesarDecryption(cipher, key):
    """
    This function decrypts a given cipher to a caesar cipher based on a passed key.

    Parameters
    ----------
    cipher : str
        The cipher being decrypted.
    key : int
        The key being used in the caesar cipher.

    Returns
    -------
    str
        The caesar cipher after encryption.
    """

    decodedCipher = ''

    for ch in cipher:
        if ch.isupper():
            decodedCipher += decryptUpper(ch, key)

        elif ch.islower():
            decodedCipher += decryptLower(ch, key)

        else:
            decodedCipher += ch

    return decodedCipher

def bruteForceDecryption(cipherText: str, vocabList: List[str]) -> str:
    """
    This function uses brute force to decrypt a given cipher text using frequency analysis of every possible key against a vocab list.

    Parameters
    ----------
    cipherText : str
        The cipher being decrypted.
    vocabList : List[str]
        A list of words being used to determine frequency of found words after an iteration of key change.

    Returns
    -------
    str
        The plain text after decryption.
    """

    plainText = ''
    mostAccurateKey = 0
    bestVocabMatch = 0

    for i in range(0, 26):
        currentVocabMatches = 0

        decryptedText = caesarDecryption(cipherText, i)
        decryptedTextLowercase = decryptedText.lower()
        searchList = decryptedTextLowercase.split()

        for word in searchList:
            if word in vocabList:
                currentVocabMatches += 1

        if currentVocabMatches > bestVocabMatch:
            bestVocabMatch = currentVocabMatches
            mostAccurateKey = i
            plainText = decryptedText

    return plainText, mostAccurateKey

if __name__ == '__main__':
    # Define vocab file here and split into accessible list
    vocabFileName = input('Please input name of vocabulary text file: ')
    file = open(vocabFileName, 'r')
    vocabList = file.read().lower().split()

    # Test caesar encryption with defined string and key
    plainText = input('\n\nPlease input a string to encrypt: ')
    encryptKey = int(input('Please input a key: '))
    cipher = caesarEncryption(plainText, encryptKey)
    print('Cipher: ' + cipher)

    # Test caesar decryption with defined cipher and key
    cipherText = input('\n\nPlease input a cipher text to decrypt: ')
    decryptKey = int(input('Please input a key: '))
    decodedCipher = caesarDecryption(cipherText, decryptKey)
    print('Cipher Decrypted: ' + decodedCipher)

    # Test brute force caesar decryption with defined cipher and vocab derived from user defined file
    bruteForceCipherText = input('\n\nPlease input a cipher text to decrypt with brute force: ')
    bruteForceValues = bruteForceDecryption(bruteForceCipherText, vocabList)
    print('Brute force cipher decrypted: ' + bruteForceValues[0])
    print('Value of key deteced from brute force decryption: ' + str(bruteForceValues[1]))

