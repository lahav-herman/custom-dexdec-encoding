from values import ALLOWED_VALUES, custom_symbols_pt1,  custom_symbols_pt2, custom_symbols_pt3, signatures_list, number_counting, letter_A, letter_B, letter_C, letter_D, letter_E, letter_F
import random
import time
from datetime import datetime

def FindNumberIndex(query):
    query = str(query)
    #reverse lookup table
    for object_index,object_value in number_counting.items():
        if object_value == query:
            return object_index
        else:
            continue
def FindSymbol_1_Index(query):
    query = str(query)
    for object_index,object_value in custom_symbols_pt1.items():
        if object_value == query:
            return object_index
        else:
            continue
def FindSymbol_2_Index(query):
    query = str(query)
    for object_index,object_value in custom_symbols_pt2.items():
        if object_value == query:
            return object_index
        else:
            continue
def FindSymbol_3_Index(query):
    query = str(query)
    for object_index,object_value in custom_symbols_pt3.items():
        if object_value == query:
            return object_index
        else:
            continue
def FindLetterAIndex(query):
    query = str(query)
    for object_index,object_value in letter_A.items():
        if object_value == query:
            return object_index
        else:
            continue
def FindLetterBIndex(query):
    query = str(query)
    for object_index,object_value in letter_B.items():
        if object_value == query:
            return object_index
        else:
            continue
def FindLetterCIndex(query):
    query = str(query)
    for object_index,object_value in letter_C.items():
        if object_value == query:
            return object_index
        else:
            continue
def FindLetterDIndex(query):
    query = str(query)
    for object_index,object_value in letter_D.items():
        if object_value == query:
            return object_index
        else:
            continue
def FindLetterEIndex(query):
    query = str(query)
    for object_index,object_value in letter_E.items():
        if object_value == query:
            return object_index
        else:
            continue
def FindLetterFIndex(query):
    query = str(query)
    for object_index,object_value in letter_F.items():
        if object_value == query:
            return object_index
        else:
            continue
def FindSignatureIndex(query):
    # return an array
    query = str(query)
    found_indexes = []
    for object_index,object_value in signatures_list.items():
        if object_value == query:
            found_indexes.append(object_index)
        else:
            continue
    return found_indexes

def AssignSignature(output_signature,signature):
    signature_index = FindSignatureIndex(signature) #first item of index array
    if len(signature_index) != 0:
        output_signature.append(signature_index[0])
    else:
        print("Signature error:", signature)

def CreateNoise(encoding_pairs,arg_noise_amount):

    if arg_noise_amount > 0:
        noise_signatures = []
        noise_values = []
        noise_pairs = []
        noise_amount = len(encoding_pairs) / arg_noise_amount

        # for now the only noise signatures generated will be from the noise signatures:
        noise_signature_array = FindSignatureIndex("")
        # for now only has 1 to 9, later I will make it have some of the numbers
        # and letters C and F

        noise_signature_array_location = 0
        noise_values_location = 0
        counter = 0

        while counter < noise_amount:
            noise_signature_array_location = random.randint(0, len(noise_signature_array)-1)
            noise_signatures.append(noise_signature_array[noise_signature_array_location]) # append into noise_signatures
            # one of the signatures from the list noise_signature_array in position n_s_a_location
            counter += 1

        counter = 0 #reset counter

        while counter < noise_amount:
            noise_values_location = random.randint(0, len(ALLOWED_VALUES)-1)
            noise_values.append(ALLOWED_VALUES[noise_values_location])
            counter += 1

        counter = 0

        while counter < noise_amount:
            # use the random list of signatures and random list of values
            noise_pairs.append(f"{noise_signatures[counter]}{noise_values[counter]}")
            counter += 1

        return noise_pairs
    else: 
        return [] #empty noise list

def EncodeCharacters(combined_char_list):
    encoding_values = []
    encoding_signatures = []
    #check every char in the array and inserts each into the value array and signature array
    for character in combined_char_list:
        if character in number_counting.values():
            encoding_values.append(FindNumberIndex(character))
            AssignSignature(encoding_signatures,"number")
        elif character in custom_symbols_pt1.values():
            encoding_values.append(FindSymbol_1_Index(character))
            AssignSignature(encoding_signatures,"symbol-1")
        elif character in custom_symbols_pt2.values():
            encoding_values.append(FindSymbol_2_Index(character))
            AssignSignature(encoding_signatures,"symbol-2")
        elif character in custom_symbols_pt3.values():
            encoding_values.append(FindSymbol_3_Index(character))
            AssignSignature(encoding_signatures,"symbol-3")
        elif character in letter_A.values():
            encoding_values.append(FindLetterAIndex(character))
            AssignSignature(encoding_signatures,"letter_a")
        elif character in letter_B.values():
            encoding_values.append(FindLetterBIndex(character))
            AssignSignature(encoding_signatures,"letter_b")
        elif character in letter_C.values():
            encoding_values.append(FindLetterCIndex(character))
            AssignSignature(encoding_signatures,"letter_c")
        elif character in letter_D.values():
            encoding_values.append(FindLetterDIndex(character))
            AssignSignature(encoding_signatures,"letter_d")
        elif character in letter_E.values():
            encoding_values.append(FindLetterEIndex(character))
            AssignSignature(encoding_signatures,"letter_e")
        elif character in letter_F.values():
            encoding_values.append(FindLetterFIndex(character))
            AssignSignature(encoding_signatures,"letter_f")
        else:
            encoding_values.append("3")
            AssignSignature(encoding_signatures,"symbol-3")

    return encoding_values,encoding_signatures

def CreatePairs(encoding_value,encoding_signature):
    #create the pairs
    encoding_pairs = []
    counter = 0
    while counter < len(encoding_value):
        encoding_pairs.append(f"{encoding_signature[counter]}{encoding_value[counter]}")
        counter +=1

    return encoding_pairs

def CombineNoiseAndEncoding(encoding_pairs,noise_pairs):
    encoding_and_noise_pairs = encoding_pairs.copy()

    counter = 0
    position = 0

    # cycling through the noise_pairs array
    while counter < len(noise_pairs):
        position = random.randint(0,len(encoding_and_noise_pairs))
        encoding_and_noise_pairs.insert(position,noise_pairs[counter])
        counter += 1

    return encoding_and_noise_pairs

def CreateEncodeSecret(secret:str):
    #the secret is a small message at the start of the encoding
    # may be will be used for something more interesting later
    secret_char_list = list(secret)

    return secret_char_list

def CombineEncodeAndMisc(secret_text, message_text, time_stamp_text):
    combined_char_list = []

    combined_char_list.extend(secret_text)
    combined_char_list.extend(message_text)
    combined_char_list.extend(time_stamp_text)

    return combined_char_list

def CreateTimeStamp():
    date = time.strftime("%d-%m-%y")
    hour = datetime.now().hour
    minute = datetime.now().minute
    clock_time = f"{hour}:{minute}"
    time_stamp_text = list(clock_time +" "+ date)

    return time_stamp_text

def AddSeparators(combined_char_list,secret_text,time_stamp_text):
    combined_char_list_and_separators = combined_char_list.copy()

    secret_separator_location = len(secret_text)
    time_stamp_separator_location = len(combined_char_list)-len(time_stamp_text) + 1
    
    combined_char_list_and_separators.insert(secret_separator_location,custom_symbols_pt3["4"])
    combined_char_list_and_separators.insert(time_stamp_separator_location,custom_symbols_pt3["5"])

    return combined_char_list_and_separators

def CheckIfFileExists(check_file_path):
    try:
    # Try to open the file
        with open(check_file_path, 'r') as file:
            return True
    except FileNotFoundError:
        return False

def CheckPairIntegrity(pair):
    if len(pair) != 2:
        return False
    elif pair[0] not in ALLOWED_VALUES:
        return False
    elif pair[1] not in ALLOWED_VALUES:
        return False 
    else:
        return True
    
def WriteOutputToFile(write_input,output_path):
    with open(output_path,"w") as file:
        file.write(write_input)