from flask import Flask, render_template, send_from_directory, abort
import json
import os

app = Flask(__name__)

# Read video data
def load_metadata():
    with open('metadata.json', 'r', encoding='utf-8') as f:
        return json.load(f)

# Process video /video=ID
@app.route('/video=<video_id>')
def show_video(video_id):
    metadata = load_metadata()
    if video_id not in metadata:
        abort(404) # No video
    
    video_data = metadata[video_id]
    return render_template('video.html', video_id=video_id, video_data=video_data)

# Give HLS files
@app.route('/videos/<video_id>/<filename>')
def serve_video(video_id, filename):
    video_dir = os.path.join('videos', video_id)
    return send_from_directory(video_dir, filename)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
