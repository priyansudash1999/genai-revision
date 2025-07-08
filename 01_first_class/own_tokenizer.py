class Encoder:
  def __init__(self, vocab_size):
    self.vocab_size = vocab_size

  def encode(self, text):
    tokenized_letter_series = {
      0: " ", 1: "a", 2: "b", 3: "c", 4: "d", 5: "e", 6: "f", 7: "g", 8: "h", 9: "i", 10: "j", 11: "k", 12: "l", 13: "m", 14: "n", 15: "o", 16: "p", 17: "q", 18: "r", 19: "s", 20: "t", 21: "u", 22: "v", 23: "w", 24: "x", 25: "y", 26: "z", 100: "A", 101: "B", 102: "C", 103: "D", 104: "E", 105: "F", 106: "G", 107: "H", 108: "I", 109: "J", 110: "K", 111: "L", 112: "M", 113: "N", 114: "O", 115: "P", 116: "Q", 117: "R", 118: "S", 119: "T", 120: "U", 121: "V", 122: "W", 123: "X", 124: "Y", 125: "Z",
    }
    letter_to_token = {v: k for k, v in tokenized_letter_series.items()}

    tokenized_arr = []
    for letter in text:
        token = letter_to_token.get(letter)
        if token is not None:
            tokenized_arr.append(token)
        else:
            raise ValueError(f"Unsupported character: '{letter}'")
    return tokenized_arr
  def decode(self, tokens):
    tokenized_letter_series = {
        0: " ", 1: "a", 2: "b", 3: "c", 4: "d", 5: "e", 6: "f", 7: "g", 8: "h", 9: "i", 10: "j",
        11: "k", 12: "l", 13: "m", 14: "n", 15: "o", 16: "p", 17: "q", 18: "r", 19: "s", 20: "t",
        21: "u", 22: "v", 23: "w", 24: "x", 25: "y", 26: "z", 100: "A", 101: "B", 102: "C", 103: "D",
        104: "E", 105: "F", 106: "G", 107: "H", 108: "I", 109: "J", 110: "K", 111: "L", 112: "M",
        113: "N", 114: "O", 115: "P", 116: "Q", 117: "R", 118: "S", 119: "T", 120: "U", 121: "V",
        122: "W", 123: "X", 124: "Y", 125: "Z"
    }

    original_string = ""
    for token in tokens:
        letter = tokenized_letter_series.get(token)
        if letter is not None:
            original_string += letter
            # print(original_string)
        else:
            original_string += ""
    
    return original_string


  def n_vocab(self):
    return self.vocab_size

encoder = Encoder(10)
print(encoder.encode(input("Give a string:- ")))
print(encoder.decode([1,2,3]))
print(encoder.n_vocab())


