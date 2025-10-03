This is a Blender 4.5 addon developed to render the normal and the opacity maps towards the camera.
Rendering images of 3D objects is useful for background objects or stationary objects due to the reduced draw call.
Coupled the image with a normal map can add 

The workflow is based off of this youtube video:
https://www.youtube.com/watch?v=yDJaSF4B138

Installation:

1. Download the "Camera_Facing_Normal.py" from this github repository
2. In Blender, go to "Edit > Preferences... > v > Install From Disk"
3. Find the Camera_Facing_Normal.py from File Manager
4. When "Camera Facing Normal" appears in the addon list, the addon has be successfully installed

To use this addon:

1. Set up your object and camera in 3D space
2. Have the camera in orthographic else a gradient will appear in the normal render
3. The Panel "Camera Facing Normal" will be in the panel of the 3D view port
4. There will be buttons to either "Render Normal" or "Render Opacity"