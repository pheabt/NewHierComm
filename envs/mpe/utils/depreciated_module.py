from .error import DeprecatedEnv


class DepreciatedModule:
    def __init__(self, name, old_version, new_version):
        def env(*args, **kwargs):
            raise DeprecatedEnv(f"{name}_{old_version} is now depreciated, use {name}_{new_version} instead")

        self.env = env
        self.raw_env = env
        self.parallel_env = env
        self.manual_control = env
