# 2. STUDENT PROFILE CONTEXT

import asyncio
#from connection import config
from agents import Agent, RunContextWrapper, Runner, function_tool
from pydantic import BaseModel
import rich
from dotenv import load_dotenv

load_dotenv()

class StudentProfile(BaseModel):
    student_id: int | str
    student_name: str
    current_semester: str
    total_courses: int


student = StudentProfile(
    student_id="STU786", 
    student_name="Syeda Gulzar Bano",
    current_semester="Q4", 
    total_courses=5
)

def dynamic_ins(wrapper: RunContextWrapper[StudentProfile], agent: Agent[StudentProfile]) -> str:
    return "When prompted, call tool 'get_student_profile' to get student profile."

@function_tool
def get_student_profile(wrapper: RunContextWrapper[StudentProfile]):
    return f'The Student Profile: {wrapper.context}'

personal_agent = Agent[StudentProfile](
    name="Agent",
    instructions=dynamic_ins,
    tools=[get_student_profile]
)

async def main():
    result = await Runner.run(
        personal_agent,
        'Provide student profile containing student name, student id, current semester, and total courses', 
        #run_config=config,
        context=student  # Local context
    )
    rich.print(result.final_output)

if __name__ == "__main__":
    asyncio.run(main())
