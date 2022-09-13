## How to run the tests?

```docker image build -t kl_numbers_task .```

```docker run -d --name kl_numbers_task -it kl_numbers_task sh```

```docker exec -it kl_numbers_task bash```

```cd tests | pytest -v```

## How to run the main code?

```docker image build -t kl_numbers_task .```

```docker run -d --name kl_numbers_task -it kl_numbers_task sh```

```docker exec -it kl_numbers_task bash```

```python main.py```

You can run ```python main.py``` multiple times 
to obtain each time a different random sorted list.
I enjoyed running it many times like a fool :D

## Algorithm 

1. Prepare a list with a number from each file. Each index in the list represents a file.
**[0,1,2]** -> **0** belongs to **first file**, 1 to second file...

2. Take a minimum number from the list above and add to the sorted list.
3. Remove from list the minimum number and add on the same index a new number from the file with the removed minimum
number.
4. If no numbers left in the file, close file.



## Possible future improvements

**Logging**

More **test coverage** (not 100%) - e.g. check new source files are created correctly

**Error handling**

**config file** - input parameters such as number_of_files=10 in configs 
instead in code

Better structure of folders and files, e.g. avoid utils

## Distribute file reading
Interesting case, I have an idea which we can gladly discuss

## Last words
Thank you very much for taking the time to write and to check the task!

