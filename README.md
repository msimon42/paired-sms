# paired-sms
## Link to production server
https://paired-sms.herokuapp.com

## Installation

1. Clone this repo on to your local machine.

2. Navigate into your repo via the command line.

3. Install Python 3.8 and pip if you have not already done so.

4. Create a virtual environment by entering the following commands:
  ```
  $ pip install virtualenv
  $ virtualenv venv
  $ source venv/bin/activate
  ```
5. Install dependencies by running requirements.txt:
  `pip install -r requirements.txt`

6. Add your Twilio API key to your environment variables  


## Send a message request using your local server

1. Enter `flask run` in the terminal to start up your server.

2. The endpoint for all message requests is `/request`. Send a POST request using the
tool of your choice to `localhost:5000/request`. The body of your request should be formatted as
follows:
        ```
        {
          'phone_number': '3035559823'
          'message': 'Hello! This is a text message'
          'sms_token': 'YOUR SMS TOKEN'
        }

        ```
The recipient's phone number must be in the exact format as in the example above. The sms token
is a secret token that must be valid in order to use this service. Contact the owner of this repo
if you would like to request a token.

3. If the request is processed with no errors, the response will look like this:
        ```
        {'response': 'success'}
        ```
4. If Twilio cannot send the message, the response will look like this:
        ```
        {'response': 'twilio error'}
        ```
5. If your request is not valid, the response will look like this:
        ```
        {'response': 'Invalid request'}
        ```

## Send a message request to the production server

1. Send a POST request to https://paired-sms.herokuapp.com/request using the same method described above.
