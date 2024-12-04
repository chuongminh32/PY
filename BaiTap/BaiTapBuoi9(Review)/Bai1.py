class person:
    def __init__(self, name, yob):
        self.name = name
        self.yob = yob

    def __str__(self):
        return (f"name: {self.name}, yob: {self.yob}")


class stu(person):
    def __init__(self, name, yob, birth, grade):
        super().__init__(name, yob)
        self.birth = birth
        self.grade = grade

    def __str__(self):
        return (f" {super().__str__()} bith: {self.birth}, grade {self.grade}")


class teacher(person):
    def __init__(self, name, yob, subject):
        super().__init__(name, yob)
        self.subject = subject

    def __str__(self):
        return (f"name: {self.name}, yob {self, yob}, subject {self.subject}")


class doctor(person):
    def __init__(self, name, yob, specialist):
        super().__init__(name, yob)
        self.specialist = specialist

    def __str__(self):
        return (f" {super().__str__()}, specialist: {self.specialist}")


class ward:
    def __init__(self, name):
        self.name = name
        self.person = []

    def add(self, p):
        self.person.append(p)

    def info(self):
        for per in self.person:
            print(per)
            print()

    def count_doctor(self):
        cnt = 0
        for per in self.person:
            if isinstance(per, doctor):
                cnt += 1

        return (f"there are {cnt} doctor in ward")

    def sortAge(seld):
        sort(self.person, key=lambda person:  person.yob)

    def Ageavg(self):
        count = 0
        sum = 0
        for per in self.person:
            if isinstance(per, teacher):
                sum += per.yob
                count += 1
        if count > 0:
            return sum/count
        else:
            return 0


def inputPerson():
    typePerson = input("Nhap loai nguoi: ")

    name = input("Nhap ten: ")
    yob = int(input("Nhap tuoi: "))

    typePerson = typePerson.lower()
    if typePerson == "student":
        b = int(input("Nam sinh: "))
        g = float(input("gpa: "))
        return stu(name, yob, b, g)
    elif typePerson == "teacher":
        subject = input("Nhap mon hoc: ")
        return teacher(name, yob, subject)
    elif typePerson == "doctor":
        spe = input("input specialist: ")
        return doctor(name, yob, spe)
    else:
        return None


if __name__ == "__main__":
    persons = []
    nameWard = input("Nhap name ward: ")
    w = ward(nameWard)
    n = int(input("Nhap so luong nguoi trong ward:  "))
    for i in range(n):
        print(f"Nhap thong tin nguoi thu {i+1}: ")
        person = inputPerson()
        w.add(person)

    w.info()
