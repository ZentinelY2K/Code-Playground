club_data = [
    {
        "first_name": "Jamie",
        "last_name": "Lopez",
        "student_id": "9023121"
    },
    {
        "first_name": "Dani",
        "last_name": "Nguyen",
        "student_id": "abc1234"
    },
    {
        "first_name": "Alex",
        "last_name": "Tran",
        "student_id": "9023188"
    }
]
for student in club_data:
    full_name = f"{student['first_name']} {student['last_name']}".lower()
    print(full_name)