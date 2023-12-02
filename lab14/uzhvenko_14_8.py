def process_kyky():
    count_runtime_errorerrorerrorsss = 0
    count_type_errorerrorerrorsss = 0
    count_value_errorerrorerrorsss = 0

    while True:  # безкінечний цикл
        you_input = input("введіть ч або 'досить' для заверш: ")

        if you_input.lower() == 'досить':  # перевірка; не забуваємо розпізнати наше слово "ДОСИТЬ"
            break

        try:
            number = int(you_input)

            if number > 9:
                raise RuntimeError("errorerrorerror: ч > 9")
            elif number < 0:
                raise TypeError("errorerrorerror: ч < 0")
            elif not (0 <= number <= 9):
                raise ValueError("errorerrorerror: ч не знаход в діапаз від 0 до 9")

        except RuntimeError as e:  # обробл типи виключень і вивод повідомлення про помилку; збільш лічильники помилок кожного типу
            print(e)
            count_runtime_errorerrorerrorsss += 1
        except TypeError as e:
            print(e)
            count_type_errorerrorerrorsss += 1
        except ValueError as e:
            print(e)
            count_value_errorerrorerrorsss += 1

    print(f"к-ть errorerrorerror RuntimeError: {count_runtime_errorerrorerrorsss}")
    print(f"к-сть errorerrorerror TypeError: {count_type_errorerrorerrorsss}")
    print(f"к-сть errorerrorerror ValueError: {count_value_errorerrorerrorsss}")


process_kyky()  # потрібна обробка вводу -> викликаємо функц
