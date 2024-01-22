import csv
import re

def autolabel(old_file, new_file):
    """
    automatically number data according to ROYIN's entry system
    :param filein: (file) a file with unedited delimiter
    :return: (file) a csv list with the numbers of the entry system
    """
    # open file for reading
    in_file = open(old_file, "r", encoding="utf-8")

    # open file for writing
    out_file = open(new_file, "w", encoding="utf-8-sig", newline='')

    # create writer for csv file
    writer = csv.writer(out_file)

    # write header
    header = ["word", "number"]
    writer.writerow(header)

    line_count = 0

    for line in in_file:
        entry_count = 0
        # strip \n from each definition
        new_line = line.strip("\n")

        # split at every ," if there are multiple definitions or ", if there are multiple pronunciations
        if "\"" in line:
            word_row = re.split(",\"|\",", new_line)

        else:
            word_row = new_line.split(",")
        # print(word_row)

        # split words; split at every ," if there are multiple definitions or ", if there are multiple pronunciations
        line_count += 1
        if line_count > 1:

            # the word is the first element of the list
            word = word_row[0]
            # the definition is the second element of the list
            definition = word_row[1]

            # Define the list of delimiters within brackets
            bracket_delimiters = []

            new_definitions = re.split(r'\s(?=[ก-ฮ]\.)|;', definition)

            for entry in new_definitions:
                print(entry)
                entry_count += 1
                writer.writerow([word, entry_count, entry])
                print(entry_count)

                count = entry.count("เช่น")

                print(entry_count)
                # if there is เช่น or หรือ within the same part of speech, label as same entry
                for letter in entry:
                    if ',' == letter:
                        writer.writerow([word, entry_count, entry])
                        print(entry_count)

                    if 'หรือ' == letter:
                        writer.writerow([word, entry_count, entry])
                        print(entry_count)

    in_file.close()
    out_file.close()

def main():
    autolabel("test2.csv", "new_file.csv")
    print("yay you did it!")

if __name__ == '__main__':
    main()