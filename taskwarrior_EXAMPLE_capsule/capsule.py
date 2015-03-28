from taskwarrior_capsules.capsule import CommandCapsule


class EXAMPLE(CommandCapsule):
    """ Describe what your capsule does right here """

    # Enter a minimum taskwarrior-capsules version that you've tested this with
    MIN_VERSION = '0.2.4'
    # Enter the highest taskwarrior-capsules version that you'd expect this to
    # work with -- note that taskwarrior-capsules follows semver, and expects
    # you to do so, too.
    MAX_VERSION = '1.0'

    # Enter a minimum taskwarrior version that you've tested this with
    MIN_TASKWARRIOR_VERSION = '2.3'
    # Enter the highest taskwarrior version that you'd expect this to work
    # with, see above.
    MAX_TASKWARRIOR_VERSION = '2.4.999'

    def handle(self, filter_args, extra_args, **kwargs):
        print "Hello World!"
        print "Filter Args: %s" % filter_args
        print "Extra Args: %s" % extra_args
        print "Kwargs: %s" % kwargs
