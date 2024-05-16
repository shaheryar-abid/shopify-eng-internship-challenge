key = "SUPERSPY"
encrypted_message = "IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV"

#Takes in the key(SUPERFLY) and the encrypted message(IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV) and decrypts message
def playfair_decryptor(key, encrypted_message):
    matrix = get_matrix(key)
    decrypted_message = ""
    for i in range(0, len(encrypted_message), 2): #splits encrypted message into pairs of letters
        decrypted_message = decrypted_message + decrypt(matrix, encrypted_message[i], encrypted_message[i+1])
    return decrypted_message.replace('X', '').replace(' ', '').upper() 
    #^Removes X, lowercase, and spaces before returning final message


#Creates the matrix using the key given
def get_matrix(key):
    key = "".join(dict.fromkeys(key))
    letters = "ABCDEFGHIKLMNOPQRSTUVWXYZ" #No J in this alphabet because usually I is taken in this cipher
    matrix = []
    used_letters = set() #All used letters go here so the same letters don't repeat in the matrix

    for char in key: #Populates flat matrix(array) with the key
        if char not in used_letters:
            matrix.append(char)
            used_letters.add(char)
    
    for char in letters: #Fills in array with the rest of the alphabet
        if char not in used_letters:
            matrix.append(char)
            used_letters.add(char)

    return [matrix[i:i+5] for i in range(0, 25, 5)] #makes the flat matrix into an actual 5x5 matrix


#Finds the coordinates of the letter in the matrix populated in get_matrix
def get_indices(matrix, char):
    for index, row in enumerate(matrix):
        if char in row:
            return index, row.index(char)
    return None


#Uses the result of 'get_indices' to decrypt the message
def decrypt(matrix, x, y): 
    rowX, columnX = get_indices(matrix, x) #Position of first letter
    rowY, columnY = get_indices(matrix, y) #Position of second letter

    if rowX == rowY: #If letters are in same row
        return matrix[rowX][(columnX - 1)%5] + matrix[rowX][(columnY - 1)%5]
    
    elif columnX == columnY: #If letters are in same column
        return matrix[(rowX-1)%5][columnX] + matrix[(rowY - 1)%5][columnX]
    
    elif rowX != rowY and columnX != columnY: #If letters are in diff rows and columns
        return matrix[rowX][columnY] + matrix[rowY][columnX]


message = playfair_decryptor(key, encrypted_message) #Decrypted message
print(message) #Prints decrypted message