alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.
len_of_text = len(text)
def encrypt(direction, text, shift):
  list_number = []
  for one_alphabet in text:
    position = 0
    for b in alphabet:
      if alphabet[position] == one_alphabet:
        list_number.append(position)
        break
      else:
        position-=1
  
  encode_list = []
  decode_list = []
  output_list = []
  if direction == "encode":
    for old_list in list_number:
      encode_list.append(old_list+shift)
    for new_list_word in encode_list:
      output_list.append(alphabet[new_list_word])
    print("".join(output_list))    
  elif direction == "decode":
    for old_list in list_number:
      decode_list.append(old_list+shift)
    for new_list_word in decode_list:
      output_list.append(alphabet[new_list_word])
    print("".join(output_list))
  else:
    print("Don't understand your command.")
      
  
  
  
  
  print(list_number)
      
encrypt(direction, text, shift)      
    