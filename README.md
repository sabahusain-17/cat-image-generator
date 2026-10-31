# Cat Image Generator

I'm doing the Hugging Face AI Agents course. In the Dummy Agent Library section, the hosted inference the course uses now requires paid credits, so I couldn't finish the agent exercises that way.

Instead, I ran a small free model in Google Colab and completed the cat image task with it.

## What it does
`generate_cat.py` generates a cat image from a text prompt using the free `stabilityai/sd-turbo` model. No paid API or token is needed.

## Run it
```bash
pip install -r requirements.txt
python generate_cat.py
```

Custom prompt:
```bash
python generate_cat.py --prompt "a black cat sleeping on a sofa" --output outputs/black_cat.png
```

The image is saved to `outputs/cat.png` by default.

## Result
The final output from my Colab run:

```
from IPython.display import Image, display
display(Image("outputs/cat.png"))
<img width="512" height="512" alt="image" src="https://github.com/user-attachments/assets/90f1ff31-6a71-48e1-85c7-67c8e1d8ace3" />

```

## Files
- `generate_cat.py`: the image generation script
- `requirements.txt`: Python dependencies
- `README.md`: this file
