codecs = ["ASCII", "UTF-32", "utf-16"]
for codec in codecs:
    with open("output_file.txt", "r", encoding=codec) as my_file:
        list_words = my_file.readline()
    print(codec.rjust(12), "|", list_words)