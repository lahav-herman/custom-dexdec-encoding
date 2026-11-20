from values import INFO
from utility_functions import CombineNoiseAndEncoding, CreateEncodeSecret, CreateTimeStamp, CreateNoise, CombineEncodeAndMisc,AddSeparators, EncodeCharacters, CreatePairs 
import time
import pyperclip

def Encode(text_to_encode,secret,arg_noise_amount):
    #start timer
    start_time = time.perf_counter()

    encoding_final_output_text = ""
    output_encoding_value = []
    output_encoding_signature = []
    output_encoding_pairs = []
    secret_char_list = CreateEncodeSecret(secret)
    time_stamp_char_list = CreateTimeStamp()

    message_char_list = list(text_to_encode)

    combined_char_list = CombineEncodeAndMisc(secret_char_list,message_char_list,time_stamp_char_list)

    combined_char_list_and_separators = AddSeparators(combined_char_list,secret_char_list,time_stamp_char_list)

    output_encoding_value,output_encoding_signature = EncodeCharacters(combined_char_list_and_separators) #------------

    output_encoding_pairs = CreatePairs(output_encoding_value,output_encoding_signature)
    
    noise_pairs = CreateNoise(output_encoding_pairs,arg_noise_amount)

    encoding_and_noise = CombineNoiseAndEncoding(output_encoding_pairs, noise_pairs)

    #seperate with a space each pair
    for item in encoding_and_noise:
        encoding_final_output_text += f"{item} "
    
    #start from 0 and stop at length-1 which means remove the last space given from my the last 2 lines of code^
    encoding_final_output_text = encoding_final_output_text[0:-1]

    #stop timer
    elapsed_time = time.perf_counter() - start_time
    print(f"{INFO} Elapsed time: {elapsed_time:.5f}")

    pyperclip.copy(encoding_final_output_text) #copy encoding to clipboard

    return encoding_final_output_text