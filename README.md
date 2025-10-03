# Camera Facing Normal (Blender 4.5 Addon)

This Blender 4.5 addon renders **normal maps** and **opacity maps** from the camera’s perspective.  
Rendering objects to images is useful for background or stationary objects because it reduces draw calls. Pairing the rendered image with a normal map can add depth and surface detail without needing a full 3D mesh.  

The workflow is based on this YouTube video:  
[https://www.youtube.com/watch?v=yDJaSF4B138](https://www.youtube.com/watch?v=yDJaSF4B138)  

---

## 🚀 Installation

1. Download the file `Camera_Facing_Normal.py` from this repository.  
2. In Blender, go to:  
   `Edit > Preferences... > Add-ons > Install from Disk...`  
3. Locate and select the `Camera_Facing_Normal.py` file in the file browser.  
4. Enable the **Camera Facing Normal** addon from the Add-ons list. Once it appears and has a checkmark, it is installed and active.  

---

## 🛠️ Usage

1. Set up your object and camera in 3D space.  
2. Switch the camera to **Orthographic** mode — otherwise, a gradient will appear in the normal render.  
3. Open the **Camera Facing Normal** panel in the **3D Viewport sidebar** (N-panel).  
4. Use the buttons provided:  
   - **Render Normal** — exports a camera-facing normal map image.  
   - **Render Opacity** — exports the opacity (alpha) map image.  

---

## 📷 Example

_Add a screenshot or GIF here showing a rendered normal map and the resulting combined sprite/texture._  

---

## 📌 Notes

- Built and tested for **Blender 4.5**.  
- Best suited for background or static objects to reduce draw calls.  
- Use orthographic camera to avoid unwanted gradients in the normal map.  
