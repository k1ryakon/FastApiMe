import asyncio


async def my_task():
    current_task = asyncio.current_task()
    print(f"Текущий объект задачи: {current_task}")

    await asyncio.sleep(1)

    # Отмена текущей задачи
    current_task.cancel()

    # До этой строки мы дойдём, т.к. невозможно отменить активную в данный момент задачу.
    print(420)

async def main():
    task = asyncio.create_task(my_task())
    await task


asyncio.run(main())