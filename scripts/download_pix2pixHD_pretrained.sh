# make the directory
mkdir -p ./checkpoints/fish_pix2pix

# set the model file path
NET_G_FILE=./checkpoints/fish_pix2pix/latest_net_G.pth
NET_D_FILE=./checkpoints/fish_pix2pix/latest_net_D.pth
net_G_url="https://ncku365-my.sharepoint.com/:u:/g/personal/nm6121030_ncku_edu_tw/Ef77KmFwjntMjxbKCke8UooB5WOo9tjKbtTsZxPkmH0PPQ?e=Rk9KQ3&download=1"
net_D_url="https://ncku365-my.sharepoint.com/:u:/g/personal/nm6121030_ncku_edu_tw/EWrrWqrJ4BlJmj8ixkIHYA8BHgjPRXY1zFPKtsjNviHMrA?e=EwgJa9&download=1"

# download the pretrained weight
echo "Downloading the pretrained weight for the fish_pix2pixHD model..."
wget -N $net_G_url -O $NET_G_FILE
wget -N $net_D_url -O $NET_D_FILE