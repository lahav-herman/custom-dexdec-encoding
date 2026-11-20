from values import ERROR, INFO, custom_symbols_pt1,  custom_symbols_pt2, custom_symbols_pt3, signatures_list, number_counting, letter_A, letter_B, letter_C, letter_D, letter_E, letter_F
import time
from utility_functions import CheckPairIntegrity
# DECODE
def Decode(text_to_decode):
    #start timer
    start_time = time.perf_counter()

    counter = 0
    pair_list = text_to_decode.split()

    output_chars = []
    output_text = ""

    signature=""
    value=""

    #integrity check before decoding
    for pair in pair_list:
        if not CheckPairIntegrity(pair):
            print(f"{ERROR} pair integrity damaged, cant decode")
            return f"{ERROR} pair integrity damaged, cant decode"


    for current_pair in pair_list:
        signature=signatures_list[current_pair[0]]
        value=current_pair[1]
        # find current number
        if signature=="number":
            current_num=number_counting[value]
            output_chars.append(current_num)
        elif signature=="symbol-1":
            current_symbol=custom_symbols_pt1[value]
            output_chars.append(current_symbol)
        elif signature=="symbol-2":
            current_symbol=custom_symbols_pt2[value]
            output_chars.append(current_symbol)
        elif signature=="symbol-3":
            current_symbol=custom_symbols_pt3[value]
            if current_symbol == "!T" or current_symbol == "!S": # remove the separator and create a newline
                output_chars.append("\n")
            else:
                output_chars.append(current_symbol)
        elif signature=="letter_a":
            current_letter=letter_A[value]
            output_chars.append(current_letter)
        elif signature=="letter_b":
            current_letter=letter_B[value]
            output_chars.append(current_letter)
        elif signature=="letter_c":
            current_letter=letter_C[value]
            output_chars.append(current_letter)
        elif signature=="letter_d":
            current_letter=letter_D[value]
            output_chars.append(current_letter)
        elif signature=="letter_e":
            current_letter=letter_E[value]
            output_chars.append(current_letter)
        elif signature=="letter_f":
            current_letter=letter_F[value]
            output_chars.append(current_letter)
        elif signature=="":
            continue
        else:
            continue

    #convert the decoded list into a single string
    while counter < len(output_chars):
        output_text += output_chars[counter]
        counter += 1

    #stop timer
    elapsed_time = time.perf_counter() - start_time
    print(f"{INFO} Elapsed time: {elapsed_time:.5f}")
    return output_text
