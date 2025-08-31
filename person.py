from agents import Agent, RunContextWrapper, Runner, trace
from pydantic import BaseModel
#from connection import config
import asyncio
import rich
from dotenv import load_dotenv

load_dotenv()

# ------------------ Example of Dynamic Context ------------------ #

class Person(BaseModel):
    name: str
    user_level: str

personOne = Person(
    name = "Ali",
    user_level="junior"
    )

async def my_dynamic_instructions(ctx: RunContextWrapper[Person], agent: Agent):
    if ctx.context.user_level == 'junior' or ctx.context.user_level == 'mid_level':
        return """
            Keep your answers simple and easy to understand.
        """
    elif ctx.context.user_level == "PHD":
        return """ Keep you vocabulary advanced and very hard like your are talking to a PHD level peron """

personal_agent = Agent(
    name = "Agent",
    instructions=my_dynamic_instructions,
)

async def main():
    with trace("Learn Dynamic Instructions"):
        result = await Runner.run(
            personal_agent, 
            'What is light?',
            #run_config=config,
            context = personOne #Local context
            )
        rich.print(result.final_output)


if __name__ == "__main__":
    asyncio.run(main())