from pydantic import BaseModel, Field
from typing import Optional, List, Annotated

class Patient(BaseModel):

    name :Annotated[str, Field(max_length=50, title = "Nmae of teh Patient", description="Give" \
    " me hte name of the patient whose name is less then 50 characters")]
    age : int = Field(gt =0, max_length= 100)
    query : Optional[list[str]] = None


def get_data(state: Patient):

    print(
        {
        "name": state.name,
        "age": state.age,
        "query": state.query
        }
    )


agee = input("please enter your age :  ")
namee = input("please enter your name :  ")


patient_info = {'age': agee, 'name' : namee, 'query': [ "heyyy " , "how are you "] }   

info = Patient(**patient_info)

# result = get_data(info)

# print(result)

get_data(info)