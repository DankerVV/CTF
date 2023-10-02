from prefect import flow, task
from prefect.blocks.system import String

string_block = String.load("future-nba-champs")

@task
def create_message():
    msg = string_block.value  
    return msg

@flow
def something_else():
    result = " gonna be champs"
    return result

@flow
def hello_world():
    sub_flow_message = something_else()
    taske_message = create_message()
    new_message = taske_message + sub_flow_message
    print(new_message)

if __name__ == "__main__":
    hello_world()