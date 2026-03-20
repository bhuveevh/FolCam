[app]
title = FolCam
package.name = folcam
package.domain = org.folcam
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,svg
version = 0.1

# Permissions
android.permissions = CAMERA, WRITE_EXTERNAL_STORAGE, READ_EXTERNAL_STORAGE, MANAGE_EXTERNAL_STORAGE

# Icon
icon.filename = %(source.dir)s/folcam.svg

# Orientation
orientation = portrait

# Requirements (GitHub build ke liye important)
requirements = python3,kivy==2.1.0,kivymd==1.1.1,plyer,pillow

# Android API
android.api = 33
android.minapi = 21
android.sdk = 33
android.archs = arm64-v8a, armeabi-v7a
fullscreen = 0
