import decode
import utility_functions
import encode
from values import ERROR, WARNING
import argparse

# ---------------------------------------------------------------------------------------+
# I wanna create my own HexDec encoding                                                  |
# sooooo here it is:                                                                     |
#                                                                                        |
# TODO: convert the encoding/decoding variables containing the values into one JSON file |
# TODO: make the array debbug_output_array have actual use                               |
# ---------------------------------------------------------------------------------------+
parser = argparse.ArgumentParser(description="Decode/Encode a string/file")
parser.add_argument("-rf", "--read-file",     help="read data from a file - the input after the command is the file path")
parser.add_argument("-rt","--read-terminal",  help="read data from the terminal - bool",action="store_true")
parser.add_argument("-s","--secret",          help="the secret key used in encription - string")
parser.add_argument("-n","--noise",           help="noise amount by [length of data]/[-n] - if no input default is no noise", type=int)
parser.add_argument("-d","--decode",          help="decode the message",                action="store_true")
parser.add_argument("-e","--encode",          help="encode the message",                action="store_true")
parser.add_argument("-ot","--output-terminal",help="output the result to the terminal", action="store_true")
parser.add_argument("-of","--output-file",    help="output the result to a file")
parser.add_argument("-c","--create-file",     help="create a custom file on runtime")
args = parser.parse_args()

output_path = r""
read_path = r""

read_file_terminal = "t"
encode_secret = ""
arg_noise_amount = 1
debbug_output = False #not implemented for now
terminal_output = False
file_output = False
encode_or_decode = ""
create_file_name = ""

debbug_output_array = [] #an array of all the debbug messages, entered encode, finished adding timestamps, finished encode, finished file write

if args.read_file:
    read_file_terminal = "f"
    read_path = args.read_file

if args.read_terminal:
    read_file_terminal = "t"

if args.secret:
    encode_secret = args.secret
else:
    encode_secret = "NO ENCODE SECRET" #if no encode placeholder secret

if args.noise:
    arg_noise_amount = args.noise
else:
    arg_noise_amount = -1 # value failing the check in CreateNoise() -> (arg_noise_amount > 0)

if args.decode:
    encode_or_decode = "d"

if args.encode:
    encode_or_decode = "e"

if args.output_terminal:
    terminal_output = True

if args.output_file:
    file_output = True
    output_path = args.output_file

if args.create_file:
    create_file_name = args.create_file
    with open(create_file_name,"w") as file:
        file.write("")

def Startup():
    # Lahav         DF A0 AB A0 BD
    output = ""
    
    if encode_or_decode[0].lower() == "e":
        if read_file_terminal[0].lower() == "f":
            if utility_functions.CheckIfFileExists(read_path):
                with open(read_path, "r") as read_file:
                    message = read_file.read()
                output = encode.Encode(message, encode_secret, arg_noise_amount)
            else:
                print(f"{ERROR} file does not exist")

        elif read_file_terminal[0].lower() == "t":
            message = input("Text to use:\n")
            output = encode.Encode(message, encode_secret, arg_noise_amount)


    elif encode_or_decode[0].lower() == "d":
        if read_file_terminal[0].lower() == "f":
            if utility_functions.CheckIfFileExists(read_path):
                with open(read_path, "r") as read_file:
                    message = read_file.read()
                output = decode.Decode(message)
            else:
                print(f"{ERROR} file does not exist")

        elif read_file_terminal[0].lower() == "t":
            message = input("Text to use:\n")
            output = decode.Decode(message)

    else:
        print(f"{ERROR} chat ur action is wrong")

    if terminal_output:
        print(output)
    elif file_output:
        utility_functions.WriteOutputToFile(output,output_path)
    else:
        print(f"{WARNING} no output method chosen")


if __name__ == "__main__":
    Startup()