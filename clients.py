import requests

class UserServiceClient:
    def __init__(self, base_uri: str):
        """
        Client for interacting with the UserService.
        :param base_uri: The base URL of the UserService (e.g., http://localhost:8000)
        """
        self.base_uri = base_uri

    def verify_user_token(self, token: str) -> dict:
        """
        Verifies a user token by calling the /users/me endpoint.
        """
        url = f"{self.base_uri}/users/me"
        payload = {
            "access_token": token,
            "token_type": "bearer"
        }
        headers = {
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        }
        
        response = requests.post(url, json=payload, headers=headers)
        response.raise_for_status() # Raise an exception for bad status codes (4xx or 5xx)
        return response.json()
    
class ShippingServiceClient:
     def __init__(self, base_uri: str):
         self.base_uri = base_uri

     def createShipping(self,orderId : int, userId : int , address : str):
        url = f"{self.base_uri}/shipping"
        payload = {
            "orderId":str(orderId),
            "userId": str(userId),
            "address" : address
        }
        headers = {
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        }
        response = requests.post(url, json=payload, headers=headers)
        response.raise_for_status() 
        return response.json()

