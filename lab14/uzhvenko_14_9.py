def read_numb_from_file(file_path):

    try:
        with open(file_path, 'r') as file:
            numbers = [float(line.strip()) for line in file.readlines()]  # список чисел, чит кожен рядок файлу, видаляючи зайві пробіли та перетворюючи на дійсні числа
        return numbers

    except FileNotFoundError as e:
        print(f"мейбі тут помилка, треба думати краще: {e}")
    except PermissionError as e:
        print(f"мейбі тут помилка, треба думати краще: {e}")
    except ValueError as e:
        print(f"мейбі тут помилка, треба думати краще: {e}")


def process_files(file_list_path):

    try:
        with open(file_list_path, 'r') as content_file:
            file_names = content_file.read().splitlines()  #  зчит вміст файлу "content.txt", ділимо його на рядки

        for file_name in file_names:  # цикл для кожного імені файлу у списку
            numbers = read_numb_from_file(file_name)
            if numbers is not None:  # перевірка на коректний результат від "read_numbers_from_file"
                total_sum = sum(numbers)
                print(f"сума чисел у файлі {file_name}: {total_sum}")

    except FileNotFoundError as e:  # працюємо з непередбачуваними ситуаціями
        print(f"error: {e}")
    except PermissionError as e:
        print(f"error: {e}")


process_files('content.txt')  # обр ф -> викл функц
