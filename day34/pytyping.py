# You can set the data type of variables to ensure strict types

age: int
name: str
height: float
is_human: bool


ages="twelve"  

def police_check(age:int) -> bool:
    if age > 18:
        can_drive = True
    else:
        can_drive = False
    return can_drive

print(police_check(ages))