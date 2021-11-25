# scrncy-devops-task

I was using `venv` so don't forget to review the `pyvenv.cfg` file and run `python3 -m venv venv`

All the requirements could be satisfied by running the `pip install -r requirements.txt` command.

The main code file is `app.py`, so you can run it as simple as `python app.py`

This is how your `.env` file may look like:

```
PROD_URL=https://horizon.stellar.org/
DEV_URL=https://horizon-testnet.stellar.org/
TEST_URL=https://raw.githubusercontent.com/dima056359/scrncy-devops-task/main/test.json
TEST1_URL=https://raw.githubusercontent.com/dima056359/scrncy-devops-task/main/test1.json
```

This is what output you should expect:

```
(code) Dmytros-MacBook-Pro:code dmytroh$ python app.py 
_URL detected: PROD_URL
_URL detected: DEV_URL
_URL detected: TEST_URL
_URL detected: TEST1_URL

main version: PROD_URL: stellar-core 18.1.0 (dc5f5a392098b82bd9453a2aa4259e7af600ad9d)

stellar-core 18.2.0 (aa5f5a392098b82bd9453a2aa4259e7af600adba) (TEST_URL) is not matching main version stellar-core 18.1.0 (dc5f5a392098b82bd9453a2aa4259e7af600ad9d)
stellar-core 18.3.3 (aa12ga392098b82bd9453a2aa4259e7af6009921) (TEST1_URL) is not matching main version stellar-core 18.1.0 (dc5f5a392098b82bd9453a2aa4259e7af600ad9d)
```
