from tkinter import Tk, Button
import asyncio
import threading
import random


def asyncio_thread(event_loop):
  print('The tasks of fetching multiple URLs begins')
  event_loop.run_until_complete(simulate_fetch_all_urls())


def execute_tasks_in_a_new_thread(event_loop):
  """ Button-Event-Handler starting the asyncio part. """
  threading.Thread(target=asyncio_thread, args=(event_loop, )).start()


async def simulate_fetch_one_url(url):
  """ We simulate fetching of URL by sleeping for a random time """
  seconds = random.randint(1, 8)
  await asyncio.sleep(seconds)
  return 'url: {}\t fetched in {} seconds'.format(url, seconds)


async def simulate_fetch_all_urls():
  """ Creating and starting 10 i/o bound tasks. """
  all_tasks = [simulate_fetch_one_url(url) for url in range(10)]
  completed, pending = await asyncio.wait(all_tasks)
  results = [task.result() for task in completed]
  print('\n'.join(results))


def check_if_button_freezed():
  print(
      'This button is responsive even when a list of i/o tasks are in progress'
  )


def main(event_loop):
  root = Tk()
  Button(
      master=root,
      text='Fetch All URLs',
      command=lambda: execute_tasks_in_a_new_thread(event_loop)).pack()
  Button(
      master=root,
      text='This will not Freeze',
      command=check_if_button_freezed).pack()
  root.mainloop()


if __name__ == '__main__':
  event_loop = asyncio.get_event_loop()
  main(event_loop)
