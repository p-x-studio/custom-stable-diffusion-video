import random
import time
from util import get_output_folder

SEED = 3664512517


class RunParams:
    def __init__(self, output_path, batch_name, init_image, prompts, **kwargs):
        W = 512
        H = 512
        self.W, self.H = map(lambda x: x - x % 64, (W, H))

        self.seed = kwargs.get("seed", SEED)
        self.sampler = "euler_ancestral"
        self.steps = 15
        self.scale = 7
        self.ddim_eta = 0.0
        self.dynamic_threshold = None
        self.static_threshold = None

        self.save_samples = True
        self.save_settings = True
        self.display_samples = True

        self.n_samples = 1
        self.n_batch = 1
        self.batch_name = batch_name
        self.filename_format = "{timestring}_{index}.png"
        self.seed_behavior = "iter"
        self.outdir = get_output_folder(output_path, batch_name)

        self.use_init = True
        self.strength = 1
        self.init_image = init_image

        self.precision = "autocast"
        self.C = 4
        self.f = 8

        self.prompts = prompts
        self.timestring = time.strftime("%Y%m%d_-_%H_%M_%S")

        self.prompt_weighting = False
        self.normalize_prompt_weights = True
        self.log_weighted_subprompts = False

        if self.seed == -1:
            self.seed = random.randint(0, 2**32 - 1)

    def dump_attributes(self):
        attributes = {}

        for attribute, value in self.__dict__.items():
            attributes[attribute] = value

        return attributes
