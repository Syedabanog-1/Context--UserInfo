from agents import Agent, RunContextWrapper, Runner, function_tool
from pydantic import BaseModel
#from connection import config
import asyncio
import rich
from dotenv import  load_dotenv
load_dotenv()

class UserInfo(BaseModel):
    user_id: int | str
    name: str

user = UserInfo(user_id= 1312321, name="Ali Jawwad")

@function_tool
def get_user_info(wrapper: RunContextWrapper[UserInfo]):
    # rich.print(wrapper.context.name)
    return f'The user info is {wrapper.context}'

personal_agent = Agent(
    name = "Agent",
    instructions="You are a helpful assistant,get user's information",
    tools=[get_user_info]
)
async def main():
    result = await Runner.run(
        personal_agent, 
        #'What is the name', 
        'user information',
        #run_config=config,
        context = user #Local context
        )
    rich.print(result.final_output)


if __name__ == "__main__":
    asyncio.run(main())
