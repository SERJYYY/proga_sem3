import unittest
from main import *


class Test(unittest.TestCase):
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

    def test_1(self):
        otm = [(i, j) for i in disks for j in pcs if i.pc_id == j.id]
        otm.sort(key=lambda x: x[1].id)
        ans = []
        for i in otm:
            if i[1].owner[0] == 'a':
                ans.append(i[1].owner)
        ans1 = sorted(list(set(ans)))
        self.assertEqual(ans1, ['admin'])

    def test_2(self):
        otm = [(i, j) for i in disks for j in pcs if i.pc_id == j.id]
        otm.sort(key=lambda x: x[1].id)
        dic = {}
        for i in otm:
            if i[1].owner in dic:
                dic[i[1].owner] = min(dic[i[1].owner], i[0].volume)
            else:
                dic[i[1].owner] = i[0].volume
        sorted_dic = sorted(dic.items(), key=lambda x: x[1])
        self.assertEqual(sorted_dic, [('admin', 500), ('user', 1000), ('employee', 2000)])

    def test_3(self):
        mtm_tmp = [(i.owner, j.disk_id) for i in pcs for j in disk_pc if i.id == j.pc_id]
        mtm = [(i[0], str(j)) for i in mtm_tmp for j in disks if i[1] == j.id]
        ans3 = sorted(mtm, key=lambda x: x[0])
        self.assertEqual(ans3, [('admin', 'HDD2, volume: 1000'), ('admin', 'SSD1, volume: 1000'), ('employee', 'HDD2, volume: 1000'), ('user', 'SSD1, volume: 1000'), ('user', 'HDD2, volume: 1000')])
