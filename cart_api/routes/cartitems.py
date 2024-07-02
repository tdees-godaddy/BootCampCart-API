import falcon
from playhouse.shortcuts import model_to_dict

from cart_api.database import DatabaseCartItem
api = falcon.App()
cartItem = CartItem()
cartItems = CartItems()
api.add_route('/v/products/{product_id:int}', product)

# Exercise 3:
# Using the database model you created in Exercise 1 create a cartitems route
# CartItems should have a responder for POST and GET
# CartItem should have responders for GET DELETE PATCH
# Your API response statuses and bodies should conform to your OpenAPI spec


class CartItems:
    obj = req.get_media()
    product = CartItems(
        name = obj["name"],
        price = obj["price"],
        quantity = obj["quantity"]
    )
    new_cartItem_row = DatabaseCartItem(name = name, price = price, quantity = quantity)
    CartItem.save()
    resp.status = falcon.HTTP_201
    resp.media = {"name": new_cartItem_row.name, "price": new_cartItem_row.price, "quantity": new_cartItem_row.price}

    def on_get(self, req, resp):
        item_rows = DatabaseCartItem.all()
        resp.media = {"name": item_rows.name, "price": item_rows.price, "quantity": item_rows.price}
        resp.status = falcon.HTTP_200

class CartItem:
    def on_get(self, req, resp, item_id)
        cartItemRow = DatabaseCartItem.get(item_id)
        resp.media = {"id": cartItemRow.id, "name": cartItemRow.name, "price": cartItemRow.price, "quantity": cartItemRow.quantity}
        resp.status = falcon.HTTP_200

    def on_delete(self, req, resp, item_id)
        cartItemRow = 