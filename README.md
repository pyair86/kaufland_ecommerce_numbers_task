## How to run the tests?

docker image build -t kl_numbers_task .

docker run -d --name kl_numbers_task -it kl_numbers_task sh

docker exec -it kl_numbers_task bash

cd tests | pytest -v

## How to run the main code?

docker image build -t kl_numbers_task .

docker run -d --name kl_numbers_task -it kl_numbers_task sh

docker exec -it kl_numbers_task bash

python main.py

you can run "python main.py" multiple times 
to obtain each time a random sorted list.
I enjoyed running it many times like a fool :D

## Algorithm 
The key is to manage the indices for each input file of 
how many numbers were read.

1. Check minimum number for each line among the input files
2. Increment the index of input file where minimum number is found
3. Append to sorted list


## Possible future improvements

**Logging**

More **test coverage** (not 100%) - e.g. check new source files are created

**Error handling** - e.g. empty files

**config file** - input parameters such as number_of_files=10 in configs 
instead in code

Better structure of folders and files I created e.g. avoid utils
