testing_dataset_url="https://ncku365-my.sharepoint.com/:u:/g/personal/nm6121030_ncku_edu_tw/ETpwAjav2EFNmDuDlwhfQzAB1aW5ohc-v5BNLSJLH8kkmg?e=AIIt2w&download=1"
testing_dataset="test_pose.zip"
# if the dataset is already downloaded, then skip downloading
if [ -f "$testing_dataset" ]; then
    echo "testing_dataset already exists. Skipping download."
else
    echo "Downloading $testing_dataset..."
    wget -N $testing_dataset_url -O "$testing_dataset"
fi

# unzip the dataset
unzip -o $testing_dataset