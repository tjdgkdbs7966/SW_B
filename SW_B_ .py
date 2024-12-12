import random
import json

# 학생 정보 생성
def generate_students():
    students = []
    for _ in range(30):
        name = chr(random.randint(65, 90)) + chr(random.randint(65, 90))
        age = random.randint(18, 22)
        score = random.randint(0, 100)
        students.append({"이름": name, "나이": age, "성적": score})
    return students

# 선택 정렬 구현
def selection_sort(data, key, reverse=False):
    n = len(data)
    for i in range(n - 1):
        least = i
        for j in range(i + 1, n):
            if (data[j][key] < data[least][key]) ^ reverse:
                least = j
        data[i], data[least] = data[least], data[i]

# 삽입 정렬 구현
def insertion_sort(data, key, reverse=False):
    n = len(data)
    for i in range(1, n):
        key_item = data[i]
        j = i - 1
        while j >= 0 and (data[j][key] > key_item[key]) ^ reverse:
            data[j + 1] = data[j]
            j -= 1
        data[j + 1] = key_item

# 퀵 정렬 구현
def quick_sort(data, key, reverse=False):
    quick_sort_recursive(data, 0, len(data) - 1, key, reverse)

def quick_sort_recursive(data, left, right, key, reverse):
    if left < right:
        pivot = partition(data, left, right, key, reverse)
        quick_sort_recursive(data, left, pivot - 1, key, reverse)
        quick_sort_recursive(data, pivot + 1, right, key, reverse)

def partition(data, left, right, key, reverse):
    pivot = data[left]
    low = left + 1
    high = right

    while True:
        while low <= high and (data[low][key] <= pivot[key]) ^ reverse:
            low += 1

        while low <= high and (data[high][key] > pivot[key]) ^ reverse:
            high -= 1

        if low <= high:
            data[low], data[high] = data[high], data[low]
        else:
            break

    data[left], data[high] = data[high], data[left]
    return high

# 기수 정렬 구현
def counting_sort(data, key, exp, reverse=False):
    n = len(data)
    output = [None] * n
    count = [0] * 10

    for item in data:
        index = (item[key] // exp) % 10
        count[index] += 1

    for i in range(1, 10):
        count[i] += count[i - 1]

    for item in reversed(data):
        index = (item[key] // exp) % 10
        output[count[index] - 1] = item
        count[index] -= 1

    for i in range(n):
        data[i] = output[i]

    if reverse:
        data.reverse()

def radix_sort(data, key, reverse=False):
    max_val = max(data, key=lambda x: x[key])[key]
    exp = 1
    while max_val // exp > 0:
        counting_sort(data, key, exp, reverse)
        exp *= 10

# 학생 정보를 JSON 파일로 저장
def save_students_to_json(students, filename="students.json"):
    with open(filename, mode='w', encoding='utf-8') as file:
        json.dump(students, file, ensure_ascii=False, indent=4)
    print(f"학생 정보를 {filename} 파일로 저장했습니다.")

# 사용자 인터페이스 구현
def main():
    students = generate_students()
    save_students_to_json(students)  # JSON 파일 저장 추가
    
    algorithms = {
        1: ("선택 정렬", selection_sort),
        2: ("삽입 정렬", insertion_sort),
        3: ("퀵 정렬", quick_sort),
        4: ("기수 정렬", radix_sort)
    }

    while True:
        print("\n학생 목록:")
        for student in students:
            print(student)

        print("\n메뉴:")
        print("1. 이름을 기준으로 정렬")
        print("2. 나이를 기준으로 정렬")
        print("3. 성적을 기준으로 정렬")
        print("4. 프로그램 종료")

        try:
            choice = int(input("정렬 기준을 선택하세요 (1, 2, 3, 4): "))
            if choice == 4:
                print("프로그램을 종료합니다.")
                break

            field = {1: "이름", 2: "나이", 3: "성적"}.get(choice)
            if not field:
                print("잘못된 입력입니다. 다시 시도하세요.")
                continue

            print("\n정렬 알고리즘:")
            for k, v in algorithms.items():
                print(f"{k}. {v[0]}")

            algo_choice = int(input("정렬 알고리즘을 선택하세요: "))
            algo_name, algo_func = algorithms.get(algo_choice, (None, None))

            if not algo_func:
                print("잘못된 입력입니다. 다시 시도하세요.")
                continue

            order = input("오름차순으로 정렬하시겠습니까? (y/n): ").strip().lower() == 'y'

            algo_func(students, key=field, reverse=not order)

            print(f"\n{algo_name}을(를) 사용하여 {field} 기준으로 {'오름차순' if order else '내림차순'} 정렬한 결과:")
            for student in students:
                print(student)

        except ValueError:
            print("잘못된 입력입니다. 숫자를 입력해주세요.")

if __name__ == "__main__":
    main()
