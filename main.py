<<<<<<< HEAD
from pydantic import BaseModel, Field
from typing import Annotated

class CourseRegistration(BaseModel):
    # Username must be between 3 and 15 characters
    username: Annotated[str, Field(min_length=3, max_length=15, title = "name of the user",description="Give the name of the user in 15 characters", examples=["jackob", "john"])]
    
    # Age must be at least 18
    age: Annotated[int, Field(gt=17, title="Student Age")] 

# If we try to use a 2-letter username, Pydantic will raise a validation error
try:
    user = CourseRegistration(username="Nadeem",age = 18)
except Exception as e:
    print(f"Validation failed: {e}")
else:
    print("user registered")
=======
print("simple first line")
print("second line")
print("third line")

def fun():
    return none
>>>>>>> c10a9ab0e52b4bb47234a888d97c0424fa4c8bfd
