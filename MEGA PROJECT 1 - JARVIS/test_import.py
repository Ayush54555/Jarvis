import musiclibrary
import os

print("✅ Imported musiclibrary from:", musiclibrary.__file__)

# Read and print the actual contents of the file being loaded
with open(musiclibrary.__file__, 'r', encoding='utf-8') as f:
    content = f.read()
    print("\n📄 CONTENTS OF LOADED FILE:\n")
    print(content)

print("\n🔍 DIR:", dir(musiclibrary))
print("🎵 MUSIC:", getattr(musiclibrary, "music", "NO MUSIC FOUND"))
