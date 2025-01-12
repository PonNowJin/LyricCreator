# LyricCreator Project

This project provides a pipeline to generate song lyrics and optionally, songs and videos, based on a given topic. It utilizes various tools and APIs to create, refine, and evaluate song lyrics, ensuring high-quality output. Below are the details and instructions for using this project.

## Features

- Generate song lyrics based on a given topic.
- Analyze and incorporate stylistic elements from reference songs.
- Iteratively refine lyrics based on evaluation scores.
- Optional creation of songs and videos.

## Setting Up the Project

1. Clone the repository:

```bash
git clone https://github.com/your-repo/song-creation.git
cd song-creation
```

2. Create and activate a virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

## Usage

### Prerequisites

Ensure the `.env` file is properly set up with necessary environment variables, such as API keys (Please refer to the `.env.example` file).

### Running the Script

To create a song, run the `SongCreation.py` script. Below is an example usage:

```python
if __name__ == '__main__':
    topic = 'title: 調查局'
    SongCreation(topic, CREATE_SONG=0, image=None, music_style=None, preprocessed=True)
```

Execute:

```
python3 SongCreation.py
```

### Function Parameters

The main function `SongCreation` has the following parameters:

| Parameter      | Type   | Description                                                            |
| -------------- | ------ | ---------------------------------------------------------------------- |
| `topic`        | `str`  | Song topic or theme.                                                   |
| `CREATE_SONG`  | `int`  | Set to 1 to create and save a song using an external API (e.g., Suno). |
| `image`        | `str`  | Path to an image for visual inspiration.                               |
| `music_style`  | `str`  | Optional parameter for specifying a music style.                       |
| `preprocessed` | `bool` | Whether the topic has already been preprocessed.                       |
| `CREATE_VIDEO` | `bool` | Set to `True` to generate a video.                                     |

### Outputs

- **Lyrics File**: Generated lyrics are saved in `outputs/lyrics.txt`.
- **Sample Songs**: Reference songs for inspiration are listed in the console output.
- **Evaluation Scores**: Each iteration’s evaluation score is displayed.
- **Conversation Reference File**: Logs of LLMs’ interaction during lyric generation are saved in `outputs/chat_history.txt` and other history files.

### Example Workflow

1. **Input**: Provide a topic, e.g., "調查局."
2. **Process**:
   - Optimize the topic prompt.
   - Find similar reference songs from embeddings.
   - Generate lyrics and iteratively refine them based on evaluation scores.
3. **Output**:
   - Save the final lyrics in the `outputs/` directory.
   - Save the LLMs’ conversation log.
   - Optionally, create a song and/or a video.

## File Structure

```
.
├── SongCreation.py            # Main script for song creation
├── Evaluation.py              # Handles evaluation of generated lyrics
├── LyricsCreator.py           # Generates song lyrics
├── Prompt_optimize.py         # Optimizes prompts for generation
├── SampleSongFetch/           # Directory containing song data and embeddings
├── outputs/                   # Directory to save generated outputs
├── .env                       # Environment variables (e.g., API keys)
└── README.md                  # Project documentation
```

## Key Modules

### `LyricsCreator`

Handles the generation of song lyrics based on the optimized topic prompt and reference songs.

### `Evaluation`

Evaluates the generated lyrics, assigning scores and providing suggestions for improvement.

### `Prompt_OPT`

Optimizes the initial topic prompt for better lyric generation.

### `find_similar_songs`

Fetches a list of reference songs that closely match the topic’s intent and style.

## Debugging

- Ensure the `outputs/` directory exists or will be created dynamically.
- If external APIs throw exceptions (e.g., `StopCandidateException`), ensure API configurations in `.env` are correct.
- Logs and intermediate outputs are printed to the console for troubleshooting.

## Notes

- The script includes functionality for generating songs and videos, but these are currently commented out. Uncomment the relevant sections if required.
- Iterative refinement continues until the lyrics achieve a score above the set threshold (default: 90).

## Example Usage

Below is an example Python script demonstrating how to use this project to generate a song:

```python
from SongCreation import SongCreation

topic = "A journey through space"
result = SongCreation(
    topic=topic,
    CREATE_SONG=1,
    image="path/to/image.jpg",
    music_style="Pop",
    preprocessed=False,
    CREATE_VIDEO=False
)

if result:
    print("Song creation process completed successfully!")
else:
    print("Song creation process failed.")
```

## License

This project is licensed under the MIT License. Feel free to modify and distribute it as per the terms of the license.

---

For any issues or contributions, please contact the project maintainer.

