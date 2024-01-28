class Disk:
    def __init__(self, id, name, volume, speed, pc_id):
        self.id = id
        self.name = name
        self.volume = volume
        self.speed = speed
        self.pc_id = pc_id

    def __str__(self):
        return f"{self.name}, volume: {self.volume}"


class PC:
    def __init__(self, id, owner):
        self.id = id
        self.owner = owner

    def __str__(self):
        return f"{self.owner}"


class PCDisks:
    def __init__(self, pc_id, disk_id):
        self.pc_id = pc_id
        self.disk_id = disk_id

    def __str__(self):
        return f"{self.disk_id[0]} - {self.pc_id[0]}"


disks = [Disk(1, "HDD1", 2000, 128, 1),
         Disk(2, "HDD2", 1000, 128, 2),
         Disk(3, "SSD1", 1000, 550, 1),
         Disk(4, "SSD2", 2000, 450, 3),
         Disk(5, "M2", 500, 600, 2)
         ]

pcs = [PC(1, "user"),
       PC(2, "admin"),
       PC(3, "employee")
       ]

disk_pc = [PCDisks(1, 3),
            PCDisks(1, 2),
            PCDisks(3, 2),
            PCDisks(5, 1),
            PCDisks(5, 3),
            PCDisks(4, 3),
            PCDisks(2, 2),
            PCDisks(2, 3),
            ]


def main():
    otm = [(i, j) for i in disks for j in pcs if i.pc_id == j.id]
    otm.sort(key=lambda x: x[1].id)
    mtm_tmp = [(i.owner, j.disk_id) for i in pcs for j in disk_pc if i.id == j.pc_id]
    mtm = [(i[0], str(j)) for i in mtm_tmp for j in disks if i[1] == j.id]
    print('Задание 1:')
    print('Название дисков установленных в ПК, где владелец начинается с \'a\':')
    ans = []
    for i in otm:
        if i[1].owner.startswith('a'):
            ans.append(i[1].owner)
            print(f"{i[0].name} установлен в {i[1]}")
    print('Пк у которых владелец начинается с \'a\':', *list(set(ans)))

    print('Задание 2:')
    print('Владельцы компьютеров с максимальными объемами дисков, установленных в них:')
    dic = {}
    for i in otm:
        if i[1].owner in dic:
            dic[i[1].owner] = min(dic[i[1].owner], i[0].volume)
        else:
            dic[i[1].owner] = i[0].volume
    sorted_dic = sorted(dic.items(), key=lambda x: x[1])
    for el in sorted_dic:
        print(f"Владелец: {el[0]}, Объем: {el[1]}")

    print('Задание 3:')
    print('Список всех компьютеров и дисков, отсортированных по компьютерам:')
    print(sorted(mtm, key=lambda x: x[0]))


if __name__ == '__main__':
    main()