from gym.envs.registration import register

regsiter(
  id = 'Pygame-v0',
  entry_point = 'gmy_game.envs:CustomEnv',
  max_episode_steps = 2000,
  )
