import operator


def start_frequency_finder():
    freq_dict = {}
    text_line = input("Enter your string: ")
    for i in text_line.split(' '):

        if i not in freq_dict:
            freq_dict[i] = 1
            continue

        freq_dict[i] += 1

    sorted_freq_dict = sorted(freq_dict.items(), key=operator.itemgetter(0))

    for i in sorted_freq_dict:
        print(i[0], i[1])


