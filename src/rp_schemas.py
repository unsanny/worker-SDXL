INPUT_SCHEMA = {
     'api_name': {
        'type': str,
        'required': False,
    },
    'training_id': {
        'type': str,
        'required': False,
        'default': None
    },
    'prompt': {
        'type': str,
        'required': True,
    },
    'negative_prompt': {
        'type': str,
        'required': False,
        'default': None
    },
    'lora_key': {
        'type': str,
        'required': False,
        'default': None
    },
    'use_vae': {
        'type': bool,
        'required': False,
        'default': True
    },
     'base64': {
        'type': bool,
        'required': False,
        'default': False
    },
    'avatars': {
        'type': object,
        'required': False,
        'default': False
    },
    'avatars2': {
        'type': object,
        'required': False,
        'default': False
    },
    'width': {
        'type': int,
        'required': False,
        'default': 1024,
        'constraints': lambda width: width in [128, 256, 384, 448, 512, 576, 640, 704, 768, 896, 1024,1152]
    },
    'height': {
        'type': int,
        'required': False,
        'default': 1024,
        'constraints': lambda height: height in [128, 256, 384, 448, 512, 576, 640, 704, 768, 896, 1024,1152]
    },
    'init_image': {
        'type': str,
        'required': False,
        'default': None
    },
    'samples': {
        'type': int,
        'required': False,
        'default': 1,
        'constraints': lambda num_outputs: 10 > num_outputs > 0
    },
    'num_inference_steps': {
        'type': int,
        'required': False,
        'default': 50,
        'constraints': lambda num_inference_steps: 0 < num_inference_steps < 500
    },
    'strength': {
        'type': float,
        'required': False,
        'default': 0.7,
        'constraints': lambda strength: 0 < strength <= 1
    },
    'guidance_scale': {
        'type': float,
        'required': False,
        'default': 7.5,
        'constraints': lambda guidance_scale: 0 < guidance_scale < 20
    },
    'refiner_strength': {
        'type': float,
        'required': False,
        'default': 0,
        'constraints': lambda refiner_strength: 0 <= refiner_strength < 1
    },
    'seed': {
        'type': int,
        'required': False,
        'default': None
    }
}