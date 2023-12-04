def create_text_file(box, surprise_name):

    with open(surprise_name, 'w') as surprise:

        way = [box[i:i+40] for i in range(0, len(box), 40)]  # рядки по 40 літер; до отакого запису комбінацій з "і" я не сама додумалася, допомога залу була присутня))


        for stick in way:
            surprise.write(stick + '\n')  # рядки у файл(відкритий); \\
            # (запис даних у файл, виклик його; рядок тексту (який вже розбит на частини по =< 40 літер -> запис у файл)


    with open(surprise_name, 'r') as surprise:  # треба це все діло вивести зараз
        content = surprise.read()
        print(content)


box = ("батько мав кота, який намагався розгадати таємниці квантового світу фізики, сидячи в коробці з-під піцци")  #ось моє творіння
surprise_name = "surprise.txt"
create_text_file(box, surprise_name)
