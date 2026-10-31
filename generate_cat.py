"""Generate an image of a cat using a free Stable Diffusion model."""

import argparse
from pathlib import Path

import torch
from diffusers import AutoPipelineForText2Image

MODEL_ID = "stabilityai/sd-turbo"
DEFAULT_PROMPT = (
    "a pure white fluffy cat with big eyes walking on a wooden floor, "
    "full body, photorealistic"
)


def load_pipeline(device: str):
    if device == "cuda":
        pipe = AutoPipelineForText2Image.from_pretrained(
            MODEL_ID, torch_dtype=torch.float16, variant="fp16"
        )
    else:
        pipe = AutoPipelineForText2Image.from_pretrained(MODEL_ID)
    return pipe.to(device)


def main():
    parser = argparse.ArgumentParser(description="Generate a cat image.")
    parser.add_argument("--prompt", default=DEFAULT_PROMPT, help="Text description of the image")
    parser.add_argument("--output", default="outputs/cat.png", help="Where to save the image")
    parser.add_argument("--steps", type=int, default=4, help="Denoising steps")
    args = parser.parse_args()

    device = "cuda" if torch.cuda.is_available() else "cpu"
    pipe = load_pipeline(device)

    # sd-turbo runs without classifier-free guidance, so guidance_scale=0.0
    image = pipe(
        prompt=args.prompt,
        num_inference_steps=args.steps,
        guidance_scale=0.0,
    ).images[0]

    output_path = Path(args.output)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    image.save(output_path)
    print(f"Saved image to {output_path}")


if __name__ == "__main__":
    main()
