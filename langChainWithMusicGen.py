from audiocraft.models import musicgen
from audiocraft.utils.notebook import display_audio
from audiocraft.data.audio import audio_write

model = musicgen.MusicGen.get_pretrained('facebook/musicgen-small', device='cuda')

PROMPTS = ['Playful and humorous with silly faces and peace signs.']
DURATION = 30
OUTPUT_FILENAME = 'omzTest'

def generate_music(input_text):    
    model.generation_params = {'use_sampling': True,
                            'temp': 1.0,
                            'top_k': 250,
                            'top_p': 0.0,
                            'cfg_coef': 3.0,
                            'two_step_cfg': False}
    model.set_generation_params(duration=DURATION)
    output_musics = model.generate( PROMPTS, progress=True)
    for i, output_music in enumerate(output_musics):
    audio_write(f'{OUTPUT_FILENAME}_{i}', output_music.cpu(), model.sample_rate, strategy="loudness", loudness_compressor=True)