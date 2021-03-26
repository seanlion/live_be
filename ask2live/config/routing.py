from django.conf.urls import url
from django.urls import re_path
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
# from channels.security.websocket import AllowedHostsOriginValidator, OriginValidator

from chat_messages.consumers import ChatConsumer

websocket_urlpatterns = [
    # path("hole/<str:room_id>")
    url(r"^hole/(?P<room_id>[\w.@+-]+)", ChatConsumer),
]
# print("websocekt url : ", websocket_urlpatterns)
# print("websocekt ChatConsumer : ", ChatConsumer)

application = ProtocolTypeRouter({
    'websocket': AuthMiddlewareStack(
            URLRouter(        
                    websocket_urlpatterns
            )
        )
})
