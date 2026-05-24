name: Build Android APK
on: [push, workflow_dispatch]

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.11'

      - name: Install Tools
        run: |
          sudo apt-get update
          sudo apt-get install -y libtool-bin cmake python3-dev ffmpeg libsdl2-dev libsdl2-image-dev libsdl2-mixer-dev libsdl2-ttf-dev libportmidi-dev libswscale-dev libavformat-dev libavcodec-dev zlib1g-dev libgstreamer1.0-dev gstreamer1.0-plugins-base gstreamer1.0-plugins-good
          pip install --upgrade pip buildozer Cython virtualenv

      - name: Build with Buildozer
        run: |
          YES=1 buildozer -v android debug

      - name: Upload APK
        uses: actions/upload-artifact@v4
        with:
          name: SHIV-AI-App
          path: bin/*.apk
          
