"""
Script to download and save ESM-1v model locally
"""

import os
import urllib.request


def download_esm1v(save_dir="./models"):
    """
    Download ESM-1v model and save it locally

    Parameters:
    -----------
    save_dir : str
        Directory where the model will be saved
    """
    print("Downloading ESM-1v model...")

    # URL to download the pre-trained ESM-1v model
    esm_url = "https://dl.fbaipublicfiles.com/fair-esm/models/esm1v_t33_650M_UR90S_1.pt"

    # Create save directory if it doesn't exist
    os.makedirs(save_dir, exist_ok=True)

    # Save path for the model
    save_path = os.path.join(save_dir, "esm1v_t33_650M_UR90S_1.pt")

    # Download the file
    print(f"Downloading from {esm_url}...")
    urllib.request.urlretrieve(esm_url, save_path)
    print(f"Model saved to {save_path}!")

    return save_path


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Download ESM-1v model")
    parser.add_argument(
        "--save_dir",
        type=str,
        default="./models",
        help="Directory where the model will be saved",
    )

    args = parser.parse_args()
    save_path = download_esm1v(args.save_dir)
