[app]

# (list) Application requirements
# comma separated e.g. requirements = sqlite3,kivy
requirements = kivy,kivymd

[buildozer]

# (str) Android architecture to build for, can be one of armeabi-v7a, arm64-v8a, x86, x86_64, all
android.arch = armeabi-v7a

# (str) Android entry point, default is ok for Kivy-based app
android.entrypoint = org.kivy.android.PythonActivity

# (str) Android release version, default to latest if not set
android.release = 7

# (str) Title of your application
title = hello

# (str) Package name
package.name = com.privite.app

# (str) Package domain (needed for android/ios packaging)
package.domain = org.test

# (str) Source code where the main.py live
source.dir = .

[target]
# (str) Target platform for the application (android / ios / macos / win)
android
