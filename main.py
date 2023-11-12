import os
import streamlit as st
from PIL import Image

trained_image_folder = "trained_plots_images/"
untrained_image_folder = "untrained_plots_images/"

configs = os.listdir(trained_image_folder)
for i in range(len(configs)):
    configs[i] = configs[i].split("_")
    # remove first element
    configs[i].pop(0)
    # remove last element
    configs[i].pop(-1)
    # Join the list
    configs[i] = "_".join(configs[i])

st.title("Compare Correctness Plots")
st.markdown("Choose the config and size to compare the correctness plots")
st.markdown("The plots on the left are for pretrained and the plots on the right are untrained models")

# Select the config
selected_config = st.multiselect("Select the config", configs, default=['layer_0'])

# select sizes
selected_size = st.multiselect("Select the string length", [16, 32, 64, 128, 256, 512, 1024], default=[16])

# sort the selected config which contain the word layer by the layer number
sorted_selected_config = []
for i in range(len(selected_config)):
    if "layer_" not in selected_config[i]:
        sorted_selected_config.append(selected_config[i])
selected_config_with_layer = []
for i in range(len(selected_config)):
    if "layer_" in selected_config[i]:
        selected_config_with_layer.append(selected_config[i])
# sort the selected_config_with_layer by the layer number
selected_config_with_layer.sort(key=lambda x: int(x.split("_")[-1]))
# add the sorted selected_config_with_layer to the sorted_selected_config
sorted_selected_config.extend(selected_config_with_layer)

selected_config = sorted_selected_config

for i in range(len(selected_config)):
    st.subheader(selected_config[i].title() + " Only")
    trained_folder = 'pythia-1b' + '_' + selected_config[i] + '_' + 'only'
    untrained_folder = 'pythia-1b_ut' + '_' + selected_config[i] + '_' + 'only'
    for size in selected_size:
        st.markdown(f"##### Size: {size}")
        img_path = f'recollection_order_dot_{size}_26.png'
        # Show both images side by side
        col1, col2 = st.columns(2)
        with col1:
            st.image(Image.open(trained_image_folder + trained_folder + '/' + img_path))
        with col2:
            st.image(Image.open(untrained_image_folder + untrained_folder + '/' + img_path))

