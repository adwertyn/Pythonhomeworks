# Function to calculate and print enrollment statistics
def enrollment_stats(university):
    arr_tution = []   # List for tuition fees
    arr_student = []  # List for  student numbers
    sum_student = 0   # Total number of students
    sum_tution = 0    # Total tuition fees
    num_univers = len(university)  # Number of universities

    for num in university:
        sum_student += num[1]       # Add student count
        sum_tution += num[2]        # Add tuition amount
        arr_tution.append(num[2])   # Collect tuition for stats
        arr_student.append(num[1])  # Collect student numbers for stats

    print("******************************")
    print(f"Total students: {sum_student}")
    print(f"Total tution: $ {sum_tution} \n")

    # Print mean and median of datas
    print(f"Student mean: {round(sum_student/num_univers)}")
    print(f"Student median: {median(arr_student, num_univers)}\n")
    
    print(f"Tuition mean: {round(sum_tution/num_univers)}")
    print(f"Tuition median: {median(arr_tution, num_univers)}")
    print("******************************")

# Function to calculate the median of a array
def median(array, cnt):
    array.sort()  # Sort list for median calculation
    if cnt % 2 == 0:
        return round((array[cnt//2] + array[cnt//2 - 1]) / 2)
    else:
        return array[cnt//2]

# Data for various universities
universities = [
    ['California Institute of Technology', 2175, 37704],
    ['Harvard', 19627, 39849],
    ['Massachusetts Institute of Technology', 10566, 40732],
    ['Princeton', 7802, 37000],
    ['Rice', 5879, 35551],
    ['Stanford', 19535, 40569],
    ['Yale', 11701, 40500]
]

# Call function to do task
enrollment_stats(universities)
