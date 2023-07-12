#example of getting the current task from the main coroutine
import asyncio
import time

#define a main corotine
async def main():
    #report a message
    print(f'{time.ctime()} main corotine started')
    #get the current task
    task = asyncio.current_task()
    #report its details
    print(f'{time.ctime()} {task}')

#start the asycio program
asyncio.run(main())
