import os
import shutil


def main() -> None:
    repo_dir = os.path.dirname(os.path.abspath(__file__))
    src_img = os.path.join(repo_dir, "entry.png")

    out_dir = "/output"
    try:
        os.makedirs(out_dir, exist_ok=True)
        dst_img = os.path.join(out_dir, "entry.png")
        shutil.copyfile(src_img, dst_img)
    except OSError:
        local_out = os.path.join(repo_dir, "output")
        os.makedirs(local_out, exist_ok=True)
        shutil.copyfile(src_img, os.path.join(local_out, "entry.png"))


if __name__ == "__main__":
    main()
