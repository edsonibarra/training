def student_attendance_record(s):
    if s.count("A") >= 2 or "LLL" in s:
        return False
    return True


def main():
    days = 'PPALLL' # False
    print(student_attendance_record(days))
    

if __name__ == '__main__':
    main()

        