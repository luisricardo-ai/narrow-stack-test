# narrow-stack-test

At NarrowStack, our client, we work a lot with files, mainly Excel and CSV.
I would like you to build a docker compose file/dockerfile with the service MageAI. 
**This container will be reproduced in another machine, so be sure it works properly.**

In MageAI, write one pipeline that opens the four files in this folder and save them as parquet files.
Everything you do beyond this will be considered as a plus (e.g. save in another service like MinIO, set up a data transformation tool, etc).

## Important
* The original test files was moved to `data/input`

* The output files are gonna be saved at `data/output`

* *To check with the parquet files was successfully created, inside the pipeline there's a block callled **_read_local_parquet.py_** that gonna print the parquet content in Logs*

## How to run?

1. Make sure that you have [Docker](https://www.docker.com/products/docker-desktop/) installed at you machine.

2. Clone the repository

3. Run the following code

```bash
# This code will download the MageAI's official image and start a new container.
docker-compose up --build
```

4. Go to http://localhost:6789/ to access the UI of MageAi

5. Go to **Pipelines** and access the pipeline called **csv_to_parquet**