import os
import shutil

MAX_IMAGE_BYTES = 1_048_576


def resolve_output_dir(repo_dir: str) -> str:
    """Resolve /output (or MAKEFUN_OUTPUT_DIR), falling back locally when needed."""
    target = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    try:
        os.makedirs(target, exist_ok=True)
        return target
    except OSError:
        local_out = os.path.join(repo_dir, "output")
        os.makedirs(local_out, exist_ok=True)
        return local_out


def validate_image(path: str) -> None:
    """Verify the source image is a complete PNG or JPEG within 1 MiB."""
    with open(path, "rb") as f:
        data = f.read()
    if len(data) == 0 or len(data) > MAX_IMAGE_BYTES:
        raise ValueError(f"Invalid image size: {len(data)} bytes")
    is_png = data.startswith(b"\x89PNG\r\n\x1a\n") and b"IEND" in data[-16:]
    is_jpeg = data.startswith(b"\xff\xd8") and data.endswith(b"\xff\xd9")
    if not (is_png or is_jpeg):
        raise ValueError("Source image must be a complete PNG or JPEG file")


def main() -> None:
    repo_dir = os.path.dirname(os.path.abspath(__file__))
    src_img = os.path.join(repo_dir, "entry.png")
    validate_image(src_img)
    out_dir = resolve_output_dir(repo_dir)
    dst_img = os.path.join(out_dir, "entry.png")
    shutil.copyfile(src_img, dst_img)


if __name__ == "__main__":
    main()
