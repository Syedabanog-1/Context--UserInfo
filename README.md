                                                             ***CONTEXT MANAGEMENT***
                                                             
Context management refers to the technique of managing resources or states (like variables, sessions, environments, etc.) during the execution of a program or function, ensuring proper setup and cleanup (e.g., opening/closing files or managing temporary data).

 RunContextWrapper is a special wrapper used in the OpenAI Agent SDK to hold and manage the execution context during a run. It gives access to metadata (like input, user info, history, etc.) and is passed to functions/tools to dynamically adapt based on the user's session or data.
 
** Example use case:**
Inside a @function_tool,
if define def func(wrapper: RunContextWrapper):, 
it means function will have access to the full run context (like user input, config, previous steps, etc.).


Objective of this programe:
**************************
This Python program demonstrates how to build a simple AI agent using the OpenAI Agent SDK. The agent retrieves and displays structured user information (name, age, alive status, roll number) from a User_Info model in response to a natural language prompt. It uses the function_tool feature to fetch contextual data and dynamically guide the agent's behavior.

Workflow:
*********
**Model Definition (User_Info):

A Pydantic model is created to define the schema of user data, including name, age, roll number, and alive status.

**Context Initialization:

A sample user (Ali) is created using the User_Info model and passed as the agent’s context.

**Instruction Setup (dynamic_ins):

A function dynamically gives instructions to the agent, telling it to use the user_information tool to fetch the user details.

**Tool Definition (@function_tool):

A function tool named user_information is registered to extract and return user information from the context in a formatted string.

**Agent Configuration:

An Agent is created, named "Triage Agent", using:

***the instructions function,

***the model from config,

***and the user_information tool.

**Runner Execution:

A user prompt is defined asking for the user's roll number, name, age, and alive status.

The Runner.run() function executes the agent using the prompt and context.

**Final Output:

The agent returns the extracted information using the function tool and the result is printed using rich.print() for styled terminal output.

OUTPUT DISPLAY:
***************

The user's roll number is: q110110, and his name is: Ali. His age is: 23, and alive status: True.

CONTEXT:
*******
***USER INFORMATION
***CUSTOMER BANK ACCOUNT DETAILS
***STUDENT PROFILE
***LIBRARY BOOK DETAILS

https://github.com/user-attachments/assets/c5160cb8-e729-4153-9ea4-cbe298502a00

<img width="1612" height="906" alt="context_library_book_details" src="https://github.com/user-attachments/assets/0ab309ca-2317-43a7-b57d-9cf0d0393797" />
<img width="1609" height="901" alt="context_student_details" src="https://github.com/user-attachments/assets/2c796431-86ce-44a9-9947-6d4aada77573" />
<img width="1611" height="905" alt="context_customer_bank_accoumt_details" src="https://github.com/user-attachments/assets/a51bf9ef-6572-4844-8495-9af39bb8bf46" />
<img width="1610" height="904" alt="Context_userinfo" src="https://github.com/user-attachments/assets/656a6349-c02d-4fd4-b576-4e268f2aba8b" />


https://github.com/user-attachments/assets/a720082a-41f4-4fd4-9a90-5153140b3414

<img width="1611" height="906" alt="context userinfo Logs-user_information-Function_call-Generation output" src="https://github.com/user-attachments/assets/db17daec-fee1-445d-8023-60e0dc1f4afa" />
<img width="1609" height="905" alt="context userinfo Logs-user_information-Function_call-Generation INPUT" src="https://github.com/user-attachments/assets/e2de28fe-3336-4854-b6aa-62353df52e2e" />
<img width="1610" height="905" alt="context userinfo Logs-user_information-Function_call" src="https://github.com/user-attachments/assets/583573f6-6751-4429-9ae9-810c0bab35f6" />
<img width="1611" height="906" alt="context userinfo Logs-TriageAgnet Generation-output" src="https://github.com/user-attachments/assets/86117bd1-d140-48ab-9277-2ad05a8047c0" />
<img width="1609" height="906" alt="context userinfo Logs-TriageAgnet Generation-INPUT" src="https://github.com/user-attachments/assets/eb047cde-563a-4a48-9b8b-23fff4e0d08f" />
<img width="1609" height="910" alt="context userinfo Logs-Agent" src="https://github.com/user-attachments/assets/be528511-c9cd-4561-af9b-c2ed6d153200" />
<img width="1609" height="907" alt="context userinfo code-output" src="https://github.com/user-attachments/assets/93a41b33-ba3a-4942-96c9-f229d8f7bea1" />



Edit
The user's roll number is: q110110, and his name is: Ali. His age is: 23, and alive status: True.
