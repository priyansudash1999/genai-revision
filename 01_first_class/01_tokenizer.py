import tiktoken
encoder = tiktoken.encoding_for_model('gpt-4o')
print("vocab size ", encoder.n_vocab)

text = "Priyansu is now like 2019 Priyansu"
tokens = encoder.encode(text)
print('Tokenized ', tokens)

# get actual text from decode data
get_text = encoder.decode(tokens)
print("Original text ", get_text)