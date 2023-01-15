def student_attendance_record(s):
    if s.count("A") >= 2 or "LLL" in s:
        return False
    return True

def student_attendance_record_ll(s):
    A_count = 0
    L_count = 0
    for c in s:
        if c == "A":
            A_count += 1
            L_count = 0
            if A_count == 2:
                return False
        elif c == "L":
            L_count += 1
            if L_count == 3:
                return False
        elif c == "P":
            L_count = 0
    return True


def main():
    days = 'PPALLL'
    print(student_attendance_record(days))
    

if __name__ == '__main__':
    main()

        