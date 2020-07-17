'''
Bài 3 - Môn Toán - Đề thi Tuyển sinh Lớp 10 Năm 2020
Câu a:
Intput: 2005
Output: Ất Dậu

Câu b:
Input:
Mậu Thân
18

Output:
[1728, 1788]

'''


can_list = ["Canh", "Tân", "Nhâm", "Quý", "Giáp", "Ất", "Bính", "Đinh", "Mậu", "Kỷ"]
chi_list = ["Thân", "Dậu", "Tuất", "Hợi", "Tí", "Sửu", "Dần", "Mẹo", "Thìn", "Tỵ", "Ngọc", "Mùi"]

def Year_to_CanChi(y):
    can = can_list[y % 10]
    chi = chi_list[y % 12]
    return can + " " + chi

def CanChi_to_Year(can, chi, tk):
    start_year = (tk - 1) * 100
    r_can = can_list.index(can)
    r_chi = chi_list.index(chi)

    year_list = []
    for y in range(start_year, start_year + 100):
        if y % 10 == r_can and y % 12 == r_chi:
            year_list.append(y)
    return year_list

year = int(input("Nhập năm: "))
print("{} là năm {}".format(year, Year_to_CanChi(year)))

can = input("Nhập can: ")
chi = input("Nhập chi: ")
century = int(input("Nhập thế kỉ: "))

print("Năm {} {} trong thế kỉ {} là năm {}".format(can, chi, century, CanChi_to_Year(can, chi, century)))







