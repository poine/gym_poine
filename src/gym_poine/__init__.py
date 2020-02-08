import sys
from gym.envs.registration import register
################################################################################
## Pendulum
##
# copy of original gym code
register(
    id='pendulum-legacy-v0',
    entry_point='gym_poine.envs:PendulumLegacyEnv',
)
