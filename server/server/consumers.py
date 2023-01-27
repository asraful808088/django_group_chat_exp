import json

from channels.consumer import AsyncConsumer
from channels.exceptions import StopConsumer


class AsyncGroupChat(AsyncConsumer):
    async def websocket_connect(self,event):
        await self.channel_layer.group_add(self.scope['url_route']['kwargs']['room_name'],self.channel_name)
        await self.send({
            'type':"websocket.accept"
        })
    async def websocket_disconnect(self,event):
        await self.channel_layer.group_discard(self.scope['url_route']['kwargs']['room_name'],self.channel_name)
        raise StopConsumer()

    async def websocket_receive(self,event):
        jsonInfo = json.loads(event['text'])

        print(jsonInfo)
        if jsonInfo['type'] =='init':
           await self.send({
            'type':"websocket.send",
            'text':json.dumps({
                'type':"init",
                'userId':self.channel_name,
            })
        })
        else:
            await self.channel_layer.group_send(self.scope['url_route']['kwargs']['room_name'],{
            'type':"chat.message",
            'message':jsonInfo['message'],
            "sender_name":jsonInfo['sender_name'],
            "sender_id":jsonInfo['sender_id']
            
             })

    async def chat_message(self,event):
        await self.send({
            'type':'websocket.send',
            'text':json.dumps({
                'type':"message",
                'message':event['message'],
                "sender_name":event['sender_name'],
                "sender_id":event['sender_id']
            })
        })