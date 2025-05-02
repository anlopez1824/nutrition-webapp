
import os
from flask import Blueprint, request, current_app
import requests
clarifai = Blueprint('clarifai', __name__, url_prefix='/api/clarifai')


@clarifai.post('/detect-food')
def detectFood():
    try:
        data = request.json
        imageUrl = data.get('image_url')
        if imageUrl is None:
            return{
                'msg': 'Invalid data. request body should contains [image_url]'
            }, 400

        foodResponse = requests.post('https://api.clarifai.com/v2/models/bd367be194cf45149e75f01d59f77ba7/outputs', json={
            "inputs": [
                {
                    "data": {
                        "image": {
                            #"url": "https://image.cnbcfm.com/api/v1/image/107417438-1716234749013-Vital_Pursuit_Whole_Grain_Bowl_Garlic_Herb_Grilled_Chicken_Bowl.jpg?v=1716256596&w=1480&h=833&ffmt=webp&vtcrop=y"
                            "url": imageUrl
                        }
                    }
                }
            ]
        }, headers={'Authorization': 'Key '+str(os.environ.get('CLARIFAI_API_KEY'))})

        foodItems = foodResponse.json()['outputs'][0]['data']['concepts']
        return {
            'foodItems': foodItems,
            'res': foodResponse.json()
        }
    except Exception as e:
        return {
            'msg': 'Something went wrong. Try again',
            'error': str(e),
            'res': foodResponse.json()
        }
