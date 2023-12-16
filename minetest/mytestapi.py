import json
import requests
import io
import base64
from PIL import Image

url = "http://127.0.0.1:7860"

payload = {
    "prompt": '''underwater steampunk photograph, ultra realistic illustration, portrait, still life of A chicken sailing a boat , fantasy, Impressionist, by Krenz Cushart, Vincent van Gogh, Stanley Artgerm Lau, Tooth Wu, cgsociety, Canon50, highly detailed, Cinematic, sci-fi, colorful, muted colors, radiant light rays
''',
    "negative_prompt":'''moon, ugly, tiling, poorly drawn hands, poorly drawn feet, poorly drawn face, out of frame, extra limbs, disfigured, deformed, body out of frame, bad anatomy, watermark, signature, cut off, low contrast, underexposed, overexposed, bad art, beginner, amateur, distorted face, blurry, draft, grainy
''',
    "steps": 20,
    "width": 1024,
    "height": 1024,
    "cfg_scale": 20,
    "clip_skip": 1,
    "batch_size": 2,
}
payloadTest = {
  "enable_hr": True,
  "denoising_strength": 0,
  "firstphase_width": 0,
  "firstphase_height": 0,
  "hr_scale": 2,
  "hr_force": True,
#   "hr_upscaler": "string",
  "hr_second_pass_steps": 0,
  "hr_resize_x": 0,
  "hr_resize_y": 0,
  "refiner_steps": 5,
  "refiner_start": 0,
  "refiner_prompt": "",
  "refiner_negative": "",
  "prompt": "puppy dog",
#   "styles": [
#     "string"
#   ],
  "seed": -1,
  "subseed": -1,
  "subseed_strength": 0,
  "seed_resize_from_h": -1,
  "seed_resize_from_w": -1,
#   "sampler_name": "string",
#   "latent_sampler": "string",
  "batch_size": 1,
  "n_iter": 1,
  "steps": 5,
  "cfg_scale": 7,
  "image_cfg_scale": 0,
  "clip_skip": 1,
  "width": 512,
  "height": 512,
  "full_quality": True,
  "restore_faces": False,
  "tiling": False,
  "do_not_save_samples": False,
  "do_not_save_grid": False,
#   "negative_prompt": "string",
  "eta": 0,
  "diffusers_guidance_rescale": 0.7,
  "hdr_clamp": False,
  "hdr_boundary": 4,
  "hdr_threshold": 3.5,
  "hdr_center": False,
  "hdr_channel_shift": 0.8,
  "hdr_full_shift": 0.8,
  "hdr_maximize": False,
  "hdr_max_center": 0.6,
  "hdr_max_boundry": 1,
#   "override_settings": {},
  "override_settings_restore_afterwards": True,
#   "script_args": [],
  "sampler_index": "Euler",
  "script_name": "string",
  "send_images": True,
  "save_images": False,
#   "alwayson_scripts": {}
}

response = requests.post(url=f'{url}/sdapi/v1/txt2img', json=payload)

r = response.json()
# print(r)
if 'error' in r and r['error']:
    print(r['error'])
else:
    print(len(r['images']))
    imageLen = len(r['images'])
    for i in range(0,imageLen):
        fileName = f'output{i}.png'
        image = Image.open(io.BytesIO(base64.b64decode(r['images'][i])))
        image.save(fileName)