main.py: the main entry of the app

notes.py: notes service module with all the endpoints

test_notes.py: unit test file for the notes module

notes_test_client.sh: the script acting as a test client

To run the test client:
```
fastapi dev ./main.py # wait until the server is up and running

chmod u+x notes_test_client.sh
./notes_test_client.sh # result will be shown in the console
```
