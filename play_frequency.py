import asyncio
import subprocess

frequency_D = 293.665 # Hertz
frequency_A = 440 # Hertz

async def play_after(delay, duration, frequency):
    await asyncio.sleep(delay)
    process = await asyncio.create_subprocess_shell(
        'play -n synth %s sin %s' % (duration/1000, frequency),
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )
    await process.communicate()

async def main():
    await asyncio.gather(
        play_after(0, 1000, frequency_D),
        play_after(0, 1000, frequency_A)
    )

asyncio.run(main())