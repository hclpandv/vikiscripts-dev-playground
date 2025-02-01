import asyncio
import time

async def brewCoffee():
    print("Start brewCoffee()")
    await asyncio.sleep(3)
    print("End brewCofee()")
    return "Coffee ready"

async def toastBread():
    print("Start toastBread()")
    await asyncio.sleep(2)
    print("End toastBread()")
    return "frokost ready"

async def main():
    start_time = time.time()
    
    coffee_task = asyncio.create_task(brewCoffee())
    toast_task = asyncio.create_task(toastBread())

    result_coffee = await coffee_task
    result_toast = await toast_task


    end_time = time.time()
    elapsed_time = end_time - start_time

    print(f"Result of brewCofee: {result_coffee}")
    print(f"Result of toastBread: {result_toast}")
    print(f"Total Execution time: {elapsed_time:.2f} seconds")

if __name__ == "__main__":
    asyncio.run(main())
