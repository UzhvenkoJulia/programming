def find_longest_word_simple(sky):
    with open(sky, 'r', encoding='utf-8') as ky:  # для себе: "encoding='utf-8'" вказує кодування файлу, що допомагає коректно зчитувати текстові дані, особливо якщо вони містять символи з різних мов
        content = ky.read()

        words = []
        current_word = ''

        for char in content:
            if char.isalpha():  # алфавітик
                current_word += char
            elif current_word:
                words.append(current_word)  # слово дод до кінця списку +
                current_word = ''

        longest_word = max(words, key=len)
        return longest_word



def count_words_simple(sky):
    with open(sky, 'r', encoding='utf-8') as ky:
        content = ky.read()

        words = []
        current_word = ''

        for char in content:
            if char.isalpha():
                current_word += char
            elif current_word:
                words.append(current_word)
                current_word = ''

        return len(words)



def clean_file_simple(sky):
    with open(sky, 'r', encoding='utf-8') as ky:
        content = ky.read()

        words = []
        current_word = ''

        for char in content:
            if char.isalpha():
                current_word += char
            elif current_word:
                words.append(current_word)
                current_word = ''

        cl_words = [word for word in words if len(word) > 1]  # список слів, в яких довжина перевищує 1 +
        cleaned_content = ' '.join(cl_words)

    with open("H.txt", 'w', encoding='utf-8') as result_ky:  # "H.txt" - мій текст файл, у якому міститься певне задане речення
        result_ky.write(cleaned_content)

    return cleaned_content  # поверт вміст для подальшого використання; "with", -> ф автоматич закритий, коли викон блоку коду вийде за межі



def remove_extra_spaces_simple(sky):
    with open(sky, 'r', encoding='utf-8') as ky:
        box = ky.readlines()

    cleaned_lines = []
    for stick in box:
        cleaned_lines.append(' '.join(stick.split()))

    with open("H.txt", 'w', encoding='utf-8') as result_ky:
        result_ky.writelines(cleaned_lines)

    return cleaned_lines



def insert_spaces_simple(sky):
    with open(sky, 'r', encoding='utf-8') as ky:
        box = ky.readlines()

    joke = []
    for line in box:
        joke.append(' '.join(line.split()))

    result_lines = [line.ljust(80) for line in joke]  # "line.ljust(80)": викликання методу рядка ljust, який доповнює рядок пробілами справа до вказаної довжини; цього не знала((

    with open("H.txt", 'w', encoding='utf-8') as result_ky:
        result_ky.writelines(result_lines)

    return result_lines



sky = "H.txt"  # приклад


result_find_longest_word = find_longest_word_simple(sky)
print(f"найдовше слово у файлі: {result_find_longest_word}")


result_count_words = count_words_simple(sky)
print(f"к-сть слів у файлі: {result_count_words}")


result_clean_ky = clean_file_simple(sky)
print(f"зміст текстового файлу після вилучення зайвих пропусків та слів із однією буквою:\n{result_clean_ky}")


result_remove_extra_spaces = remove_extra_spaces_simple(sky)
print(f"зміст текстового файлу після вилучення пропусків на початку, в кінці та між словами (окрім одного):\n{result_remove_extra_spaces}")


result_insert_spaces = insert_spaces_simple(sky)
print(f"зміст текстового файлу після вставки пропусків рівномірно між словами:\n{result_insert_spaces}")
