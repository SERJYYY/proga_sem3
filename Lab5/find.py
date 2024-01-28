import json

week = ('Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота')


def get_lessons_with_teacher(lessons, teacher_name):
    target_lessons = []
    for lesson in lessons:
        if lesson["type"] != 'none':
            for les in lesson['lesson']:
                teacher = les.get('teacher')
                if teacher and teacher_name in teacher:
                    target_lessons.append({"lesson_n": lesson["lesson_number"], "lesson": les})
    return target_lessons


def get_lessons_with_classroom(lessons, classroom_to_find):
    target_lessons = []
    for lesson in lessons:
        if lesson["type"] != 'none':
            for les in lesson['lesson']:
                classroom = les.get('classroom')
                if classroom and classroom_to_find in classroom:
                    target_lessons.append({"lesson_n": lesson["lesson_number"], "lesson": les})
    return target_lessons


def print_lessons(lessons):
    for day_name in week:
        lessons_day = [lesson for lesson in lessons if lesson["day"] == day_name]
        if lessons_day:
            print(day_name)
            for l in lessons_day:
                print(f'{l["lesson_n"]}| {l["classroom"]:6} | {l["group"]:8} | {l["subject"]} {l["mode"]}', end='')
                if l["type"] == "числитель":
                    print(" по числителям")
                elif l["type"] == "знаменатель":
                    print(" по знаменателям")
                else:
                    print()


def find_std(data, mode=None):
    if mode is None:
        mode = input("?: ")
        pass

    if mode == "teacher":
        info = input("Введите имя препода:")
        variants, matched_lessons = find_by_filter(data, mode, info)

        if len(variants) == 0:
            return None
        elif len(variants) > 1:
            print(f"Найдено {len(variants)} преподов по вашему запросу")
            i = 1
            for t in variants:
                print(f"{i}. {t}")
                i += 1
            choose = int(input("Выберете кого показать: ")) - 1
            var = variants[choose]
        else:
            var = variants[0]

        lessons = [lesson for lesson in matched_lessons if lesson[mode] == var]
        lessons.sort(key=lambda les: (week.index(les['day']), les['lesson_n']))

        print_lessons(lessons)





def find_by_filter(data, mode, info):
    filter_lesson = None
    if mode == "teacher":
        filter_lesson = get_lessons_with_teacher
    elif mode == "classroom":
        filter_lesson = get_lessons_with_classroom

    res = []
    schedule = data["schedule"]

    for group in schedule:
        week_schedule = group["schedule"]
        for day in week_schedule:
            lessons = day["lessons"]

            founded_lessons = filter_lesson(lessons, info)

            if founded_lessons:
                for les in founded_lessons:
                    target = {"group": group["group"], "day": day["day"], "lesson_n": les["lesson_n"]}
                    les_info = les['lesson']
                    if les_info.get('split_type'):
                        target["type"] = les_info.get('split_type')
                    else:
                        target["type"] = "общий"

                    if les_info.get('classroom'):
                        target["classroom"] = les_info["classroom"]
                    target["subject"] = les_info["subject"]
                    target["mode"] = les_info["mode"]
                    if les_info.get('teacher'):
                        target["teacher"] = les_info["teacher"]

                    res.append(target)

    founded_variants = sorted(list({lesson[mode] for lesson in res}))
    return founded_variants, res

def find_by_teacher(data):
    teacher = input("Введите препода: ")
    res = []
    # teacher = "Белоусов"
    schedule = data["schedule"]

    for group in schedule:
        week_schedule = group["schedule"]
        for day in week_schedule:
            lessons = day["lessons"]
            lessons_with_teacher = get_lessons_with_teacher(lessons, teacher)

            if lessons_with_teacher:
                for les in lessons_with_teacher:
                    target = {"group": group["group"], "day": day["day"], "lesson_n": les["lesson_n"]}
                    les_info = les['lesson']
                    if les_info.get('split_type'):
                        target["type"] = les_info.get('split_type')
                    else:
                        target["type"] = "общий"

                    target["classroom"] = les_info["classroom"]
                    target["subject"] = les_info["subject"]
                    target["mode"] = les_info["mode"]
                    if les_info.get('teacher'):
                        target["teacher"] = les_info["teacher"]

                    res.append(target)
    teachers = sorted(list({lesson["teacher"] for lesson in res}))
    if len(teachers) == 0:
        print("Этого препода не существует или у него нет пар или у него только лабы")
        return
    elif len(teachers) > 1:
        print(f"Найдено {len(teachers)} преподов по вашему запросу")
        i = 1
        for t in teachers:
            print(f"{i}. {t}")
            i += 1
        choose = int(input("Выберете кого показать: ")) - 1
        choosen_teacher = teachers[choose]
    else:
        choosen_teacher = teachers[0]

    lessons = [lesson for lesson in res if lesson['teacher'] == choosen_teacher]

    lessons.sort(key=lambda x: (week.index(x['day']), x['lesson_n']))
    for day_name in week:
        lessons_day = [lesson for lesson in lessons if lesson["day"] == day_name]
        if lessons_day:
            print(day_name)
            for l in lessons_day:
                print(f'{l["lesson_n"]}| {l["classroom"]:6} | {l["group"]:8} | {l["subject"]} {l["mode"]}', end='')
                if l["type"] == "числитель":
                    print(" по числителям")
                elif l["type"] == "знаменатель":
                    print(" по знаменателям")
                else:
                    print()


def find_by_classroom(data):
    classroom = input("Введите кабинет: ")
    res = []
    schedule = data["schedule"]

    for group in schedule:
        week_schedule = group["schedule"]
        for day in week_schedule:
            lessons = day["lessons"]
            lessons_with_teacher = get_lessons_with_classroom(lessons, classroom)

            if lessons_with_teacher:
                for les in lessons_with_teacher:
                    target = {"group": group["group"], "day": day["day"], "lesson_n": les["lesson_n"]}
                    les_info = les['lesson']
                    if les_info.get('split_type'):
                        target["type"] = les_info.get('split_type')
                    else:
                        target["type"] = "общий"

                    target["classroom"] = les_info["classroom"]
                    target["subject"] = les_info["subject"]
                    target["mode"] = les_info["mode"]
                    if (les_info.get('teacher')):
                        target["teacher"] = les_info["teacher"]

                    res.append(target)
    classrooms = sorted(list({lesson["classroom"] for lesson in res}))
    if len(classrooms) == 0:
        print("Кабинет не найден")
        return
    elif len(classrooms) > 1:
        print(f"Найдено {len(classrooms)} кабинетов.")
        i = 1
        for t in classrooms:
            print(f"{i}. {t}")
            i += 1
        choose = int(input("Выберете что показать: ")) - 1
        choosen_classroom = classrooms[choose]
    else:
        choosen_classroom = classrooms[0]

    lessons = [lesson for lesson in res if lesson['classroom'] == choosen_classroom]

    print(lessons)
    lessons.sort(key=lambda x: (week.index(x['day']), x['lesson_n']))
    for day_name in week:
        lessons_day = [lesson for lesson in lessons if lesson["day"] == day_name]
        if lessons_day:
            print(day_name)
            for l in lessons_day:
                print(f'{l["lesson_n"]}| {l["teacher"]:20} | {l["group"]:8} | {l["subject"]} {l["mode"]}', end='')
                if l["type"] == "числитель":
                    print(" по числителям")
                elif l["type"] == "знаменатель":
                    print(" по знаменателям")
                else:
                    print()


if __name__ == "__main__":
    DATA_FILE = "data_tmp.json"
    with open(DATA_FILE, 'r') as data_file:
        data = json.load(data_file)
        find_std(data)
