# all of the functions ton run the custom gym environment 
import gymnasium as gym
from gymnasium import spaces


# custom env for the chaser
class CustomEnv(gym.Env):
    metadata = {'render.modes': ['human']}

    def __init__(self, arg1, arg2):
        super(CustomEnv, self).__init__()
        # Define action and observation space
        # They must be gym.spaces objects
        # Example when using discrete actions, Box for continuous action
        self.action_space = spaces.Discrete(N_DISCRETE_ACTIONS)
        # Example for using image as input (channel-first; channel-last also works)
        self.observation_space = spaces.Box(low=0, high=255, shape=(N_CHANNELS, HEIGHT, WIDTH), dtype=np.uint8)

    def step(self, action):
        # Execute one time step within the environment
        ...
        return observation, reward, done, info

    def reset(self):
        # Reset the state of the environment to an initial state
        ...
        return observation

    def render(self, mode='human'):
        # Render the environment to the screen
        ...

    def close(self):
        # Cleanup
        ...

    def reward(self, state):
        # Reward function
        ...