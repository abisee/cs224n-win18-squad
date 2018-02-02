"""Downloads the GloVe vectors and unzips them"""

import zipfile
import argparse
import os
from squad_preprocess import maybe_download

def setup_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--download_dir", required=True) # where to put the downloaded glove files
    return parser.parse_args()


def main():
    args = setup_args()
    glove_base_url = "http://nlp.stanford.edu/data/"
    glove_filename = "glove.6B.zip"

    print "\nDownloading wordvecs to {}".format(args.download_dir)

    if not os.path.exists(args.download_dir):
        os.makedirs(args.download_dir)

    maybe_download(glove_base_url, glove_filename, args.download_dir, 862182613L)
    glove_zip_ref = zipfile.ZipFile(os.path.join(args.download_dir, glove_filename), 'r')

    glove_zip_ref.extractall(args.download_dir)
    glove_zip_ref.close()


if __name__ == '__main__':
    main()
