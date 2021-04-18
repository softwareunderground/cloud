from typing import Optional

from fastapi import FastAPI, Request, Response, Form
from pydantic import BaseModel


class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None

class SlackBase(BaseModel):
    token: str

# class SlackCommand(SlackBase):
class SlackCommand(BaseModel):
    token: str
    team_id: str
    team_domain: str
    is_enterprise_install: bool
    enterprise_id: Optional[str] = None
    enterprise_name: Optional[str] = None
    channel_id: str
    channel_name: str
    user_id: str
    user_name: str
    command: str
    text: str
    response_url: str
    trigger_id: str
    api_app_id: str

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post('/newsletter')
async def route(req: Request) -> Response:
    # item = MyItem(** await req.form())
    form = await req.form()
    print('three')
    print(form)
    user_name = form["user_name"]

    res = {}
    # res["user_name"] = user_name
    res["text"] = f"Hello {user_name} :wave:"
    # res[""]

    # Uncomment the line below for the response to be visible to everyone
    # res["response_type"] = "in_channel"
    res['attachments'] = [
            {
                'fallback': 'Required plain-text summary of the attachment.',
                'color': '#36a64f',
                'pretext': 'Optional text above the attachment block',
                'author_name': 'Bobby Tables',
                'author_link': 'http://flickr.com/bobby/',
                'author_icon': 'http://flickr.com/icons/bobby.jpg',
                'title': 'Slack API Documentation',
                'title_link': 'https://api.slack.com/',
                'text': 'Optional text that appears within the attachment',
                'fields': [
                    {
                        'title': 'Priority',
                        'value': 'High',
                        'short': False
                    }
                ],
                'image_url': 'http://my-website.com/path/to/image.jpg',
                'thumb_url': 'http://example.com/path/to/thumb.png'
            }
        ]
    res2 = {
      # "channel": "C1H9RESGL",
      "text": "New Paid Time Off request from Fred Enriquez",
      "blocks": [
    		{
    			"type": "header",
    			"text": {
    				"type": "plain_text",
    				"text": "New request :wave:"
    			}
    		},
    		{
    			"type": "section",
    			"fields": [
    				{
    					"type": "mrkdwn",
    					"text": "*Type:*\nPaid Time Off"
    				},
    				{
    					"type": "mrkdwn",
    					"text": "*Created by:*\n<example.com|Fred Enriquez>"
    				}
    			]
    		},
    		{
    			"type": "section",
    			"fields": [
    				{
    					"type": "mrkdwn",
    					"text": "*When:*\nAug 10 - Aug 13"
    				}
    			]
    		},
    		{
    			"type": "section",
    			"text": {
    				"type": "mrkdwn",
    				"text": "<https://example.com|View request>"
    			}
    		}
    	]
    }
    # return Response(content=item.json())
    # return f"Hello {res['user_name']} :wave:"
    return res2

@app.post('/newsletter3')
async def login(user_name: str = Form(...)):
    # return {"username": user_name}
    return "Got it! Thanks :thumbsup:"
