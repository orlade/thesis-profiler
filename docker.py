import sumo
import altruism
from util import ROOT, call, calls_to_string
import world

SUMO_IMAGE = 'similitude/sumo-simmer'
ALTRUISM_IMAGE = 'similitude/netlogo-samples-simmer'
WORLD_IMAGE = 'similitude/h2-world-simmer'
# POSTGIS_IMAGE = 'similitude/sumo-simmer'
# IMAGES = [SUMO_IMAGE, ALTRUISM_IMAGE, POSTGIS_IMAGE]
IMAGES = [SUMO_IMAGE, ALTRUISM_IMAGE, WORLD_IMAGE]


def run_sumo():
    docker_run_all(SUMO_IMAGE, sumo.randomHourMinutes_calls())

def run_altruism():
    calls = altruism.altruism_calls()
    return docker_run_all(ALTRUISM_IMAGE, calls)

def run_world():
    docker_run_all(WORLD_IMAGE, world.cityLanguage_calls())


def docker_run_all(image,  calls, opts=None):
    if opts is None:
        opts = []
    opts += ['-v', '%s:%s' % (ROOT,ROOT), '--entrypoint', '/bin/sh']
    return docker_run(image, ['-c', '%s' % calls_to_string(calls)], opts)


def docker_run(image, args, opts=None):
    if opts is None:
        opts = []
    return call(['sudo', 'docker', 'run'] + opts + [image] + args)
