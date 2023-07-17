"""
This is a homework module for first lesson in module 2
"""

import random as rn


def one_random_word():
    """
    Бере зі списку слів одне рандомне слово.
    :return: str
    """
    random_word_list = ["яблуко",
                        "груша",
                        "слива",
                        "вишня",
                        "полуниця",
                        "абрикос",
                        "ананас",
                        "мандарин",
                        "виноград",
                        "персик"]

    random_word = rn.choice(random_word_list)

    return random_word


def get_number_of_attempts():
    """
    Отримує від користувача число - кількість спроб за які він хоче вгадати слово.
    :return: int
    """

    number_of_attempts = int(input("Введіть кількість спроб, за яку Ви хотіли б відгадати слово!\n"))

    return number_of_attempts


def get_input_symbols():
    """
     Отримує від користувача або букву, або ціле слово.
    :return: str
    """
    input_symbols = input("Оберіть один з двох варіантів:\n"
                          "1. Якщо хочете вгадати літеру в слові, то введіть одну літеру! \n"
                          "2. Якщо ж хочете вгадати одразу слово повністю, то введіть його повністю! \n"
                          "Очікую або букву, або ціле слово:\n").lower()
    valid_symbols = 'абвгґдеєжзиіїйклмнопрстуфхцчшщьюя'

    for char in input_symbols:
        if char not in valid_symbols:
            print("Можливо Ви випадково ввели символ який не є літерою кирилиці.\nАле є гарна новина! "
                  "Ваша спроба не згорає! Щоб відгадати - введіть літеру або слово ще раз!")
            return get_input_symbols()

    if len(input_symbols) == 1:
        print(f"Ви ввели літеру {input_symbols}.")
        return input_symbols

    elif len(input_symbols) > 1:
        print(f"Ви ввели слово \"{input_symbols}\".")
        return input_symbols

    else:
        print("Нажаль Ви не ввели жодного символу. Можливо Ви випадково натиснули клавішу Enter?\nАле є гарна новина!"
              " Ваша спроба не згорає! Щоб відгадати - введіть літеру або слово ще раз!")
        return  get_input_symbols()


def create_character_mask(guessed_word_param: str):
    """
    створює маску із символів * для слова яке загадане
    :param guessed_word_param:
    :return: str
    """


    character_mask = ""
    for char in guessed_word_param:
        character_mask = character_mask + "*"

    print(f"Ось маска слова, яке слід відгадати: {character_mask}")
    return character_mask


def users_char_option_handler(users_try_to_guess_param: str,
                              character_mask_param: str,
                              guessed_word_param: str
):
    """
    перевіряє чи запропонована користувачем літера є у слові яке користувач прагне відгадати.
    Якщо така літера є, то функція відкриває цю літеру замість символу *.
    :param users_try_to_guess_param:
    :param guessed_word_closed_with_asterisks_param:
    :param guessed_word_param:
    :return: str
    """
    guessed_word_param_list = list(guessed_word_param)
    # print(guessed_word_param_list)

    character_mask_param_list = list(character_mask_param)
    # print(character_mask_param_list)

    if users_try_to_guess_param in guessed_word_param:

        number_of_symbol_position = len(guessed_word_param) - 1

        for char in guessed_word_param:

            while number_of_symbol_position >= 0:

                if users_try_to_guess_param == guessed_word_param_list[number_of_symbol_position]:
                    character_mask_param_list[number_of_symbol_position] = users_try_to_guess_param

                number_of_symbol_position -= 1


    return ''.join(character_mask_param_list)


def field_of_wonders():
    """
    1. Бере зі списку слів одне рандомне слово.
    2. Отримує від користувача число - кількість спроб вгадати.
    3. Очікує від користувача або букву, або ціле слово.
    4. Якщо користувач пише слово, функція перевіряє чи це не те саме число, якщо так то вказує що користувач вгадав
    слово, або в іншому випадку вказує що слово не правильне.
    5. Якщо користувач ввів літеру, то функція перевіряє чи є ця літера у слові, та якщо є, виводить слово, де зірочками
    будуть закриті всі літери, які користувач ще не вгадав, або "Такої літери немає".
    6. Якщо кількість спроб закінчиться, вказує користувачю, що він програв та закінчує роботу.
    :return: None
    """


    print("Розпочинаємо гру! \nЗагадане слово - це назва фрукта українською мовою!")

    # Бере зі списку слів одне рандомне слово.
    guessed_word = one_random_word()

    # створює маску із символів * для слова яке загадане
    character_mask = create_character_mask(guessed_word)

    # Отримує від користувача число - кількість спроб за які він хоче вгадати слово.
    counter_of_attempts = get_number_of_attempts()

    #Запам'ятовуємо початкову кількість спроб, яку вказав користувач, щоб потім підказати йому скільки спроб
    #він витратив на розгадування
    primary_counter_of_attempts = counter_of_attempts

    while counter_of_attempts > 0:

        input_symbols = get_input_symbols()  # Отримує від користувача або букву, або ціле слово.

        if len(input_symbols) == 1:

            if input_symbols in guessed_word:
                print(f"Вітання! Літера \"{input_symbols}\" є у загаданому слові. Крім того, оскільки Ви "
                      f"відгадали літеру, то це відкриття цієї літери не рахується як спроба! \nКількість спроб"
                      f" зберігається! Уперед!")
                character_mask = str(users_char_option_handler(input_symbols, character_mask, guessed_word))
                print(f"Тепер маска виглядає так {character_mask}")

                if character_mask == guessed_word:
                    print(f"Вітаємо! Ви виграли! Ви вгадали слово \"{guessed_word}\" відкривши усі літери!")
                    print(f"Кількість Ваших спроб за які Ви знайшли правильну відповідь становить:"
                          f" {primary_counter_of_attempts - counter_of_attempts+1} !")
                    break

            else:
                print(f"Літери \"{input_symbols}\" не має у загаданому слові. Спробуйте ще раз!")
                print(f"Маска залишається такою як і була {character_mask}.")
                counter_of_attempts -= 1

                if counter_of_attempts == 0:
                    print(f"На жаль спроби закінчилися. Цього разу Ви не виграли. Відгадка була \"{guessed_word} ! "
                          f"Спробуте зіграти ще раз!")
                    break

        elif len(input_symbols) > 1:

            if input_symbols == guessed_word:
                print(f"Вітаємо! Ви виграли! Ви вгадали слово \"{guessed_word}\" !")
                print(f"Кількість Ваших спроб за які Ви знайшли правильну відповідь становить:"
                      f" {primary_counter_of_attempts - counter_of_attempts+1} !")
                break

            else:
                print(f"Ви не вгадали. Відгадка була \"{guessed_word}\"! Спробуйте розпочати гру з початку! ")
                break



        print(f"Кількість спроб, що залишилися: {counter_of_attempts} ! Вперед!")

        if counter_of_attempts == 1:
            print("Зверніть увагу! Остання спроба! Потрібно вгадати!")


field_of_wonders()
