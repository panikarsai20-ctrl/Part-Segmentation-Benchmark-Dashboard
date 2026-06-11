import os
import streamlit as st
from PIL import Image

# 1. Page Settings
st.set_page_config(page_title="Model Evaluation Bench", layout="wide")
st.title("🔬 Part Segmentation Benchmark Dashboard")
st.markdown("Compare visual segmentation outputs across CLIP and DINOv3 architectures.")

# Explicitly mapping your directory names
BASE_DIR = "evaluation_outs"
MODELS = ["CLIP", "DINOv3", "CLIP-SAM", "DINOv3-SAM"]

if not os.path.exists(BASE_DIR):
    st.error(f"⚠️ Directory path `{BASE_DIR}/` not found. Please verify the folder spelling.")
    st.stop()

# 2. Sidebar Controls
st.sidebar.header("🕹️ Configuration Dashboard")

# Toggle between label styles matching your subfolder names exactly
label_mode = st.sidebar.radio(
    "🏷️ Select Panel View Style:",
    ["with labels", "without labels"],
    format_func=lambda x: "3-Panel (With Class Labels)" if x == "with labels" else "2-Panel (Without Labels)"
)

# Scan for unique images inside the selected subfolders
all_images = set()
for model in MODELS:
    target_scan_dir = os.path.join(BASE_DIR, model, label_mode)
    if os.path.exists(target_scan_dir):
        files = [f for f in os.listdir(target_scan_dir) if f.lower().endswith(('.jpg', '.jpeg', '.png', '.webp'))]
        all_images.update(files)

all_images = sorted(list(all_images))

if not all_images:
    st.warning(f"⚠️ No image files discovered inside the `{label_mode}` directory variants.")
    st.stop()

selected_image = st.sidebar.selectbox("🎯 Target Image File:", all_images)
display_layout = st.sidebar.radio("🖥️ Presentation Format:", ["Compare All 4 Models", "Single Model Deep-Dive"])

# 3. Core Image Slicing Logic
def get_sliced_panels(img_path, mode):
    if not os.path.exists(img_path):
        return None, None, None
    try:
        full_img = Image.open(img_path)
        w, h = full_img.size
        
        if mode == "with labels":
            # 3-Panel Breakdown: 40% (Original) | 40% (Mask) | 20% (Legend Text)
            left_boundary = int(w * 0.40)
            right_boundary = int(w * 0.80)
            original = full_img.crop((0, 0, left_boundary, h))
            mask = full_img.crop((left_boundary, 0, right_boundary, h))
            legend = full_img.crop((right_boundary, 0, w, h))
            return original, mask, legend
        else:
            # 2-Panel Breakdown: 50% (Original) | 50% (Mask without labels)
            midpoint = int(w * 0.50)
            original = full_img.crop((0, 0, midpoint, h))
            mask = full_img.crop((midpoint, 0, w, h))
            return original, mask, None
            
    except Exception:
        return None, None, None

# 4. Render Interface Layout
st.subheader(f"📄 Target File: `{selected_image}` ({label_mode.title()} View)")

if display_layout == "Compare All 4 Models":
    st.markdown("### 🗺️ Cross-Model Mask Output Variations")
    
    # Render a 4-column layout block for your 4 model variants
    grid_cols = st.columns(len(MODELS))
    
    for idx, model in enumerate(MODELS):
        with grid_cols[idx]:
            st.markdown(f"**🤖 {model}**")
            image_path = os.path.join(BASE_DIR, model, label_mode, selected_image)
            orig, mask, legend = get_sliced_panels(image_path, label_mode)
            
            if mask is not None:
                st.image(mask, use_container_width=True)
            else:
                st.caption("❌ Output file missing.")
                
    # Footer anchors: reference tools for users analyzing the masks
    st.markdown("---")
    ref_col1, ref_col2 = st.columns([2, 1])
    for model in MODELS:
        image_path = os.path.join(BASE_DIR, model, label_mode, selected_image)
        orig, mask, legend = get_sliced_panels(image_path, label_mode)
        if orig is not None:
            with ref_col1:
                st.markdown("**📸 Reference Raw Input Image**")
                st.image(orig, width=450)
            if legend is not None:
                with ref_col2:
                    st.markdown("**🏷️ Label Index Legend**")
                    st.image(legend, width=220)
            break

else:
    # Single Model Comprehensive Deep-Dive
    st.markdown("---")
    active_model = st.selectbox("📂 Focus on Architecture Type:", MODELS)
    
    image_path = os.path.join(BASE_DIR, active_model, label_mode, selected_image)
    orig, mask, legend = get_sliced_panels(image_path, label_mode)
    
    if orig is not None:
        if label_mode == "with labels":
            c1, c2, c3 = st.columns([4, 4, 2])
            with c1:
                st.markdown("### 📸 Input Image")
                st.image(orig, use_container_width=True)
            with c2:
                st.markdown("### 🎨 Mask Matrix")
                st.image(mask, use_container_width=True)
            with c3:
                st.markdown("### 🏷️ Assigned Text Classes")
                st.image(legend, use_container_width=True)
        else:
            c1, c2 = st.columns(2)
            with c1:
                st.markdown("### 📸 Input Image")
                st.image(orig, use_container_width=True)
            with c2:
                st.markdown("### 🎨 Clean Mask Image")
                st.image(mask, use_container_width=True)
    else:
        st.error(f"⚠️ Image file `{selected_image}` not found in path: `{active_model}/{label_mode}/`.")
