# README

## Resources

https://github.com/alexdlaird/pyngrok
https://www.digitalocean.com/community/tutorials/how-to-write-a-slash-command-with-flask-and-python-3-on-ubuntu-16-04
https://api.slack.com/tutorials/slash-commands-style-guide

### `mrkdwn`

Slack has its own Markdown implementation : [`mrkdwn`](https://api.slack.com/reference/surfaces/formatting#basics)

## Installation

python -m venv ~/Work/venvs/slack
source ~/Work/venvs/slack/bin/activate
pip install -r requirements

## Ngrok

[Ngrok](https://ngrok.com/)
[get started guide](https://dashboard.ngrok.com/get-started/setup)


```shell
./ngrok authtoken xxxxxxxxxxxxxxxxxxxxxxxxxxx
```

```shell
./ngrok 8000
```

Copy the forwarding address to the slash command Request URL.

## Slack App

Start the API backend:

```shell
uvicorn main:app --reload
```

### Create App

...

## Webapp

https://fastapi.tiangolo.com/tutorial/request-forms/
https://stackoverflow.com/questions/61872923/supporting-both-form-and-json-encoded-bodys-with-fastapi
https://www.twilio.com/blog/build-sms-email-bridge-python-fastapi-twilio
