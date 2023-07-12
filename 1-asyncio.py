#example of runing a coroutine
import asyncio

#define a coroutine
async def custom_coro():
    # wait for a tak to be done
    # awit another coroutine
     await asyncio.sleep(1)

# main corotine
async def main():
     # execute my custom corotine
     await custom_coro()

#start the coroutine programs
asyncio.run(main())
