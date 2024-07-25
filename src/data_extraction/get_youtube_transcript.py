from youtube_transcript_api import YouTubeTranscriptApi

def get_transcript(video_id):
    transcript = YouTubeTranscriptApi.get_transcript(video_id)
    transcript_text = " ".join([entry['text'] for entry in transcript])
    return transcript_text

if __name__ == "__main__":
    video_id = "TX9qSaGXFyg"  # Replace with the actual video ID
    transcript_text = get_transcript(video_id)
    with open("E:/DeepSolv_Assignment/data/youtube/video_transcript.txt", "w", encoding="utf-8") as f:
        f.write(transcript_text)
