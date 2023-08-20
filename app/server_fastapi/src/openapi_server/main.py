# coding: utf-8

"""
    Forex Trading Platform API

    A RESTful API to simulate a Forex trading platform with WebSocket support for real-time order updates.

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


from fastapi import FastAPI

from apis.cancel_order import router as cancel_order_router
from apis.get_order import router as get_order_router
from apis.get_orders import router as get_orders_router
from apis.place_order import router as place_order_router
from apis.web_socket_connect import router as web_socket_connect_router

app = FastAPI(
    title="Forex Trading Platform API",
    description="A RESTful API to simulate a Forex trading platform with WebSocket support for real-time order updates.",
    version="1.0.0",
)

app.include_router(cancel_order_router)
app.include_router(get_order_router)
app.include_router(get_orders_router)
app.include_router(place_order_router)
app.include_router(web_socket_connect_router)
