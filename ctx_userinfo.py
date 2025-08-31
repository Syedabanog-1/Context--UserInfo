import asyncio
#from connection import config
from agents import Agent, trace, RunContextWrapper, Runner, function_tool
from pydantic import BaseModel
import rich
from dotenv import load_dotenv

load_dotenv()

class UserInfo(BaseModel):
    user_id: int | str
    name: str


# Create context object
user = UserInfo(user_id=192110, name="Syeda Gulzar Bano")


def dynamic_ins(wrapper: RunContextWrapper[UserInfo], agent: Agent[UserInfo]) -> str:
    return "When prompted call tool 'get_user_info' to get user information."


@function_tool
def get_user_info(wrapper: RunContextWrapper[UserInfo]):
    return f"The user info: {wrapper.context}"


# Create the agent
personal_agent = Agent(
    name="Agent",
    instructions=dynamic_ins,
    tools=[get_user_info],
)


async def main():
    with trace("User Information"):
        result = await Runner.run(
        personal_agent,
        'get user name',
        #'GET User Information',
        #run_config=config,
        context=user  # Local context
    )
    rich.print(result.final_output)


if __name__ == "__main__":
    asyncio.run(main())
