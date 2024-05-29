import os
from PIL import Image


def align_images(
    source_folder, domainA_folder="trainA", domainB_folder="trainB", target_folder="train"
):
    combined_folder = os.path.join(source_folder, target_folder)
    if not os.path.exists(combined_folder):
        os.makedirs(combined_folder)

    domain_A_files = get_file_paths(os.path.join(source_folder, domainA_folder))
    domain_B_files = get_file_paths(os.path.join(source_folder, domainB_folder))

    print(f"saving aligned images to {combined_folder}")
    # Align images
    for i in range(len(domain_A_files)):
        filename = os.path.basename(domain_A_files[i]).split(".")[0]

        img_A = Image.open(domain_A_files[i])
        img_B = Image.open(domain_B_files[i])
        assert img_A.size == img_B.size

        aligned_image = Image.new("RGB", (img_A.size[0] * 2, img_A.size[1]))
        aligned_image.paste(img_A, (0, 0))
        aligned_image.paste(img_B, (img_A.size[0], 0))
        # default save as {filename}.jpg
        aligned_image.save(os.path.join(combined_folder, f"{filename}.jpg"))
        # else save as {index}.jpg
        # aligned_image.save(os.path.join(train_folder, f"{i:04d}.jpg"))
    print("Done!")


def get_file_paths(folder):
    image_file_paths = []
    for root, dirs, filenames in os.walk(folder):
        filenames = sorted(filenames)
        for filename in filenames:
            input_path = os.path.abspath(root)
            file_path = os.path.join(input_path, filename)
            if filename.endswith(".png") or filename.endswith(".jpg"):
                image_file_paths.append(file_path)

        break  # prevent descending into subfolders
    return image_file_paths


if __name__ == "__main__":

    # align train
    align_images(source_folder="training_pose2img")

    # align test
    align_images(
        source_folder="test_pose",
        domainA_folder="source",
        domainB_folder="testA",
        target_folder="dance2pose",
    )
