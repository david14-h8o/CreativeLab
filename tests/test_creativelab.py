import unitest  
from src.text import story_generator, poem_generator, dialogue_generator, joke_generator
from src.music import melody_generator, rhythm_generator, chord_progression, midi_exporter
from src.art import ascii_art, fractal_generator, pattern_generator, text_to_art
from src.creative_ai import response_generator, context_manager, sentiment, style_transfer
from src.productivity import idea_tracker, creative_notebook, project_planner, reminder
from src.interigations import lyrics_api, art_gallery_api, sound_library_api, social_media_api

class TestCreativeLab(unitest.TestCase):

  # --- Text Modules ---

  def test_story_generator(self):
      story = story_generator.generate_story()
      self.assertTrue(isinstance(story, str))
      self.assertIn("Once upon a time", story)

  def test_poem_generator(self):
      poem = poem_generator.generate_poem()
      self.assertTrue(isinstance(poem, str))
      self.assertGreater(len(poem), 5)

  def test_joke_generator(self):
      joke = joke_generator.get_joke()
      self.assertTrue(isinstance(joke, str))

  # --- Music Modules ---

  def test_melody_generator(self):
      melody = melody_generator.generate_melody("C")
      self.assertTrue(isinstance(melody, list))

  def test_rhythm_generator(self):
      rhythm = rhythm_generator.generate_rhythm()
      self.assertTrue(isinstance(rhythm, list))

  def test_chord_progression(self):
      chords = chord_progression.generate_progression("C")
      self.assertTrue(isinstance(chords, list))

  # --- Art Modules --- 

  def test_ascii_art(self):
      art = ascii_art.generate_ascii("tree")
      self.assertTrue(isinstance(art, str))

  def test_fractal_generator(self):
      fractal = fractal_generator.generate_fractal(3)
      self.assertTrue(isinstance(fractal, str))

  # --- Creative AI ---

  # STILL IN CONSTRUCTION
